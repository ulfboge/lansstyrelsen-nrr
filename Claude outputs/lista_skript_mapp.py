#!/usr/bin/env python3
"""
lista_skript_mapp.py
=====================
Listar alla filer i en mapp (t.ex. din jobbmapp på G:) och bygger en manifest-CSV
som är lätt att gå igenom tillsammans med Claude för att identifiera vilka skript
som är överspelade och kan arkiveras/rensas bort.

Ingen arcpy krävs - vanligt Python räcker (bara standardbiblioteket).

Vad skriptet gör:
  1. Listar alla filer i mappen (icke-rekursivt som standard, sätt REKURSIVT = True
     nedan för att även gå igenom undermappar).
  2. För varje fil: storlek, senast ändrad-datum, och (för .py-filer) en kort
     SHA256-hash + ett utdrag ur modulens docstring/kommentarer - till hjälp för
     att gissa vad filen gör och vilken version det är.
  3. Grupperar filer som troligen hör ihop (samma "familjenamn" när man tar bort
     suffix som _KORRIGERAD, _V2, _V3, _NY och prefix som jobbdator_) - samma
     princip som archive/README.md i natura-2000-repot redan använder för de
     skript som arkiverades 2026-09-18.
  4. Flaggar EXAKTA dubbletter (byte-för-byte identiskt innehåll, oavsett
     filnamn) - dessa är de säkraste att ta bort direkt.
  5. Skriver en CSV-manifest (skript_manifest_<datum>.csv) i samma mapp, plus en
     kort sammanfattning i terminalen.

Skriptet TAR INTE BORT något själv - det bara listar och föreslår grupperingar.
Radering gör du själv, efter genomgång.

Använd så här:
  1. Kör: python lista_skript_mapp.py "G:\\Sökväg\\Till\\Din\\Jobbmapp"
     (eller redigera MAPP nedan och kör utan argument)
  2. Skicka den skapade CSV-filen till Claude (eller klistra in innehållet), så
     går vi igenom den tillsammans och beslutar vad som kan arkiveras/tas bort -
     precis som med forbered_gdb_for_publicering_KORRIGERAD.py.
"""

import sys
import re
import csv
import hashlib
from pathlib import Path
from datetime import datetime

# ===========================================================================
# KONFIGURATION
# ===========================================================================

# Mapp att lista. Om du kör skriptet med en sökväg som argument
# (python lista_skript_mapp.py "G:\...") används den istället för denna.
MAPP = r"G:\Sokvag\Till\Din\Jobbmapp"

# Sätt till True för att även gå igenom undermappar.
REKURSIVT = False

# Filändelser som ska räknas som "skript" och få docstring-utdrag + hash.
SKRIPT_ANDELSER = {".py"}

# Filändelser som helt ska hoppas över i listningen.
IGNORERA_ANDELSER = {".lock", ".pyc"}

# Suffix som strippas bort för att gissa vilken "familj" en fil tillhör,
# t.ex. bygg_nnk_lyrx_KORRIGERAD_V3.py och bygg_nnk_lyrx.py grupperas ihop.
SUFFIX_MONSTER = [
    r"_KORRIGERAD_V\d+$",
    r"_KORRIGERAD$",
    r"_DIREKT$",
    r"_V\d+$",
    r"_NY$",
    r"_gammal$",
    r"_backup$",
    r"_old$",
]

# Prefix som strippas bort på samma sätt.
PREFIX_MONSTER = [
    r"^jobbdator_",
]


def gissa_familj(stamnamn: str) -> str:
    """Strippar kända versions-/kopior-suffix och prefix för att gruppera filer
    som troligen är olika versioner av samma skript."""
    namn = stamnamn
    for monster in PREFIX_MONSTER:
        namn = re.sub(monster, "", namn)
    andrad = True
    while andrad:
        andrad = False
        for monster in SUFFIX_MONSTER:
            ny = re.sub(monster, "", namn)
            if ny != namn:
                namn = ny
                andrad = True
    return namn or stamnamn


