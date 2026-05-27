# CLAUDE.md – Naturrestaureringsuppdraget, Länsstyrelsen Södermanland

> Projektinstruktioner för Claude. Läs detta dokument i sin helhet innan du utför arbete i detta repo.

---

## 1. Projektkontext

**Uppdrag:** Implementering av EU:s naturrestaureringsförordning (NRR – Nature Restoration Regulation) i Södermanlands län, på uppdrag av Länsstyrelsen i Södermanlands län.

**Tjänst:** Två personer anställs för att genomföra naturrestaureringsuppdraget. Rollen innefattar GIS-analys, fältinventering, databasarbete och rapportering med fokus på Natura 2000-områden och biologisk mångfald i länet.

**Arbetsgivare:** Länsstyrelsen i Södermanlands län, Nyköping  
**Avdelning:** Natur- och landsbygdsavdelningen (Naturvårdsenheten)  
**Tidshorisont:** 2026–2027 (projekttiden anpassas efter uppdraget)

**Viktiga datum:**
- Sverige ska lämna nationell restaureringsplan till EU-kommissionen: **1 september 2026**
- Naturvårdsverket slutredovisade sitt underlag: 26 februari 2026

---

## 2. Organisationsstruktur – Länsstyrelsen Södermanland

Länsstyrelsen i Södermanlands län är organiserad i **fem avdelningar** med underliggande enheter:

| Avdelning | Relevans för uppdraget |
|-----------|------------------------|
| **Natur- och landsbygdsavdelningen** | Primär avdelning – naturvårdsenheten, Natura 2000, restaurering, LONA |
| **Miljö- och vattenavdelningen** | Sekundär – vattenförekomster, klimatanpassning, miljötillsyn |
| **Samhällsbyggnadsavdelningen** | Samverkan – grön infrastruktur, planering, GIS |
| Rättsavdelningen | Tillstånd, juridik |
| Administrativ avdelning | HR, ekonomi, IT |

**Närmast berörda enheter:**
- **Naturvårdsenheten** – inventering, skötsel av naturreservat, Natura 2000
- **GIS-enheten / Geodatasamordning** – gemensam GIS-infrastruktur för alla länsstyrelser via gis.lansstyrelsen.se

---

## 3. Teknisk miljö och verktyg

### GIS-system (primärt)
Länsstyrelsen använder **ESRI ArcGIS**-plattformen som primärt GIS-system:

- **ArcGIS Enterprise Portal** (v11.5.0) – internt geodataportal, ext-geoportal.lansstyrelsen.se
- **ArcGIS Pro** – arbetsbordsapplikation för GIS-analys
- **ArcGIS Online** – webbkartor och delning
- **ArcGIS Server / REST API** – tjänster (WMS/WFS/Feature Services)
- **WebbGIS** – publika kartvisare (gis.lansstyrelsen.se/webbgis)
- **Geodatakatalogen** – metadata och geodatainventering (gis.lansstyrelsen.se/geodata)

> OBS: ChatGPT-planen rekommenderar QGIS + PostGIS. Länsstyrelsen använder primärt ESRI-verktyg. QGIS kan användas som komplement men ArcGIS Pro är standard.

### Kontorssystem (Microsoft 365)
Länsstyrelsen, som statlig myndighet, använder **Microsoft 365**:

- **Teams** – kommunikation och möten
- **SharePoint** – dokumenthantering och intranät
- **Planner / To Do** – uppgiftshantering
- **Word / Excel / PowerPoint** – dokument, rapporter, presentationer
- **Power BI** – visualiseringar och dashboards
- **Outlook** – e-post och kalender
- **OneDrive** – fillagring

### Databas
- **Länsstyrelsens ESRI Geodatabase** (File Geodatabase / Enterprise GDB) – primärt
- **PostGIS/PostgreSQL** – möjligt komplement för analys
- **SDE (Spatial Database Engine)** – via ArcGIS Enterprise

