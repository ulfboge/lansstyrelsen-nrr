> **Arkiverad.** Detta dokument (version 1.1, 2026-05-27) är ersatt av den formella projektplanen
> version 2.0: [`docs/Projektplan_NRF_Sodermanland_2026_v2.docx`](../Projektplan_NRF_Sodermanland_2026_v2.docx)
> (2026-09-04). Version 1.1 skrevs innan anställningen började och är inaktuell — bland annat är
> fältarbetet flyttat till 2027 och kontaktpersonen (Stefan Henriksson) har slutat. Behålls här som
> historik.

---

# Projektplan – Genomförande av naturrestaureringsförordningen (NRF)
## Länsstyrelsen i Södermanlands län, Naturskyddsenheten

**Version:** 1.1  
**Datum:** 2026-05-27  
**Uppdragsgivare:** Länsstyrelsen i Södermanlands län – Naturskyddsenheten  
**Referens:** 2451-2026  

---

## 1. Bakgrund och uppdrag

Länsstyrelserna har ett **regeringsuppdrag** att implementera EU:s
naturrestaureringsförordning (NRF, förordning 2024/1991) regionalt.
Uppdraget innebär att länsstyrelsen ska:

- Bedöma statusen för **livsmiljötyper** i beslutade Natura 2000-områden
- Bedöma arealen för olika livsmiljötyper
- Klassificera om status för dessa är i **gott, icke gott eller okänt tillstånd**

Resultaten rapporteras till **Naturvårdsverket** som samordnar den nationella
nivån. Det är Naturvårdsverket — inte länsstyrelserna — som ansvarar för
rapporteringen vidare till EU-kommissionen.

Tjänsten är placerad på **Naturskyddsenheten** (ca 15 personer), som ingår i
Naturavdelningen och arbetar med myndighetsutövning kring skydd och bevarande
av naturvärden i Södermanlands län.

---

## 2. Mål

### Primärt mål
Genomföra länsstyrelsens del av NRF-uppdraget: statusbedömning av livsmiljötyper
i länets beslutade Natura 2000-områden med klassificering per habitattyp.

### Delmål
1. Etablera en fungerande arbetsprocess för statusbedömning (GIS + fält)
2. Producera en bedömning av areal och tillstånd per livsmiljötyp och objekt
3. Identifiera och prioritera objekt med störst restaureringsbehov
4. Säkerställa samverkan med berörda aktörer (internt, kommuner, markägare, NV)
5. Leverera underlag till Naturvårdsverket i tid

---

## 3. Leveranser

| # | Leverans | Format | Mottagare |
|---|----------|--------|-----------|
| L1 | Statusbedömning: areal och tillstånd per livsmiljötyp × Natura 2000-objekt | GDB / Excel | Naturvårdsverket, intern |
| L2 | Kartor: livsmiljötyper med statusklassificering i Södermanland | ArcGIS Pro / PDF | Naturskyddsenheten, länsledning |
| L3 | Prioriteringslista: objekt med restaureringsbehov | Excel / Word | Naturskyddsenheten |
| L4 | Åtgärdsförslag per prioriterat objekt | Word | Markägare, kommuner, NV |
| L5 | Intern dokumentation av metodik och datamodell | Markdown / Word | Naturskyddsenheten |

---

## 4. Avgränsningar

- Geografiskt scope: **Södermanlands län** (länskod D / 04)
- Objekt: **beslutade Natura 2000-områden** (SCI och SPA)
- Livsmiljötyper enligt bilaga I i art- och habitatdirektivet
- Statusklassificering: **gott / icke gott / okänt** (NRF-terminologi)
- Projektion: SWEREF 99 TM (EPSG:3006) för alla geodatalager

---

## 5. Organisation

| Roll | Ansvar |
|------|--------|
| Naturskyddshandläggare (projektansvar) | Projektledning, GIS-analys, samverkan, rapportering |
| Naturskyddsenheten (kollegor) | Expertbidrag, fältsamarbete, intern förankring |
| Naturvårdsenheten | Nära samverkan – förvaltning och skötsel av naturreservat |
| GIS-enheten / Geodatasamordning | ArcGIS Enterprise-åtkomst, karttjänster |
| Chef (Stefan Henriksson) | Styrning, prioritering, eskalering |
| Naturvårdsverket | Nationell samordning, mottagare av bedömningsunderlag |
| Kommuner i länet | Dialog om lokala restaureringsinsatser |
| Markägare | Samverkan kring åtgärder på privat mark |

---

## 6. Tidsplan

### Fas 1 – Uppstart och orientering

| Aktivitet | Klart |
|-----------|-------|
| Systemåtkomst: ArcGIS Pro, ArcGIS Enterprise, SharePoint, NNK | Mån 1 |
| Genomgång av NRF-uppdraget och NV:s vägledning | Mån 1 |
| Möten med kollegor, GIS-enheten och chef | Mån 1 |
| Inventering av befintliga data och karteringsunderlag för länet | Mån 1 |
| Genomgång av NNK (Nationell Naturtypskartering) för Södermanland | Mån 1–2 |

