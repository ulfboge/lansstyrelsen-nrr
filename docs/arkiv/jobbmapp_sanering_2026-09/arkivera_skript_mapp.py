#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
arkivera_skript_mapp.py
========================
Flyttar de skript/filer i jobbmappen (G:) som identifierats som HISTORIK eller
ARKIVERA i README_sanering.md till en archive/-undermapp - samma princip som
natura-2000-repots egen archive/README.md redan använder.

Klassificeringen nedan är HÅRDKODAD utifrån en fullständig genomläsning av
skriptens innehåll och den verifierade körordningen (2026-09-22) - inte en
gissning baserad på filnamn. Ändra inte listorna utan att ha läst
README_sanering.md igen.

Filer som INTE nämns nedan (t.ex. jobbdator_koppla_nnk_skyddskategori.py,
jobbdator_UPPDATERA_tillstand_verifierad_brygga.py, forbered_gdb_for_publicering.py,
jobbdator_bygg_nnk_lyrx_KORRIGERAD_V3.py, diagnostik_geometrisk_matchning_direkt.csv,
naturtyp_koder.py, jobbdator_diagnostik_nnk_lyrx_V2.py,
LstD_NNK_Granskning_publicering.aprx, naturreservat_nationalpark_utvidgat.geojson)
är AKTIV PIPELINE och rörs ALDRIG av det här skriptet.

D_NNK_Granskning.aprx flyttas heller INTE automatiskt - den kräver att du
själv bekräftar att den inte används till något annat (se README_sanering.md).

SÄKERHET:
  - Skriptet TAR ALDRIG BORT något, bara flyttar (shutil.move).
  - Kör som TORRKÖRNING (dry run) som standard - skriver bara ut vad som
    SKULLE hända. Inget flyttas förrän du kör med --utfor.
  - Skriver aldrig över en fil som redan finns i archive/ - hoppar över med
    en varning istället.
  - Skriver en archive/README.md med tabellen nedan, i samma stil som
    natura-2000-repots archive/README.md, så spårbarheten följer med.

Använd så här:
  1. Antingen: redigera MAPP nedan till din jobbmapp och kör:
       python arkivera_skript_mapp.py
     Eller: ange sökvägen som argument (då används den istället för MAPP):
       python arkivera_skript_mapp.py "G:\\Sökväg\\Till\\Din\\Jobbmapp"
  2. Detta ger en TORRKÖRNING - inget flyttas, bara en förhandsgranskning skrivs ut.
  3. När det ser rätt ut, lägg till --utfor sist för att faktiskt flytta filerna:
       python arkivera_skript_mapp.py --utfor
       python arkivera_skript_mapp.py "G:\\Sökväg\\Till\\Din\\Jobbmapp" --utfor