### Datakällor (öppna svenska myndighetskällor)
Se `docs/datakallor.md` för fullständig lista.

Prioriterade källor:
- Naturvårdsverket (Natura 2000 WFS/WMS, NMD2023)
- Lantmäteriet (administrativa gränser, höjddata – CC0)
- SLU Artdatabanken (art- och naturtypsregistreringar)
- SMHI (klimat- och hydrologidata)
- Jordbruksverket (betesmark, jordbruksarealer)
- Copernicus/EU (CORINE Land Cover)

---

## 4. Arbetsuppgifter och ansvarsområden

### Primära arbetsuppgifter

#### A. GIS-analys och kartproduktion
- Kartläggning av livsmiljötyper (habitat) i Natura 2000-områden
- Statusbedömning (god / icke god / okänd) per habitattyp
- Rumsliga analyser: area-beräkningar, buffertanalyser, fragmenteringsanalys
- Framtagning av tematiska kartor i ArcGIS Pro
- Publicering av karttjänster (WMS/WFS) via ArcGIS Enterprise

#### B. Datainsamling och fältinventering
- Inventering av naturvärden i fält (artobservationer, habitatstatus)
- Datainmatning i ESRI-databaser och nationella system (SERS, LifeWatch)
- Koordinering med SLU Artdatabanken och Naturvårdsverket

#### C. Databasarbete och ETL
- Bygga och underhålla geodatabaser (ESRI File GDB / Enterprise GDB)
- ETL-flöden för att hämta och transformera data från öppna tjänster
- Projektion: SWEREF 99 TM (EPSG:3006) för alla lager

#### D. Rapportering och dokumentation
- Delrapporter vid milstolpar
- Slutrapport med metodik, resultat och rekommendationer
- Beslutsunderlag för naturvård och restaureringsåtgärder
- Dokumentation av datamodeller och ETL-processer

#### E. Visualiseringar och presentationer
- Kartor och diagram i PowerPoint för styrgrupp och beslutsfattare
- Eventuell interaktiv dashboard i Power BI eller ArcGIS Dashboard
- Presentationer för kommuner, myndigheter och intressenter

#### F. Samverkan och koordinering
- Samarbete med Naturvårdsverket, Skogsstyrelsen, HaV, Jordbruksverket
- Dialog med kommuner i Södermanlands län
- Rapportering till EU (via nationell plan)

---

## 5. Tidsplan (uppskattad)

| Fas | Period | Innehåll |
|-----|--------|----------|
| Uppstart | Mån 1 | Orientering, systemåtkomst, verktygsinlärning (ArcGIS Pro, SharePoint), kontakter |
| Datainsamling | Mån 1–3 | ETL från NV, LM, SLU, SMHI. Geodatabas-setup. |
| Fältinventering | Mån 2–5 | Inventering i Natura 2000-områden i länet |
| Analys | Mån 3–6 | GIS-analyser, statusbedömningar, kartproduktion |
| Rapportering | Mån 5–7 | Delrapporter, visualiseringar, slutrapport |
| Presentation | Mån 7 | Presentation för intressenter, leverans |

> Nationell restaureringsplan ska lämnas till EU 1 september 2026 – synka leveranser mot detta.

---

## 6. Nyckelresurser och länkar

| Resurs | URL / Plats |
|--------|-------------|
| Länsstyrelsen Södermanland | https://www.lansstyrelsen.se/sodermanland |
| GIS på länsstyrelserna | https://gis.lansstyrelsen.se |
| ArcGIS Geoportal (LST) | https://ext-geoportal.lansstyrelsen.se |
| Naturvårdsverket NRR | https://www.naturvardsverket.se/amnesomraden/mark-och-vattenanvandning/eu-forordning-for-att-restaurera-natur/ |
| Nationell restaureringsplan | https://www.naturvardsverket.se/om-oss/regeringsuppdrag/slutredovisade-regeringsuppdrag/forslag-till-nationell-restaureringsplan/ |
| Geodatakatalogen LST | https://gis.lansstyrelsen.se/geodata/geodatakatalogen/ |
| Lantmäteriet öppna data | https://www.lantmateriet.se/oppnadata |
| SLU Artdatabanken | https://www.artdatabanken.se |
| NMD2023 (NV) | https://geodata.naturvardsverket.se |
| Öppna tjänster Natura 2000 | https://ext-geodatakatalog-forv.lansstyrelsen.se |

