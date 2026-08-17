# Arbetsplan NNK 2026 — statusbedömning av livsmiljötyper inom Natura 2000

## Länsstyrelsen i Södermanlands län · Naturskyddsenheten · ref. 2451-2026

**Version:** 1.3
**Datum:** 2026-08-17
**Omfattning:** Natura 2000 (SCI/SAC) i D-län som huvudspår, naturreservat och nationalpark som parallellt screeningspår
**Bemanning:** 1 handläggare heltid + 1 kollega ca 50 %
**Underlag:** `docs/underlag/FAQ - om uppdraget och hur det genomförs_version 1_1.pdf` (2026-07-03) · `docs/underlag/handledning/Handledning NNK 20260703.pdf` · `docs/underlag/handledning/Lathud_granskning_WebbGIS_KartLitS_20260714.pdf` · `docs/underlag/D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx` · `docs/underlag/kartering.csv`
**Syskondokument:** `docs/nnk/runbook_nnk_2026.md` (steg för steg, 68 uppgifter) · `docs/nnk/kontrollrum_nnk_2026.html` (Gantt och avbockning) · `docs/nnk/metodik_forvaltarkunskap.md` (arbetspaket H) · `docs/nnk/blankett_forvaltarkunskap_nnk.xlsx` · `docs/nnk/nnk_kunskapslage_dashboard.html` · `scripts/analysis/koppla_omraden.py`

---

## 0. Sammanfattning — vad det här året faktiskt handlar om

Regeringsuppdraget sträcker sig över 2026 och 2027, men **2026 är inte ett produktionsår — det är ett kartläggnings- och planeringsår.** FAQ fråga 6 säger klart vad som ska vara klart vid årsskiftet: en redovisning av *vad vi vet*, *vad vi inte vet*, och *en plan för hur det okända ska bli känt*. Själva tillståndsbedömningen ska vara klar under 2027.

Två förhållanden gör att arbetet i D-län ser annorlunda ut än man först skulle tro:

**1. Utbredningsproblemet är mycket litet på land — men enormt i havet.**
Av 17 741 ha "osäker natura-/icke-natura" inom länets Natura 2000-områden ligger **16 912 ha (95 %) i marin miljö**. Kvar på land och i limniska miljöer finns bara ca **445 ha osäker** och **108 ha obestämd** naturtyp. Och FAQ fråga 16 och 29 säger uttryckligen att marina livsmiljötyper *inte* ska läggas in i NNK och att arbetsgruppen för akvatiska miljöer startar först hösten 2026. **Slutsats: lägg ingen tid på det marina i år. Den terrestra utbredningsfrågan är på ett par hundra hektar — den går att lösa.**

**2. Tillståndsproblemet är nästan totalt — men får inte lösas ännu.**
**8 587 av 9 980 polygoner (86 %) inom länets Natura 2000-områden har "Ej bedömd status".** Bara 482 polygoner är klassade som fullgod och 336 som icke fullgod livsmiljötyp. Samtidigt säger FAQ fråga 30 att NNK under sommaren 2026 får **nya attribut för tillståndsbedömning**, driftsatta i slutet av september, och att Naturvårdsverket **rekommenderar att man avvaktar** med tillståndsbedömning i NNK tills dess. FAQ fråga 10 upprepar det för terrestra livsmiljötyper: vänta på fastställda vägledningar.

**Det ger årets arbete en tydlig form:**

| Period | Vad som görs | Varför |
|---|---|---|
| v34–v39 (aug–sep) | Orientering, systemåtkomst, skrivbordsgranskning av **utbredning och gränser**, fältkontroll i prioriterade hävdberoende objekt medan säsongen håller | Fältsäsongen tar slut; tillståndsattributen finns inte än |
| v40–v46 (okt–nov) | Nya NNK-attribut driftsatta → börja registrera tillstånd där kunskapen redan finns; systematisk genomgång batch för batch | Verktyget finns; sen höst passar skrivbordsarbete |
| v47–v52 (dec) | Sammanställning av kunskapsläge + **plan för 2027**, underlag till årsredovisningen | Det är detta som är 2026 års faktiska leverans |

---

## 1. Kravnedbrytning — vad som ska vara klart när

Direkt ur FAQ fråga 6, översatt till D-läns förutsättningar.

### 1.1 Klart 2026, inom Natura 2000

| Krav | Läge i D-län idag | Insats |
|---|---|---|
| Areal av livsmiljötyper i gott/inte gott tillstånd (där det är känt) | 482 pol. fullgod, 336 icke fullgod — ca 8 % av polygonerna | Registrera i NNK efter driftsättning v40 |
| Areal där tillståndet är okänt, inkl. osäker/obestämd naturtyp och utvecklingsmark | 8 587 pol. ej bedömd status; 445 ha osäker terr.; 108 ha obestämd; 167 pol. utvecklingsmark | Kvantifiera per objekt — arbetspaket C |
| Redovisning av vilka livsmiljötyper per N2000-område som omfattas av osäkerhet | Går att generera ur NNK-uttaget | Arbetspaket E1 |
| **Plan** för hur osäker utbredning och okänt tillstånd ska bli känt | Saknas | **Årets huvudleverans — arbetspaket F** |

### 1.2 Klart 2027

- Livsmiljötypernas utbredning (yta/linje/punkt) och tillstånd (gott/inte gott) inom Natura 2000
- Slutredovisning till regeringen
- Inom naturreservat och nationalpark: areal i gott/inte gott där det är känt, areal osäker/okänd, samt plan för åtgärdande

### 1.3 Klart 2028

- Utbredning och tillstånd i NNK för samtliga skyddade områden
- Åtgärdsområden i IT-stöd för skötsel (SkötselDOS)
- Uppgifterna i NNK förs över till SDF → EU-rapportering

> **Konsekvens för planeringen:** naturreservaten har 2027 som deadline, inte 2028. Därför ska de inte ignoreras i år — men de behöver bara en screening (arbetspaket G), inte full genomgång.

---

## 2. Kunskapsläget i D-län — nollmätning per 2026-01-20

### 2.1 Natura 2000 (SCI/SAC), 197 områden

| Mått | Värde |
|---|---|
| Totalt skyddat | 50 009 ha |
| Karterat i NNK | 44 852 ha (90 %) |
| Okarterat | 5 158 ha — varav 4 845 ha i **Båven** (SE0220303) och 299 ha i Tullgarn södra |
| Karterat som livsmiljötyp | 22 851 ha |
| — varav **terrestert** | **7 821 ha** |
| — varav limniskt | 9 377 ha |
| — varav marint | 5 696 ha |

### 2.2 Terrestra livsmiljötyper — det som faktiskt ska bedömas

