# scripts/analysis/

Analysverktyg för NNK i Södermanlands län. Körs mot underlag i `docs/underlag/` och skriver till `data/nnk/` respektive `docs/nnk/`.

## Skript

| Skript | Indata | Utdata |
|--------|--------|--------|
| `nnk_kunskapslage.py` | `docs/underlag/D_NNK_statistik_…xlsx` | `data/nnk/nnk_d.json` |
| `koppla_omraden.py` | `docs/underlag/naturtypskarta/NNK_YTA.shp` (eller `NNK_SHP`) | `data/nnk/nnk_yta_med_sitecode.csv` / `.gpkg` |
| `bygg_blankett.py` | `nnk_d.json`, `nnk_yta_med_sitecode.csv` | `docs/nnk/blankett_forvaltarkunskap_nnk.xlsx` |
| `bygg_kontrollrum.py` | `uppgifter.py` | `docs/nnk/runbook_nnk_2026.md` och `kontrollrum_nnk_2026.html` |
| `uppgifter.py` | — | Källregister för runbook och kontrollrum. Redigera här. |

`kontrollrum_mall.html` är mallen som `bygg_kontrollrum.py` fyller med data.

## Beroenden

```
pip install openpyxl geopandas requests pandas
```

`koppla_omraden.py` hämtar SCI-lagret från Naturvårdsregistret vid första körningen och cachar det i `data/raw/n2000/`.
