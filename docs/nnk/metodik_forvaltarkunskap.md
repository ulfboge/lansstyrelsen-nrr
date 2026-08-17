# Från förvaltarkunskap till NNK

## Metodik för att fånga in och registrera Naturvårdsenhetens kunskap om livsmiljötyper

**Datum:** 2026-08-17
**Gäller:** Natura 2000-områden och statliga naturreservat i Södermanlands län
**Version:** 1.1 — reviderad efter genomgång av den publika NNK-produktbeskrivningen
**Bygger på:** Handledning för NNK (NV, 2026-07-03, NV-26-002862) · Lathund granskning WebbGIS-KartLitS (2026-07-10) · FAQ om uppdraget v1.1 (2026-07-03) · NNK publik produktbeskrivning

---

## 1. Varför detta är rätt spår — och att det är sanktionerat

Naturvårdsverket säger uttryckligen att lokalkännedom är en godkänd kunskapskälla. Det är värt att ha citaten redo när du tar upp det internt:

> "För att säkerställa att rätt livsmiljötyp anges behövs ofta kompletterande information, **såsom lokalkännedom och/eller nyare fältinventeringar**."
> — Handledning för NNK, avsnitt 4.1

> "Utgå ifrån **befintlig kunskap från löpande förvaltning** och titta vid behov på kartunderlag, bevarandeplaner och skötselplaner."
> — Lathund granskning WebbGIS-KartLitS, *Utgångspunkter*

> "I bevarandeplaner, beslut och skötselplaner tillsammans med annan information som samlats in vid skyddsarbete, **förvaltning** eller vid uppföljning."
> — FAQ fråga 9, om vilken befintlig kunskap som ska användas

Och avgörande: karteringsstatus **2 – Granskad vid skrivbordet** definieras som *"Denna yta har granskats av länsstyrelsen baserat på kunskap från t ex andra inventeringar"*. Det finns alltså redan en färdig kod för precis den här sortens kunskap. Du behöver inte uppfinna någon konstruktion — du behöver bara använda den.

---

## 2. Vad NNK-uttaget säger om problemets storlek

Analys av `docs/underlag/kartering.csv` respektive `docs/underlag/naturtypskarta/NNK_YTA` — **samma lager**, 14 830 polygoner, hela länet, alla skyddsformer.

> **Viktigt om källan.** Detta är den **publika** Natura naturtypskartan, inte NNK Ajourhålla. Handledningen (avsnitt 1.3) säger att den publika versionen extraheras ur Ajourhålla och att *"några av attributen som finns i NNK Ajourhålla tas bort, såsom kommentarer och användaruppgifter"*. Tre fält är följaktligen tomma i samtliga 14 830 rader: `KOMMENTAR`, `NNK_KOMMEN` och `REDIGERARE`. **Det går alltså inte att dra slutsatsen att kommentarsfältet är oanvänt i länet** — det är borttaget ur exporten. Beviset ligger i datat: `REDIGERATA` (datum för attributredigering) har värden i 12 612 rader medan `REDIGERARE` (vem som redigerade) är tomt i alla 14 830. Attributen *har* redigerats; användaruppgifterna är strippade.
>
> **Konsekvens:** allt som rör grunder, kommentarer och vem som gjort vad måste kontrolleras mot ett uttag ur **NNK Ajourhålla** via ArcGIS Pro. Den publika versionen duger för utbredning, naturtyp, status och datum — inte för spårbarhet.

Följande går däremot att läsa direkt ur den publika versionen, eftersom dessa fält inte strippas:

| Observation | Antal | Innebörd |
|---|---|---|
| Polygoner med `NATURTYPSS = 5` (ej bedömd status) | 13 266 (89 %) | |
| — varav karteringsstatus **2 Granskad vid skrivbordet** | **9 824** | Ytan har granskats, men tillståndet registrerades aldrig |
| — varav karteringsstatus **3 Besökt i fält** | 122 | |
| — varav karteringsstatus **4 Inventerad i fält** | 155 | |
| — varav karteringsstatus **5 Åtgärdas** | 141 | |
| — varav karteringsstatus 1 Ej granskad | 2 592 | |
| — varav karteringsstatus saknas | 432 | |

**a) 277 ytor har faktisk fältkunskap men saknar tillståndsbedömning.** Någon har varit på plats — och tillståndet finns inte i NNK. Det är den snabbaste vinsten i hela uppdraget och kräver inget nytt fältarbete, bara att någon letar rätt på protokollet. Kontrollera `KOMMENTAR` för just dessa ytor i Ajourhålla först — där kan grunden redan stå.