| Kategori | Areal | Kommentar |
|---|---|---|
| Skog | 4 206 ha | 9010 taiga dominerar (2 987 ha) |
| Gräsmark | 2 676 ha | 9070 trädklädd betesmark 928 ha, 8230 hällmarkstorräng 487 ha, 6270 silikatgräsmark 463 ha |
| Våtmark | 638 ha | |
| Stränder | 277 ha | främst 1621 |
| Berg | 22 ha | |
| Dyner | 2 ha | |
| **Summa** | **7 821 ha** | |
| varav **hävdberoende** | **2 661 ha** | högsta prioritet enligt FAQ fråga 11 |

### 2.3 Naturtypsstatus — polygoner inom N2000

| Status | Antal | Andel |
|---|---|---|
| Fullgod Natura-naturtyp | 482 | 4,8 % |
| Icke fullgod Natura-naturtyp | 336 | 3,4 % |
| Utvecklingsmark | 167 | 1,7 % |
| Övrigt, icke Natura-naturtyp | 237 | 2,4 % |
| **Ej bedömd status** | **8 587** | **86,0 %** |
| Status saknas | 171 | 1,7 % |

### 2.4 Karteringsstatus och ursprung — kvalitetsrisken

| Mått | Värde | Innebörd |
|---|---|---|
| Granskad vid skrivbordet | 8 578 | |
| Ej granskad | 335 | |
| Besökt/inventerad i fält | 744 (7,5 %) | Verklig fältkunskap finns i en liten minoritet |
| Ursprung **BIDOS** | 9 576 (96 %) | Basinventeringen, vägledningar **före 2011** — FAQ fråga 28: "generellt gammalt, har sannolikt aldrig kontrollerats närmare" |
| Ursprung NNK | 395 | |

I hela länets NNK-uttag (`docs/underlag/kartering.csv` / `docs/underlag/naturtypskarta/NNK_YTA`, 14 830 polygoner för alla skyddsformer) är **81 % skapade 2012** — migreringen från BIDOS. Endast 31 polygoner är redigerade under 2025. **Underlaget är i praktiken 14 år gammalt.**

> Uttaget är den **publika** Natura naturtypskartan. Den saknar områdesidentitet och strippar kommentarer och användaruppgifter (handledningen 1.3). Områdeskopplingen är löst geometriskt med `scripts/analysis/koppla_omraden.py`, som knyter 9 609 ytor till länets 197 Natura 2000-områden — validerat mot statistikuttaget till 0,1 %. För spårbarhetsfälten krävs ett uttag ur NNK Ajourhålla.

### 2.5 Sällsynta livsmiljötyper i länet (< 50 ha inom N2000)

Dessa har högt prioriteringsvärde enligt FAQ fråga 11 (liten utbredning) och samlas i ett fåtal objekt:

`9162` 0,6 · `8210` 1,1 · `1620` 1,3 · `6430` 1,3 · `1640` 1,8 · `2181` 1,9 · `8232` 2,4 · `9750` 2,7 · `1220` 3,7 · `7231` 4,4 · `6280` 5,8 · `9110` 6,3 · `5133` 7,2 · `5130` 7,6 · `9180` 10,3 · `6230` 15,8 · `4030` 15,8 · `8220` 20,8 · `6210` 25,2 · `6110` 26,6 · `8231` 28,8 · `9060` 29,0 · `9072` 29,0 · `7230` 34,4 · `9190` 41,4 · `3260` 43,8 · `7110` 47,0 ha

---

## 3. Hierarkisk arbetsstruktur (WBS)

```
NNK/NRF 2026 — Södermanland
│
├── A. Etablering och förutsättningar                      [v34–v36]
│   ├── A1  Systemåtkomst och behörigheter
│   ├── A2  Metodik- och regelverksgenomgång
│   ├── A3  Intern förankring och rollfördelning
│   └── A4  Arbetsmiljö för data (repo, mallar, versionshantering)
│
├── B. Fältsäsong 2026 — det som inte kan vänta            [v34–v41]
│   ├── B1  Fältplanering och urval
│   ├── B2  Fältkontroll hävdberoende gräsmark (batch B)
│   ├── B3  Fältkontroll sällsynta livsmiljötyper (batch C, D)
│   └── B4  Fältdokumentation och inmatningsunderlag
│
├── C. Skrivbordsgranskning av utbredning                  [v35–v46]
│   ├── C1  Granskningsrutin och checklista
│   ├── C2  Batch S — storobjekt (Skärgårdsreservaten, Nynäs)
│   ├── C3  Batch A — kust och skärgård
│   ├── C4  Batch B — ängs- och hagmark inland
│   ├── C5  Batch C — våtmark och vattendrag
│   ├── C6  Batch D — skog och ädellöv
│   └── C7  Okarterade ytor (Båven, Tullgarn södra)
│
├── D. Tillståndsbedömning i NNK                           [v40–v50]
│   ├── D1  Driftsättning nya NNK-attribut, utbildning
│   ├── D2  Registrering där kunskap redan finns
│   ├── D3  Registrering av fältdata från B
│   └── D4  Avvikelser mot bevarandeplan/reservatsbeslut
│
├── E. Sammanställning av kunskapsläget                    [v45–v50]
│   ├── E1  Uttag och statistik per objekt och livsmiljötyp
│   ├── E2  Kvantifiering av osäkerhet och kunskapsluckor
│   └── E3  WebbGIS-dokumentation (KartLitS-mall)
│
├── F. Plan för 2027 — årets huvudleverans                 [v46–v52]
│   ├── F1  Insatsbehov och volymuppskattning
│   ├── F2  Prioritering och antaganden
│   ├── F3  Vad vi gör själva / vad vi behöver hjälp med
│   └── F4  Underlag till årsredovisningen
│
├── G. Parallellspår naturreservat och nationalpark        [v42–v52]
│   ├── G1  Screening av NR/NP utanför N2000
│   └── G2  Grovplan för 2027
│
└── H. Förvaltardialog — Naturvårdsenhetens kunskap        [v35–v48]
    ├── H1  Kartläggning av vem som förvaltar vad
    ├── H2  Åtgärdas-ytorna — länets egen olösta lista
    ├── H3  Förvaltarsamtal och blankettinsamling
    ├── H4  Eftersök av odokumenterade underlag
    └── H5  Registrering i granskningslager och NNK
```

---

## 4. Arbetspaket i detalj

### A. Etablering och förutsättningar · v34–v36

