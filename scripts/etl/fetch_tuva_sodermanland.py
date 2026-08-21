"""
fetch_tuva_sodermanland.py
--------------------------
Hämtar ängs- och betesmarksinventeringen (TUVA) för Södermanlands län
från samma källa som e-tjänsten https://etjanst.sjv.se/tuvaut/

1. Söker via Jordbruksverkets REST-API (hagenpub) med g=04
2. Exporterar CSV (komplett / senaste / summerad) som i TUVA-gränssnittet
3. Hämtar objektsrapporter (JSON) per fält-ID
4. Hämtar kartskikt via WFS, filtrerat på lans_kod=04, SWEREF 99 TM

Utdata: docs/tuva/sodermanland/
"""

from __future__ import annotations

import csv
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "docs" / "tuva" / "sodermanland"
EXPORT_DIR = OUT / "export"
REPORT_DIR = OUT / "objektrapporter"
GIS_DIR = OUT / "gis"

HAGEN = "https://etjanst.sjv.se/hagenpub"
WFS = "https://epub.sjv.se/inspire/opendata/wfs"
WFS_NATURTYP = "https://epub.sjv.se/inspire/inspire/wfs"
LAN = "04"
USER_AGENT = "Lansstyrelsen-Sodermanland-NRF/1.0 (naturrestaurering)"
TIMEOUT = 180


def _http(method: str, url: str, body=None, timeout: int = TIMEOUT) -> tuple[bytes, dict]:
    data = None if body is None else json.dumps(body).encode("utf-8")
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
    }
    if body is not None:
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    last: Exception | None = None
    for attempt in range(1, 5):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read(), dict(resp.headers)
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
            time.sleep(2 * attempt)
    raise RuntimeError(f"Misslyckades {method} {url}: {last}")


def _json(method: str, url: str, body=None, timeout: int = TIMEOUT):
    raw, _ = _http(method, url, body, timeout=timeout)
    return json.loads(raw.decode("utf-8"))


def sokmodell(alla_inventeringar: bool) -> dict:
    return {
        "filled": False,
        "filtered": False,
        "searchAllInventeringar": alla_inventeringar,
        "searchLevels": [{"id": "geografi_", "searchLevels": [{"id": LAN}]}],
        "faltIdList": [],
    }


def hamta_faltid(alla: bool) -> tuple[list[str], dict]:
    result = _json("PUT", f"{HAGEN}/rest/base/perform", sokmodell(alla))
    falt = [str(x) for x in (result.get("faltIdList") or [])]
    lan = next((x for x in (result.get("lan") or []) if x.get("id") == LAN), {})
    return falt, lan


def exportera_csv(kind: str, body: dict) -> Path:
    endpoints = {
        "komplett": "/rest/base/generateCSV",
        "filtrerad": "/rest/base/generateCSVbySearch",
        "summerad": "/rest/base/generateCSVbySum",
    }
    path = endpoints[kind]
    res = _json("PUT", HAGEN + path, body, timeout=300)
    filename = res.get("string") if isinstance(res, dict) else None
    if not filename:
        raise RuntimeError(f"CSV-export {kind} gav inget filnamn: {res}")
    url = HAGEN + "/csv?id=" + urllib.parse.quote(filename)
    raw, headers = _http("GET", url, timeout=300)
    safe = filename.replace(" ", "_").replace(":", "-")
    dest = EXPORT_DIR / safe
    dest.write_bytes(raw)
    print(f"  CSV {kind}: {dest.name} ({len(raw)} byte)")
    return dest


def hamta_wfs(url: str, type_name: str, dest: Path, cql: str) -> int:
    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typeName": type_name,
        "outputFormat": "application/json",
        "srsName": "EPSG:3006",
        "maxFeatures": "20000",
        "cql_filter": cql,
    }
    full = url + "?" + urllib.parse.urlencode(params)
    raw, _ = _http("GET", full, timeout=300)
    dest.write_bytes(raw)
    try:
        n = len(json.loads(raw.decode("utf-8")).get("features") or [])
    except Exception:
        n = -1
    print(f"  WFS {type_name}: {n} objekt -> {dest.name} ({len(raw)} byte)")
    return n


def _bbox_from_geojson(path: Path) -> str | None:
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    xs: list[float] = []
    ys: list[float] = []

    def walk(coords):
        if isinstance(coords, (int, float)):
            return
        if coords and isinstance(coords[0], (int, float)):
            xs.append(float(coords[0]))
            ys.append(float(coords[1]))
            return
        for c in coords:
            walk(c)

    for feat in data.get("features") or []:
        geom = (feat.get("geometry") or {}).get("coordinates")
        if geom:
            walk(geom)
    if not xs:
        return None
    pad = 500
    return f"{min(xs)-pad},{min(ys)-pad},{max(xs)+pad},{max(ys)+pad}"


def hamta_naturtyper_for_faltid(dest: Path, faltid: set[str], aob_path: Path) -> int:
    """Naturtypslagret saknar lanskod; hamtas med BBOX och filtreras pa falt-ID."""
    bbox = _bbox_from_geojson(aob_path)
    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typeName": "inspire:HB.Angs-och_betesmarksinventeringen_naturtyper",
        "outputFormat": "application/json",
        "srsName": "EPSG:3006",
        "maxFeatures": "50000",
    }
    if bbox:
        params["bbox"] = bbox + ",EPSG:3006"
    full = WFS_NATURTYP + "?" + urllib.parse.urlencode(params)
    try:
        raw, _ = _http("GET", full, timeout=300)
        data = json.loads(raw.decode("utf-8"))
    except Exception as e:
        print(f"  Naturtyper WFS hoppades over: {e}")
        return 0
    feats = [
        f
        for f in (data.get("features") or [])
        if str((f.get("properties") or {}).get("faltid") or "") in faltid
    ]
    data["features"] = feats
    data["numberReturned"] = len(feats)
    dest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"  WFS naturtyper: {len(feats)} objekt -> {dest.name}")
    return len(feats)