**b) 141 ytor har karteringsstatus 5 "Åtgärdas".** Här skiljer sig de två källorna åt, och båda betydelserna är relevanta:

- Den **publika produktbeskrivningen** kallar koden *"äldre kod som finns kvar från basinventeringen"* som betydde *"att det behövdes kompletterande uppgifter för att bestämma naturtypen"*.
- **Handledningen 2026** (tabell 7) beskriver den som länsstyrelsens administrativa stöd för ytor man bör återkomma till, och som *ska* kompletteras med en kommentar.

Datat pekar entydigt på den första: 139 av 141 har ursprung BIDOS, samtliga redigerades 2007–2008 (tre stycken 2019), och alla har naturtypsstatus 5. Det här är alltså **basinventeringens egen markering "vi kunde inte bestämma naturtypen här" — en dokumenterad kunskapslucka som stått öppen i nitton år.** Efter koppling till områdesidentitet (avsnitt 8) visar de sig ligga koncentrerat i sju objekt:

| Objekt | Antal ytor | Areal | Dominerande livsmiljötyper |
|---|---|---|---|
| SE0220129 Skärgårdsreservaten | 91 | 48,4 ha | 9070/9071/9072 trädklädd betesmark (33), 1630 strandäng (18), 8230/8231 hällmarkstorräng (14) |
| SE0220020 Strandstuviken | 25 | 35,9 ha | 1630 strandäng (15), 6910 öppen kultiverad gräsmark (5) |
| SE0220174 Marvikarna | 7 | 55,2 ha | 3110 näringsfattiga slättsjöar (2), 4810 obestämd hed/gräsmark (2) |
| SE0220602 Vilsta | 6 | 5,3 ha | 7142 kärr och gungflyn (4), 9070 trädklädd betesmark (2) |
| SE0220231 Rågö | 5 | 1,9 ha | 1630 strandäng (4) |
| SE0220337 Storhultet | 4 | 28,0 ha | 9080 lövsumpskog (3), 9010 taiga (1) |
| SE0220176 Tovhulta stormosse | 3 | 12,6 ha | 7110 högmossar (3) |

Fördelningen är talande: nästan uteslutande hävdberoende marker — precis den kategori FAQ fråga 11 sätter högst. Och den ligger i objekt som redan är prioritet 1 i arbetsplanen. **Det gör listan till den bästa öppningsfrågan i ett förvaltarsamtal.**

**c) FAQ fråga 4 kräver spårbarhet som den publika versionen inte kan visa.** Ni ska ange *vad som ligger till grund för bedömningen av utbredning*, *vad som ligger till grund för bedömningen av tillstånd*, och *hur aktuella dessa två bedömningar är*. Kontrollera först vad som faktiskt står i `KOMMENTAR` i Ajourhålla — det avgör om detta är en lucka eller bara osynlig i exporten. Oavsett svar gäller regeln framåt: ingen ytredigering bör lämna kommentarsfältet tomt.

---

## 3. Flödet — två steg, inte ett

Förvaltarkunskap är i regel andrahandsinformation som du inte själv har verifierat. Den ska inte gå rakt in i den nationella databasen. Använd det tvåstegsflöde KartLitS är byggt för:

```
   FÖRVALTARE                DU                        NNK Ajourhålla
   (Naturvårdsenheten)       (Naturskyddsenheten)      (nationell databas)

   ┌─────────────┐    1     ┌──────────────────┐  3   ┌──────────────────┐
   │ Blankett /  │ ───────► │ WebbGIS-KartLitS │ ───► │ ArcGIS Pro       │
   │ samtal      │          │ granskningslager │      │ ut-/incheckning  │
   │             │          │  = FÖRSLAG       │      │  = SKARPT        │
   └─────────────┘          └──────────────────┘      └──────────────────┘
                                     │  2                      ▲
                                     ▼                         │
                             Avstämning: räcker            Endast det du
                             underlaget? Ska något         står bakom
                             fältkontrolleras först?
```

**Varför två steg:**

