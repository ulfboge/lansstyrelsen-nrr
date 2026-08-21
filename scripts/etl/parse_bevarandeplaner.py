#!/usr/bin/env python3
"""
parse_bevarandeplaner.py
-------------------------
Extraherar strukturerad information ur Skyddad naturs bevarandeplaner
(PDF) för Natura 2000-omraden i Sodermanlands lan, som underlag for
NNK-statusbedomning och "Blankett forvaltarkunskap".

Tva kanda malldesigner forekommer i materialet:
  A) Aldre mall (fore ca 2013): tabell "Ingaende naturtyper enligt
     habitatdirektivet" (kod, namn, areal), separata artlistor per
     direktiv, samt narrativ text med "Karaktarsarter:"-rader.
  B) Nyare mall (fran ca 2013): en sektion per naturtyp/art med
     "Areal: X ha", "Beskrivning", "Bevarandemal", "Bevarandetillstand"
     (Gynnsamt / Ej Gynnsamt), samt en avslutande sektion
     "Exempel pa arter i omradet" indelad per artgrupp.

Bada mallarna forsoks tolkas per fil; vad som inte gick att tolka
loggas i parse_log snarare an att tystas ner.

Kalla for varje rad: index.csv (sitecode -> dokument-URL), byggt av
fetch_skyddadnatur_dokument.py.

Utdata (data/analysis/):
  bevarandeplan_platser.csv     en rad per Natura 2000-omrade (metadata)
  bevarandeplan_naturtyper.csv  en rad per naturtyp i planen (mall A/B)
  bevarandeplan_arter.csv       en rad per utpekad art (habitat-/fageldirektivet)
  bevarandeplan_exempelarter.csv en rad per art i "Exempel pa arter i omradet" (mall B)
  bevarandeplan_parselogg.csv   vad som kunde/inte kunde tolkas per fil
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import pdfplumber

REPO = Path(__file__).resolve().parents[2]
DOC_DIR = REPO / "docs" / "skyddadnatur" / "natura2000" / "dokument"
INDEX_CSV = REPO / "docs" / "skyddadnatur" / "natura2000" / "index.csv"
OUT_DIR = REPO / "data" / "analysis"

NATURTYP_RE = re.compile(r"^(\d{4})\s*-\s*(.+)$")
FAGEL_RE = re.compile(r"^(A\d{3})\s*-\s*(.+)$")
HABITATART_RE = re.compile(r"^(?:Nr\s*)?(\d{3,4})\s+([A-ZÅÄÖa-zåäö][\w \-]+?)\s*\(([A-Z][a-z]+ [a-z\-]+)\)\s*$")

ARTGRUPP_RUBRIKER = {
    "Växter", "Kärlväxter", "Mossor", "Lavar", "Svampar",
    "Insekter", "Fjärilar", "Skalbaggar", "Fåglar", "Fiskar",
    "Kräftdjur", "Grod- och kräldjur", "Däggdjur", "Trollsländor",
}


def load_index():
    """sitecode -> {namn, url (forsta Bevarandeplan-dokumentet), lokal_fil}"""
    idx = {}
    with INDEX_CSV.open(encoding="utf-8-sig") as f:
        r = csv.DictReader(f, delimiter=";")
        for row in r:
            kod = row["sitecode"]
            if not kod or row.get("status") not in ("ok", "finns"):
                continue
            # Forsta bevarandeplan-dokumentet racker - de flesta objekt har bara ett.
            if kod not in idx or "bevarandeplan" in (row.get("dokument_typ") or "").lower():
                idx[kod] = {
                    "namn": row["namn"],
                    "url": row["url"],
                    "lokal_fil": row["lokal_fil"],
                }
    return idx


def extract_metadata(text_p1_p2: str, sitecode: str):
    meta = {"sitecode": sitecode}
    m = re.search(r"Totalareal[:\s]*([\d\s]+)", text_p1_p2)
    if not m:
        m = re.search(r"Områdets totala areal:\s*([\d,\.\s]+)\s*ha", text_p1_p2)
    if m:
        meta["totalareal_ha"] = m.group(1).replace(" ", "").replace(",", ".")
    m = re.search(r"(?:Bevarandeplanen )?[Ff]astställd(?: av Länsstyrelsen)?:?\s*(\d{4}-\d{2}-\d{2})", text_p1_p2)
    if m:
        meta["faststalld_datum"] = m.group(1)
    m = re.search(r"Diarienummer\D*(\S[\d\-\.]+\d)", text_p1_p2)
    if not m:
        m = re.search(r"Dnr:?\s*([\d\-]+)", text_p1_p2)
    if m:
        meta["diarienummer"] = m.group(1)
    m = re.search(r"Kommun:\s*([^\n]+)", text_p1_p2)
    if m:
        meta["kommun"] = m.group(1).strip()
    return meta


def parse_mall_a(pdf, sitecode, url, rows_nt, rows_art):
    """Aldre mall: tabell 'Ingaende naturtyper...' + separata artlistor."""
    found_table = False
    found_arter = False
    for page in pdf.pages:
        text = page.extract_text() or ""
        if "Ingående naturtyper enligt habitatdirektivet" in text:
            for table in page.extract_tables():
                for row in table:
                    cells = [c for c in row if c]
                    if len(cells) < 2:
                        continue
                    kod, namn = cells[0], cells[1]
                    areal = cells[2] if len(cells) > 2 else ""
                    m = NATURTYP_RE.match(f"{kod} - {namn}") if kod and not re.match(r"^\d{4}$", kod) else None
                    if re.match(r"^\d{4}$", (kod or "").strip()):
                        rows_nt.append({
                            "sitecode": sitecode, "naturtypskod": kod.strip(),
                            "naturtypsnamn": (namn or "").strip(), "areal_ha": (areal or "").strip(),
                            "bevarandetillstand": "", "mall": "A", "kalla_url": url,
                        })
                        found_table = True
        if "Ingående arter enligt habitatdirektivet" in text or "Ingående arter enligt fågeldirektivet" in text:
            for line in text.splitlines():
                line = line.strip()
                fm = FAGEL_RE.match(line)
                hm = HABITATART_RE.match(line)
                if fm:
                    rows_art.append({
                        "sitecode": sitecode, "direktiv": "fagel", "kod": fm.group(1),
                        "namn": fm.group(2).split("(")[0].strip(),
                        "vetenskapligt_namn": (re.search(r"\(([^)]+)\)", fm.group(2)) or [None, ""])[1]
                        if re.search(r"\(([^)]+)\)", fm.group(2)) else "",
                        "kalla_url": url,
                    })
                    found_arter = True
                elif hm:
                    rows_art.append({
                        "sitecode": sitecode, "direktiv": "habitat", "kod": hm.group(1),
                        "namn": hm.group(2).strip(), "vetenskapligt_namn": hm.group(3).strip(),
                        "kalla_url": url,
                    })
                    found_arter = True
    return found_table, found_arter


def parse_mall_b(full_text, sitecode, url, rows_nt, rows_art):
    """Nyare mall: en sektion per naturtyp/art med Areal/Bevarandetillstand,
    foregangen av en sammanfattande lista "Naturtyper och arter som ska
    bevaras i omradet:".

    Rubrikformen "kod - namn" forekommer bade i sammanfattningslistan och
    som rubrik for den egna sektionen langre ner - dessutom kan enstaka
    "kod - text"-liknande rader smyga sig in fran den generiska inlednings-
    texten (t.ex. "2000 - naturtyperna och arterna har..." fran "Natura
    2000-"-radbrytningar). For att inte lata sadana falska traffar sluka
    hela efterfoljande sektioner (som hande med ett naivt icke-girigt
    sok-fram-till-"Bevarandetillstand"-monster) hittas forst ALLA
    rubrikpositioner, och varje sektions text avgransas till narmaste
    NASTA rubrik - inte till narmaste "Bevarandetillstand".
    """
    found_section = False
    summary_idx = full_text.find("Naturtyper och arter som ska bevaras i området")
    if summary_idx == -1:
        return False
    body = full_text[summary_idx:]

    heading_re = re.compile(r"^(?P<kod>\d{4}|A\d{3})\s*-\s*(?P<namn>[^\n]+)$", re.MULTILINE)
    matches = list(heading_re.finditer(body))
    if not matches:
        return False

    # Sammanfattningslistan direkt efter rubriken ar en tatt packad svit av
    # rubriker (en per rad). Anvand den for att avgora VILKA koder som ar
    # riktiga naturtyper/arter i just denna plan - annars kan en enstaka
    # sen "kod - text"-liknande rad langt bort i dokumentet (t.ex. ett
    # diarienummer som radbryts som "3576-2010." eller "Natura 2000-"
    # som radbryts till "2000 - naturtyperna...") felaktigt tolkas som en
    # egen naturtyp/art.
    valid_koder = set()
    prev_end = None
    for m in matches:
        if prev_end is not None and m.start() - prev_end > 150:
            break
        valid_koder.add(m.group("kod"))
        prev_end = m.end()

    occurrences = {}
    for m in matches:
        occurrences.setdefault(m.group("kod"), []).append(m)

    for kod, occ in occurrences.items():
        if kod not in valid_koder:
            continue  # inte en del av sammanfattningslistan - troligen falsk traff
        heading_match = occ[-1]  # sista forekomsten = den egna sektionsrubriken, inte sammanfattningslistan
        namn = heading_match.group("namn").strip()
        start = heading_match.end()
        later_starts = [m.start() for m in matches if m.start() > heading_match.start()]
        end = min(later_starts) if later_starts else len(body)
        section_text = body[start:end]

        areal_m = re.search(r"Areal:\s*([\d,\.]+)\s*ha", section_text)
        areal = areal_m.group(1).replace(",", ".") if areal_m else ""
        status_m = re.search(r"Bevarandetillstånd\s*\n?\s*(Gynnsamt|Ej [Gg]ynnsamt|Okänt)", section_text)
        status = status_m.group(1).strip() if status_m else ""

        # Habitatdirektivets bilaga II-arter (icke-faglar) har OCKSA 4-siffriga
        # koder, t.ex. 1013 Kalkkarrsgrynsnacka (Vertigo geyeri) eller 1903
        # Gulyxne (Liparis loeselii) - de gar alltsa INTE att skilja fran
        # naturtypskoder enbart pa att koden ar 4 siffror. Formatet skiljer
        # sig dock: artrubriker foljer "Svenskt namn, Vetenskapligt namn"
        # (komma + kursiverat Genus-epitet), vilket naturtypsrubriker aldrig
        # gor - anvand det som avgorande signal istallet for kodformatet.
        sci = ""
        nm = namn
        sm = re.search(r",\s*([A-ZÅÄÖ][a-zåäö]+ [a-zåäö\-]+)$", namn)
        if sm:
            sci = sm.group(1)
            nm = namn.split(",")[0].strip()

        if re.match(r"^\d{4}$", kod) and not sm:
            rows_nt.append({
                "sitecode": sitecode, "naturtypskod": kod, "naturtypsnamn": namn,
                "areal_ha": areal, "bevarandetillstand": status, "mall": "B", "kalla_url": url,
            })
        else:
            rows_art.append({
                "sitecode": sitecode, "direktiv": "fagel" if kod.startswith("A") else "habitat",
                "kod": kod, "namn": nm, "vetenskapligt_namn": sci,
                "bevarandetillstand": status, "kalla_url": url,
            })
        found_section = True
    return found_section


def parse_exempelarter(full_text, sitecode, url, rows_ex):
    idx = full_text.find("Exempel på arter i området")
    if idx == -1:
        return False
    tail = full_text[idx + len("Exempel på arter i området"):]
    end = re.search(r"\n(Referenser|Bilagor|Inventeringar)\b", tail)
    block = tail[: end.start()] if end else tail[:3000]
    grupp = None
    found = False
    for raw in block.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line in ARTGRUPP_RUBRIKER:
            grupp = line
            continue
        if grupp and len(line) < 60 and not line.startswith(("•", "-", "http")):
            rows_ex.append({"sitecode": sitecode, "artgrupp": grupp, "artnamn": line, "kalla_url": url})
            found = True
    return found


CID_RE = re.compile(r"\(cid:\d+\)")

def clean_text(text: str) -> str:
    """pdfplumber renderar ibland punktlistemarkorer som '(cid:153)' etc
    nar teckensnittets bullet-glyph saknar Unicode-mappning. Stad upp for
    lasbarhet i utdata."""
    return CID_RE.sub("•", text)

def parse_karaktarsarter(full_text, sitecode, url, rows_kar):
    found = False
    for m in re.finditer(r"Karaktärsarter:\s*([^\n]+(?:\n(?![A-ZÅÄÖ][a-zåäö ]+\n)[^\n]+)*)", full_text):
        snippet = clean_text(m.group(1).strip())
        # gissa vilken naturtyp stycket tillhor genom att leta senaste kursiverade rubrik ovanfor - for grovt, hoppa over
        rows_kar.append({"sitecode": sitecode, "karaktarsarter_text": snippet, "kalla_url": url})
        found = True
    return found


BATCH_DIR = OUT_DIR / "_batches"

FIELDS = {
    "bevarandeplan_platser.csv": ["sitecode", "namn", "kommun", "totalareal_ha", "diarienummer", "faststalld_datum", "kalla_url"],
    "bevarandeplan_naturtyper.csv": ["sitecode", "naturtypskod", "naturtypsnamn", "areal_ha", "bevarandetillstand", "mall", "kalla_url"],
    "bevarandeplan_arter.csv": ["sitecode", "direktiv", "kod", "namn", "vetenskapligt_namn", "bevarandetillstand", "kalla_url"],
    "bevarandeplan_exempelarter.csv": ["sitecode", "artgrupp", "artnamn", "kalla_url"],
    "bevarandeplan_karaktarsarter.csv": ["sitecode", "karaktarsarter_text", "kalla_url"],
    "bevarandeplan_parselogg.csv": ["sitecode", "fil", "sidor", "mall_a_tabell", "mall_a_arter",
                                     "mall_b_sektioner", "exempelarter", "karaktarsarter", "fel"],
}


def merge_batches():
    """Slar ihop alla _batches/<suffix>/*.csv till de slutgiltiga filerna i OUT_DIR.
    Anvands nar filerna tolkats i flera omgangar (t.ex. pga tidsgranser per korning)."""
    for name, fields in FIELDS.items():
        all_rows = []
        for batch_csv in sorted(BATCH_DIR.glob(f"*/{name}")):
            with batch_csv.open(encoding="utf-8-sig") as f:
                r = csv.DictReader(f, delimiter=";")
                all_rows.extend(r)
        p = OUT_DIR / name
        with p.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, delimiter=";")
            w.writeheader()
            for row in all_rows:
                w.writerow({k: row.get(k, "") for k in fields})
        print(f"  {name}: {len(all_rows)} rader (sammanslaget) -> {p}")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Valfri batchning: `python parse_bevarandeplaner.py --start N --end M --suffix S`
    # tolkar bara files[N:M] och skriver till data/analysis/_batches/S/*.csv, sa att
    # hela korpusen kan behandlas i flera kortare omgangar. `--merge` slar sedan ihop
    # alla batchar till de slutgiltiga filerna i data/analysis/.
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
    print(f"{len(idx)} platser i index.csv")

    rows_platser, rows_nt, rows_art, rows_ex, rows_kar, rows_log = [], [], [], [], [], []

    all_files = sorted(DOC_DIR.glob("*.pdf"))
    files = all_files[start:end] if (start or end is not None) else all_files
    print(f"{len(files)} PDF-filer att tolka (av {len(all_files)} totalt, start={start} end={end})")

    for i, path in enumerate(files, 1):
        sitecode = path.name.split("_", 1)[0]
        meta = idx.get(sitecode, {})
        url = meta.get("url", "")
        log = {"sitecode": sitecode, "fil": path.name, "sidor": 0,
               "mall_a_tabell": False, "mall_a_arter": False,
               "mall_b_sektioner": False, "exempelarter": False,
               "karaktarsarter": False, "fel": ""}
        try:
            with pdfplumber.open(path) as pdf:
                log["sidor"] = len(pdf.pages)
                head_text = "\n".join((p.extract_text() or "") for p in pdf.pages[:2])
                site_meta = extract_metadata(head_text, sitecode)
                site_meta["namn"] = meta.get("namn", "")
                site_meta["kalla_url"] = url
                rows_platser.append(site_meta)

                a_tab, a_art = parse_mall_a(pdf, sitecode, url, rows_nt, rows_art)
                log["mall_a_tabell"], log["mall_a_arter"] = a_tab, a_art

                full_text = "\n".join((p.extract_text() or "") for p in pdf.pages)
                log["mall_b_sektioner"] = parse_mall_b(full_text, sitecode, url, rows_nt, rows_art)
                log["exempelarter"] = parse_exempelarter(full_text, sitecode, url, rows_ex)
                log["karaktarsarter"] = parse_karaktarsarter(full_text, sitecode, url, rows_kar)
        except Exception as e:
            log["fel"] = str(e)
        rows_log.append(log)
        if i % 25 == 0:
            print(f"  {i}/{len(files)}")

    out_dir = (BATCH_DIR / suffix) if suffix else OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    def write_csv(name, rows, fields):
        p = out_dir / name
        with p.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, delimiter=";")
            w.writeheader()
            for r in rows:
                w.writerow({k: r.get(k, "") for k in fields})
        print(f"  {name}: {len(rows)} rader -> {p}")

    write_csv("bevarandeplan_platser.csv", rows_platser, FIELDS["bevarandeplan_platser.csv"])
    write_csv("bevarandeplan_naturtyper.csv", rows_nt, FIELDS["bevarandeplan_naturtyper.csv"])
    write_csv("bevarandeplan_arter.csv", rows_art, FIELDS["bevarandeplan_arter.csv"])
    write_csv("bevarandeplan_exempelarter.csv", rows_ex, FIELDS["bevarandeplan_exempelarter.csv"])
    write_csv("bevarandeplan_karaktarsarter.csv", rows_kar, FIELDS["bevarandeplan_karaktarsarter.csv"])
    write_csv("bevarandeplan_parselogg.csv", rows_log, FIELDS["bevarandeplan_parselogg.csv"])

    n = len(rows_log)
    any_nt = sum(1 for l in rows_log if l["mall_a_tabell"] or l["mall_b_sektioner"])
    any_ex = sum(1 for l in rows_log if l["exempelarter"])
    any_kar = sum(1 for l in rows_log if l["karaktarsarter"])
    errs = sum(1 for l in rows_log if l["fel"])
    print(f"\nSammanfattning: {n} filer. Naturtyper hittade i {any_nt}. "
          f"Exempel-pa-arter hittade i {any_ex}. Karaktarsarter-text hittade i {any_kar}. Fel: {errs}.")


if __name__ == "__main__":
    main()
