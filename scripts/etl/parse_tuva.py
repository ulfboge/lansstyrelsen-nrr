#!/usr/bin/env python3
"""
parse_tuva.py
-------------
Extraherar strukturerad information ur TUVA-objektrapporter (JSON) fran
Jordbruksverkets angs- och betesmarksinventering for Sodermanlands lan,
som underlag for NNK-statusbedomning och "Blankett forvaltarkunskap".

TUVA-objektrapporten ar uppbyggd av tva delar per fil:
  - "headers": ett schema-trad (id/title/varde=alltid 0.0/underrubriker)
    som beskriver VILKA falt som finns for just detta objekt - id-strangen
    ("GR:naturtyper:6270_-_Silikatgräsmarker", "FF:KÄRLV:14041:24" osv)
    ar nyckeln, "title" ar det manskligt lasbara namnet.
  - "resultat": en lista med ett varde-dict per delyta/inventeringstillfalle
    dar samma id-strangar ar nycklar mot FAKTISKA inrapporterade varden
    (areal i ha, textuella forekomstgrader som "Riklig forekomst", eller
    procentandelar for havd/fuktighet/produktionshojande atgarder).
    (Headers-tradets egna "value"-falt ar alltid 0.0 - det ar bara metadata,
    de riktiga vardena ligger i resultat[].values.)

Kalla for varje rad: index.csv (faltid -> objektrapport_ui), byggt av
TUVA-hamtningsskriptet.

Utdata (data/analysis/):
  tuva_faltmetadata.csv  en rad per falt-ID (grundvarden)
  tuva_naturtyper.csv    en rad per naturtyp/delyta inom faltet (areal i ha)
  tuva_arter.csv         en rad per registrerad art/artgrupp (signalarter
                          karlvaxter, trad och buskar) med forekomstgrad
  tuva_havd.csv          en rad per havd-/fuktighets-/paverkansvarde (%)
  tuva_parselogg.csv     vad som kunde/inte kunde tolkas per fil

Stods batchning likt parse_bevarandeplaner.py:
  python parse_tuva.py --start N --end M --suffix S   (delresultat)
  python parse_tuva.py --merge                         (slar ihop batchar)
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DOC_DIR = REPO / "docs" / "tuva" / "sodermanland" / "objektrapporter"
INDEX_CSV = REPO / "docs" / "tuva" / "sodermanland" / "index.csv"
OUT_DIR = REPO / "data" / "analysis"
BATCH_DIR = OUT_DIR / "_batches_tuva"

FIELDS = {
    "tuva_faltmetadata.csv": ["faltid", "lan", "kommun", "areal_ha", "markslag",
                               "fastighet", "inventeringsdatum", "karaktar_text",
                               "floravarden_antal", "kalla_url"],
    "tuva_naturtyper.csv": ["faltid", "naturtypskod", "naturtypsnamn", "areal_ha", "kalla_url"],
    "tuva_arter.csv": ["faltid", "artgrupp", "artnamn", "forekomst", "kalla_url"],
    "tuva_havd.csv": ["faltid", "kategori", "varde_namn", "andel_procent", "kalla_url"],
    "tuva_parselogg.csv": ["faltid", "fil", "resultat_antal", "naturtyper_hittade",
                            "arter_hittade", "havd_hittade", "fel"],
}

NATURTYP_KOD_RE = re.compile(r"^(\d{3,4})\s*-\s*(.+)$")


def load_index():
    """faltid -> {lan, kommun, areal_ha, markslag, inventeringsdatum, fastighet, url}"""
    idx = {}
    with INDEX_CSV.open(encoding="utf-8-sig") as f:
        r = csv.DictReader(f, delimiter=";")
        for row in r:
            faltid = row.get("faltid")
            if not faltid:
                continue
            idx[faltid] = {
                "lan": row.get("lan", ""),
                "kommun": row.get("kommun", ""),
                "areal_ha": row.get("areal_ha", ""),
                "markslag": row.get("markslag", ""),
                "inventeringsdatum": row.get("inventeringsdatum", ""),
                "fastighet": row.get("fastighet", ""),
                "url": row.get("objektrapport_ui", ""),
            }
    return idx


def build_id_title_map(headers, out=None):
    """Vandrar headers-tradet rekursivt och bygger id -> title."""
    if out is None:
        out = {}
    for h in headers or []:
        hid = h.get("id")
        if hid:
            out[hid] = h.get("title", hid)
        build_id_title_map(h.get("headers") or [], out)
    return out


def parse_one(data, faltid, url, rows_meta, rows_nt, rows_art, rows_havd):
    id_title = build_id_title_map(data.get("headers") or [])
    resultat = data.get("resultat") or []
    found_nt = found_art = found_havd = False

    for values in (r.get("values", {}) for r in resultat):
        # --- Grundvarden / metadata ---
        karaktar = values.get("GR:karaktar", "")
        flora = values.get("GR:kvaliteter:Fl", "")
        rows_meta.append({
            "faltid": faltid,
            "lan": values.get("GR:lan", ""),
            "kommun": values.get("GR:kommun", ""),
            "areal_ha": values.get("GR:areal", ""),
            "markslag": values.get("GR:markslag", ""),
            "fastighet": values.get("GR:fastighet", ""),
            "inventeringsdatum": values.get("GR:inventeringsdatum", ""),
            "karaktar_text": karaktar,
            "floravarden_antal": flora,
            "kalla_url": url,
        })

        # --- Naturtyper (GR:naturtyper:<slug> -> areal i ha) ---
        for key, val in values.items():
            if not key.startswith("GR:naturtyper:"):
                continue
            title = id_title.get(key, key)
            # title-format: "6270 - Silikatgräsmarker (ha)" eller "KULTIVERAD FODERMARK (ha)"
            namn = re.sub(r"\s*\(ha\)\s*$", "", title).strip()
            m = NATURTYP_KOD_RE.match(namn)
            kod = m.group(1) if m else ""
            if m:
                namn = m.group(2).strip()
            rows_nt.append({
                "faltid": faltid, "naturtypskod": kod, "naturtypsnamn": namn,
                "areal_ha": val, "kalla_url": url,
            })
            found_nt = True

        # --- Arter: signalarter karlvaxter (FF:KÄRLV:*) samt trad/buskar (TB:ARTER:*) ---
        for prefix, grupp in (("FF:KÄRLV:", "Signalarter kärlväxter"), ("TB:ARTER:", "Träd och buskar")):
            for key, val in values.items():
                if not key.startswith(prefix):
                    continue
                artnamn = id_title.get(key, key)
                rows_art.append({
                    "faltid": faltid, "artgrupp": grupp, "artnamn": artnamn,
                    "forekomst": val, "kalla_url": url,
                })
                found_art = True

        # --- Hävd / fuktighet / påverkan / markförhållanden (HPM:*, procentvärden) ---
        for key, val in values.items():
            if not key.startswith("HPM:"):
                continue
            title = id_title.get(key, key)
            varde_namn = re.sub(r"\s*\(%\)\s*$", "", title).strip()
            # kategori = HPM:HÄVDSTAT / HPM:FUKT / HPM:PRODHÖJ / HPM:STENJORD osv
            kategori_id = ":".join(key.split(":")[:2])
            kategori = id_title.get(kategori_id, kategori_id)
            rows_havd.append({
                "faltid": faltid, "kategori": kategori, "varde_namn": varde_namn,
                "andel_procent": val, "kalla_url": url,
            })
            found_havd = True

    return found_nt, found_art, found_havd, len(resultat)


def merge_batches():
    for name, fields in FIELDS.items():
        all_rows = []
        for batch_csv in sorted(BATCH_DIR.glob(f"*/{name}")):
            with batch_csv.open(encoding="utf-8-sig") as f:
                all_rows.extend(csv.DictReader(f, delimiter=";"))
        p = OUT_DIR / name
        with p.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, delimiter=";")
            w.writeheader()
            for row in all_rows:
                w.writerow({k: row.get(k, "") for k in fields})
        print(f"  {name}: {len(all_rows)} rader (sammanslaget) -> {p}")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    argv = sys.argv[1:]
    if "--merge" in argv:
        merge_batches()
        return
    start, end, suffix = 0, None, None
    if "--start" in argv:
        start = int(argv[argv.index("--start") + 1])
    if "--end" in argv:
        end = int(argv[argv.index("--end") + 1])
    if "--suffix" in argv:
        suffix = argv[argv.index("--suffix") + 1]

    idx = load_index()
    print(f"{len(idx)} falt i index.csv")

    rows_meta, rows_nt, rows_art, rows_havd, rows_log = [], [], [], [], []

    all_files = sorted(DOC_DIR.glob("*.json"))
    files = all_files[start:end] if (start or end is not None) else all_files
    print(f"{len(files)} JSON-filer att tolka (av {len(all_files)} totalt, start={start} end={end})")

    for i, path in enumerate(files, 1):
        faltid = path.stem
        meta = idx.get(faltid, {})
        url = meta.get("url", "")
        log = {"faltid": faltid, "fil": path.name, "resultat_antal": 0,
               "naturtyper_hittade": False, "arter_hittade": False,
               "havd_hittade": False, "fel": ""}
        try:
            with path.open(encoding="utf-8") as f:
                data = json.load(f)
            found_nt, found_art, found_havd, n_res = parse_one(
                data, faltid, url, rows_meta, rows_nt, rows_art, rows_havd
            )
            log["resultat_antal"] = n_res
            log["naturtyper_hittade"] = found_nt
            log["arter_hittade"] = found_art
            log["havd_hittade"] = found_havd
        except Exception as e:
            log["fel"] = str(e)
        rows_log.append(log)
        if i % 200 == 0:
            print(f"  {i}/{len(files)}")

    out_dir = (BATCH_DIR / suffix) if suffix else OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    def write_csv(name, rows):
        p = out_dir / name
        fields = FIELDS[name]
        with p.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, delimiter=";")
            w.writeheader()
            for r in rows:
                w.writerow({k: r.get(k, "") for k in fields})
        print(f"  {name}: {len(rows)} rader -> {p}")

    write_csv("tuva_faltmetadata.csv", rows_meta)
    write_csv("tuva_naturtyper.csv", rows_nt)
    write_csv("tuva_arter.csv", rows_art)
    write_csv("tuva_havd.csv", rows_havd)
    write_csv("tuva_parselogg.csv", rows_log)

    n = len(rows_log)
    any_nt = sum(1 for l in rows_log if l["naturtyper_hittade"])
    any_art = sum(1 for l in rows_log if l["arter_hittade"])
    any_havd = sum(1 for l in rows_log if l["havd_hittade"])
    errs = sum(1 for l in rows_log if l["fel"])
    print(f"\nSammanfattning: {n} filer. Naturtyper hittade i {any_nt}. "
          f"Arter hittade i {any_art}. Hävd-data hittade i {any_havd}. Fel: {errs}.")


if __name__ == "__main__":
    main()
