# Naturrestaureringsuppdraget – Länsstyrelsen Södermanland

Projektrepo för implementering av EU:s naturrestaureringsförordning (NRR) i Södermanlands län.

## Hemsida

🌐 **[Öppna projektöversikten →](https://ulfboge.github.io/lansstyrelsen-nrr)**

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
| **[nnk-granskning-2026](https://github.com/ulfboge/nnk-granskning-2026)** | Publikt | **NNK-granskning 2026** — kontrollpanel, arbetsplan, runbook, metodik |
| **[natura-2000](https://github.com/ulfboge/natura-2000)** | Privat | NNK-analysskript, NV-underlag, KartLits 2027, jobbdatorns skript för granskningslagret |

NNK-arbetsdokumenten ligger publikt i `nnk-granskning-2026` — [öppna kontrollpanelen](https://ulfboge.github.io/nnk-granskning-2026). Pipeline, rådata och NV:s underlag ligger i det privata `natura-2000`. **Åtkomst till natura-2000:** du äger repot som `ulfboge`. Kollegor bjuds in under Settings → Collaborators.

```
lansstyrelsen-nrr/          ← du är här (publikt)
├── index.html              # GitHub Pages
├── docs/                   # plan, datakällor, NRR-guide, presentation
├── docs/skyddadnatur/      # index över bevarandeplaner
├── docs/tuva/              # TUVA-export för länet
└── scripts/etl/            # lättvikts-ETL

nnk-granskning-2026/         ← publikt, GitHub Pages
├── index.html              # kontrollpanel
├── kontrollrum.html        # gantt och avbockning
├── kunskapslage.html       # kunskapsläge per objekt
└── docs/                   # arbetsplan, runbook, metodik

natura-2000/                ← separat privat repo
├── docs/underlag/          # NV:s handledning, statistik, KartLits 2027
├── scripts/analysis/       # NNK-analys, källa för runbook och kontrollrum
├── scripts/falt/           # fältschema för tillståndsbedömning 2027
├── deliveries/             # granskningslagret och jobbdatorns skript 01–07
└── archive/                # Origo-webbkartan, junipaketet m.m. (ersatt)
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

**NNK-granskning 2026:** [kontrollpanel](https://ulfboge.github.io/nnk-granskning-2026) · [repo](https://github.com/ulfboge/nnk-granskning-2026) (publikt)

**Natura 2000-pipeline och rådata:** [natura-2000](https://github.com/ulfboge/natura-2000) (privat) — översikt i [docs/verktyg.md](docs/verktyg.md).

---

*Länsstyrelsen i Södermanlands län · Natur- och landsbygdsavdelningen*