"""

import sys
import os
import shutil
import argparse
from pathlib import Path
from datetime import date

# Redigera denna om du inte vill ange sökvägen som argument varje gång.
MAPP = r"G:\Sokvag\Till\Din\Jobbmapp"

# ===========================================================================
# KLASSIFICERING (från README_sanering.md, 2026-09-22)
# ===========================================================================
# Varje post: filnamn -> (kategori, motivering)

HISTORIK = {
    "Join_tillstand_NNK_yta.csv": (
        "HISTORIK",
        "Rådata som en gång (17/9) gav upphov till bryggans korstabell. "
        "Konsumeras inte längre av något aktivt skript - spara för spårbarhet."
    ),
    "jobbdator_diagnostik_geometrisk_matchning_DIREKT.py": (
        "HISTORIK",
        "Skriptet som byggde korstabellen diagnostik_geometrisk_matchning_direkt.csv "
        "(som ligger kvar AKTIV i jobbmappen). Behövs bara igen om NV levererar ett "
        "nytt Ajourhålla-uttag - då ändras GlobalID igen och bryggan måste räknas om."
    ),
    "jobbdator_diagnostik_nv_globalid.py": (
        "HISTORIK",
        "Del av felsökningen 17/9 - bekräftade att GlobalID hade bytts mellan "
        "gammal och ny NNK-export."
    ),
    "jobbdator_diagnostik_join_tillstand.py": (
        "HISTORIK",
        "Samma felsökning, tidigast i kedjan (08:35) - bekräftade att direkt "
        "GlobalID-matchning gav 0 träffar."
    ),
}

ARKIVERA = {
    "jobbdator_bygg_nnk_lyrx.py": (
        "ARKIVERA",
        "Äldre (16/9), redan dokumenterad i repots archive/README.md som ersatt "
        "av jobbdator_bygg_nnk_lyrx_KORRIGERAD_V3.py."
    ),
    "forbered_gdb_for_publicering_KORRIGERAD.py": (
        "ARKIVERA",
        "Samma fil som redan arkiverats i repot - skiljer sig bara på dagens "
        "forandringsorsak_forslag-tillägg, som saknas här."
    ),
    "jobbdator_diagnostik_geometrisk_matchning_KORRIGERAD.py": (
        "ARKIVERA",
        "Tidigare försök (08:49), ersatt av DIREKT-varianten (08:59) - DIREKT är "
        "bevisligen den som användes (dess output är bryggans indata)."
    ),
    "jobbdator_uppdatera_tillstand_fran_bevarandeplan_KORRIGERAD.py": (
        "ARKIVERA",
        "Det första (övergivna) försöket att matcha direkt på GlobalID, innan "
        "krisen upptäcktes. Ersatt av den verifierade bryggan."
    ),
    "jobbdator_diagnostik_kommentarfalt.py": (
        "ARKIVERA",
        "Fristående engångskontroll av kommentarsfält (10:41), inget beroende "
        "till kedjan."
    ),
    "jobbdator_diagnostik_nnk_lyrx.py": (
        "ARKIVERA",
        "Basversion, ersatt av V2."
    ),
    "jobbdator_diagnostik_nnk_lyrx_KORRIGERAD.py": (
        "ARKIVERA",
        "Mellansteg, ersatt av V2."
    ),
    "D_NNK_Granskning.atbx": (
        "ARKIVERA",
        "I praktiken tom custom-toolbox (203 byte innehåll, inga egna verktyg)."
    ),
}

ATT_FLYTTA = {**HISTORIK, **ARKIVERA}

ARKIVMAPP_NAMN = "archive"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "mapp", nargs="?", default=None,
        help="Sökväg till jobbmappen som ska rensas. Utelämnas: MAPP-konstanten ovan används."
    )
    p.add_argument(
        "--utfor", action="store_true",
        help="Utför flytten på riktigt. Utan denna flagga körs bara en torrkörning."
    )
    args = p.parse_args()

    mapp = Path(args.mapp) if args.mapp else Path(MAPP)
    if not mapp.is_dir():
        sys.exit(
            f"Hittar inte mappen: {mapp}\n"
            "Antingen redigera MAPP-konstanten högst upp i skriptet, eller ange "
            "sökvägen som argument, t.ex.:\n"
            '  python arkivera_skript_mapp.py "G:\\Din\\Mapp"'
        )

    arkiv = mapp / ARKIVMAPP_NAMN
    lage = "UTFÖR" if args.utfor else "TORRKÖRNING (inget flyttas)"
    print("=" * 78)
    print(f"ARKIVERING AV SKRIPT - {lage}")
    print("=" * 78)
    print("Mapp:      ", mapp)
    print("Arkivmapp: ", arkiv)
    print()

    if not args.utfor:
        print(">>> Detta är en torrkörning. Kör med --utfor för att faktiskt flytta filer.\n")

    hittade = []
    saknade = []

    for filnamn, (kategori, motivering) in sorted(ATT_FLYTTA.items()):
        kalla = mapp / filnamn
        if not kalla.is_file():
            saknade.append(filnamn)
            continue
        hittade.append((filnamn, kategori, motivering))
        mal = arkiv / filnamn
        if mal.exists():
            print(f"[HOPPAR ÖVER] {filnamn} finns redan i {ARKIVMAPP_NAMN}/ - rör inte")
            continue
        print(f"[{kategori:9}] {filnamn}")
        print(f"             -> {ARKIVMAPP_NAMN}/{filnamn}")
        if args.utfor:
            arkiv.mkdir(exist_ok=True)
            shutil.move(str(kalla), str(mal))

    print()
    if saknade:
        print("Ej hittade i mappen (redan flyttade, eller annat namn):")
        for f in saknade:
            print(f"  - {f}")
        print()

    if args.utfor and hittade:
        arkiv.mkdir(exist_ok=True)
        skriv_readme(arkiv, hittade)
        print(f"Skrev {arkiv / 'README.md'}")

    print()
    print(f"Klart. {len(hittade)} filer {'flyttade' if args.utfor else 'skulle flyttas'}, "
          f"{len(saknade)} inte hittade.")
    print()
    print("Följande filer rörs ALDRIG av det här skriptet (AKTIV PIPELINE eller kräver "
          "din egen bedömning): jobbdator_koppla_nnk_skyddskategori.py, "
          "jobbdator_UPPDATERA_tillstand_verifierad_brygga.py, "
          "forbered_gdb_for_publicering.py, jobbdator_bygg_nnk_lyrx_KORRIGERAD_V3.py, "
          "diagnostik_geometrisk_matchning_direkt.csv, naturtyp_koder.py, "
          "jobbdator_diagnostik_nnk_lyrx_V2.py, LstD_NNK_Granskning_publicering.aprx, "
          "naturreservat_nationalpark_utvidgat.geojson, D_NNK_Granskning.aprx.")


def skriv_readme(arkiv: Path, hittade):
    idag = date.today().isoformat()
    rader = [
        f"# Arkiverade skriptversioner (städat {idag})",
        "",
        "Flyttade hit av arkivera_skript_mapp.py, baserat på README_sanering.md "
        f"({idag}). Inget är raderat - bara flyttat.",
        "",
        "| Fil | Kategori | Varför |",
        "|---|---|---|",
    ]
    for filnamn, kategori, motivering in sorted(hittade):
        rader.append(f"| `{filnamn}` | {kategori} | {motivering} |")
    rader.append("")
    (arkiv / "README.md").write_text("\n".join(rader), encoding="utf-8")


if __name__ == "__main__":
    main()
