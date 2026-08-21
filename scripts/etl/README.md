# scripts/etl/

Hämtning av öppna myndighetsdata. Utdata hamnar i `data/raw/` (ignoreras av Git).

| Skript | Hämtar | Destination |
|--------|--------|-------------|
| `fetch_natura2000.py` | Natura 2000-polygoner för D-län via WFS | `data/raw/natura2000_sodermanland.geojson` |
| `fetch_skyddadnatur_dokument.py` | Bevarandeplaner för N2000 i D-län via NV REST-API | `docs/skyddadnatur/natura2000/` |
| `fetch_tuva_sodermanland.py` | TUVA ängs- och betesmark för D-län (CSV, objektsrapporter, WFS) | `docs/tuva/sodermanland/` |

Projektion: SWEREF 99 TM (EPSG:3006). Den fulla 11-stegspipelinen ligger i `natura-2000`-repot.