| ID | Aktivitet | Klart | Ansvar |
|---|---|---|---|
| A1.1 | Beställ och verifiera behörighet: ArcGIS Pro, NNK in-/utcheckning, ArcGIS Enterprise, SkötselDOS, Artportalen, KartLitS WebbGIS | v35 | Handläggare |
| A1.2 | Verifiera att NNK-utcheckning fungerar mot ett testobjekt | v35 | Handläggare |
| A1.3 | Åtkomst till samverkansytan för Livsmiljötyper (dokument, manualer, kodlista) | v34 | Handläggare |
| A2.1 | Läs `Handledning NNK 20260703.pdf` och `Lathud_granskning_WebbGIS_KartLitS_20260714.pdf` | v34 | Båda |
| A2.2 | Gå igenom `Kodlista_NNK_20260703.xlsx` — särskilt kategoriindelning 2026 och undergrupper | v35 | Handläggare |
| A2.3 | Installera `KartLits_NNK_GIS_mall_v_2` och testa mot ett objekt | v35 | Handläggare |
| A2.4 | Hämta fastställda vägledningar för livsmiljötyper — **kontrollera vilka som är fastställda vs. remiss** (FAQ f.10) | v36 | Handläggare |
| A3.1 | Avstämning med chef: mandat, tidsbudget, förväntad leverans till årsredovisningen | v35 | Handläggare |
| A3.2 | Kartlägg vem på Naturvårdsenheten som förvaltar vilka objekt — de sitter på skötselhistoriken | v36 | Handläggare |
| A3.3 | Rollfördelning med 50 %-kollegan (se avsnitt 6) | v35 | Båda |
| A3.4 | Anmäl er till KartLitS arbetsgrupper (skog, gräsmark, våtmark) och funktionsbrevlådan `kartlitsN2000@naturvardsverket.se` | v36 | Handläggare |
| A4.1 | Skapa arbetsstruktur: uttagsmapp, granskningslogg, fältprotokoll | v36 | Handläggare |
| A4.2 | Etablera rutin för NNK-uttag så att statistiken kan följas över tid | v36 | Handläggare |

**Leverans A:** Fungerande arbetsplats, dokumenterad rollfördelning, bekräftad tolkning av uppdraget.

---

### B. Fältsäsong 2026 · v34–v41 — **tidskritiskt**

Fältsäsongen för gräsmark tar slut i praktiken kring månadsskiftet september/oktober. Detta är den enda delen av årets arbete som har ett hårt fönster.

| ID | Aktivitet | Klart | Ansvar |
|---|---|---|---|
| B1.1 | Välj ut 15–25 objekt ur batch B + de sällsynta typerna i batch C och D | v34 | Handläggare |
| B1.2 | Stäm av urvalet med förvaltarna på Naturvårdsenheten — vilka objekt har de aktuell kunskap om? Besök inte det som redan är känt | v35 | Handläggare |
| B1.3 | Boka fältdagar, klarlägg markägarkontakter | v35 | Kollega |
| B2.1 | Fältkontroll hävdberoende gräsmark, ca 8–10 fältdagar | v36–v40 | Båda |
| B3.1 | Riktade besök på sällsynta typer: 7110 Tovhulta stormosse, 7230 Bråtamossen/Pilgöljan, 9060 Fjellskäfte/Tore Grav, 9180 Lotsängsbacken, 6280 Persö, 4030 Lundäng/Åsa gravfält | v36–v41 | Handläggare |
| B4.1 | Dokumentera per besökt yta: livsmiljötyp, hävdstatus, strukturer/funktioner, typiska arter, påverkan, bedömd tillståndsklass, osäkerhet | löpande | Båda |
| B4.2 | Artobservationer → Artportalen (FAQ f.8) | löpande | Båda |
| B4.3 | Identifierat åtgärdsbehov → SkötselDOS (FAQ f.8) | löpande | Kollega |

> **Viktigt:** dokumentera bedömningen och grunden för den redan i fält, men **mata inte in tillståndet i NNK förrän de nya attributen är driftsatta (v40)**. Använd fältprotokoll som mellanlager.

**Leverans B:** 15–25 fältkontrollerade objekt med dokumenterad bedömningsgrund.

---

### C. Skrivbordsgranskning av utbredning · v35–v46

Detta är volymarbetet. Rutinen körs batch för batch och gäller **utbredning och gränser** — inte tillstånd.

#### C1 Granskningsrutin per objekt

1. Öppna objektet i KartLitS WebbGIS-mallen och i ArcGIS Pro mot NNK
2. Läs bevarandeplanen: vilka livsmiljötyper är utpekade, vilka är prioriterade bevarandevärden, vilka bevarandemål finns
3. Jämför bevarandeplanens typer mot vad NNK faktiskt visar — notera differenser
4. Kontrollera mot aktuella flygbilder och ortofoto: syns uppenbara förändringar sedan 2012?
5. Kontrollera mot TUVA (ängs- och betesmarksinventeringen), VMI, VISS och Artportalen
6. Bedöm per yta: *stämmer utbredningen?* → OK / justera / kontrolleras i fält / osäker
7. Notera i WebbGIS-mallen: vad som granskats, vad som behöver kontrolleras vidare, vad som bör ändras i NNK
8. Justera geometrier i NNK **endast** där redigeringen påverkar arealen meningsfullt (FAQ f.12: minsta karteringsenhet 0,25 ha generellt, 1 ha skog/våtmark, 0,5 ha ädellöv/lövsump/svämskog)

#### C2–C6 Batchar

| Batch | Objekt | Terr. areal | Hävdber. | Sällsynt | Polygoner | Period |
|---|---|---|---|---|---|---|
| **S** Storobjekt | 2 | 1 863 ha | 670 ha | 93 ha | 4 348 | v41–v46 |
| **A** Kust & skärgård | 6 | 1 692 ha | 691 ha | 66 ha | 1 858 | v38–v42 |
| **B** Ängs- & hagmark inland | 16 | 851 ha | 684 ha | 6 ha | 447 | v35–v38 |
| **C** Våtmark & vattendrag | 6 | 378 ha | 9 ha | 128 ha | 401 | v42–v44 |
| **D** Skog & ädellöv | 10 | 393 ha | 57 ha | 92 ha | 264 | v43–v46 |

**Batch S** (Skärgårdsreservaten SE0220129 med 2 915 polygoner och Nynäs SE0220126 med 1 433) rymmer **44 % av länets samtliga N2000-polygoner**. De ska inte köras som vanliga objekt — se avsnitt 5.3.

Ordningen är medvetet vald: batch B först eftersom de objekten är små, hävdberoende och snabba att gå igenom, vilket ger rutinen och tidsuppskattningen kalibrerad innan de tunga batcharna.

#### C7 Okarterade ytor