- Granskningslagret är designat som ett *förslagslager* — dess rullistor heter "Livsmiljötyp, **behov av justering**" och "Tillstånd, **behov av justering**". Det är rätt hemvist för "förvaltaren tror att…".
- Lagret har fält som NNK saknar och som är byggda för just spårbarhet: `faltinventerare`, `egen_bet`, `kommentar_kontroll`, `Kommentar_metod`, `kommentar_livsmil_utbred`, samt `kontroll1–3` och `metod` för vad som återstår att kontrollera.
- Enligt FAQ fråga 9.1 är det granskningslagret som blir underlaget till planen för 2027. Kunskap som stannar där är alltså inte bortkastad — den är levererad.
- Om förvaltarens uppgift senare visar sig fel har du inte kontaminerat den nationella databasen.

**När hoppa direkt till steg 3?** När uppgiften är dokumenterad och du kan hänvisa till källan — ett uppföljningsprotokoll, en ängs- och betesmarksinventering, en skötselplan med daterad statusbeskrivning. Då är det inte hearsay utan ett kunskapsunderlag, och karteringsstatus 2 gäller direkt.

---

## 4. Fältmappning — vilken uppgift hamnar var

Kolumnnamnen i blanketten (`blankett_forvaltarkunskap_nnk.xlsx`) är valda så att de mappar rakt av.

| Vad förvaltaren berättar | Blankettkolumn | Granskningslager (WebbGIS) | NNK Ajourhålla |
|---|---|---|---|
| "Det är rätt livsmiljötyp" | Stämmer livsmiljötyp | `justering` = *Inget behov av justering* | `NATURTYP` oförändrad |
| "Det är egentligen 9070, inte 9010" | Föreslagen livsmiljötyp 1–3 | `justering` = *Ändring till annan livsmiljötyp*, `livsmiljötyp1–3` | `NATURTYP` |
| "Det är inte livsmiljötyp än, men kan bli" | Föreslagen livsmiljötyp 1–3 + Utvecklingsmark = Ja | `justering` = *Ändring till utvecklingsmark*, `livsmiljötyp1–3` blir målnaturtyper | `NATURTYPSS` = 3, `MALNATUR1–3` |
| "Den är i bra skick" | Tillstånd = Gott | `tillstand`, `procent_gott` | `NATURTYPSS` = 1 |
| "Den är igenvuxen / behöver restaureras" | Tillstånd = Icke gott | `tillstand`, `procent_ej_gott` | `NATURTYPSS` = 2 |
| "Halva ytan är fin, halva har vuxit igen" | Andel gott / ej gott / osäker (%) | `procent_gott`, `procent_ej_gott`, `procent_osaker` | Nya tillståndsfält, **driftsätts sept 2026** |
| "Jag vet inte" | Tillstånd = Okänt | `tillstand` = *Okänt (kan ej bedöma)* | `NATURTYPSS` = 5 |
| "Gränsen stämmer inte" | Utbredning, behov av justering | `utbredning` | Geometri — **endast om ≥ minsta karteringsenhet** |
| **På vilken grund** hen vet det | Grund för bedömning | `Kommentar_metod` + `metod` | `KOMMENTAR` |
| **När** hen senast var där | År för senaste bedömning | `habitat_period_lastdata_end` | Slutdatum senaste inventering |
| **Vem** som bedömt | Bedömare | `faltinventerare` | `KOMMENTAR` (namn + roll) |
| "Det borde någon titta närmare på" | Vad ska kontrolleras | `kontroll1–3`, `kommentar_kontroll` | `KARTERINGS` = 5 + `KOMMENTAR` |
| Fri kommentar | Kommentar | `kommentar_tillstand` / `kommentar_livsmil_utbred` | `KOMMENTAR` |

**Kodvärden för `Vad ska kontrolleras`** (från lathunden, tre likadana rullistor så flera val går att göra): Typiska och karakteristiska arter · Strukturer · Hävd · Funktioner (hydrologi, störningar) · Morfologi (jordart, formationer) · Annan negativ påverkan

**Kodvärden för `Metod för kontroll`**: Fältbesök · Fältinventering (standardiserad metodik) · Skrivbord / Granska mot andra underlag · Annan metod
*Obs: detta fält är framåtsyftande — det anger vilken metod som **bör** användas, inte hur du hittills gjort.*

---

## 5. Sex beslutsregler — där det går fel

### R1. Igenväxning på grund av utebliven skötsel ändrar inte livsmiljötypen

Detta är den vanligaste och allvarligaste fällan i förvaltarsamtal, eftersom en förvaltare naturligt säger "den ängen är ingen äng längre".

