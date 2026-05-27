# Projektplan – Naturrestaureringsuppdraget
## Länsstyrelsen i Södermanlands län, 2026–2027

**Version:** 1.0  
**Datum:** 2026-05-27  
**Uppdragsgivare:** Länsstyrelsen i Södermanlands län, Natur- och landsbygdsavdelningen  
**Projektledning:** Naturvårdsenheten  

---

## 1. Bakgrund och syfte

EU:s naturrestaureringsförordning (NRR, förordning 2024/1991) trädde i kraft 2024 och
ställer bindande krav på EU:s medlemsstater att restaurera försämrade ekosystem.
Sverige ska lämna en **nationell restaureringsplan** till EU-kommissionen senast
**1 september 2026**.

Naturvårdsverket slutredovisade sitt underlagsarbete den 26 februari 2026.
Länsstyrelserna ansvarar för regional implementering — att omsätta nationella mål
till konkreta åtgärder i länet.

**Syftet med detta uppdrag** är att:
- Kartlägga och bedöma bevarandestatus för habitattyper i länets Natura 2000-områden
- Identifiera restaureringsbehov och prioritera åtgärder
- Leverera underlag till den nationella restaureringsplanen
- Bygga en geodatainfrastruktur för löpande uppföljning 2026–2027

---

## 2. Mål och leveranser

### Primära leveranser (före 1 september 2026)

| # | Leverans | Format | Mottagare |
|---|----------|--------|-----------|
| L1 | Kartskikt: Natura 2000-habitat med preliminär bevarandestatus | File GDB + WFS | Naturvårdsverket, intern |
| L2 | Prioriteringstabell: restaureringsbehov per habitat × objekt | Excel / CSV | Naturvårdsenheten |
| L3 | Länsöversikt: area per status och habitatkodserie | Rapport + kartor | Länsledning, NV |
| L4 | Underlag till nationell restaureringsplan | Word / PDF | Naturvårdsverket |

### Sekundära leveranser (2026–2027)

| # | Leverans | Format | Mottagare |
|---|----------|--------|-----------|
| L5 | Fältinventeringsresultat: uppdaterade habitatbedömningar | File GDB | Naturvårdsenheten |
| L6 | Åtgärdsplan per prioriterade objekt | Word / PDF | Kommuner, länsledning |
| L7 | Interaktiv dashboard / webbkarta | ArcGIS Online / Power BI | Internt + publikt |
| L8 | Slutrapport med metodik och rekommendationer | PDF | Länsledning, NV, EU |

---

## 3. Avgränsningar

- Geografiskt scope: **Södermanlands län** (länskod D / 04)
- Primärt fokus: **Natura 2000-områden** (SCI och SPA)
- Habitattyper enligt bilaga I i art- och habitatdirektivet
- Bedömningsskala: preliminär (pipeline-heuristik) → reviderad efter fältinventering
- Projektion: **SWEREF 99 TM (EPSG:3006)** för alla geodatalager

---

## 4. Organisation och ansvar

| Roll | Ansvar |
|------|--------|
| Naturvårdsenheten (uppdragsgivare) | Strategisk styrning, godkännande av leveranser, kontakt NV |
| Projektmedarbetare (GIS/analys) | Pipeline, geodataarbete, kartproduktion, rapportering |
| Projektmedarbetare (fält/inventering) | Fältinventering, datainmatning, artobservationer |
| GIS-enheten / Geodatasamordning | ArcGIS Enterprise-åtkomst, publicering av karttjänster |
| Naturvårdsverket | Nationell samordning, mottagare av underlag |

---

## 5. Tidsplan

Tidsplanen är anpassad mot EU-deadlinen **1 september 2026** som fast slutpunkt
för de primära leveranserna.

### Fas 1 – Uppstart (juni 2026)

| Aktivitet | Ansvar | Klart |
|-----------|--------|-------|
| Systemåtkomst: ArcGIS Pro, ArcGIS Enterprise, SharePoint | IT / GIS-enheten | 2026-06-15 |
| Orientering NRR-förordningen och NV:s nationella underlag | Projektmedarbetare | 2026-06-15 |
| Kontaktmöten: Naturvårdsenheten, GIS-enheten, NV | Projektledning | 2026-06-20 |
| Konfigurera geodatainfrastruktur (File GDB, projektion) | GIS/analys | 2026-06-20 |
| Körning av befintlig pipeline (`natura-2000`) mot aktuell data | GIS/analys | 2026-06-30 |

### Fas 2 – Datainsamling och GIS-analys (juni–juli 2026)

| Aktivitet | Ansvar | Klart |
|-----------|--------|-------|
| Hämta och förbereda NV Natura 2000 SCI/SPA (steg 1–2 i pipeline) | GIS/analys | 2026-07-01 |
| Hämta naturtypskartan Södermanland (Naturtypskartan_D) | GIS/analys | 2026-07-01 |
| Aktivera och hämta TUVA (betesmark) via Jordbruksverket | GIS/analys | 2026-07-10 |
| Aktivera och hämta VISS (vattenförekomster) | GIS/analys | 2026-07-10 |
| Hämta VMI (våtmarksinventeringen) | GIS/analys | 2026-07-10 |
| Köra prioritetsanalys med initiala betyg (steg 3) | GIS/analys | 2026-07-15 |
| Producera länsöversikt med area per status (steg 11) | GIS/analys | 2026-07-20 |
| Exportera till ArcGIS Pro (steg 10, `.gdb` + `.lyrx`) | GIS/analys | 2026-07-20 |