| Objekt | Okarterat | Åtgärd |
|---|---|---|
| Båven SE0220303 | 4 845 ha av 6 200 | Sjöyta, limniskt. **Lägg ingen tid på ytterkanterna** (FAQ f.16). Ange livsmiljötyp i befintliga ytor om förekomsten är känd. Notera i planen som medvetet nedprioriterat. |
| Tullgarn södra SE0220034 | 299 ha av 2 014 | Kontrollera vad ytan består av — om terrestert är det ett faktiskt karteringsgap som ska anmälas till Metria (FAQ f.26) |

**Leverans C:** Granskningslogg för 40 P1-objekt, dokumenterade differenser mot bevarandeplan, lista över ytor som kräver fältkontroll 2027.

---

### D. Tillståndsbedömning i NNK · v40–v50

| ID | Aktivitet | Klart | Ansvar |
|---|---|---|---|
| D1.1 | Bevaka driftsättning av nya NNK-attribut (planerad slutet av september) | v39–v40 | Handläggare |
| D1.2 | Gå igenom nya attributlistan och den uppdaterade kodlistan; notera att tillstånd nu anges som **procentuell andel av ytan** — ytor behöver inte längre delas | v40 | Båda |
| D1.3 | Genomför/delta i NV:s utbildning för de nya attributen | v40–v41 | Båda |
| D2.1 | Registrera tillstånd för de ytor där kunskapen redan finns: 482 fullgoda + 336 icke fullgoda + de objekt som har aktuella skötselplaner och nyliga uppföljningar | v41–v48 | Båda |
| D2.2 | Dokumentera **grunden** för varje bedömning och **hur aktuell** den är (FAQ f.4) — utan detta är bedömningen inte spårbar | löpande | Båda |
| D2.3 | Där tillståndet är oförändrat sedan tidigare bedömning: registrera det aktivt med grund och datum — "oförändrat" är också ett svar (FAQ f.9) | löpande | Båda |
| D3.1 | Mata in fältdata från arbetspaket B | v41–v45 | Båda |
| D4.1 | Notera avvikelser mot fastställd bevarandeplan/reservatsbeslut (FAQ f.24) | löpande | Handläggare |
| D4.2 | Lista objekt där nuvarande beslut/skötselplan **hindrar** nödvändig skötsel → revideringsbehov | v48 | Handläggare |
| D4.3 | Utvecklingsmark: peka ut ytor där bevarandemål finns om utökad areal, ange upp till tre målnaturtyper (FAQ f.23). Idag har bara 87 polygoner i hela länet en angiven målnaturtyp | v45–v50 | Handläggare |

> **Håll tillbaka där osäkerheten är verklig.** FAQ fråga 22: är ni inte säkra och kan inte prioritera fältinsats — behåll tidigare bedömning eller ange okänt tillstånd, och dokumentera vad ni är osäkra på. Gissa inte.

**Leverans D:** Tillstånd registrerat för de ytor där kunskap finns; resten dokumenterat som okänt med angiven anledning.

---

### E. Sammanställning av kunskapsläget · v45–v50

| ID | Aktivitet | Klart |
|---|---|---|
| E1.1 | Nytt NNK-uttag för D-län, samma struktur som januariuttaget → möjliggör före/efter-jämförelse | v45 |
| E1.2 | Statistik per Natura 2000-område: areal per livsmiljötyp × tillståndsklass | v46 |
| E1.3 | Statistik per livsmiljötyp för hela länet | v46 |
| E2.1 | Kvantifiera per objekt: areal i okänt tillstånd, areal osäker/obestämd naturtyp, areal utvecklingsmark | v47 |
| E2.2 | Redovisning av **vilka livsmiljötyper per objekt** som omfattas av osäkerhet — explicit krav i FAQ f.6 | v47 |
| E2.3 | Kvalitetsbrister på systemnivå: BIDOS-ursprung, ålder på kartering, saknade attribut, gränskvalitet | v47 |
| E3.1 | Fyll i KartLitS WebbGIS-mallen för granskade objekt (FAQ f.9.1) | löpande |

**Leverans E:** Kunskapslägesrapport för D-län per 2026-12-31.

---

### F. Plan för 2027 · v46–v52 — **årets huvudleverans**

FAQ fråga 9 anger exakt vad NV vill ha in. Planen ska besvara fem frågor:

| ID | Fråga att besvara | Innehåll |
|---|---|---|
| F1.1 | **Vilka insatser krävs för att komma till rätta med bristerna, och vem gör det?** | Uppdelning: eget fältarbete / eget skrivbordsarbete / Metria / NV:s arbetsgrupper / konsult |
| F1.2 | Volymuppskattning | Antal objekt, hektar och fältdagar per livsmiljötypsgrupp. Kalibrera mot faktisk tidsåtgång i batch B (därav ordningen i avsnitt C) |
| F2.1 | **Er prioritering — var är det viktigast att samla in ny kunskap och vad behöver ni veta?** | Ordningsföljd med motivering per livsmiljötypsgrupp |
| F2.2 | **Vilka antaganden och generaliseringar skulle kunna göras?** | Konkreta förslag, t.ex.: kan hävdstatus i TUVA användas som proxy för tillstånd i 6270/6510? Kan 8230 hällmarkstorräng antas oförändrad utan fältbesök? Kan 9010 taiga i objekt utan avverkning antas oförändrad? Detta är den fråga som ger störst avlastning om NV accepterar generaliseringarna |
| F3.1 | **Vad gör ni själva och vad behöver ni hjälp med?** | Tydlig gräns, med marina och limniska miljöer explicit lämnade till HaV och de nationella karteringarna |
| F4.1 | Underlag till årsredovisningen 2026 | Antal områden bedömda, antal områden med plan — de två tal regeringsuppdraget faktiskt efterfrågar |

**Leverans F:** Plan för 2027 till Naturvårdsverket + text till årsredovisningen.

---

### G. Parallellspår naturreservat och nationalpark · v42–v52

Naturreservat och nationalpark har deadline 2027, inte 2028. I D-län finns ca 24 914 ha NR/NP utanför N2000-överlapp, varav bara 4 103 ha (8 %) är karterat som Natura-naturtyp — betydligt sämre kunskapsläge än inom N2000.

| ID | Aktivitet | Klart |
|---|---|---|
| G1.1 | Gå igenom flik 3 i NNK-statistiken: vilka NR har stor areal utanför N2000 och prioriterade bevarandevärden i syftet? | v44 |
| G1.2 | Screening: vilka reservat innehåller hävdberoende marker eller sällsynta livsmiljötyper? | v46 |
| G1.3 | Grov volymuppskattning för 2027 | v48 |
| G2.1 | Ta med NR/NP i planen till NV (arbetspaket F) som ett eget avsnitt | v50 |

