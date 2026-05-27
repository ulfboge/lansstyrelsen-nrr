# Naturrestaureringsuppdraget – Länsstyrelsen Södermanland

Projektrepo för implementering av EU:s naturrestaureringsförordning (NRR) i Södermanlands län.

## Hemsida

🌐 **[Öppna projektöversikten →](https://ulfboge.github.io/lansstyrelsen-nrr)**

*(GitHub Pages aktiveras via: Settings → Pages → Source: Deploy from branch → main → / (root))*

## Om projektet

Länsstyrelsen i Södermanlands län har rekryterat två personer för att genomföra naturrestaureringsuppdraget enligt EU-förordning 2024/1991. Uppdraget innefattar:

- Kartläggning av habitattyper och naturvärden i Natura 2000-områden
- GIS-analys och kartproduktion (ArcGIS Pro + ArcGIS Enterprise)
- Databasarbete och ETL-pipelines för öppna myndighetskällor
- Rapportering och beslutsunderlag
- Samverkan med NV, Skogsstyrelsen, HaV och länets kommuner

**Viktigt datum:** Sverige ska lämna nationell restaureringsplan till EU-kommissionen **1 september 2026**.

## Repo-struktur

```
├── index.html          # GitHub Pages hemsida (projektöversikt)
├── CLAUDE.md           # Projektinstruktioner för Claude
├── README.md           # Denna fil
├── docs/               # Dokumentation
│   ├── projektplan.md
│   ├── datakallor.md
│   └── datamodell.md
├── scripts/
│   ├── etl/            # Python ETL-skript
│   └── analysis/       # Analysverktyg
└── .gitignore
```

## Teknisk stack

| Kategori | Verktyg |
|----------|---------|
| GIS (primärt) | ESRI ArcGIS Pro, ArcGIS Enterprise, ArcGIS Online |
| Kontorssystem | Microsoft 365 (Teams, SharePoint, Planner, Power BI) |
| Databas | ESRI Geodatabase, PostGIS (komplement) |
| Scripting | Python (arcpy, geopandas) |
| Versionshantering | Git / GitHub |

## Kom igång

Se [CLAUDE.md](CLAUDE.md) för fullständiga projektinstruktioner.

---

*Länsstyrelsen i Södermanlands län · Natur- och landsbygdsavdelningen*
