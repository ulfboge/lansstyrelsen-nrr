# data/

Geodataregister och mallar för den publika projektytan. All geodata ska vara i **SWEREF 99 TM (EPSG:3006)**.

## Innehåll

| Sökväg | Vad som hör hemma här |
|--------|------------------------|
| `sources_sodermanland.csv` | Datakälleregister. Sätt `enabled=1` för att aktivera en källa. |
| `templates/` | Bedömningsmall för skrivbords- och fältbedömning |
| `nnk/`, `uttag/` | Pekare — bearbetad NNK och uttag ligger i [natura-2000](https://github.com/ulfboge/natura-2000) |
| `raw/` | Nedladdningar (skapas av ETL, ignoreras av Git) |