> Gör inte mer än screening i år. Poängen är att 2027 inte ska börja med en överraskning.

---

### H. Förvaltardialog — Naturvårdsenhetens kunskap · v35–v48

En stor del av det länsstyrelsen faktiskt vet om sina skyddade områden finns hos reservatsförvaltarna på Naturvårdsenheten och har aldrig nått NNK. Analysen av den publika Natura naturtypskartan för länet visar två konkreta luckor: **277 ytor har fältdata men saknar tillståndsbedömning**, och **141 ytor har karteringsstatus 5 "Åtgärdas"** — basinventeringens egen markering för att naturtypen inte gick att bestämma, oförändrad sedan 2008.

> **Notera om källan:** `KOMMENTAR`, `NNK_KOMMEN` och `REDIGERARE` är tomma i samtliga 14 830 polygoner i det publika uttaget, men det beror på att den publika versionen strippar kommentarer och användaruppgifter (handledningen 1.3) — inte nödvändigtvis på att fälten är oanvända. Kontrollera dem mot ett uttag ur NNK Ajourhålla innan slutsatser dras.

Naturvårdsverket godkänner uttryckligen lokalkännedom som kunskapskälla (Handledning för NNK 4.1; lathunden, *Utgångspunkter*; FAQ fråga 9). Detta är alltså inte en genväg utan den metod uppdraget förutsätter.

Fullständig metodik finns i `docs/nnk/metodik_forvaltarkunskap.md`. Insamlingsinstrument: `docs/nnk/blankett_forvaltarkunskap_nnk.xlsx`.

| ID | Aktivitet | Klart | Ansvar |
|---|---|---|---|
| H1.1 | Kartlägg vilken förvaltare som ansvarar för vilka objekt; fyll i kolumn *Förvaltare* i blanketten | v36 | Kollega |
| H1.2 | Förankra upplägget med Naturvårdsenhetens chef — det är deras tid du ber om | v36 | Handläggare |
| H2.1 | Gå igenom de 141 Åtgärdas-ytorna. Kopplade till objekt: **Skärgårdsreservaten 91, Strandstuviken 25, Marvikarna 7, Vilsta 6, Rågö 5, Storhultet 4, Tovhulta stormosse 3** — samtliga inom Natura 2000, nästan uteslutande hävdberoende marker | v37 | Handläggare |
| H2.2 | Checka ut NNK **Ajourhålla** i ArcGIS Pro och kontrollera `KOMMENTAR` för Åtgärdas-ytorna och de 277 fältbesökta — grunden kan redan stå där | v37 | Handläggare |
| H2.3 | Kör `scripts/analysis/koppla_omraden.py` mot NVR-lagret för att få `NVRID` på de 5 221 ytor som ligger utanför Natura 2000 — behövs för arbetspaket G | v43 | Kollega |
| H3.1 | Boka förvaltarsamtal, ca 60 min per förvaltare, flera objekt per möte | v37 | Kollega |
| H3.2 | Genomför samtalen — börja med Åtgärdas-ytorna, gå därefter på hävdberoende marker | v38–v44 | Båda |
| H3.3 | Samordna med fältplaneringen (B1.2): besök inte det förvaltaren redan kan svara på | löpande | Handläggare |
| H4.1 | Eftersök odokumenterade underlag: uppföljningsprotokoll, ÄoB-blanketter, konsultrapporter, skötselplansbilagor, foton | v38–v46 | Kollega |
| H4.2 | Registrera funna underlag i datakälleregistret `data/sources_sodermanland.csv` | löpande | Kollega |
| H5.1 | För in i KartLitS granskningslager samma vecka som samtalet | löpande | Båda |
| H5.2 | Registrera i NNK efter avstämning — tillståndsfälten först efter driftsättning v40 | v41–v48 | Handläggare |
| H5.3 | Skicka avstämning tillbaka till förvaltaren på det du fört in | löpande | Handläggare |

**Prioritetsordning i samtalen:** Åtgärdas-ytorna → hävdberoende marker i batch B och A → sällsynta livsmiljötyper i batch C och D → utvecklingsmark.

**De tre reglerna som måste sitta innan första samtalet** (fullständigt resonemang i metodiken):

- **En igenvuxen äng är fortfarande en äng.** Beror förändringen på utebliven skötsel står livsmiljötypen kvar och tillståndet sätts till icke gott — den klassas inte om. Lathunden är uttrycklig: bristande bevarandeåtgärder *"är inte en giltig anledning att ändra"*.
- **Förändringsorsak 3, inte 2.** Kunskap som funnits men aldrig registrerats är en komplettering. Sätter man kod 2 rapporterar länet in arealförändringar som aldrig inträffat.
- **Fråga alltid efter årtal.** Utan datering går FAQ fråga 4:s krav på hur aktuell bedömningen är inte att besvara.

**Leverans H:** Ifyllda blanketter, registrerad kunskap i granskningslagret, och en dokumenterad lista över underlag som fanns men inte var kända.

> **Varför detta ligger tidigt:** förvaltarnas svar avgör vilka objekt som behöver fältbesök. Kommer H3.2 igång först efter fältsäsongen har man besökt fel platser.

---

## 5. Prioritering

### 5.1 Prioriteringsgrunder (FAQ fråga 11)

1. Livsmiljötyper i behov av **löpande åtgärder** (hävdberoende) — 2 661 ha i länet
2. Förekomster som **inte har gott tillstånd** eller där risk för försämring är hög
3. Förekomster där **åtgärder gjorts eller planeras**
4. Livsmiljötyper med **liten utbredning** i länet eller i Sverige — 27 koder under 50 ha

### 5.2 Prioritetsklasser

| Klass | Objekt | Kriterium | Insats 2026 |
|---|---|---|---|
| **P1** | 40 | ≥ 20 ha hävdberoende **eller** ≥ 5 ha sällsynt livsmiljötyp | Full skrivbordsgranskning + fältkontroll där möjligt |
| **P2** | 43 | ≥ 20 ha terrester livsmiljötyp eller ≥ 5 ha osäker/obestämd | Skrivbordsgranskning om tid finns, annars 2027 |
| **P3** | 108 | Övriga objekt med terrester livsmiljötyp | 2027 |
| **P4** | 6 | Ingen terrester livsmiljötyp (rent limniska/marina) | Ingen insats — dokumentera som medvetet nedprioriterat |

De 40 P1-objekten rymmer **5 178 ha av länets 7 821 ha terrestra livsmiljötyper (66 %)** och **2 111 ha av 2 661 ha hävdberoende mark (79 %)**. Med andra ord: en femtedel av objekten täcker fyra femtedelar av det som betyder något.