def hamta_objekt(falt_id: str) -> tuple[str, str, int]:
    safe = falt_id.replace("/", "-")
    dest = REPORT_DIR / f"{safe}.json"
    if dest.exists() and dest.stat().st_size > 0:
        return falt_id, "finns", dest.stat().st_size
    url = f"{HAGEN}/rest/base/object/{urllib.parse.quote(falt_id)}"
    raw, _ = _http("GET", url, timeout=60)
    dest.write_bytes(raw)
    return falt_id, "ok", len(raw)


def main() -> None:
    for d in (EXPORT_DIR, REPORT_DIR, GIS_DIR):
        d.mkdir(parents=True, exist_ok=True)

    print("Soker TUVA Sodermanland (senaste inventering) ...")
    falt_senaste, lan_senaste = hamta_faltid(False)
    print(f"  {len(falt_senaste)} fält-ID, areal {lan_senaste.get('areal')} ha")

    print("Soker TUVA Sodermanland (alla inventeringsdatum) ...")
    falt_alla, lan_alla = hamta_faltid(True)
    print(f"  {len(falt_alla)} fält-ID, areal {lan_alla.get('areal')} ha")

    print("Exporterar CSV ...")
    csv_alla = exportera_csv(
        "komplett",
        {"faltIdList": falt_alla, "searchAllInventeringar": True},
    )
    csv_senaste = exportera_csv(
        "komplett",
        {"faltIdList": falt_senaste, "searchAllInventeringar": False},
    )
    csv_sum = exportera_csv(
        "summerad",
        {**sokmodell(True), "faltIdList": falt_alla, "filtered": False},
    )

    print("Hamtat WFS-kartskikt ...")
    n_aob = hamta_wfs(
        WFS,
        "opendata:angs_och_betesmarkinventering",
        GIS_DIR / "angs_och_betesmark_sodermanland.geojson",
        "lans_kod='04'",
    )
    n_nt = hamta_naturtyper_for_faltid(
        GIS_DIR / "naturtyper_sodermanland.geojson",
        set(falt_alla),
        GIS_DIR / "angs_och_betesmark_sodermanland.geojson",
    )

    print(f"Hamtar {len(falt_alla)} objektrapporter ...")
    n_ok = n_skip = n_fail = 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(hamta_objekt, fid) for fid in falt_alla]
        for i, fut in enumerate(as_completed(futs), start=1):
            try:
                _, status, _ = fut.result()
                if status == "ok":
                    n_ok += 1
                else:
                    n_skip += 1
            except Exception as e:
                n_fail += 1
                if n_fail <= 5:
                    print(f"  FEL: {e}")
            if i % 500 == 0:
                print(f"  {i}/{len(falt_alla)}")

    # Index från kompletta CSV:n (första kolumnen är Fält-ID)
    index_rows: list[dict] = []
    if csv_alla.exists():
        text = csv_alla.read_text(encoding="utf-8-sig", errors="replace")
        reader = csv.DictReader(text.splitlines(), delimiter=";")
        seen: set[str] = set()
        for row in reader:
            fid = (row.get("Fält-ID") or row.get(" Fält-ID") or "").strip()
            if not fid or fid in seen:
                continue
            seen.add(fid)
            index_rows.append(
                {
                    "faltid": fid,
                    "lan": row.get("Län") or row.get("Län"),
                    "kommun": row.get("Kommun"),
                    "areal_ha": row.get("Areal (ha)"),
                    "markslag": row.get("Markslag"),
                    "inventeringsdatum": row.get("Inventeringsdatum"),
                    "fastighet": row.get("Fastighetsnamn"),
                    "objektrapport_ui": f"https://etjanst.sjv.se/tuvaut/?f=&id={fid}",
                    "objektrapport_api": f"{HAGEN}/rest/base/object/{fid}",
                    "lokal_json": f"docs/tuva/sodermanland/objektrapporter/{fid.replace('/', '-')}.json",
                }
            )

    index_csv = OUT / "index.csv"
    fields = [
        "faltid",
        "lan",
        "kommun",
        "areal_ha",
        "markslag",
        "inventeringsdatum",
        "fastighet",
        "objektrapport_ui",
        "objektrapport_api",
        "lokal_json",
    ]
    with index_csv.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter=";")
        w.writeheader()
        w.writerows(index_rows)

    meta = {
        "kalla": "https://etjanst.sjv.se/tuvaut/",
        "api": f"{HAGEN}/rest/base",
        "lan": "Södermanlands län (04)",
        "hamtat_datum": date.today().isoformat(),
        "antal_faltid_senaste": len(falt_senaste),
        "antal_faltid_alla": len(falt_alla),
        "areal_ha_senaste": lan_senaste.get("areal"),
        "areal_ha_alla": lan_alla.get("areal"),
        "kommuner": lan_senaste.get("kommun"),
        "csv_alla": str(csv_alla.relative_to(REPO)).replace("\\", "/"),
        "csv_senaste": str(csv_senaste.relative_to(REPO)).replace("\\", "/"),
        "csv_summerad": str(csv_sum.relative_to(REPO)).replace("\\", "/"),
        "wfs_aob_objekt": n_aob,
        "wfs_naturtyper_objekt": n_nt,
        "objektrapporter_nedladdade": n_ok,
        "objektrapporter_fanns": n_skip,
        "objektrapporter_fel": n_fail,
    }
    (OUT / "index.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("\nKlart.")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
