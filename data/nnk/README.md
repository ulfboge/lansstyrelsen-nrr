# data/nnk/

Bearbetad Natura naturtypskarta för D-län, med områdesidentitet.

## Filer

| Fil | Skapas av | Innehåll |
|-----|-----------|----------|
| `nnk_yta_med_sitecode.csv` | `scripts/analysis/koppla_omraden.py` | NNK-ytor med SITECODE, områdesnamn och bevarandeplan (utan geometri) |
| `nnk_yta_med_sitecode.gpkg` | samma | Samma tabell med geometri. Ignoreras av Git. |
| `nnk_d.json` | `scripts/analysis/nnk_kunskapslage.py` | Nollmätning: summering, objekt med prioritet P1–P4, areal per kod |

CSV:n är indata till `bygg_blankett.py` och till statistik per objekt (uppgift E1.2).

Kör om `koppla_omraden.py` mot ett nytt uttag i `data/uttag/` genom att sätta miljövariabeln `NNK_SHP` till uttagets sökväg.