### 5.3 Särskild hantering av storobjekten

Skärgårdsreservaten (SE0220129) och Nynäs (SE0220126) innehåller tillsammans 4 348 polygoner. Att gå igenom dem yta för yta är inte realistiskt.

**Föreslagen metod:**

1. Stratifiera på livsmiljötyp och storlek — hantera de stora, betydande ytorna individuellt
2. Behandla små hällmarks- och skogsytor gruppvis med gemensam bedömningsgrund, dokumenterad som just en generalisering
3. Skärgårdsreservaten har redan 198 fältkontrollerade polygoner — den kunskapen ska återanvändas, inte göras om
4. Ta upp objekten som ett explicit exempel i planen till NV: **"så här tänker vi hantera storobjekt, är det acceptabelt?"** FAQ fråga 10 uppmuntrar uttryckligen att skicka in knepiga fall till funktionsbrevlådan

---

## 6. Roller och tidsbudget

### 6.1 Fördelning

| | Handläggare (100 %) | Kollega (50 %) |
|---|---|---|
| Huvudansvar | Metodik, NNK-redigering, bedömningar, planen till NV | Fältstöd, dataunderlag, dokumentation |
| Arbetspaket A | A1, A2, A3, A4 | A2.1, A3.3 |
| Arbetspaket B | B1, B3, B4 | B1.3, B2, B4.3 |
| Arbetspaket C | C1, C2, C3, C7 | C4, C5, C6 |
| Arbetspaket D | D1, D2, D4 | D1, D2.1, D3 |
| Arbetspaket E | E2 | E1, E3 |
| Arbetspaket F | Hela | F1.2 underlag |
| Arbetspaket G | G2 | G1 |
| Arbetspaket H | H1.2, H2, H5 | H1.1, H3.1, H4 |

### 6.2 Grov tidsbudget v34–v52 (ca 19 veckor)

| Arbetspaket | Handläggare | Kollega |
|---|---|---|
| A Etablering | 10 dagar | 4 dagar |
| B Fältsäsong | 15 dagar | 10 dagar |
| C Skrivbordsgranskning | 26 dagar | 16 dagar |
| D Tillståndsbedömning | 13 dagar | 8 dagar |
| E Sammanställning | 8 dagar | 5 dagar |
| F Plan för 2027 | 12 dagar | 2 dagar |
| G Naturreservat | 3 dagar | 4 dagar |
| H Förvaltardialog | 8 dagar | 7 dagar |
| Möten, samverkan, oförutsett | 12 dagar | 5 dagar |
| **Summa** | **107 dagar** | **61 dagar** |

> Tiden till arbetspaket H är tagen från C och D, inte lagd ovanpå. Det är en medveten växling: varje objekt där förvaltaren kan svara direkt är ett objekt du slipper granska från grunden, och de 277 ytorna med befintlig fältkunskap men utan tillståndsbedömning kostar mindre att lösa via ett samtal än via en skrivbordsgranskning.

---

## 7. Tidplan v34–v52 2026

| Vecka | Handläggare | Kollega | Milstolpe |
|---|---|---|---|
| v34 | A1.3, A2.1, B1.1 | A2.1 | |
| v35 | A1.1, A1.2, A2.2, A2.3, A3.1, A3.3, B1.2 | B1.3, **H1.1 förvaltarkartläggning** | |
| v36 | A2.4, A3.2, A3.4, A4, **H1.2**, **B2 fält** | **B2 fält**, H1.1 klar, C4 batch B | **M1: arbetsplats klar** |
| v37 | **B2 fält**, **H2.1 Åtgärdas-ytorna**, H2.2 | C4 batch B, **H3.1 boka samtal** | |
| v38 | **B2 fält**, C3 batch A, **H3.2 samtal** | C4 batch B klar, **H3.2**, H4.1 | **M2: batch B granskad** |
| v39 | B3 fält, C3 batch A, D1.1, H3.2 | C3 batch A, H3.2, H4.1 | |
| v40 | **B3 fält sista**, D1.2, D1.3 | D1.2, D1.3 | **M3: nya NNK-attribut driftsatta** |
| v41 | C2 batch S start, D2.1, H5.2 | C3 batch A klar, D3.1, H4.1 | **M4: fältsäsong avslutad** |
| v42 | C2 batch S, D2.1, H3.2 | C5 batch C, G1.1, H3.2 | |
| v43 | C2 batch S, D2.1, H5.2 | C5 batch C, C6 batch D, H4.1 | |
| v44 | C2 batch S, C7, **H3.2 sista samtalen** | C6 batch D, G1.1 klar, H3.2 | **M8: förvaltardialog genomförd** |
| v45 | C2 batch S, D3.1, H5.2 | E1.1, C6 batch D, H4.1 klar | |
| v46 | C2 batch S klar, F1.1 | E1.2, E1.3, G1.2 | **M5: alla P1-objekt granskade** |
| v47 | E2.1, E2.2, E2.3, F1.2 | E3.1 | |
| v48 | D4.2, F2.1, F2.2, H5.2 klar | G1.3, D2.1 | |
| v49 | F2, F3.1 | E3.1 klar | |
| v50 | F4.1, G2.1, D4.3 | D4.3 | **M6: kunskapslägesrapport klar** |
| v51 | Förankring internt, remiss till NV | | |
| v52 | Slutjustering, inlämning | | **M7: plan för 2027 levererad** |

### Milstolpar

| # | Milstolpe | Vecka | Datum |
|---|---|---|---|
| M1 | Arbetsplats, behörigheter och metodik på plats | v36 | ~2026-09-04 |
| M2 | Batch B granskad — rutinen kalibrerad | v38 | ~2026-09-18 |
| M3 | Nya NNK-attribut driftsatta, utbildning genomförd | v40 | ~2026-10-02 |
| M4 | Fältsäsong 2026 avslutad och dokumenterad | v41 | ~2026-10-09 |
| M8 | Förvaltardialogen genomförd, kunskapen registrerad i granskningslagret | v44 | ~2026-10-30 |
| M5 | Samtliga 40 P1-objekt skrivbordsgranskade | v46 | ~2026-11-13 |
| M6 | Kunskapslägesrapport D-län klar | v50 | ~2026-12-11 |
| M7 | Plan för 2027 levererad till NV + underlag till årsredovisningen | v52 | ~2026-12-23 |

---

## 8. Avgränsningar — vad som medvetet inte görs 2026

Att kunna motivera bortval är lika viktigt som att prioritera. Samtliga punkter har stöd i FAQ:n.

