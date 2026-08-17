# docs/underlag/naturtypskarta/

Publik Natura naturtypskarta för Södermanlands län (länskod D). Detta är *inte* NNK Ajourhålla — kommentarer och användaruppgifter är strippade.

## Geodata

| Lager | Geometri | Användning |
|-------|----------|------------|
| `NNK_YTA` | ytor | Primärt underlag. Default-indata till `scripts/analysis/koppla_omraden.py` |
| `NNK_LIN` | linjer | Vattendrag och liknande |
| `NNK_PKT` | punkter | Punktförekomster |
| `NNK_TOLKNING` | ytor | Tolkningsunderlag |

Shapefiler (`.shp`, `.dbf`, m.fl.) ignoreras av Git — de finns bara lokalt. `.lyrx`-filerna (ArcGIS Pro-symbologi) versionshanteras.

## Övrigt

| Fil | Innehåll |
|-----|----------|
| `NNK_publik_produktbeskrivning.pdf` | Produktbeskrivning för den publika NNK |
| `Beskrivning_NNK_koder.pdf` | Kodförklaringar |
| `NNK-*.lyrx` | Färdig symbologi för karteringsstatus, naturtypsstatus m.m. |

Koordinatsystem: SWEREF 99 TM (EPSG:3006).
