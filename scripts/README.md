# scripts/

Lättvikts-ETL för det här publika repot. Den tunga pipelinen och NNK-analysen ligger i det privata syskonrepot [natura-2000](https://github.com/ulfboge/natura-2000).

## Mappar

| Mapp | Innehåll |
|------|----------|
| `etl/` | Hämtning av öppna data till `data/raw/` |
| `analysis/` | Pekare — NNK-skripten körs i `natura-2000` |

```powershell
python scripts/etl/fetch_natura2000.py
```