| Avgränsning | Stöd |
|---|---|
| **Marina livsmiljötyper läggs inte in i NNK.** 16 912 ha osäker marin areal lämnas orörd; nationella marina karteringar är underlaget | f.16 |
| **Limniska ytterkanter justeras inte.** Livsmiljötyp anges i befintliga ytor/linjer där förekomsten är känd; strandlinjer och vattendragsgeometri lämnas | f.16 |
| **Båvens okarterade 4 845 ha** åtgärdas inte i år | f.16, f.29 |
| **Grottor, branter, sandstäpp, inlandssandmarker** — nationella karteringsunderlag räcker | f.16 |
| **Obetydliga (icke signifikanta) livsmiljötyper inom N2000** — endast areal redovisas, ingen tillståndsbedömning | f.15 |
| **Standard Data Form / N2000-databasen uppdateras inte.** Uppgifterna hämtas automatiskt från NNK | f.17 |
| **Tillståndsbedömningar med osäkert underlag görs inte.** Behåll tidigare bedömning eller ange okänt, dokumentera osäkerheten | f.22 |
| **Uppdateringar under minsta karteringsenhet görs inte** (0,25 ha generellt, 1 ha skog/våtmark, 0,5 ha ädellöv) | f.12 |
| **Tidigare signifikansbedömningar görs inte om** — endast nytillkomna livsmiljötyper bedöms | f.15 |
| **Naturreservat utanför N2000** får screening, inte genomgång | f.6 (deadline 2027) |

---

## 9. Risker

| Risk | Sannolikhet | Konsekvens | Åtgärd |
|---|---|---|---|
| Nya NNK-attribut försenas förbi september | Medel | Hög — hela D-paketet skjuts | Fyll v40–v43 med C-arbete i stället; dokumentera bedömningar i fältprotokoll och WebbGIS-mallen så inget arbete går förlorat |
| Vägledningar för terrestra livsmiljötyper inte fastställda i tid | Medel | Medel | FAQ f.10 säger uttryckligen att man får avvakta. Dokumentera vilka typer som blockeras och ta med i planen |
| Fältsäsongen tar slut innan urvalet är klart | Hög | Medel | B1.1 är klart redan v34. Prioritera hävdberoende gräsmark före allt annat |
| Storobjekten sväljer hela hösten | Hög | Hög | Stratifierad metod (5.3), tidsatt fönster v41–v46, hård avgränsning |
| Försenad systemåtkomst | Hög | Medel | Börja med det som går utan NNK-skrivrättighet: bevarandeplaner, WebbGIS-mallen, statistikuttaget |
| BIDOS-underlaget visar sig sämre än väntat vid granskning | Medel | Medel | Det är ett resultat i sig — kvantifiera och lyft i planen som insatsbehov, gör inte om karteringen själv (f.26: Metria har inte det uppdraget heller) |
| Kollegans 50 % äts upp av andra uppgifter | Medel | Medel | Lägg kollegans arbete på avgränsade batchar som går att pausa utan att blockera huvudspåret |

---

## 10. Frågor att ta upp med Naturvårdsverket / KartLitS

Skickas till `kartlitsN2000@naturvardsverket.se` (FAQ f.10). Ju tidigare desto bättre — svaren styr hösten.

1. **Storobjekt:** Är stratifierad, gruppvis bedömning av Skärgårdsreservatens 2 915 polygoner en acceptabel metod? Finns det andra län med samma problem?
2. **Generaliseringar:** Kan hävdstatus i TUVA användas som proxy för tillstånd i 6270/6510? Kan 8230 hällmarkstorräng antas oförändrad utan fältbesök?
3. **BIDOS-ursprung:** 96 % av länets polygoner kommer från basinventeringen med vägledningar före 2011. Vilken ambitionsnivå förväntas för systematisk korrigering — och vad ligger inom Metrias uppdrag?
4. **Båven:** 4 845 ha okarterat i ett limniskt objekt. Bekräfta att detta ska lämnas till den nationella limniska karteringen.
5. **Tullgarn södra:** 299 ha okarterat — är det ett karteringsgap som ska felanmälas till Metria?
6. **Tidpunkt:** Bekräfta driftsättningsdatum för de nya tillståndsattributen, och när utbildning ges.
7. **Formatet för planen:** FAQ f.7 säger att formatet återkommer "så snart vi kan". Efterfråga det tidigt så att E-arbetet kan struktureras rätt från början.

---

## 11. Uppföljning

- Veckoavstämning handläggare–kollega, 30 min måndagar
- Månadsavstämning med chef vid milstolparna M1, M3, M5, M6
- Granskningsloggen uppdateras löpande — den är underlaget till både E och F
- Nytt NNK-uttag v45 med samma struktur som januariuttaget ger mätbar progress: andel polygoner med bedömd status ska ha rört sig från 8 %

---

## Bilaga 1 — P1-objekt (40 st), rangordnade

