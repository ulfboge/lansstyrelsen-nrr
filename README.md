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

## Repostruktur

| Repo | Synlighet | Innehåll |
|------|-----------|----------|
| **[lansstyrelsen-nrr](https://github.com/ulfboge/lansstyrelsen-nrr)** (detta) | Publikt | Projektöversikt, plan, datakällor, GitHub Pages |
| **[natura-2000](https://github.com/ulfboge/natura-2000)** | Privat | Python-pipeline, Origo-webbkarta, ArcGIS Pro (`.aprx`) |

Pipeline och kartor utvecklas i det privata repot; denna sida länkar dit. **Åtkomst till natura-2000:** begär inbjudan från projektägaren.

```
lansstyrelsen-nrr/          ← du är här
├── index.html              # GitHub Pages
├── docs/                   # plan, datakallor, verktyg.md (översikt)
└── scripts/                # planerade ETL/analys (lättvikt)

natura-2000/                ← separat privat repo
├── scripts/01–11           # datapipeline
├── web/public/             # Origo-webbkarta
└── deliveries/             # ArcGIS-paket (.aprx)
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

**Natura 2000-pipeline (Python, Origo, ArcGIS Pro):** [natura-2000](https://github.com/ulfboge/natura-2000) — dokumentation i [docs/verktyg.md](docs/verktyg.md).

---

*Länsstyrelsen i Södermanlands län · Natur- och landsbygdsavdelningen*
