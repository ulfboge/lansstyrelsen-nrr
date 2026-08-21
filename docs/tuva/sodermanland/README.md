# TUVA – ängs- och betesmark, Södermanlands län

Lokalt uttag från Jordbruksverkets e-tjänst [TUVA](https://etjanst.sjv.se/tuvaut/) för **Södermanlands län** (länskod 04).

Hämtat **2026-08-21** via samma API som kartverktyget (`/hagenpub/rest`) plus öppna WFS-lager.

Sökningen i TUVA: Geografi → Län → Södermanland. Resultat i tjänsten: **3 700 marker**, **13 730 ha** (senaste inventering).

## Innehåll

| Del | Antal | Sökväg |
|-----|------:|--------|
| Marker (fält-ID) | 3 700 | `index.csv` |
| Komplett CSV, alla inventeringsdatum | 5,6 MB | `export/` |
| Komplett CSV, senaste inventering | 5,3 MB | `export/` |
| Summerad CSV per kommun | 9 rader | `export/` |
| Objektsrapporter (JSON) | 3 700 | `objektrapporter/` |
| Kartskikt ängs- och betesmark (GeoJSON, EPSG:3006) | 3 822 ytor | `gis/` |
| Kartskikt naturtyper (GeoJSON, EPSG:3006) | 11 609 ytor | `gis/` |

Objektsrapporter och GeoJSON ignoreras av Git p.g.a. storlek (ca 70 MB). Index och CSV-export versionshanteras.

GIS-lagret har fler ytor (3 822) än sökningen i TUVA (3 700) eftersom WFS även innehåller historiska/ej aktuella geometrier. Naturtypsytorna är nedbrutna delytor enligt art- och habitatdirektivet.

## Kommuner (senaste inventering)

| Kommun | Antal | Areal (ha) |
|--------|------:|-----------:|
| Nyköping | 913 | 3 942 |
| Katrineholm | 681 | 2 366 |
| Flen | 594 | 2 148 |
| Eskilstuna | 534 | 1 611 |
| Gnesta | 377 | 1 129 |
| Strängnäs | 292 | 1 342 |
| Vingåker | 157 | 433 |
| Trosa | 146 | 718 |
| Oxelösund | 6 | 40 |

Alla inventeringsdatum ger samma 3 700 fält-ID men **14 683 ha** (fler besök/arealer i den kompletta filen).

## Uppdatera uttaget

```powershell
python scripts/etl/fetch_tuva_sodermanland.py
```

Skriptet hoppar över objektsrapporter som redan finns. CSV och GeoJSON skrivs om.

Öppna en enskild mark i TUVA: `https://etjanst.sjv.se/tuvaut/?f=&id=FÄLT-ID`

## Licens och källa

Öppna data från Jordbruksverket. Ange källan *Ängs- och betesmarksinventeringen (TUVA), Jordbruksverket* vid vidare användning. Projektion för GIS: **SWEREF 99 TM (EPSG:3006)**.
