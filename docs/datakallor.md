# Datakällor – Naturrestaureringsuppdraget

Alla geografiska data projiceras till **SWEREF 99 TM (EPSG:3006)**.

| Organisation | Data | Format/Tjänst | Licens | URL |
|---|---|---|---|---|
| Naturvårdsverket (NV) | Natura 2000-områden (SCI/SPA), livsmiljötyper, skyddade arter | WMS/WFS/REST | INSPIRE / CC BY | https://geodata.naturvardsverket.se |
| Naturvårdsverket (NV) | Nationella marktäckedata (NMD2023) | Raster/GeoJSON | CC0 | https://geodata.naturvardsverket.se/nedladdning/marktacke/ |
| Lantmäteriet | Administrativa gränser, höjdmodell, hydrografi, vägar, ortnamn | WFS/WCS/API/Nedladdning | CC0 | https://www.lantmateriet.se/oppnadata |
| SLU Artdatabanken | Artobservationer, naturtypsregistreringar | API/Öppna filer | CC BY 4.0 | https://www.artdatabanken.se |
| GBIF | Artobservationer med koordinater (Södermanland) | REST API → GeoPackage | CC BY 4.0 | https://api.gbif.org/v1/occurrence/search |
| SMHI | Klimat- och hydrologidata, vattenflöden | API/CSV | CC BY | https://opendata.smhi.se |
| Jordbruksverket | Arealer, betesmark, jordbruksmark | Nedladdning CSV/Geo | CC BY | https://jordbruksverket.se |
| SGU | Geologi, jordarter, berggrund | WMS/WFS | CC0 | https://www.sgu.se/produkter-och-tjanster/api-er-och-oppen-data/ |
| Copernicus / EU | CORINE Land Cover, Sentinel-bilder | Nedladdning | Öppen | https://land.copernicus.eu |
| Länsstyrelsen (LST) | Regionala naturinventeringar, egna geodata | Intern GDB / GDK | Intern | https://gis.lansstyrelsen.se/geodata/geodatakatalogen/ |
| HaV | Marina naturvärden, vattenförekomster | WFS/API | CC BY | https://www.havochvatten.se/data-kartor-och-statistik/ |

## GBIF ETL-pipeline

Artobservationer från GBIF hämtas via ett automatiserat FME-arbetsflöde:

**Repo:** `C:\Users\galag\GitHub\fme\SpatialETLTool`

**Workspace:** `workspace/GBIF_Occurrence_To_GeoPackage.fmw`

Flödet hanterar automatisk paginering (max 300 poster/anrop), bygger punktgeometri, reprojicerar till SWEREF99 TM och filtrerar mot Södermanlands länsgräns. Output: `artobs_gbif.gpkg` (EPSG:3006).

Output används i:
- `natura-2000/web/public/data/artobs_gbif.gpkg` (Origo-webbkartan)
- Underlag för NRR-bedömning av artförekomst i Natura 2000-områden

## Öppna tjänster Natura 2000 (Länsstyrelserna)
- Metadatapost: `https://ext-geodatakatalog-forv.lansstyrelsen.se/PlaneringsKatalogen/GetMetaDataById?id=404DA7DB-9ED4-4B6C-B26C-DA8352817B9C_C`

## ArcGIS REST Services (LST)
- Extern geoportal: `https://ext-geoportal.lansstyrelsen.se/arcgis/rest/services`
