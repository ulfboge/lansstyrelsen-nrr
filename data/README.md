# data/

Geodata, register och mallar för NRR-arbetet i Södermanlands län. All geodata ska vara i **SWEREF 99 TM (EPSG:3006)**.

## Innehåll

| Sökväg | Vad som hör hemma här |
|--------|------------------------|
| `sources_sodermanland.csv` | Datakälleregister. Sätt `enabled=1` för att aktivera en källa. |
| `templates/` | Bedömningsmall för skrivbords- och fältbedömning |
| `nnk/` | Bearbetad NNK: områdeskoppling och nollmätning |
| `uttag/` | Råa NNK-uttag med datum i filnamnet |
| `raw/` | Nedladdningar (skapas av ETL, ignoreras av Git) |

Stora geodatafiler (`.gpkg`, shapefiler, zip:ade paket) versionshanteras inte. CSV-register och mallar gör det.
