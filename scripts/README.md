# scripts/

Python-skript för det här repot. Den tunga Natura 2000-pipelinen (steg 01–11) ligger i det privata syskonrepot `natura-2000` — kör den därifrån.

## Mappar

| Mapp | Innehåll |
|------|----------|
| `etl/` | Hämtning av öppna data till `data/raw/` |
| `analysis/` | NNK-analys för D-län: nollmätning, områdeskoppling, blankett och kontrollrum |

Kör från repo-roten eller från skriptets mapp. Sökvägar är relativa mot repo-roten, inte mot aktuell arbetskatalog.

```powershell
python scripts/analysis/nnk_kunskapslage.py
python scripts/analysis/koppla_omraden.py
python scripts/etl/fetch_natura2000.py
```