### Fas 2 – Datainsamling och GIS-analys

| Aktivitet | Klart |
|-----------|-------|
| Hämta och kvalitetssäkra Natura 2000-gränser (SCI/SPA) | Mån 2 |
| Hämta naturtypskartan för Södermanland (Naturtypskartan_D) | Mån 2 |
| Komplettera med TUVA (betesmark), VISS (vatten), VMI (våtmark) | Mån 2–3 |
| Beräkna areal per livsmiljötyp och Natura 2000-objekt | Mån 3 |
| Initial statusklassificering baserad på karteringsdata | Mån 3 |
| Identifiera objekt med `okant`-status som kräver fältkontroll | Mån 3 |

### Fas 3 – Fältinventering (löpande)

| Aktivitet | Klart |
|-----------|-------|
| Planera fältinsatser utifrån prioriteringslista | Mån 2 |
| Fältbesök och habitatbedömningar i prioriterade objekt | Mån 2–6 |
| Datainmatning i NNK och/eller GIS-databas | Löpande |
| Revidera statusklassificering efter fältdata | Löpande |

### Fas 4 – Samverkan och åtgärdsplanering

| Aktivitet | Klart |
|-----------|-------|
| Intern förankring av prioriteringar med Naturskyddsenheten | Mån 4 |
| Dialog med berörda markägare om restaureringsåtgärder | Mån 4–6 |
| Samverkan med kommuner, Skogsstyrelsen, HaV, Jordbruksverket | Löpande |
| Utarbeta åtgärdsförslag per prioriterat objekt (L4) | Mån 5–6 |

### Fas 5 – Rapportering och leverans

| Aktivitet | Klart |
|-----------|-------|
| Sammanställa statusbedömning (L1) | Mån 6 |
| Producera kartor och länsöversikt (L2) | Mån 6 |
| Leverera underlag till Naturvårdsverket | Mån 7 |
| Dokumentera metodik (L5) | Mån 7 |

> Notera: Naturvårdsverket ansvarar för att förmedla underlagen vidare
> till EU-kommissionen. Länsstyrelsens leverans går till NV.

---

## 7. Arbetsprocess för statusbedömning

Statusklassificering per livsmiljötyp × Natura 2000-objekt görs i tre steg:

**Steg 1 – Karteringsdata (GIS)**
Arealbedömning baseras på Naturtypskartan (NNK), Natura 2000-gränser
och kompletterande källor (TUVA, VMI, VISS). Initial status sätts till
`okant` om fältdata saknas.

**Steg 2 – Fältkontroll**
Objekt med `okant`-status och hög ekologisk prioritet besöks i fält.
Bedömning dokumenteras i `data/templates/assessment_template_sodermanland.csv`
med fälten: kondition, osäkerhet, bedömare, datum, föreslagen åtgärd.

**Steg 3 – Revidering och leverans**
Fältdata matas in, statusklassificering revideras och leveranspaket
produceras till Naturvårdsverket.

---

## 8. Verktyg

| Verktyg | Användning |
|---------|------------|
| ArcGIS Pro | GIS-analys, kartproduktion, habitatbedömning |
| NNK (Nationell Naturtypskartering) | IT-stöd för naturtypskartering och datainmatning |
| ArcGIS Enterprise | Publicering av karttjänster och datadelning |
| Python-pipeline (`natura-2000`) | Automatiserad datahämtning och ETL |
| Microsoft 365 | Dokument, kommunikation, Teams-möten |

Se `docs/verktyg.md` för pipeline-dokumentation.

---

## 9. Risker

| Risk | Sannolikhet | Konsekvens | Åtgärd |
|------|-------------|------------|--------|
| Försenad systemåtkomst (ArcGIS Enterprise, NNK) | Hög | Medel | Starta med lokalt ArcGIS Pro + öppna data |
| Svårtillgängliga objekt i fält (mark, terräng, väder) | Medel | Låg–Medel | Boka tidiga fältperioder, buffertdagar |
| Bristfällig befintlig kartering (många `okant`) | Medel | Medel | Prioritera hårt; dokumentera osäkerheter tydligt |
| Ändrade krav eller vägledning från NV | Medel | Hög | Löpande kontakt med NV; agil planering |
| Intressekonflikter med markägare | Låg–Medel | Medel | Tidig dialog; förankra via Naturskyddsenheten |

---

## 10. Uppföljning

- Löpande avstämning med chef och kollegor på Naturskyddsenheten
- Statusuppdatering i `docs/projektplan.md` vid varje fas-skifte
- Leveranstidpunkter synkas med Naturvårdsverkets vägledning

---

*Version 1.1 – Reviderad baserat på jobbbeskrivning ref. 2451-2026 · 2026-05-27*