> "Behåll dock livsmiljötypen om en faktisk förändring beror på brist på 'nödvändiga bevarandeåtgärder' – det är inte en giltig anledning att ändra, snarare har länen skyldighet att vidta nödvändiga bevarandeåtgärder. Ytan är då förmodligen i 'Icke gott tillstånd' (restaureringsmark enligt basinventeringsmanualer)."
> — Lathunden, *Vad kan vi ändra på?*

**Rätt hantering:** livsmiljötypen står kvar, `NATURTYPSS` sätts till **2 – Icke fullgod**. FAQ fråga 22 säger samma sak: om prioriterade bevarandevärden håller på att förloras ska de återställas snarare än klassas om, särskilt när orsaken är brist på skötsel, praktiska överväganden eller omfattande störningar.

Konsekvensen om man gör fel: länets areal av hävdberoende livsmiljötyper krymper på papperet, restaureringsbehovet försvinner ur statistiken, och NRF-uppföljningen visar en förbättring som inte finns.

### R2. Förändringsorsak — nästan aldrig kod 2

Handledningen 5.4: attributet finns *"för att kunna identifiera och sammanställa verkliga arealförändringar för livsmiljötyper från kvalitetsförbättrande åtgärder i databasen"*.

| Situation | `FORANDRING` |
|---|---|
| Kunskapen fanns hos förvaltaren men var aldrig registrerad | **3 – Komplettering** |
| Karteringen var fel från början (flygbildstolkningen missade) | **1 – Rättning av felaktig kartering** |
| Naturen har faktiskt förändrats sedan karteringen | **2 – Faktisk förändring av bevarandestatus/naturtypsareal** |

Nästan all förvaltarkunskap är **kod 3**. Slarvar du och sätter kod 2 rapporterar länet in arealförändringar som aldrig hänt.

### R3. Karteringsstatus speglar underlaget, inte din ansträngning

| Underlag | `KARTERINGS` |
|---|---|
| Förvaltarens minnesbild, skötselplan, bevarandeplan, äldre inventering | **2 – Granskad vid skrivbordet** |
| Förvaltaren har faktiskt varit på ytan nyligen och kan bedöma naturtypen | **3 – Besökt i fält** |
| Standardiserad inventering: uppföljning, ängs- och betesmarksinventering, basinventeringsmetodik | **4 – Inventerad i fält** |
| Du vet att något är fel men inte vad | **5 – Åtgärdas** + obligatorisk kommentar |

Handledningen är tydlig med att kod 2 förutsätter att *"underlaget som använts bedöms vara så aktuellt att uppgifterna fortfarande är giltiga"*. En förvaltares minnesbild från 2015 av en hävdberoende mark är sannolikt inte aktuell — då är svaret okänt tillstånd plus kod 5, inte en gissning.

### R4. Osäkerhet dokumenteras, den gissas inte bort

> "Är ni inte säkra, och det inte går att prioritera fältinsatser för att inhämta tillräcklig kunskap om förhållandena idag är det bättre att behålla tidigare bedömning eller till exempel ange att tillståndet är okänt eller inte gott. Dokumentera vad ni är osäkra på, så det kan kontrolleras eller följas upp när det kan prioriteras."
> — FAQ fråga 22

Ett dokumenterat "okänt" med angiven anledning är en fullgod leverans 2026. En gissning är det inte.

### R5. Utvecklingsmark har två formella krav

Lathunden: *"Används målnaturtyper så förutsätts att Naturtypsstatus är satt till 'Utvecklingsmark' och att **Naturtyp utgörs av en icke-natura-naturtyp**."*

Alltså: en yta kan inte samtidigt vara livsmiljötyp 6270 och utvecklingsmark mot 6270. Är den redan livsmiljötyp är den livsmiljötyp — i gott eller icke gott tillstånd. Upp till tre målnaturtyper får anges (`MALNATUR1–3`).

I hela länet har idag bara 87 polygoner en angiven målnaturtyp. Förvaltarna vet i regel mycket väl vilka ytor som är på väg åt rätt håll — det är en av de mest värdefulla sakerna att fråga om, och FAQ fråga 23 påpekar att ytor med påtaglig utvecklingspotential normalt är högre prioriterade för skydds- och skötselresurser.

### R6. Utpekade livsmiljötyper har ett särskilt skydd

