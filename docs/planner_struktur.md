# Microsoft Planner – NRR Södermanland 2026–2027

> Förberedelse inför tjänststart 10 augusti 2026.
> Skapa denna plan i Planner via Teams när du har fått åtkomst till Länsstyrelsens M365-miljö.

---

## Inställningar

| Fält | Värde |
|------|-------|
| **Plannamn** | NRR Södermanland 2026–2027 |
| **Grupp** | Naturskyddsenheten (skapa ny om gruppen saknas) |
| **Synlighet** | Privat → dela med enhetschef och ev. kollega |

---

## Buckets (kolumner)

Skapa dessa buckets i ordning – de motsvarar projektets faser:

| # | Bucket | Motsvararar GitHub-milstolpe |
|---|--------|-------------------------------|
| 1 | 📋 Backlog | – |
| 2 | 🚀 Uppstart | Fas 1: Uppstart |
| 3 | 🗄️ Datainsamling | Fas 2: Datainsamling |
| 4 | 🌿 Fältinventering | Fas 3: Fältinventering |
| 5 | 🔬 Analys | Fas 4: Analys |
| 6 | 📝 Rapportering | Fas 5: Rapportering |
| 7 | ✅ Leverans | Fas 6: Leverans |

---

## Uppgifter per bucket

### 🚀 Uppstart (aug–sep 2026)

| Uppgift | Förfallodatum | Prioritet | Checklista |
|---------|---------------|-----------|-----------|
| Systemåtkomst: ArcGIS, SharePoint, Teams, SERS | 2026-08-21 | Urgent | ArcGIS Pro-licens; Portal; SERS; LifeWatch; VPN |
| Introduktionsmöten: Naturskyddsenheten och GIS-enheten | 2026-08-28 | Urgent | Enhetschef; kollegor; GIS-enheten; interna rutiner |
| Kontakt med Naturvårdsverket om NRR-krav | 2026-09-05 | Hög | NV-samordnare; leveransformat; deldatum |
| Genomgång av befintliga Natura 2000-karteringar | 2026-09-10 | Hög | Ladda ned skikt; identifiera luckor; dokumentera |

### 🗄️ Datainsamling (aug–okt 2026)

| Uppgift | Förfallodatum | Prioritet | Checklista |
|---------|---------------|-----------|-----------|
| ETL – NV: Natura 2000 WFS/WMS | 2026-09-30 | Hög | WFS-anslutning; polygoner Södermanland; File GDB |
| ETL – Lantmäteriet: gränser och höjddata | 2026-09-30 | Hög | Kommungränser; NH2+; SWEREF 99 TM |
| ETL – SLU Artdatabanken | 2026-10-15 | Medel | Artportalen/SERS; filtrera på länet; importera |
| ETL – SMHI och Jordbruksverket | 2026-10-15 | Medel | Hydrologi; betesmark (LPIS); CORINE |
| Geodatabas-setup: ESRI File GDB | 2026-10-31 | Hög | nrr_sodermanland_2026.gdb; domäner; attributschema |

### 🌿 Fältinventering (sep 2026 – jan 2027)

| Uppgift | Förfallodatum | Prioritet | Checklista |
|---------|---------------|-----------|-----------|
| Planering av fältinventering | 2026-09-20 | Hög | Prioritera områden; protokoll; utrustning |
| Fältinventering omgång 1 – höst 2026 | 2026-11-30 | Hög | GPS-insamling; foto; habitatstatus; SERS-inmatning |
| Fältinventering omgång 2 – vår/sommar 2027 | 2027-06-30 | Medel | Komplettering; sommarhabitat; kvalitetssäkring |
| Datainmatning och QA i SERS/LifeWatch | 2027-01-10 | Hög | Validera koordinater; habitatkodning; export |

### 🔬 Analys (okt 2026 – feb 2027)

| Uppgift | Förfallodatum | Prioritet | Checklista |
|---------|---------------|-----------|-----------|
| Statusbedömning per habitattyp | 2027-01-31 | Urgent | Kriterier; klassificering; osäkerheter; granskning |
| GIS-analyser: areal, buffert, fragmentering | 2027-01-31 | Hög | Areaberäkning SWEREF 99 TM; buffert; konnektivitet |
| Kartproduktion i ArcGIS Pro | 2027-02-10 | Medel | Översiktskarta; tematiska kartor; WMS/WFS-export |

### 📝 Rapportering (dec 2026 – mar 2027)

| Uppgift | Förfallodatum | Prioritet | Checklista |
|---------|---------------|-----------|-----------|
| Delrapport 1 – Datainsamling och inventeringsläge | 2026-12-15 | Medel | Status ETL; fältläge; riskanalys; nästa steg |
| Delrapport 2 – Preliminära statusbedömningar | 2027-02-01 | Medel | Preliminär klassificering; arealtabell; kartor |
| Visualiseringar: Power BI / ArcGIS Dashboard | 2027-02-28 | Medel | Nyckeltal; interaktiv karta; exportfigurer |
| Slutrapport: metodik, resultat och rekommendationer | 2027-03-10 | Urgent | Metodik; arealtabell; kartbilagor; rekommendationer |

### ✅ Leverans (mar 2027)

| Uppgift | Förfallodatum | Prioritet | Checklista |
|---------|---------------|-----------|-----------|
| Presentation för intressenter | 2027-03-20 | Hög | PowerPoint; intern presentation; NV-presentation |
| Leverans av underlag till Naturvårdsverket | 2027-03-31 | Urgent | Geodata (GDB); rapport (PDF); arealtabell (Excel); metadata |

---

## Etiketter (Labels i Planner)

Skapa dessa kategorier under planinställningar:

| Etikett | Färg | Användning |
|---------|------|-----------|
| GIS | Grön | GIS-analyser och kartproduktion |
| Fält | Orange | Fältinventering och habitatbedömning |
| Data | Blå | Datainsamling och ETL |
| Rapport | Röd | Rapportering och dokumentation |
| Samverkan | Lila | Dialog och koordinering med aktörer |
| Projektledning | Gul | Intern samordning och administration |

---

## Tips för användning

- **Synka med Teams-möten:** Länka Planner-uppgifter till Teams-kanalens flikar
- **Påminnelser:** Sätt påminnelse 1 vecka före förfallodatum för Urgent-uppgifter
- **Kommentarer:** Använd uppgiftens kommentarsfält som logg (vad gjordes, datum)
- **Bifogade filer:** Länka till SharePoint-dokument direkt från uppgiften
- **Veckogenomgång:** Gör en snabb genomgång varje måndag – flytta klara uppgifter, justera prioritet

---

*Skapad: 2026-05-28 | Uppdateras vid behov under projektet*