---

## 7. Kodstandarder och namnkonventioner

### Filnamn
- Använd svenska för dokumentnamn: `rapport_naturvarden_2026.docx`
- Kod/skript: engelska med snake_case: `fetch_natura2000.py`
- GIS-lager: svenska med understreck: `natura2000_sodermanland_pol.shp`

### Projektion
- **SWEREF 99 TM (EPSG:3006)** används för ALLA geografiska data

### Versionskontroll (detta repo)
- Branches: `main` (stabil), `develop` (aktiv utveckling)
- Commits: Svenska meddelanden, t.ex. `Lägg till ETL-skript för Natura 2000`
- Använd `.gitignore` för stora datafiler (geodata lagras ej i Git)

### Python-skript
- Python 3.10+
- Bibliotek: `arcpy` (om tillgång finns), `geopandas`, `requests`, `sqlalchemy`
- Dokumentera alla skript med docstrings på svenska

---

## 8. Riskhantering

| Risk | Sannolikhet | Konsekvens | Åtgärd |
|------|-------------|------------|--------|
| Försenad systemåtkomst (ArcGIS, SharePoint) | Hög | Medel | Påbörja med öppna data och QGIS tills ArcGIS-licens aktiveras |
| Datainkonsistens mellan källor | Medel | Hög | Validering mot kända värden, metadata-kontroll |
| Ändrade krav från NV / EU | Medel | Hög | Agil planering, regelbunden dialog med uppdragsgivare |
| Resursbrist (kompetens) | Låg–Medel | Medel | Intern samverkan, kontakta GIS-enheten |
| Tekniska problem (ESRI-licenser) | Låg | Hög | QGIS som backup, support via LST IT |

---

## 9. Repo-struktur

```
Länsstyrelsen/
├── CLAUDE.md              ← Denna fil (projektinstruktioner för Claude)
├── README.md              ← Publik projektbeskrivning
├── index.html             ← GitHub Pages hemsida
├── docs/
│   ├── projektplan.md     ← Detaljerad projektplan
│   ├── datakallor.md      ← Datakällor och licenser
│   ├── datamodell.md      ← ER-diagram och tabellstruktur
│   └── riskanalys.md      ← Risklogg
├── scripts/
│   ├── etl/               ← ETL-skript (Python)
│   └── analysis/          ← Analysverktyg (Python/SQL)
├── templates/
│   └── rapport_mall.docx  ← Rapportmall (Swedish)
└── .gitignore
```

---

## 10. Instruktioner för Claude

När du arbetar i detta projekt, Claude:

1. **Skriv alltid på svenska** (med undantag för kod och tekniska termer på engelska)
2. **Använd ESRI-terminologi** i GIS-relaterade svar, inte enbart QGIS/PostGIS
3. **Referera till NRR** (naturrestaureringsförordningen) och nationell plan vid strategiska beslut
4. **Spara leverabler** i rätt undermappar enligt repo-strukturen ovan
5. **Verifiera datakällor** mot listan i `docs/datakallor.md` innan du föreslår nya
6. **Synka tidplanen** mot EU-deadlinen 1 september 2026
7. **Kontrollera** om filer finns innan du skriver nya (undvik dubbletter)
8. **GitHub Pages** (index.html) uppdateras när projektplanen förändras

---

*Senast uppdaterad: 2026-05-27*