> "Vi har ett särskilt ansvar för livsmiljötyper som legat till grund för utpekandet av ett Natura 2000-område och som tidigare har rapporterats för området. Det samma gäller prioriterade bevarandevärden som är en del av syfte och skäl för ett beslut om naturreservat. Livsmiljötyper som utgör prioriterade bevarandevärden bör karteras mer noggrant och **enbart ändras om tidigare bedömningar är uppenbart fel eller det faktisk skett en förändring**."
> — FAQ fråga 19

Kontrollera därför alltid bevarandeplanen innan du ändrar en utpekad typ. Länken finns i WebbGIS-lagret *NV Natura2000 områden*, raden `BEVPLAN` i attributtabellen.

---

## 6. Datering — det som glöms bort

Två nya fält i NNK, *Startdatum/Slutdatum senaste inventering av naturtypen*, motsvarar `habitat_period_lastdata_start` / `_end` i granskningslagret:

> "Slut representerar senast det gjordes en bedömning och start gången före det. Har det skett en faktisk förändring ska datumen representera den tidsperiod inom vilken förändringen skedde. Eftersom det är nya fält är dessa tomma idag, **uppdatera framför allt slutdatum när ni granskar**."
> — Handledningen, bilaga 1

Det här är den enda mekanism som gör FAQ fråga 4:s krav på *"hur aktuella dessa två bedömningar är"* besvarbart. Fråga alltid förvaltaren om årtal, även när svaret blir "någon gång runt 2018". Ett osäkert årtal är oändligt mycket bättre än inget.

---

## 7. Så lägger du upp samtalet

**Före (30 min per objekt):**

1. Ta fram objektet i WebbGIS-KartLitS, tänd `LstAB NNK granskning` och `NV Naturtypskartan NNK`
2. Läs bevarandeplanen — vilka livsmiljötyper är utpekade och vilka bevarandemål finns
3. Filtrera blanketten till objektets rader
4. Markera raderna med karteringsstatus 3, 4 eller 5 — de har en historia

**Under (45–60 min per förvaltare, flera objekt):**

1. Börja med **Åtgärdas-ytorna** — "basinventeringen kunde inte bestämma naturtypen här, vet du vad det är?" Det är den bästa öppningsfrågan som finns: den är konkret, den erkänner att kunskapen finns hos dem, och den gäller en lucka som stått öppen sedan 2008.
2. Gå igenom hävdberoende marker objekt för objekt: hävdas den, av vem, hur länge till, vad är trenden
3. Fråga efter **dokument du inte känner till**: uppföljningsprotokoll, ÄoB-blanketter, konsultrapporter, gamla skötselplansbilagor, foton. Handledningen kallar det kompletterande information — det är guld och ligger ofta på en enhets-mapp ingen letat i.
4. Fråga specifikt om **utvecklingsmark**: vilka ytor är på väg att bli livsmiljötyp, vilka har ni restaurerat
5. Fråga om **gränser** bara där det rör större arealer — under minsta karteringsenhet är det inte värt tiden
6. Avsluta med: vad borde vi kontrollera i fält, och vilka objekt kan vi lämna som de är

**Efter (30 min per objekt):**

1. För in i granskningslagret samma vecka — minnesbilder av andras minnesbilder blir snabbt oanvändbara
2. Sätt `faltinventerare` = förvaltarens namn, inte ditt
3. Sätt `habitat_period_lastdata_end` = året förvaltaren angav
4. Skriv `Kommentar_metod` i klartext: *"Uppgift från NN, förvaltare, samtal 2026-09-xx. Bygger på hens fältbesök hösten 2024 samt skötselplan 2019."*
5. Skicka tillbaka en avstämning på det du fört in — förvaltaren ska känna igen sin egen uppgift

---

## 8. Områdesidentitet — löst, men bara för den publika versionen

Varken `docs/underlag/kartering.csv` eller `docs/underlag/naturtypskarta/NNK_YTA` innehåller något områdes-ID. Det är inget fel i din export — den publika NNK har helt enkelt inte fältet. Kopplingen görs i stället geometriskt.

**Detta är gjort:** `scripts/analysis/koppla_omraden.py` hämtar det rikstäckande SCI-lagret från Naturvårdsregistret, filtrerar till Södermanland (197 områden) och kopplar varje NNK-yta till det Natura 2000-område den har störst arealöverlapp med.

