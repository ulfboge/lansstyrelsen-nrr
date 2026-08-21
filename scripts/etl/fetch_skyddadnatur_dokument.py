"""
fetch_skyddadnatur_dokument.py
------------------------------
Hämtar samtliga beslutsdokument (främst bevarandeplaner) för Natura 2000-
områden i Södermanlands län från Naturvårdsverkets öppna REST-API, samma
källa som kartverktyget Skyddad natur.

Källa:
  https://skyddadnatur.naturvardsverket.se/
  https://geodata.naturvardsverket.se/n2000/rest/v3
  https://geodata.naturvardsverket.se/handlingar/rest/dokument/{id}

Utdata: docs/skyddadnatur/natura2000/

Krav: Python 3.10+ (endast standardbiblioteket)
"""

from __future__ import annotations

import csv
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT_DIR = REPO / "docs" / "skyddadnatur" / "natura2000"
DOC_DIR = OUT_DIR / "dokument"

BASE = "https://geodata.naturvardsverket.se/n2000/rest/v3"
LAN = "D"  # Södermanlands län
LIMIT = 1000
USER_AGENT = "Lansstyrelsen-Sodermanland-NRF/1.0 (naturrestaurering)"
MAX_RETRIES = 4
TIMEOUT = 120


def _request(url: str, binary: bool = False):
    req = urllib.request.Request(
        url,
        headers={"Accept": "*/*", "User-Agent": USER_AGENT},
    )
    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                data = resp.read()
                headers = dict(resp.headers)
                if binary:
                    return data, headers
                return json.loads(data.decode("utf-8")), headers
        except urllib.error.HTTPError as e:
            if e.code in (204, 404) and not binary:
                return [], {}
            last_err = e
            if e.code in (429, 500, 502, 503, 504) and attempt < MAX_RETRIES:
                time.sleep(2 * attempt)
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
            time.sleep(2 * attempt)
    raise RuntimeError(f"Misslyckades att hämta {url}: {last_err}")