### Fas 3 – Fältinventering (juni–september 2026, löpande)

| Aktivitet | Ansvar | Klart |
|-----------|--------|-------|
| Planera fältinsatser: prioritera objekt med `okant`-status | Fält + GIS | 2026-06-30 |
| Fältinventering omgång 1 (prioriterade A-objekt) | Fält | 2026-08-01 |
| Datainmatning omgång 1 → uppdatera `assessment_template` | Fält + GIS | 2026-08-10 |
| Fältinventering omgång 2 (B-objekt, komplettering) | Fält | 2026-08-25 |
| Datainmatning omgång 2 | Fält + GIS | 2026-08-30 |

### Fas 4 – Reviderad analys och kartor (augusti 2026)

| Aktivitet | Ansvar | Klart |
|-----------|--------|-------|
| Uppdatera prioritetsanalys med fältdata (ersätt defaultvärden) | GIS/analys | 2026-08-10 |
| Köra om pipeline med reviderade betyg (steg 3–11) | GIS/analys | 2026-08-12 |
| Kartproduktion: tematiska kartor per habitatkodserie | GIS/analys | 2026-08-20 |
| QA/validering av geometrier och attribut | GIS/analys | 2026-08-22 |

### Fas 5 – Rapportering och leverans (augusti–september 2026)

| Aktivitet | Ansvar | Klart |
|-----------|--------|-------|
| Delrapport: länsöversikt + prioriteringar (L2, L3) | Projektmedarbetare | 2026-08-20 |
| Slutleverans kartskikt till NV (L1) | GIS/analys | 2026-08-25 |
| Underlag till nationell restaureringsplan (L4) | Projektmedarbetare | 2026-08-28 |
| **EU-deadline: nationell restaureringsplan** | NV / Sverige | **2026-09-01** |

### Fas 6 – Fortsatt arbete (oktober 2026–2027)

| Aktivitet | Period |
|-----------|--------|
| Fördjupad fältinventering (B- och C-objekt) | Höst 2026 |
| Åtgärdsplan per prioriterade objekt (L6) | Q4 2026 |
| Webbkarta / Power BI-dashboard (L7) | Q4 2026 – Q1 2027 |
| Uppföljning och revidering av bedömningar | Löpande |
| Slutrapport (L8) | Q2 2027 |

---

## 6. Datakällor

Se `docs/datakallor.md` för fullständig lista med licenser och API-information.

Prioritetsordning för datainsamling:

| Prioritet | Källa | Typ | Metod |
|-----------|-------|-----|-------|
| 1 | Naturvårdsverket – Natura 2000 SCI/SPA | Vektorgräns | Automatisk (pipeline) |
| 1 | Naturvårdsverket – Naturtypskartan D | Habitatvektor | Automatisk (pipeline) |
| 2 | Jordbruksverket – TUVA (betesmark) | Vektorytor | Manuell export |
| 2 | VISS – vattenförekomster | Vektorytor | Manuell export / API |
| 2 | VMI – våtmarksinventering | Vektorytor | Manuell katalogval |
| 3 | SLU Artdatabanken – artobservationer | Punkter | API (Artportalen) |
| 3 | Lantmäteriet – administrativa gränser | Vektor | Automatisk (CC0) |
| 3 | SMHI – hydrologi | Raster/vektor | API |

---

## 7. Verktyg och infrastruktur

| Kategori | Verktyg | Syfte |
|----------|---------|-------|
| GIS (primärt) | ArcGIS Pro + ArcGIS Enterprise | Analys, kartproduktion, publicering |
| Pipeline | Python (geopandas, requests) | Datahämtning och ETL |
| Geodatabas | File GDB (ESRI) | Primär lagring och leverans |
| Versionshantering | Git / GitHub | Kod och dokumentation |
| Dokument | Microsoft 365 (Word, PowerPoint) | Rapporter och presentationer |
| Kommunikation | Teams / Outlook | Intern samverkan |

Pipeline körs från `C:\Users\galag\GitHub\natura-2000` — se `docs/verktyg.md`.

---

## 8. Risker

| Risk | Sannolikhet | Konsekvens | Åtgärd |
|------|-------------|------------|--------|
| Försenad systemåtkomst (ArcGIS Enterprise, SharePoint) | Hög | Medel | Starta med lokalt ArcGIS Pro + öppna data |
| Tidsbrist inför EU-deadline 1 sep | Hög | Hög | Prioritera L1–L4 hårt; skjut L5–L8 till höst |
| Datainkonsistens (NV vs fält) | Medel | Hög | Markera osäker data med `okant`, dokumentera avvikelser |
| Ändrade krav från NV / EU-kommissionen | Medel | Hög | Löpande dialog med NV; agil planering |
| Väder / tillgänglighet fältlokaler | Medel | Låg–Medel | Buffertvekor inlagda i fas 3 |
| Resursbrist (en av två medarbetare sjuk) | Låg | Hög | Prioritera A-objekt; skala ned B/C till höst |

---

## 9. Uppföljning och rapportering

- **Veckomöte** med Naturvårdsenheten under fas 2–4 (juni–augusti)
- **Delrapport** efter fas 2 (leverans L2/L3, senast 20 augusti)
- **Slutleverans** fas 5 (senast 28 augusti, buffer till 1 september)
- **Statusuppdatering** i detta repo: `docs/projektplan.md` uppdateras vid milstolpar

---

*Projektplan upprättad: 2026-05-27 · Nästa revidering: efter fas 1 (2026-06-30)*
