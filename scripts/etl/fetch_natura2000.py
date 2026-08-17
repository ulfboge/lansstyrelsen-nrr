"""
fetch_natura2000.py
-------------------
ETL-skript: Hämtar Natura 2000-data från Naturvårdsverkets WFS-tjänst
och sparar till lokal GeoJSON-fil i SWEREF 99 TM (EPSG:3006).

Krav: pip install requests geopandas pyproj
Länsstyrelsen Södermanland – Naturrestaureringsuppdraget 2026
"""

import requests
import geopandas as gpd
import json
from pathlib import Path

# --- Konfiguration ---
REPO = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Naturvårdsverkets WFS-tjänst för Natura 2000
NV_WFS_URL = "https://ext-geodatakatalog-forv.lansstyrelsen.se/geo/wfs"

PARAMS = {
    "service": "WFS",
    "version": "2.0.0",
    "request": "GetFeature",
    "typeNames": "lst:NR_NaturaOmrade",  # Justera layer-namn efter tjänsten
    "outputFormat": "application/json",
    "srsName": "EPSG:3006",  # SWEREF 99 TM
    "CQL_FILTER": "LAN_KOD='04'",  # Södermanland = länskod 04
}


def hamta_natura2000():
    """Hämta Natura 2000-polygoner för Södermanlands län."""
    print("Hämtar Natura 2000-data från NV WFS...")
    try:
        response = requests.get(NV_WFS_URL, params=PARAMS, timeout=60)
        response.raise_for_status()
        data = response.json()

        gdf = gpd.GeoDataFrame.from_features(data["features"], crs="EPSG:3006")
        utfil = OUTPUT_DIR / "natura2000_sodermanland.geojson"
        gdf.to_file(utfil, driver="GeoJSON")

        print(f"✓ Sparade {len(gdf)} Natura 2000-områden till: {utfil}")
        print(f"  Kolumner: {list(gdf.columns)}")
        return gdf

    except requests.RequestException as e:
        print(f"✗ Fel vid anrop till WFS: {e}")
        return None


if __name__ == "__main__":
    hamta_natura2000()