def _safe_name(text: str) -> str:
    text = urllib.parse.unquote(text or "")
    text = text.replace("/", "-").replace("\\", "-")
    text = re.sub(r'[<>:"|?*]', "_", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text or "dokument"


def _filename(site_kod: str, doc: dict) -> str:
    original = _safe_name(doc.get("namn") or "")
    typ = _safe_name(doc.get("typ") or "dokument")
    ext = Path(original).suffix.lower() if original else ""
    if not ext:
        mime = (doc.get("mimeType") or "").lower()
        ext = ".pdf" if "pdf" in mime or mime == ".pdf" else ".bin"
        if original and not original.endswith(ext):
            original = original + ext
    if original.lower().startswith(site_kod.lower()):
        stem = Path(original).stem
        return f"{stem}{ext}"
    stem = Path(original).stem
    if stem.lower().startswith("bevarandeplan"):
        return f"{site_kod}_{typ}_{stem}{ext}"
    return f"{site_kod}_{typ}_{stem}{ext}"


def hamta_omraden() -> list[dict]:
    url = f"{BASE}/omrade?lan={urllib.parse.quote(LAN)}&limit={LIMIT}"
    omraden, _ = _request(url)
    omraden = sorted(omraden, key=lambda o: o.get("kod") or "")
    return omraden


def hamta_dokument(kod: str) -> list[dict]:
    docs, _ = _request(f"{BASE}/omrade/{urllib.parse.quote(kod)}/dokument")
    return docs or []


def ladda_ned_fil(url: str, dest: Path) -> int:
    data, _ = _request(url, binary=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return len(data)


def main() -> None:
    DOC_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Hämtar Natura 2000-områden i län {LAN} …")
    omraden = hamta_omraden()
    print(f"Hittade {len(omraden)} områden.")

    index: list[dict] = []
    n_ok = n_skip = n_fail = n_empty = 0

    for i, omr in enumerate(omraden, start=1):
        kod = omr.get("kod") or ""
        namn = omr.get("namn") or ""
        docs = hamta_dokument(kod)
        if not docs:
            n_empty += 1
            index.append(
                {
                    "sitecode": kod,
                    "namn": namn,
                    "omradestyp": (omr.get("omradesTyp") or {}).get("key"),
                    "areal_ha": omr.get("areaHa"),
                    "dokument_id": "",
                    "dokument_typ": "",
                    "dokument_namn": "",
                    "mime": "",
                    "url": "",
                    "lokal_fil": "",
                    "status": "saknas",
                    "storlek_byte": 0,
                }
            )
            print(f"[{i}/{len(omraden)}] {kod} {namn}: inga dokument")
            continue

        used_names: set[str] = set()
        for doc in docs:
            fname = _filename(kod, doc)
            if fname in used_names:
                stem, ext = Path(fname).stem, Path(fname).suffix
                fname = f"{stem}_{doc.get('id')}{ext}"
            used_names.add(fname)
            dest = DOC_DIR / fname
            url = doc.get("fileUrl") or (
                f"https://geodata.naturvardsverket.se/handlingar/rest/dokument/{doc.get('id')}"
            )
            status = "ok"
            size = dest.stat().st_size if dest.exists() else 0
            try:
                if dest.exists() and dest.stat().st_size > 0:
                    n_skip += 1
                    status = "finns"
                    size = dest.stat().st_size
                else:
                    size = ladda_ned_fil(url, dest)
                    n_ok += 1
                    time.sleep(0.15)
            except Exception as e:
                n_fail += 1
                status = f"fel: {e}"
                size = 0
                print(f"[{i}/{len(omraden)}] FEL {kod} {fname}: {e}")

            index.append(
                {
                    "sitecode": kod,
                    "namn": namn,
                    "omradestyp": (omr.get("omradesTyp") or {}).get("key"),
                    "areal_ha": omr.get("areaHa"),
                    "dokument_id": doc.get("id"),
                    "dokument_typ": doc.get("typ"),
                    "dokument_namn": doc.get("namn"),
                    "mime": doc.get("mimeType"),
                    "url": url,
                    "lokal_fil": str(dest.relative_to(REPO)).replace("\\", "/"),
                    "status": status,
                    "storlek_byte": size,
                }
            )
        print(
            f"[{i}/{len(omraden)}] {kod} {namn}: "
            f"{len(docs)} dokument"
        )

    index_csv = OUT_DIR / "index.csv"
    fields = [
        "sitecode",
        "namn",
        "omradestyp",
        "areal_ha",
        "dokument_id",
        "dokument_typ",
        "dokument_namn",
        "mime",
        "url",
        "lokal_fil",
        "status",
        "storlek_byte",
    ]
    with index_csv.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter=";")
        w.writeheader()
        w.writerows(index)

    meta = {
        "kalla": "https://skyddadnatur.naturvardsverket.se/",
        "api": BASE,
        "lan": "Södermanlands län (D)",
        "hamtat_datum": date.today().isoformat(),
        "antal_omraden": len(omraden),
        "antal_dokumentrader": len(index),
        "nedladdade": n_ok,
        "redan_fanns": n_skip,
        "saknade": n_empty,
        "fel": n_fail,
        "total_byte": sum(r["storlek_byte"] for r in index if r["status"] in ("ok", "finns")),
    }
    (OUT_DIR / "index.json").write_text(
        json.dumps({"meta": meta, "dokument": index}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("\nKlart.")
    print(f"  Områden:     {len(omraden)}")
    print(f"  Nedladdade:  {n_ok}")
    print(f"  Redan fanns: {n_skip}")
    print(f"  Saknade:     {n_empty}")
    print(f"  Fel:         {n_fail}")
    print(f"  Index:       {index_csv}")


if __name__ == "__main__":
    main()
