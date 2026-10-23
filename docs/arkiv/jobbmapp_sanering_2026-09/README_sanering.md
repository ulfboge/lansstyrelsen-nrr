# Sanering av jobbmappen (G:), 2026-09-22

Underlag för att rensa `jobbdator_*`-skript och relaterade filer i jobbmappen på G:,
baserat på en fullständig genomläsning av dataflödet (inte bara filnamn/docstrings)
och den körordning som verifierades 2026-09-17 och bekräftades 2026-09-22.

Flytta INTE eller radera INTE något innan du läst hela tabellen — kolumnen
"Aktiv/Historik/Arkivera" är den viktiga.

## Den verifierade aktiva kedjan (kör i denna ordning vid varje ombyggnad av gdb:n)

1. `jobbdator_koppla_nnk_skyddskategori.py` — bygger om gdb:n från grunden.
2. `jobbdator_UPPDATERA_tillstand_verifierad_brygga.py` — MÅSTE köras här, innan steg 3.
   Matchar på fältet `globalid`, som steg 3 döper om. Läser
   `diagnostik_geometrisk_matchning_direkt.csv` (se nedan — flytta ALDRIG den filen till
   arkivet, den är ett aktivt indata, inte en diagnostikrapport).
3. `forbered_gdb_for_publicering.py` — domäner, alias, Double→Long, GlobalID-döpning,
   editor tracking, metadata. Köres EN gång per gdb, i Pro:s Python-fönster.
4. `jobbdator_bygg_nnk_lyrx_KORRIGERAD_V3.py` — uppdaterar lyrx-filerna (symbologi,
   popup, fältsynlighet). Rör aldrig gdb-data (ingen arcpy), så ordningen mot steg 2–3
   spelar ingen roll för just den här filen.
5. Diagnostik/kontroll (`jobbdator_diagnostik_nnk_lyrx_V2.py`).
6. Publicering (Share As Web Layer → Overwrite → GK Konfigurator).

## Filgenomgång

| Fil | Aktiv/Historik/Arkivera | Varför |
|---|---|---|
| `jobbdator_koppla_nnk_skyddskategori.py` | **AKTIV** | Steg 1 |
| `jobbdator_UPPDATERA_tillstand_verifierad_brygga.py` | **AKTIV** | Steg 2 — måste köras vid varje ombyggnad, bekräftat 2026-09-22 |
| `forbered_gdb_for_publicering.py` | **AKTIV** | Steg 3 |
| `jobbdator_bygg_nnk_lyrx_KORRIGERAD_V3.py` | **AKTIV** | Steg 4 |
| `diagnostik_geometrisk_matchning_direkt.csv` | **AKTIV (data)** | Krävs av steg 2 vid varje körning — trots namnet är detta inte en engångsdiagnostikrapport utan den löpande källan för tillstånd/kommentar_tillstand/fältinventerare |
| `naturtyp_koder.py` | **AKTIV** | Kodlistemodul, importeras av steg 1 |
| `jobbdator_diagnostik_nnk_lyrx_V2.py` | **AKTIV** | Steg 5, senaste diagnostikversionen |
| `Join_tillstand_NNK_yta.csv` | **HISTORIK** | Rådata som en gång (17/9) gav upphov till bryggans korstabell ovan. Konsumeras inte längre av något aktivt skript — spara för spårbarhet |
| `jobbdator_diagnostik_geometrisk_matchning_DIREKT.py` | **HISTORIK** | Skriptet som byggde korstabellen. Behövs bara igen om NV levererar ett nytt Ajourhålla-uttag (då ändras GlobalID igen och hela bryggan måste räknas om) |
| `jobbdator_diagnostik_nv_globalid.py` | **HISTORIK** | Del av felsökningen 17/9 (bekräftade att GlobalID hade bytts) |
| `jobbdator_diagnostik_join_tillstand.py` | **HISTORIK** | Samma felsökning, tidigast i kedjan |
| `jobbdator_bygg_nnk_lyrx.py` (utan suffix) | **ARKIVERA** | Äldre (16/9), redan dokumenterad i repots `archive/README.md` som ersatt av KORRIGERAD_V3 |
| `forbered_gdb_for_publicering_KORRIGERAD.py` | **ARKIVERA** | Samma fil som redan arkiverats i repot — skiljer sig bara på dagens `forandringsorsak_forslag`-tillägg, som saknas här |
| `jobbdator_diagnostik_geometrisk_matchning_KORRIGERAD.py` | **ARKIVERA** | Tidigare försök (08:49), ersatt av DIREKT (08:59) — DIREKT är beviserligen den som användes (dess output är bryggans indata) |
| `jobbdator_uppdatera_tillstand_fran_bevarandeplan_KORRIGERAD.py` | **ARKIVERA** | Första (övergivna) försöket att matcha direkt på GlobalID, innan ni upptäckte att GlobalID hade bytts. Ersatt av den verifierade bryggan |
| `jobbdator_diagnostik_kommentarfalt.py` | **ARKIVERA** | Fristående engångskontroll av kommentarsfält, inget beroende till kedjan |
| `jobbdator_diagnostik_nnk_lyrx.py` | **ARKIVERA** | Basversion, ersatt av V2 |
| `jobbdator_diagnostik_nnk_lyrx_KORRIGERAD.py` | **ARKIVERA** | Mellansteg, ersatt av V2 |
| `D_NNK_Granskning.atbx` | **ARKIVERA/RADERA** | I praktiken tom custom-toolbox (203 byte innehåll, inga egna verktyg) |
| `D_NNK_Granskning.aprx` | **KOLLA SJÄLV** | 4/9, äldre lageruppsättning (Map/Map1 med olika lager än publiceringsprojektet). Ser ut som ett tidigt utkast, ersatt av `LstD_NNK_Granskning_publicering.aprx` — bekräfta att du inte använder den till något annat innan du tar bort den |
| `LstD_NNK_Granskning_publicering.aprx` | **AKTIV** | Det löpande publiceringsprojektet |
| `naturreservat_nationalpark_utvidgat.geojson` | **AKTIV** | Samma storlek som repots `data/analysis/`-kopia — förväntad lokal arbetskopia för jobbdatorn (som saknar repot), inte skräp |

## Viktigast att komma ihåg

`diagnostik_geometrisk_matchning_direkt.csv` ska INTE arkiveras eller flyttas bort från
`C:\Aprx_Projekt\` — trots att namnet låter som en engångsrapport är den den faktiska
källan för `tillstand`/`kommentar_tillstand`/`faltinventerare` vid varje körning av
`jobbdator_UPPDATERA_tillstand_verifierad_brygga.py`.