def sha256_kort(path: Path, langd: int = 12) -> str:
    """Kort SHA256-hash (första `langd` tecken) - identiska filer får samma
    hash, oavsett filnamn. Läser filen i bitar så stora filer inte äter minne."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for bit in iter(lambda: f.read(65536), b""):
                h.update(bit)
        return h.hexdigest()[:langd]
    except OSError:
        return "LASFEL"


def docstring_utdrag(path: Path, max_tecken: int = 300) -> str:
    """Plockar ut modulens docstring (texten mellan de tre första \"\"\"-paren)
    eller, om ingen docstring finns, de första kommentarsraderna (#) överst i
    filen. Trunkerar till max_tecken och byter radbrytningar mot ' | ' så det
    får plats på en CSV-rad."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""

    match = re.search(r'"""(.*?)"""', text, re.DOTALL)
    if match:
        utdrag = match.group(1).strip()
    else:
        rader = []
        for rad in text.splitlines():
            s = rad.strip()
            if s.startswith("#"):
                rader.append(s.lstrip("#").strip())
            elif rader:
                break
        utdrag = "\n".join(rader)

    utdrag = " | ".join(line.strip() for line in utdrag.splitlines() if line.strip())
    if len(utdrag) > max_tecken:
        utdrag = utdrag[:max_tecken].rstrip() + "…"
    return utdrag


def samla_filer(mapp: Path, rekursivt: bool):
    if rekursivt:
        return [p for p in mapp.rglob("*") if p.is_file()]
    return [p for p in mapp.iterdir() if p.is_file()]


def main():
    mapp = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(MAPP)
    if not mapp.is_dir():
        sys.exit(f"Hittar inte mappen: {mapp}")

    filer = samla_filer(mapp, REKURSIVT)
    filer = [f for f in filer if f.suffix.lower() not in IGNORERA_ANDELSER]
    filer.sort(key=lambda p: p.name.lower())

    rader = []
    for f in filer:
        try:
            stat = f.stat()
        except OSError:
            continue
        ar_skript = f.suffix.lower() in SKRIPT_ANDELSER
        rad = {
            "Filnamn": f.relative_to(mapp).as_posix(),
            "Storlek_KB": round(stat.st_size / 1024, 1),
            "Senast_andrad": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
            "Familj": gissa_familj(f.stem) if ar_skript else "",
            "Hash_kort": sha256_kort(f) if ar_skript else "",
            "Docstring_utdrag": docstring_utdrag(f) if ar_skript else "",
        }
        rader.append(rad)

    if not rader:
        print(f"Inga filer hittades i {mapp}.")
        return

    datum = datetime.now().strftime("%Y%m%d")
    ut_csv = mapp / f"skript_manifest_{datum}.csv"
    with open(ut_csv, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rader[0].keys()))
        writer.writeheader()
        writer.writerows(rader)

    print(f"Manifest skrivet: {ut_csv}  ({len(rader)} filer)\n")

    # --- Sammanfattning: exakta dubbletter (samma hash, olika filnamn) ---
    hash_till_filer = {}
    for rad in rader:
        if rad["Hash_kort"]:
            hash_till_filer.setdefault(rad["Hash_kort"], []).append(rad["Filnamn"])

    dubbletter = {h: fl for h, fl in hash_till_filer.items() if len(fl) > 1}
    if dubbletter:
        print("EXAKTA DUBBLETTER (byte-för-byte identiskt innehåll):")
        for h, fl in dubbletter.items():
            print(f"  - {', '.join(fl)}")
        print()
    else:
        print("Inga exakta dubbletter hittade.\n")

    # --- Sammanfattning: skriptfamiljer med fler än en version ---
    familj_till_filer = {}
    for rad in rader:
        if rad["Familj"]:
            familj_till_filer.setdefault(rad["Familj"], []).append(rad)

    flera_versioner = {fam: fl for fam, fl in familj_till_filer.items() if len(fl) > 1}
    if flera_versioner:
        print("MÖJLIGA VERSIONSFAMILJER (kontrollera vilken som senast användes):")
        for fam, fl in sorted(flera_versioner.items()):
            fl_sorterad = sorted(fl, key=lambda r: r["Senast_andrad"])
            for r in fl_sorterad:
                print(f"    - {r['Filnamn']}  ({r['Senast_andrad']}, {r['Storlek_KB']} KB)")
            print()

    print("Skicka CSV-filen (eller klistra in innehållet) till Claude för genomgång.")


if __name__ == "__main__":
    main()