| # | Sitecode | Områdesnamn | Hävdberoende (ha) | Terrester livsmiljötyp (ha) | Sällsynt (ha) | Sällsynta koder | Polygoner | Fältkontrollerade |
|---|---|---|---|---|---|---|---|---|
| 1 | SE0220129 | Skärgårdsreservaten | 501.3 | 1341.5 | 69.3 | 1220,1620,4030,5133,6210,6230 | 2915 | 198 |
| 2 | SE0220126 | Nynäs | 168.7 | 521.8 | 23.9 | 1640,4030,6110,6210,6230,8231 | 1433 | 30 |
| 3 | SE0220439 | Askö | 218.3 | 346.0 | 6.9 | 1220,1640,2181,8231,9006 | 506 | 48 |
| 4 | SE0220020 | Strandstuviken | 155.6 | 268.4 | 15.5 | 1220,1640,8231,8232,9006,9190 | 255 | 40 |
| 5 | SE0220077 | Ridö-Sundbyholmsarkipelagen södra | 84.5 | 408.9 | 14.8 | 9110,9190 | 195 | 12 |
| 6 | SE0220034 | Tullgarn södra | 90.6 | 327.1 | 24.4 | 1620,6110,6210 | 254 | 38 |
| 7 | SE0220110 | Skåraviken | 94.9 | 94.9 | 0.0 | – | 43 | 0 |
| 8 | SE0220017 | Svanviken-Lindbacke | 73.6 | 73.6 | 5.0 | 5130 | 30 | 1 |
| 9 | SE0220231 | Rågö | 72.4 | 174.3 | 4.5 | 8220,8231,9006,9072 | 371 | 15 |
| 10 | SE0220063 | Sparreholms ekhagar | 83.3 | 83.3 | 0.0 | – | 25 | 0 |
| 11 | SE0220176 | Tovhulta stormosse | 0.0 | 47.0 | 47.0 | 7110 | 8 | 0 |
| 12 | SE0220218 | Stendörren | 69.7 | 167.8 | 0.0 | – | 277 | 11 |
| 13 | SE0220304 | Kilaån-Vretaån | 6.2 | 45.9 | 44.9 | 3260,9750 | 214 | 41 |
| 14 | SE0220602 | Vilsta | 12.3 | 248.2 | 7.9 | 9006,9072 | 146 | 8 |
| 15 | SE0220182 | Segersön | 44.0 | 96.7 | 0.0 | – | 65 | 0 |
| 16 | SE0220118 | Labro ängar | 52.4 | 52.4 | 0.0 | – | 22 | 0 |
| 17 | SE0220343 | Askholmen | 20.2 | 54.9 | 18.0 | 9072,9190 | 41 | 14 |
| 18 | SE0220150 | Tåkenön | 38.1 | 85.8 | 0.0 | – | 50 | 2 |
| 19 | SE0220106 | Fjällmossen norra | 0.4 | 230.5 | 7.4 | 9006 | 144 | 109 |
| 20 | SE0220085 | Gripsholms Hjorthage | 36.6 | 36.6 | 0.0 | – | 7 | 0 |
| 21 | SE0220363 | Lindön | 31.4 | 57.4 | 0.0 | – | 27 | 0 |
| 22 | SE0220115 | Marsviken-Marsäng | 42.8 | 42.8 | 0.4 | 6230 | 26 | 2 |
| 23 | SE0220206 | Floden | 31.1 | 31.1 | 0.0 | – | 13 | 0 |
| 24 | SE0220228 | Ånhammarsnäset | 20.4 | 28.8 | 0.5 | 6430 | 30 | 0 |
| 25 | SE0220088 | Herröknanäs | 28.8 | 33.4 | 0.0 | – | 13 | 0 |
| 26 | SE0220603 | Jungfruvassen | 34.4 | 52.0 | 0.0 | – | 12 | 4 |
| 27 | SE0220344 | Lövön | 25.7 | 35.4 | 0.0 | – | 20 | 0 |
| 28 | SE0220309 | Brebol | 24.4 | 24.4 | 0.0 | – | 42 | 0 |
| 29 | SE0220435 | Gesta | 21.8 | 21.8 | 0.0 | – | 22 | 0 |
| 30 | SE0220137 | Bråtamossen | 0.0 | 25.8 | 14.9 | 7230 | 10 | 0 |
| 31 | SE0220503 | Fjellskäfte | 0.0 | 15.0 | 15.0 | 9060 | 10 | 0 |
| 32 | SE0220211 | Ekorneberg | 8.5 | 8.5 | 6.6 | 6230 | 11 | 0 |
| 33 | SE0220217 | Tore Grav | 0.0 | 10.2 | 10.2 | 9060 | 1 | 0 |
| 34 | SE0220234 | Persö | 5.8 | 8.0 | 5.8 | 6280 | 20 | 0 |
| 35 | SE0220130 | Lotsängsbacken | 0.0 | 13.8 | 8.3 | 9180 | 8 | 0 |
| 36 | SE0220103 | Pilgöljan | 0.1 | 8.4 | 7.6 | 7230,7231 | 9 | 0 |
| 37 | SE0220348 | Tynnelsö Djurgård | 8.2 | 21.2 | 8.2 | 9072 | 19 | 1 |
| 38 | SE0220507 | Lundäng | 1.1 | 7.5 | 6.4 | 4030 | 4 | 0 |
| 39 | SE0220438 | Åsa gravfält | 1.0 | 6.2 | 5.2 | 4030 | 4 | 0 |
| 40 | SE0220021 | Sjösakärren | 2.2 | 20.9 | 5.7 | 7230 | 16 | 1 |

## Bilaga 2 — Batchindelning

| Batch | Sitecodes |
|---|---|
| **S** Storobjekt | SE0220129, SE0220126 |
| **A** Kust & skärgård | SE0220439, SE0220020, SE0220034, SE0220231, SE0220218, SE0220077 |
| **B** Ängs- & hagmark inland | SE0220110, SE0220017, SE0220063, SE0220118, SE0220182, SE0220150, SE0220085, SE0220363, SE0220115, SE0220206, SE0220088, SE0220603, SE0220344, SE0220309, SE0220435, SE0220228 |
| **C** Våtmark & vattendrag | SE0220176, SE0220137, SE0220103, SE0220021, SE0220106, SE0220304 |
| **D** Skog & ädellöv | SE0220602, SE0220343, SE0220503, SE0220217, SE0220130, SE0220211, SE0220234, SE0220348, SE0220507, SE0220438 |

---

## Bilaga 3 — Reproducerbarhet och precision

Samtliga siffror i denna plan är beräknade ur `docs/underlag/D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx` flik *2. N2000_NNK* med skriptet `scripts/analysis/nnk_kunskapslage.py`. Kör om skriptet mot ett nytt NNK-uttag för att uppdatera nollmätningen.

**Precision:** summering per objekt avviker med ca 0,2 % från länstotalerna i flik *1. Översikt_län* (44 852 ha mot 44 955 ha karterat inom N2000). Skillnaden beror på Natura 2000-områden som korsar länsgräns samt arealer inom EEZ, vilket beskrivs i flikens *Beskrivning*. Avvikelsen saknar betydelse för prioriteringen men bör anges om siffrorna används i formell redovisning — **använd då länstotalerna i flik 1 som auktoritativ källa**, och objektsiffrorna för prioritering.

Kategoriindelningen (Skog, Gräsmark, Våtmark m.fl.) följer kolumnrubrikerna *Kategori 2026* i statistikuttaget. Klassningen av *hävdberoende* och *sällsynt* är gjord i denna plan, inte i källdata, och kan justeras i skriptet:

- **Hävdberoende:** 1630, 1631, 5130, 5133, 6110, 6210, 6230, 6270, 6280, 6410, 6412, 6430, 6510, 6520, 8230, 8231, 8232, 9070, 9071, 9072
- **Sällsynt:** livsmiljötyp med < 50 ha total karterad areal inom länets Natura 2000-områden, marina koder undantagna

---

*Underlag: NNK-statistik per Natura 2000-område, D-län, uttag 2026-01-20 (Naturvårdsverket) samt NNK-kartering D-län, 14 830 polygoner. Samtliga arealer avser karterad areal inom Natura 2000 (SCI/SAC).*

*Arbetsplan v1.3 · 2026-08-17 — arbetspaket H tillagt; källkritisk rättelse om den publika NNK:s strippade attribut; områdeskoppling genomförd; nedbrytning till 68 uppgifter med 302 steg i runbooken och kontrollrummet*
