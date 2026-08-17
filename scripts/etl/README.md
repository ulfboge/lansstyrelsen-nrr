# scripts/etl/

Hämtning av öppna myndighetsdata. Utdata hamnar i `data/raw/` (ignoreras av Git).

| Skript | Hämtar | Destination |
|--------|--------|-------------|
| `fetch_natura2000.py` | Natura 2000-polygoner för D-län via WFS | `data/raw/natura2000_sodermanland.geojson` |

Projektion: SWEREF 99 TM (EPSG:3006). Den fulla 11-stegspipelinen ligger i `natura-2000`-repot.