| Resultat | |
|---|---|
| Ytor kopplade till Natura 2000 | 9 609 |
| Ytor utanför Natura 2000 | 5 221 (21 724 ha) — ligger i naturreservat och nationalpark utan N2000-överlapp |
| Områden med träff | 197 av 197 |
| Ytor som skär flera områden | 3 — tilldelade det med störst överlapp |
| Ytor delvis utanför beslutsgränsen | 82 — `andel_inom < 0,95`; karteringen går ibland utanför gränsen, vilket produktbeskrivningen avsnitt 2.2 varnar för |

**Validering:** summan av den klippta arealen inom Natura 2000 blir 44 798 ha, mot 44 852 ha i Naturvårdsverkets statistikuttag per 2026-01-20. Avvikelsen är 0,1 % och beror på att gränserna hämtats vid olika tillfällen. Kopplingen håller.

Utdata: `data/nnk/nnk_yta_med_sitecode.gpkg` och `.csv` med fälten `SITECODE`, `OMRADE`, `BEVPLAN` (direktlänk till bevarandeplanen), `area_ha`, `overlapp_ha`, `andel_inom` och `antal_omraden`.

**Det som återstår:**

| Behov | Hur |
|---|---|
| `NVRID` för de 5 221 ytorna utanför N2000 | Samma metod mot NVR-lagret från Naturvårdsregistret — behövs inför naturreservatsspåret 2027 (arbetspaket G) |
| `KOMMENTAR`, `NNK_KOMMEN`, `REDIGERARE` | Finns bara i **NNK Ajourhålla**. Checka ut i ArcGIS Pro och exportera — den publika versionen kan aldrig ge detta |
| `habitat_period_lastdata_start` / `_end` | Nya dateringsfälten, finns i Ajourhålla |
| `habitat_priority_all`, `habitat_priority_6210_7130` | Prioriterad livsmiljötyp enligt habitatdirektivet, finns i Ajourhålla |

Med ett Ajourhålla-uttag kan samma skript köras om och då ger det full spårbarhet på polygonnivå.

---

## 9. Innan incheckning i NNK

Från handledningen avsnitt 3.3 och checklistan i 2.3:

- [ ] Kör toolboxen i ArcGIS Pro på det utcheckade området — reglerna kontrolleras där
- [ ] Alla obligatoriska attribut ifyllda med godkända värden (undantag: fritextfälten)
- [ ] Inga överlapp mellan ytor; inga glapp; linjer och ytor korsar inte sig själva
- [ ] Topologifel: prioritera överlapp, åtgärda hål > 0,25 ha och remsor > 10 m, strunta i mindre
- [ ] `FORANDRING` satt på allt du ändrat — se R2
- [ ] `KARTERINGS` uppdaterad — se R3
- [ ] Slutdatum för senaste bedömning ifyllt — se avsnitt 6
- [ ] `KOMMENTAR` ifylld med grund och källa — inte tom, aldrig mer tom
- [ ] Systematiska fel i grundkarteringen rapporterade till `NNK-kartering@metria.se`

> **Tidsordning:** avvakta med att registrera *tillstånd* i NNK tills de nya attributen driftsatts (slutet av september 2026, FAQ fråga 30). Fram till dess samlar du in via blankett och granskningslager. Utbredning, livsmiljötyp, karteringsstatus, förändringsorsak och kommentarer kan du registrera direkt.

---

## 10. Vad detta ger till årets leverans

FAQ fråga 9 vill ha svar på fem frågor, och förvaltardialogen bidrar direkt till fyra av dem:

| FAQ-fråga | Vad dialogen ger |
|---|---|
| Vilka insatser krävs och vem gör det | Förvaltarna kan säga vad de själva kan bidra med inom ordinarie förvaltning |
| Er prioritering — var är det viktigast att samla in ny kunskap | De vet vilka marker som är på väg åt fel håll |
| Vilka antaganden och generaliseringar kan göras | *"Alla betesmarker med aktivt jordbruksstöd och pågående hävd antas vara i gott tillstånd"* är den sortens generalisering som bara kan formuleras med förvaltarnas underlag — och som avlastar mest om NV accepterar den |
| Vad gör ni själva, vad behöver ni hjälp med | Skiljelinjen blir konkret när man vet vad som redan är känt |

---

*Metodik v1.1 · 2026-08-17 · hör ihop med `docs/nnk/arbetsplan_nnk_2026.md` (arbetspaket H) `docs/nnk/blankett_forvaltarkunskap_nnk.xlsx` och `scripts/analysis/koppla_omraden.py`*
