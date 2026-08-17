# -*- coding: utf-8 -*-
"""Uppgiftsregister for NNK/NRF 2026 - Lansstyrelsen Sodermanland.

Varje uppgift har id, arbetspaket, veckor, ansvar, leverans, beroenden och
konkreta steg. Registret ar kallan till bade kontrollrummet (HTML) och
runbooken (markdown).
"""

PAKET = {
    "A": ("Etablering och förutsättningar", "v34–v36"),
    "B": ("Fältsäsong 2026", "v34–v41"),
    "C": ("Skrivbordsgranskning av utbredning", "v35–v46"),
    "D": ("Tillståndsbedömning i NNK", "v40–v50"),
    "E": ("Sammanställning av kunskapsläget", "v45–v50"),
    "F": ("Plan för 2027", "v46–v52"),
    "G": ("Naturreservat och nationalpark", "v42–v52"),
    "H": ("Förvaltardialog", "v35–v48"),
}

MILSTOLPAR = [
    ("M1", 36, "Arbetsplats, behörigheter och metodik på plats", "2026-09-04"),
    ("M2", 38, "Batch B granskad — rutinen kalibrerad", "2026-09-18"),
    ("M3", 40, "Nya NNK-attribut driftsatta, utbildning genomförd", "2026-10-02"),
    ("M4", 41, "Fältsäsong 2026 avslutad och dokumenterad", "2026-10-09"),
    ("M8", 44, "Förvaltardialogen genomförd, kunskapen registrerad", "2026-10-30"),
    ("M5", 46, "Samtliga 40 P1-objekt skrivbordsgranskade", "2026-11-13"),
    ("M6", 50, "Kunskapslägesrapport D-län klar", "2026-12-11"),
    ("M7", 52, "Plan för 2027 levererad till NV", "2026-12-23"),
]

LEVERANSER = [
    ("L-A", "Fungerande arbetsplats och dokumenterad rollfördelning", "A", 36, "Internt"),
    ("L-H1", "Förvaltarkarta: vem förvaltar vilka objekt", "H", 36, "Internt"),
    ("L-B", "15–25 fältkontrollerade objekt med dokumenterad bedömningsgrund", "B", 41, "Underlag till D och F"),
    ("L-H2", "Ifyllda blanketter från förvaltarsamtalen", "H", 44, "Underlag till C, D och F"),
    ("L-C", "Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027", "C", 46, "KartLitS WebbGIS"),
    ("L-D", "Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt", "D", 48, "NNK Ajourhålla"),
    ("L-G", "Screening av naturreservat med volymuppskattning för 2027", "G", 48, "Underlag till F"),
    ("L-E", "Kunskapslägesrapport D-län per 2026-12-31", "E", 50, "Naturvårdsverket, internt"),
    ("L-F1", "Plan för 2027 enligt FAQ fråga 9", "F", 52, "Naturvårdsverket"),
    ("L-F2", "Underlag till årsredovisningen 2026", "F", 52, "Länsledningen"),
]

# ---------------------------------------------------------------------------
# u = (id, rubrik, paket, v_start, v_slut, ansvar, leverans, beroenden, steg[])
# ansvar: H = handlaggare, K = kollega, HK = bada
# ---------------------------------------------------------------------------

U = [

# ============================== A ==============================
("A1.1", "Beställ och verifiera systembehörigheter", "A", 34, 35, "H", "", [], [
 "Skicka en samlad beställning till IT/behörighetsansvarig. Lista exakt: ArcGIS Pro med NNK-tillägget, NNK Ajourhålla (läs OCH skriv — läsrättighet räcker inte), ArcGIS Enterprise-portalen, KartLitS WebbGIS, SkötselDOS, Artportalen (rapportörskonto), samverkansytan för Livsmiljötyper.",
 "Ange i beställningen att det gäller regeringsuppdraget NRF, ref. 2451-2026 — det brukar korta handläggningstiden.",
 "Notera datum för varje beställning i granskningsloggen. Behörighet är den enskilt vanligaste förseningsorsaken i planen.",
 "Medan du väntar: allt i arbetspaket A2 och H2.1 går att göra utan behörigheter, liksom att läsa bevarandeplaner.",
]),
("A1.2", "Verifiera att NNK-utcheckning fungerar mot ett testobjekt", "A", 35, 35, "H", "", ["A1.1"], [
 "Öppna ArcGIS Pro. Skapa ett nytt projekt: `NNK_D_2026`. Sätt kartans koordinatsystem till SWEREF 99 TM (EPSG:3006) — Map Properties → Coordinate Systems → sök 3006.",
 "Anslut till NNK Ajourhålla enligt manualen på VIC Natur (vicnatur.naturvardsverket.se/nnk). Insert → Connections → Database, eller den anslutningsfil IT tillhandahåller.",
 "Välj ett litet testobjekt — förslag: SE0220012 Nävsjöskogen, 5,0 ha, 1 polygon. Minimal risk om något går fel.",
 "Checka ut området. Kontrollera att du får ut geometri OCH attribut, och att fälten KOMMENTAR, NNK_KOMMEN och REDIGERARE finns (de saknas i den publika versionen).",
 "Gör INGEN ändring. Checka in igen direkt och verifiera att det går utan fel.",
 "Notera i granskningsloggen: fungerar utcheckning ja/nej, vilken version av tillägget, eventuella felmeddelanden.",
]),
("A1.3", "Åtkomst till samverkansytan för Livsmiljötyper", "A", 34, 34, "H", "", [], [
 "Begär åtkomst till Naturvårdsverkets samverkansyta för Livsmiljötyper.",
 "Ladda hem allt under Dokument: manualer från basinventeringen och uppföljningen, handledningen för länsstyrelsernas granskning inklusive checklista, kodlistan.",
 "Bokmärk menyn längst till vänster — där ligger länken till NNK-manualerna på VIC Natur.",
 "Spara ned i `docs/underlag/` och notera nedladdningsdatum. Dokumenten uppdateras löpande under projektet.",
]),
("A2.1", "Läs handledningen och lathunden", "A", 34, 34, "HK", "", [], [
 "Läs `docs/underlag/handledning/Handledning NNK 20260703.pdf`, 26 sidor. Prioritera avsnitt 2.3 (checklistan), 3.2 (minsta karteringsenhet), 5 (attributen) och bilaga 1 (fältlistan).",
 "Läs `docs/underlag/handledning/Lathud_granskning_WebbGIS_KartLitS_20260714.pdf`, 9 sidor. Avsnittet *Vad kan vi ändra på?* är det viktigaste i hela uppdraget.",
 "Läs `docs/nnk/metodik_forvaltarkunskap.md` avsnitt 5 — de sex beslutsreglerna.",
 "Skriv ut checklistan på sidan 9 i handledningen och ha den framme vid varje granskning.",
]),
("A2.2", "Gå igenom kodlistan", "A", 35, 35, "H", "", ["A1.3"], [
 "Öppna `docs/underlag/handledning/Kodlista_NNK_20260703.xlsx`.",
 "Filtrera kolumnen *Kategori 2026* på Gräsmark, Skog och Våtmark — det är de kategorier D-läns arbete gäller. Marina och limniska koder kan du hoppa över i år.",
 "Notera undertyperna för de koder som dominerar i länet: 9010 taiga, 9070/9071/9072 trädklädd betesmark, 8230/8231/8232 hällmarkstorräng, 6270 silikatgräsmark, 1630/1631 strandäng.",
 "Lär dig skillnaden mellan de tre flaggkategorierna: *Naturanaturtyp* (livsmiljötyp), *Obestämd naturanaturtyp* (vet att det är livsmiljötyp, inte vilken) och *Osäker natura/icke-natura* (vet inte om det är livsmiljötyp alls). De kräver helt olika åtgärder.",
 "Skapa ett eget urval i `docs/nnk/` med de ca 40 koder som faktiskt förekommer i D-län — det räcker gott.",
]),
("A2.3", "Installera KartLitS GIS-mall och testa den", "A", 35, 35, "H", "", ["A1.2"], [
 "Packa upp `docs/underlag/handledning/KartLits_NNK_GIS_mall_v_2.zip` till en lokal projektmapp.",
 "Mallen innehåller `KartLits_NNK_granskning.gdb` med tre tomma lager i SWEREF 99 TM: NNK_naturaobjekt_yta, _lin och _pkt. Plus tre .lyrx-filer med färdig symbologi.",
 "Lägg till lagren i ArcGIS Pro-projektet och applicera .lyrx-filerna: högerklick på lagret → Symbology → Import from Layer File.",
 "Granska attributtabellen för NNK_naturaobjekt_yta. Fälten du kommer använda: `tillstand`, `procent_gott`, `procent_ej_gott`, `procent_osaker`, `justering`, `utbredning`, `livsmiljötyp1–3`, `malnaturtyp1–3`, `kontroll1–3`, `metod`, `granskat`, `faltinventerare`, `egen_bet`, `habitat_period_lastdata_start`/`_end` samt fyra kommentarsfält.",
 "Testa att lägga till en dummy-post och fylla i fälten, så att du känner igen dem i WebbGIS-gränssnittet. Radera den sedan.",
]),
("A2.4", "Hämta fastställda vägledningar — kontrollera status", "A", 36, 36, "H", "", [], [
 "Gå till Naturvårdsverkets sida *Natura 2000 i Sverige* → vägledningar för naturtyper.",
 "Ladda hem vägledningarna för de livsmiljötyper som finns i D-län. Prioritera 9010, 9070, 8230, 6270, 6410, 1630, 7110, 7140, 7230, 9080, 9190.",
 "Kontrollera för varje: är den FASTSTÄLLD eller på REMISS? FAQ fråga 10 säger att en remissversion inte ska användas som grund för bedömning.",
 "Notera i granskningsloggen vilka typer som saknar fastställd vägledning. De blockeras och ska med i planen för 2027 (uppgift F1.1) som ett eget stycke.",
 "Kom ihåg: nu gällande vägledningar är från 2026 för akvatiska livsmiljötyper samt taiga (9010) och örtrik skog med gran (9050), men från 2011–2012 för övriga terrestra typer.",
]),
("A3.1", "Avstämning med chef", "A", 35, 35, "H", "", [], [
 "Boka 60 min med Stefan Henriksson.",
 "Ta med: `docs/nnk/nnk_kunskapslage_dashboard.html` (öppna i webbläsare — nyckeltalen finns överst) och arbetsplanens avsnitt 0.",
 "Punkter att få beslut om: (1) att 2026 är ett kartläggningsår, inte ett produktionsår; (2) att marina miljöer medvetet lämnas; (3) tidsbudget 107 dagar handläggare + 61 dagar kollega; (4) att kollegans 50 % faktiskt är skyddad tid.",
 "Fråga specifikt vad som förväntas i årsredovisningen för 2026 och när texten ska vara inne.",
 "Dokumentera besluten i granskningsloggen — särskilt bortvalen. De är det du kommer behöva försvara.",
]),
("A3.2", "Kartlägg förvaltaransvaret på Naturvårdsenheten", "A", 36, 36, "H", "", [], [
 "Be Naturvårdsenheten om deras förvaltningsindelning — vem ansvarar för vilka objekt.",
 "Om ingen sammanställd lista finns: utgå från `docs/nnk/blankett_forvaltarkunskap_nnk.xlsx`, fliken Blankett, kolumn B–C, och be dem fylla i kolumn I *Förvaltare*.",
 "Prioritera att få de sju objekten med Åtgärdas-ytor täckta: SE0220129 Skärgårdsreservaten, SE0220020 Strandstuviken, SE0220174 Marvikarna, SE0220602 Vilsta, SE0220231 Rågö, SE0220337 Storhultet, SE0220176 Tovhulta stormosse.",
 "Detta är samma sak som H1.1 — gör dem i ett svep.",
]),
("A3.3", "Rollfördelning med kollegan", "A", 35, 35, "HK", "", [], [
 "Gå igenom arbetsplanens avsnitt 6.1 tillsammans.",
 "Kollegan tar: batch B, C och D i skrivbordsgranskningen, dataunderlag och uttag, förvaltarbokningar, eftersök av dokument, screening av naturreservat.",
 "Du tar: metodik, all NNK-redigering, bedömningarna, storobjekten, planen till NV.",
 "Sätt en fast veckoavstämning, 30 min måndagar. Bestäm var granskningsloggen ligger så båda skriver i samma.",
 "Viktigt: lägg kollegans arbete på avgränsade batchar som går att pausa — 50 % tid blir i praktiken ofta mindre.",
]),
("A3.4", "Anmäl er till KartLitS arbetsgrupper", "A", 36, 36, "H", "", ["A1.3"], [
 "Maila `kartlitsN2000@naturvardsverket.se`. Anmäl er till arbetsgrupperna för skog, gräsmark och våtmark.",
 "Passa på att i samma mail ställa frågorna i arbetsplanens avsnitt 10 — särskilt om storobjekten och om generaliseringar. Svaren styr hela hösten, så ju tidigare desto bättre.",
 "Notera att arbetsgrupperna för akvatiska miljöer och fjäll startar hösten 2026 — de är inte relevanta för D-län i år.",
 "Spara svaren i `docs/nnk/` — de är underlag till planen för 2027.",
]),
("A4.1", "Skapa arbetsstruktur för dokumentation", "A", 36, 36, "H", "", [], [
 "Mapparna `docs/faltprotokoll/` och `data/uttag/` finns redan. Skapa `docs/nnk/granskningslogg.md` — en rad per objekt: sitecode, namn, datum, vem, vad som granskats, vad som ändrats, vad som återstår, osäkerheter.",
 "Fältdokumentation: en fil per fältdag i `docs/faltprotokoll/`.",
 "NNK-uttag: spara i `data/uttag/` med datum i filnamnet så före/efter-jämförelser går att göra.",
 "Committa i Git efter varje arbetsdag. Loggen är underlaget till både arbetspaket E och F — den får inte gå förlorad.",
 "Kontrollera att `data/uttag/*.gpkg` och `data/nnk/*.gpkg` ligger i `.gitignore` — stora geodatafiler hör inte hemma i Git.",
]),
("A4.2", "Etablera rutin för NNK-uttag", "A", 36, 36, "H", "", ["A1.2"], [
 "Dokumentera exakt hur du gör uttaget, så att det går att upprepa identiskt i v45: vilket lager, vilka fält, vilket filter, vilket format.",
 "Uttaget ska innehålla minst: NOID, NATURTYP, NATURTYPKO, NATURTYPSS, KARTERINGS, FORANDRING, URSPRUNG, KOMMENTAR, NNK_KOMMEN, REDIGERARE, REDIGERATA, REDIGERATG, SKAPATDATU, MALNATUR1–3, samt de nya tillstånds- och dateringsfälten när de driftsatts.",
 "Exportera som shapefile eller GPKG till `data/uttag/nnk_YYYYMMDD.gpkg`.",
 "Kör `python scripts/analysis/koppla_omraden.py` mot uttaget för att få SITECODE på varje yta. Sätt miljövariabeln NNK_SHP till uttagets sökväg först.",
 "Kör `python scripts/analysis/nnk_kunskapslage.py` för att uppdatera nollmätningen.",
]),

# ============================== B ==============================
("B1.1", "Välj ut objekt för fältsäsongen", "B", 34, 34, "H", "", [], [
 "Öppna `docs/nnk/nnk_kunskapslage_dashboard.html`, avsnitt 4. Filtrera på Prioritet 1.",
 "Välj 15–25 objekt. Utgå från batch B (ängs- och hagmark inland, 16 objekt, små och snabba) plus de sällsynta typerna i batch C och D.",
 "Kriterium: hög hävdberoende areal ELLER sällsynt livsmiljötyp, OCH kolumnen *Fältkontr.* = 0. Har objektet redan fältdata är det slöseri att åka dit.",
 "Kolla restiden — gruppera objekt geografiskt så en fältdag täcker flera.",
 "Skriv listan i granskningsloggen med motivering per objekt. Den blir bilaga till planen för 2027.",
]),
("B1.2", "Stäm av urvalet med förvaltarna", "B", 35, 35, "H", "", ["B1.1", "A3.2"], [
 "Skicka listan till berörda förvaltare med en enda fråga: vilka av de här kan ni redan svara på, och vilka behöver vi faktiskt åka till?",
 "Detta är den viktigaste tidsbesparingen i hela hösten. Varje objekt förvaltaren kan svara på är en sparad fältdag.",
 "Stryk objekt de har aktuell kunskap om och lyft in dem i blanketten (H3.2) i stället.",
 "Uppdatera fältlistan och notera i loggen vilka som ströks och varför.",
]),
("B1.3", "Boka fältdagar och klarlägg markägarkontakter", "B", 35, 35, "K", "", ["B1.2"], [
 "Boka 8–10 fältdagar mellan v36 och v40. Lägg buffertdagar — väder och tillgänglighet slår ut fältdagar.",
 "Kontrollera markägarförhållanden per objekt. På statligt förvaltade reservat behövs normalt ingen förhandskontakt; på privatägd mark inom Natura 2000 bör markägaren informeras.",
 "Boka in förvaltaren på minst ett par av dagarna — deras lokalkännedom i fält är värd mer än en blankett.",
 "Sammanställ körschema och kontaktlista i `docs/faltprotokoll/faltplan_2026.md`.",
]),
("B2.1", "Fältkontroll hävdberoende gräsmark", "B", 36, 40, "HK", "L-B", ["B1.3"], [
 "Ta med: utskrift av objektets NNK-ytor, bevarandeplanen, vägledningen för aktuell livsmiljötyp, fältprotokollmall, GPS eller mobil med Artportalen.",
 "Per yta, bedöm i denna ordning: (1) stämmer livsmiljötypen? (2) stämmer utbredningen grovt? (3) pågår hävd? (4) finns de typiska arterna och strukturerna vägledningen kräver? (5) vilket tillstånd — gott, icke gott, eller varierar det inom ytan?",
 "Varierar tillståndet inom ytan: uppskatta andelen i procent. De nya NNK-fälten tar procent, så ytan behöver inte delas.",
 "Fotografera varje bedömd yta. Ett foto med koordinat är det bästa framtida underlaget som finns.",
 "OBS regel R1: en igenvuxen äng där orsaken är utebliven skötsel är fortfarande samma livsmiljötyp — i icke gott tillstånd. Klassa inte om den.",
 "Mata inte in i NNK ännu — tillståndsattributen driftsätts först v40. Använd fältprotokollet som mellanlager.",
]),
("B3.1", "Riktade besök på sällsynta livsmiljötyper", "B", 36, 41, "H", "L-B", ["B1.3"], [
 "Objekt och typer: 7110 högmossar i Tovhulta stormosse (SE0220176), 7230 rikkärr i Bråtamossen (SE0220137) och Pilgöljan (SE0220103), 9060 åsbarrskog i Fjellskäfte (SE0220503) och Tore Grav (SE0220217), 9180 ädellövskog i Lotsängsbacken (SE0220130), 6280 alvar i Persö (SE0220234), 4030 torra hedar i Lundäng (SE0220507) och Åsa gravfält (SE0220438).",
 "Sällsynta typer motiverar noggrannare dokumentation än vanliga — de väger tungt i länets totala areal av just den typen.",
 "Läs vägledningen för typen i bilen innan besöket. Definitionerna för de här typerna är snäva.",
 "Tovhulta stormosse har dessutom 3 Åtgärdas-ytor — ta med den frågan dit.",
 "Notera särskilt om typen faktiskt uppfyller kriterierna. Sällsynta typer är ofta felkarterade åt båda håll.",
]),
("B4.1", "Fältdokumentation per besökt yta", "B", 36, 41, "HK", "L-B", [], [
 "Dokumentera per yta: NOID eller objektid, livsmiljötyp, hävdstatus, strukturer och funktioner, typiska arter, påverkan, bedömd tillståndsklass med procentandelar, samt vad du är osäker på.",
 "Skriv ALLTID datum och bedömare. Utan det går FAQ fråga 4:s krav på aktualitet inte att besvara.",
 "Skriv osäkerheten i klartext: *\"kunde inte avgöra om fältskiktet uppfyller 6270 — behöver besök i juni\"* är en fullgod leverans. En gissning är det inte.",
 "Spara i `docs/faltprotokoll/YYYY-MM-DD_objekt.md` samma dag som besöket.",
]),
("B4.2", "Artobservationer till Artportalen", "B", 36, 41, "HK", "", [], [
 "Rapportera typiska och karakteristiska arter i Artportalen, med koordinat.",
 "FAQ fråga 8 pekar ut Artportalen som rätt plats — inte NNK. NNK ska inte innehålla artuppgifter.",
 "Rapportera samma dag eller senast dagen efter, medan bestämningarna är färska.",
 "Notera i fältprotokollet att observationerna är rapporterade, så kopplingen finns kvar.",
]),
("B4.3", "Åtgärdsbehov till SkötselDOS", "B", 36, 41, "K", "", [], [
 "Identifierat skötsel- eller restaureringsbehov förs in i SkötselDOS, inte i NNK. FAQ fråga 8.",
 "NNK beskriver vad som finns; SkötselDOS beskriver vad som ska göras. Blanda inte ihop dem.",
 "Koppla noteringen till objektet och beskriv åtgärden konkret.",
 "Stäm av med förvaltaren innan du för in — det är de som ska utföra åtgärden.",
]),

# ============================== C ==============================
("C1.1", "Etablera granskningsrutinen", "C", 35, 35, "H", "", ["A2.1", "A2.3"], [
 "Skriv ned rutinen i `docs/nnk/granskningslogg.md` som en mall du kopierar per objekt.",
 "Rutinen per objekt, åtta steg: (1) öppna objektet i KartLitS WebbGIS och i ArcGIS Pro mot NNK; (2) läs bevarandeplanen — vilka livsmiljötyper är utpekade, vilka är prioriterade bevarandevärden, vilka bevarandemål finns; (3) jämför bevarandeplanens typer mot vad NNK visar, notera differenser; (4) kontrollera mot aktuellt ortofoto och IR-ortofoto — syns uppenbara förändringar sedan 2012?; (5) kontrollera mot TUVA, VMI, VISS och Artportalen; (6) bedöm per yta: stämmer utbredningen — OK / justera / kontrolleras i fält / osäker; (7) notera i WebbGIS-mallen; (8) justera geometri i NNK endast där det påverkar arealen meningsfullt.",
 "Minsta karteringsenhet, från handledningen tabell 9: 0,25 ha generellt, 1 ha skog icke-natura och öppen myr, 0,5 ha skog natura, 2 ha ovan trädgränsen. Minsta karteringsbredd 10 m.",
 "Lägg större vikt vid gränsen mellan livsmiljötyp och icke-livsmiljötyp än vid gränser mellan olika livsmiljötyper — de senare är gradvisa och svåra att avgränsa exakt.",
 "Testa rutinen på ett litet objekt först och tidsätt den. Tidsåtgången är indata till volymuppskattningen i F1.2.",
]),
("C2.1", "Batch S — storobjekten Skärgårdsreservaten och Nynäs", "C", 41, 46, "H", "L-C", ["C1.1", "A3.4"], [
 "SE0220129 Skärgårdsreservaten (2 915 polygoner) och SE0220126 Nynäs (1 433) rymmer tillsammans 44 % av länets samtliga N2000-polygoner. Yta för yta är inte realistiskt.",
 "Stratifiera i ArcGIS Pro: symbolisera på NATURTYPKO och sortera attributtabellen på Shape_Area fallande.",
 "Hantera individuellt: alla ytor över 5 ha, alla hävdberoende ytor, alla sällsynta livsmiljötyper, alla Åtgärdas-ytor (91 i Skärgårdsreservaten).",
 "Hantera gruppvis: små hällmarks- och skogsytor med samma kod och samma bedömningsgrund. Selektera med Select By Attributes, sätt attributen i grupp, och skriv EN gemensam kommentar som anger att det är en generalisering och på vilken grund.",
 "Skärgårdsreservaten har redan 198 fältkontrollerade polygoner. Filtrera fram dem (KARTERINGS 3 eller 4) och återanvänd kunskapen — gör inte om den.",
 "Invänta svar från KartLitS (A3.4) på om metoden accepteras innan du kör hela vägen. Fråga 1 i arbetsplanens avsnitt 10.",
]),
("C3.1", "Batch A — kust och skärgård", "C", 38, 42, "HK", "L-C", ["C1.1"], [
 "Sex objekt: SE0220439 Askö, SE0220020 Strandstuviken, SE0220034 Tullgarn södra, SE0220231 Rågö, SE0220218 Stendörren, SE0220077 Ridö-Sundbyholmsarkipelagen södra. 1 692 ha terrester livsmiljötyp, varav 691 ha hävdberoende.",
 "Kör granskningsrutinen C1.1 per objekt.",
 "Särskilt att titta på: 1630 strandängar — hävdas de fortfarande? Strandstuviken har 15 Åtgärdas-ytor av typen 1630 och Rågö har 4.",
 "Marina ytor inom objekten: rör dem inte. FAQ fråga 16.",
 "Tullgarn södra har 299 ha okarterat — se C7.1.",
]),
("C4.1", "Batch B — ängs- och hagmark inland", "C", 35, 38, "K", "L-C", ["C1.1"], [
 "16 objekt: SE0220110 Skåraviken, SE0220017 Svanviken-Lindbacke, SE0220063 Sparreholms ekhagar, SE0220118 Labro ängar, SE0220182 Segersön, SE0220150 Tåkenön, SE0220085 Gripsholms Hjorthage, SE0220363 Lindön, SE0220115 Marsviken-Marsäng, SE0220206 Floden, SE0220088 Herröknanäs, SE0220603 Jungfruvassen, SE0220344 Lövön, SE0220309 Brebol, SE0220435 Gesta, SE0220228 Ånhammarsnäset. 851 ha terrester, 684 ha hävdberoende, bara 447 polygoner.",
 "Denna batch går FÖRST, medvetet: objekten är små och snabba, vilket kalibrerar rutinen och tidsuppskattningen innan de tunga batcharna.",
 "Tidsätt varje objekt och notera i loggen. Siffran används i F1.2.",
 "TUVA är det viktigaste sidounderlaget här — nästan allt är ängs- och betesmark.",
 "Milstolpe M2 i v38: batchen klar och rutinen kalibrerad.",
]),
("C5.1", "Batch C — våtmark och vattendrag", "C", 42, 44, "K", "L-C", ["C1.1"], [
 "Sex objekt: SE0220176 Tovhulta stormosse, SE0220137 Bråtamossen, SE0220103 Pilgöljan, SE0220021 Sjösakärren, SE0220106 Fjällmossen norra, SE0220304 Kilaån-Vretaån. 378 ha terrester, varav 128 ha sällsynta typer.",
 "Sällsynta typer här: 7110 högmossar (47 ha i länet), 7230 rikkärr (34 ha), 7231 rikkärr undertyp (4 ha), 3260 vattendrag (44 ha), 9750 svämskog (2,7 ha).",
 "Limniska ytor: ange livsmiljötyp i befintliga ytor och linjer där förekomsten är känd, men justera INTE ytterkanter eller vattendragsgeometri. FAQ fråga 16.",
 "VMI är sidounderlaget för våtmarkerna, VISS för vattendragen.",
 "Fjällmossen norra har 109 fältkontrollerade polygoner — återanvänd.",
]),
("C6.1", "Batch D — skog och ädellöv", "C", 43, 46, "K", "L-C", ["C1.1"], [
 "Tio objekt: SE0220602 Vilsta, SE0220343 Askholmen, SE0220503 Fjellskäfte, SE0220217 Tore Grav, SE0220130 Lotsängsbacken, SE0220211 Ekorneberg, SE0220234 Persö, SE0220348 Tynnelsö Djurgård, SE0220507 Lundäng, SE0220438 Åsa gravfält. 393 ha terrester, 92 ha sällsynta typer.",
 "Sällsynta typer: 9060 åsbarrskog (29 ha), 9072 ädellövdominerad betesmark (29 ha), 9180 ädellövskog i branter (10 ha), 4030 torra hedar (16 ha), 9110 bokskog (6 ha), 6280 alvar (6 ha).",
 "För 9010 taiga: kontrollera hällmarker i anslutning — handledningen 3.1 påpekar att grundkarteringen avgränsat taiga främst inom produktiv skog, så angränsande hällmarker kan behöva justeras.",
 "Kontrollera avverkningsanmälningar via Skogsstyrelsen för objekt med skogsmark — det är den vanligaste faktiska förändringen.",
 "Vilsta har 6 Åtgärdas-ytor.",
]),
("C7.1", "Okarterade ytor — Båven och Tullgarn södra", "C", 44, 44, "H", "L-C", ["C1.1"], [
 "SE0220303 Båven: 4 845 ha okarterat av 6 200 ha. Det är sjöytan. Lägg INGEN tid på ytterkanterna — FAQ fråga 16 och 29. Ange livsmiljötyp i befintliga ytor om förekomsten är känd. Dokumentera i loggen att det är medvetet nedprioriterat, med hänvisning till FAQ.",
 "SE0220034 Tullgarn södra: 299 ha okarterat av 2 014 ha. Kontrollera i ArcGIS Pro vad ytan består av — lägg NNK-lagret över objektsgränsen och titta på hålen.",
 "Är hålet terrestert är det ett faktiskt karteringsgap. Felanmäl till `NNK-kartering@metria.se` med sitecode, en skärmbild och en kort beskrivning.",
 "Är det vatten gäller samma sak som för Båven.",
 "Notera resultatet i loggen — båda posterna ska med i kunskapslägesrapporten (E2.1).",
]),

# ============================== D ==============================
("D1.1", "Bevaka driftsättningen av de nya NNK-attributen", "D", 39, 40, "H", "", [], [
 "FAQ fråga 30: nya attribut för tillståndsbedömning införs sommaren 2026, driftsättning planerad till slutet av september.",
 "Maila `kartlitsN2000@naturvardsverket.se` i v39 och be om bekräftat datum samt när utbildning ges.",
 "Kontrollera i ArcGIS Pro när attributen dykt upp: checka ut testobjektet igen och titta efter fälten för tillstånd i procent.",
 "Blir det försenat: fyll v40–v43 med arbetspaket C i stället. Ingen tid går förlorad, bedömningarna dokumenteras i fältprotokoll och granskningslager under tiden.",
]),
("D1.2", "Gå igenom den nya attributlistan", "D", 40, 40, "HK", "", ["D1.1"], [
 "Läs igenom vad som ändrats. Två saker är viktiga: fältnamnen byter från *natura-naturtyp* till *livsmiljötyp*, och tillstånd anges nu som procentuell andel av ytan.",
 "Konsekvensen av procentandelen: du behöver INTE längre dela upp en yta för att ange olika tillstånd. Det sparar mycket geometriarbete.",
 "Namnbytet sker automatiskt — det du redan lagt in påverkas inte.",
 "Uppdatera granskningsrutinen och fältprotokollmallen med de nya fälten.",
]),
("D1.3", "Delta i NV:s utbildning", "D", 40, 41, "HK", "", ["D1.1"], [
 "Anmäl båda till utbildningen så snart datum finns.",
 "Ta med konkreta frågor från arbetet: storobjektsmetoden, generaliseringar, hur procentandelarna ska tolkas för mosaikartade ytor.",
 "Anteckna och lägg i `docs/nnk/`. Notera särskilt allt som avviker från handledningen från juli.",
]),
("D2.1", "Registrera tillstånd där kunskapen redan finns", "D", 41, 48, "HK", "L-D", ["D1.2"], [
 "Börja med de 277 ytorna som har karteringsstatus 3 eller 4 (fältdata) men naturtypsstatus 5 (ej bedömd). Det är hela uppdragets snabbaste vinst — kunskapen finns, den registrerades aldrig.",
 "Hitta dem: i ArcGIS Pro, Select By Attributes på NNK-lagret: `KARTERINGS IN ('3 - Besökt i fält','4 - Inventerad i fält') AND NATURTYPSS LIKE '5%'`.",
 "Leta upp underlaget bakom varje: uppföljningsprotokoll, ÄoB-blankett, basinventeringsprotokoll. Kollegan söker parallellt i H4.1.",
 "Ta därefter de 482 fullgoda och 336 icke fullgoda — kontrollera att bedömningen fortfarande är rimlig och komplettera med procentandelar och datering.",
 "Checka ut objektet i ArcGIS Pro, sätt attributen, kör toolboxen, checka in. Arbeta objekt för objekt, inte spritt — utcheckning är områdesbaserad.",
]),
("D2.2", "Dokumentera grunden för varje bedömning", "D", 41, 48, "HK", "L-D", [], [
 "Varje redigerad yta ska ha KOMMENTAR ifylld. Formatet: vad bedömningen bygger på, vem som gjort den, och när.",
 "Exempel: *\"Tillstånd bedömt utifrån uppföljning 2023-06 (protokoll i SkötselDOS) samt uppgift från NN, förvaltare, 2026-09-24. Hävd pågår men otillräcklig i södra delen.\"*",
 "Fyll även Slutdatum senaste inventering (`habitat_period_lastdata_end`) — det är enda sättet att besvara FAQ fråga 4:s krav på aktualitet.",
 "Utan detta är bedömningen inte spårbar, och kan inte redovisas i kunskapslägesrapporten.",
]),
("D2.3", "Registrera aktivt även oförändrat tillstånd", "D", 41, 48, "HK", "L-D", [], [
 "Är tillståndet oförändrat sedan tidigare bedömning — registrera det ändå, med grund och datum. FAQ fråga 9: \"oförändrat\" är också ett svar.",
 "Skillnaden mellan *ej bedömd* och *bedömd som oförändrad* är hela poängen med årets uppdrag.",
 "Sätt karteringsstatus 2 om grunden är befintlig kunskap, och uppdatera slutdatum till dagens datum.",
]),
("D3.1", "Mata in fältdata från arbetspaket B", "D", 41, 45, "HK", "L-D", ["B4.1", "D1.2"], [
 "Gå igenom fältprotokollen i `docs/faltprotokoll/` objekt för objekt.",
 "Checka ut objektet i ArcGIS Pro, sätt naturtypsstatus, procentandelar, karteringsstatus 3 eller 4, förändringsorsak, kommentar och slutdatum.",
 "Karteringsstatus: 3 Besökt i fält om ni bedömt utifrån ett besök; 4 Inventerad i fält endast om ni följt en standardiserad metodik.",
 "Förändringsorsak: 3 Komplettering om kunskapen bara var oregistrerad; 1 Rättning om karteringen var fel; 2 Faktisk förändring endast om naturen faktiskt ändrats.",
 "Kör toolboxen och checka in per objekt.",
]),
("D4.1", "Notera avvikelser mot bevarandeplan och beslut", "D", 41, 48, "H", "", [], [
 "FAQ fråga 24: när det du dokumenterar i NNK avviker från fastställd bevarandeplan eller reservatsbeslut ska länsstyrelsen göra en notering om avvikelsen.",
 "För en enkel lista i granskningsloggen: objekt, livsmiljötyp, vad bevarandeplanen säger, vad NNK nu visar, och varför.",
 "Bedömningen av vilka faktiska åtgärder som ska vidtas ingår INTE i KartLitS — men noteringen ska finnas.",
 "Bevarandeplanen når du via WebbGIS-lagret *NV Natura2000 områden*, raden BEVPLAN i attributtabellen. Länken finns även i `data/nnk/nnk_yta_med_sitecode.csv`.",
]),
("D4.2", "Lista objekt där beslut hindrar nödvändig skötsel", "D", 48, 48, "H", "", ["D4.1"], [
 "FAQ fråga 24 sista stycket: kommer ni fram till att nuvarande beslut eller skötselplan hindrar nödvändig skötsel för att upprätthålla livsmiljötyp i gott tillstånd, ska en notering om revideringsbehov göras.",
 "Sammanställ dessa fall i ett eget avsnitt i granskningsloggen.",
 "Detta blir ett eget stycke i planen till NV och ett underlag till Naturvårdsenhetens revideringsplanering.",
 "Stäm av med förvaltarna innan du skriver — de känner besluten.",
]),
("D4.3", "Peka ut utvecklingsmark och ange målnaturtyper", "D", 45, 50, "H", "L-D", ["D1.2"], [
 "Idag har bara 87 polygoner i hela länet en angiven målnaturtyp. FAQ fråga 23 säger att ytor med bevarandemål om utökad areal BÖR pekas ut som utvecklingsmark.",
 "Gå igenom bevarandeplanerna för P1-objekten: finns mål om att utöka arealen av någon livsmiljötyp? Finns mål om återskapande eller restaurering i reservatsbesluten?",
 "Formella krav: naturtypsstatus sätts till 3 Utvecklingsmark, NATURTYP måste vara en icke-natura-kod, och MALNATUR1–3 anger vad ytan ska bli. Upp till tre målnaturtyper.",
 "Prioritera ytor med påtaglig utvecklingspotential — de är enligt FAQ fråga 23 normalt högre prioriterade för skydds- och skötselresurser än ytor med ringa potential.",
 "Arronderingsmark och mark som på längre sikt skulle kunna restaureras sätts som icke-natura-typ, inte utvecklingsmark.",
 "Förvaltarna vet i regel mycket väl vilka ytor som är på väg åt rätt håll — ta frågan i H3.2.",
]),

# ============================== E ==============================
("E1.1", "Nytt NNK-uttag för före/efter-jämförelse", "E", 45, 45, "K", "L-E", ["A4.2"], [
 "Kör uttagsrutinen från A4.2 igen, exakt samma struktur som januariuttaget.",
 "Spara som `data/uttag/nnk_20261110.gpkg`.",
 "Kör `python scripts/analysis/koppla_omraden.py` — sätt NNK_SHP till det nya uttaget.",
 "Kör `python scripts/analysis/nnk_kunskapslage.py` och jämför mot nollmätningen. Nyckeltalet: andel polygoner med bedömd status ska ha rört sig från 8 %.",
 "Spara utskriften i granskningsloggen — det är den mätbara progressen.",
]),
("E1.2", "Statistik per Natura 2000-område", "E", 46, 46, "K", "L-E", ["E1.1"], [
 "Ta fram areal per livsmiljötyp × tillståndsklass per objekt ur det nya uttaget.",
 "Använd `data/nnk/nnk_yta_med_sitecode.csv` som grund — den har redan SITECODE på varje yta.",
 "Pivotera i Python eller Excel: rader = sitecode × naturtypskod, kolumner = tillståndsklass, värden = hektar.",
 "Detta är kärnan i vad FAQ fråga 6 efterfrågar för 2026.",
]),
("E1.3", "Statistik per livsmiljötyp för hela länet", "E", 46, 46, "K", "L-E", ["E1.1"], [
 "Aggregera samma data till länsnivå: areal per livsmiljötyp × tillståndsklass.",
 "Jämför mot nollmätningen i `docs/nnk/nnk_kunskapslage_dashboard.html` avsnitt 2.",
 "Lyft fram de hävdberoende typerna separat — de är uppdragets prioritet.",
]),
("E2.1", "Kvantifiera kunskapsluckorna per objekt", "E", 47, 47, "H", "L-E", ["E1.2"], [
 "Per objekt: areal i okänt tillstånd, areal osäker naturtyp, areal obestämd naturtyp, areal utvecklingsmark, areal okarterat.",
 "Detta är den exakta redovisning FAQ fråga 6 kräver av 2026.",
 "Ta med Båven (4 845 ha okarterat) och Tullgarn södra (299 ha) med motivering till varför de inte åtgärdats.",
]),
("E2.2", "Redovisa vilka livsmiljötyper per objekt som är osäkra", "E", 47, 47, "H", "L-E", ["E2.1"], [
 "Explicit krav i FAQ fråga 6: ni ska kunna säga vilka livsmiljötyper i vilket område som omfattas av osäkerhet.",
 "Producera en tabell: sitecode × livsmiljötyp × typ av osäkerhet (utbredning / tillstånd / båda) × areal.",
 "Sortera så att de hävdberoende och sällsynta typerna hamnar överst.",
]),
("E2.3", "Kvalitetsbrister på systemnivå", "E", 47, 47, "H", "L-E", ["E1.1"], [
 "Sammanställ: andel polygoner med BIDOS-ursprung, åldersfördelning på karteringen, saknade attribut, gränskvalitet, topologifel.",
 "Nollmätningen: 96 % BIDOS inom N2000, 81 % skapade 2012, endast 7,5 % någonsin fältbesökta.",
 "Detta är inte kritik av länet — det är ett resultat som ska in i planen för 2027 som ett insatsbehov, och en del av det ligger hos Metria.",
 "Systematiska fel i grundkarteringen anmäls till `NNK-kartering@metria.se`.",
]),
("E3.1", "Fyll i KartLitS WebbGIS-mallen för granskade objekt", "E", 38, 48, "K", "L-C", ["C1.1"], [
 "Öppna KartLitS WebbGIS, logga in med Automatisk inloggning.",
 "Zooma till objektet. Se till att lagret *LstAB NNK granskning* är aktivt. Tänd även *NV Naturtypskartan NNK* så färger och mönster syns.",
 "Klicka Redigera → välj lager *LstAB NNK granskning* → pilen under Redigera geoobjekt → infoklicka på polygonen.",
 "Fyll i: Livsmiljötyp behov av justering, Utbredning behov av justering, Livsmiljötyp 1–3, Kommentar livsmiljötyp och utbredning, Tillstånd behov av justering, procentandelarna, Kommentar tillstånd, Vad ska kontrolleras 1–3, Metod för kontroll, och sist Granskat = Ja eller Påbörjat.",
 "Spara med *Uppdatera* längst ner. Klicka ALDRIG *Ta bort* — det raderar hela geoobjektet. Vill du avbryta: bakåtpilen vid Redigera geoobjekt → Ignorera redigeringar.",
 "Enligt FAQ fråga 9.1 är det detta lager som blir underlaget till planen för 2027.",
]),

# ============================== F ==============================
("F1.1", "Vilka insatser krävs och vem gör det", "F", 46, 49, "H", "L-F1", ["E2.1"], [
 "Dela upp insatsbehovet i fem kategorier: eget fältarbete, eget skrivbordsarbete, Metria, NV:s arbetsgrupper, konsult.",
 "Metria har enligt FAQ fråga 26 INTE uppdrag att göra om tidigare karteringar, kartera med högre detaljering utifrån länsspecifika underlag, eller fältkontrollera. Räkna inte med det.",
 "Marina och limniska miljöer läggs uttryckligen på HaV och de nationella karteringarna.",
 "Ta med de livsmiljötyper som saknar fastställd vägledning (från A2.4) som ett eget stycke — de är blockerade av NV, inte av er.",
]),
("F1.2", "Volymuppskattning för 2027", "F", 47, 48, "H", "L-F1", ["C4.1", "E2.1"], [
 "Räkna antal objekt, hektar och fältdagar per livsmiljötypsgrupp.",
 "Kalibrera mot faktisk tidsåtgång i batch B — därför ligger den batchen först i planen. Ta tiden per objekt ur granskningsloggen.",
 "Underlag: 197 objekt totalt, varav 40 P1 klara 2026. Kvar: 43 P2, 108 P3, 6 P4 (P4 kräver ingen insats).",
 "Räkna separat för naturreservat utanför N2000: 24 914 ha, varav bara 8 % karterat som livsmiljötyp. Underlag från G1.3.",
]),
("F2.1", "Er prioritering för 2027", "F", 48, 49, "H", "L-F1", ["F1.2"], [
 "Ange ordningsföljd med motivering per livsmiljötypsgrupp, enligt FAQ fråga 11: hävdberoende först, därefter liten utbredning, förekomster med risk för försämring, och förekomster där åtgärder gjorts eller planeras.",
 "Var konkret om vad ni behöver veta, inte bara var. \"Vi behöver veta om hävden i 6270 upprätthålls\" är mer användbart än \"vi behöver besöka fler gräsmarker\".",
 "Koppla till de kvarvarande P2- och P3-objekten.",
]),
("F2.2", "Antaganden och generaliseringar", "F", 48, 49, "H", "L-F1", ["H3.2"], [
 "Detta är den fråga som ger störst avlastning om NV accepterar förslagen. Lägg mest tid här.",
 "Konkreta förslag att pröva: kan hävdstatus i TUVA användas som proxy för tillstånd i 6270 och 6510? Kan 8230 hällmarkstorräng antas oförändrad utan fältbesök, givet att den är svårpåverkad? Kan 9010 taiga i objekt utan avverkningsanmälan antas oförändrad? Kan betesmark med aktivt jordbruksstöd och pågående hävd antas vara i gott tillstånd?",
 "Varje generalisering behöver: vad den innebär, vilket underlag den vilar på, hur många hektar den skulle avlasta, och vilken risk den medför.",
 "Förvaltarnas svar från H3.2 är det som gör förslagen trovärdiga — utan dem är de gissningar.",
 "Skicka gärna in förslagen till KartLitS redan innan planen är klar. Ett tidigt ja är värt mycket mer än ett sent.",
]),
("F3.1", "Vad ni gör själva och vad ni behöver hjälp med", "F", 49, 49, "H", "L-F1", ["F1.1"], [
 "Dra gränsen tydligt. Marina och limniska miljöer lämnas explicit.",
 "Ange vad som kräver resurstillskott för att klaras till 2027, och vad som klaras inom befintlig bemanning.",
 "Ta med storobjekten som ett eget stycke — de är länets största enskilda utmaning.",
]),
("F4.1", "Underlag till årsredovisningen 2026", "F", 50, 52, "H", "L-F2", ["E2.1", "F2.1"], [
 "Regeringsuppdraget efterfrågar två tal: antal områden bedömda och antal områden med plan.",
 "Skriv kort — årsredovisningstext är sällan mer än ett stycke per uppdrag.",
 "Bifoga kunskapslägesrapporten som underlag om det efterfrågas.",
 "Stäm av med chef i god tid före inlämningsdatumet (fråga efter det i A3.1).",
]),

# ============================== G ==============================
("G1.1", "Gå igenom flik 3 i NNK-statistiken", "G", 42, 44, "K", "L-G", [], [
 "Öppna `docs/underlag/D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx`, fliken *3. NP_NR_exkl_överlapp*.",
 "Filtrera på Län = D. Sortera på kolumnen *Area NVR utanför N2000* fallande.",
 "Notera vilka reservat som har stor areal utanför N2000-överlappet — de är det egentliga arbetet 2027.",
 "Läge idag: 24 914 ha NR/NP utanför N2000-överlapp, varav bara 4 103 ha (8 %) karterat som livsmiljötyp. Betydligt sämre kunskapsläge än inom N2000.",
 "Läs reservatsbesluten för de största: vilka prioriterade bevarandevärden anges i syftet? Det styr prioriteringen på samma sätt som utpekade livsmiljötyper gör inom N2000.",
]),
("G1.2", "Screening av hävdberoende och sällsynta typer i reservaten", "G", 46, 46, "K", "L-G", ["G1.1"], [
 "Använd samma prioriteringsgrunder som för N2000: hävdberoende marker och sällsynta livsmiljötyper först.",
 "Kolumnerna längst till höger i flik 3 ger areal per naturtypskod per reservat — samma struktur som flik 2.",
 "Producera en enkel topplista: de 20 reservat som har mest hävdberoende eller sällsynt areal utanför N2000.",
 "Gör INTE mer än screening i år. Poängen är att 2027 inte ska börja med en överraskning.",
]),
("G1.3", "Grov volymuppskattning för naturreservaten", "G", 48, 48, "K", "L-G", ["G1.2"], [
 "Räkna antal reservat, hektar och uppskattade fältdagar, med samma tidsantaganden som i F1.2.",
 "Notera vilka som redan har aktuella skötselplaner eller uppföljningar — de går snabbare.",
 "Lämna över till F1.2 och G2.1.",
]),
("G2.1", "Ta med NR/NP i planen till Naturvårdsverket", "G", 50, 50, "H", "L-F1", ["G1.3", "F1.2"], [
 "Skriv ett eget avsnitt i planen om naturreservat och nationalpark.",
 "Poängtera deadline: NR/NP ska enligt FAQ fråga 6 vara klara 2027, inte 2028. Det är lätt att missa.",
 "Ange vad som är gjort (screening) och vad som återstår (allt annat).",
]),

# ============================== H ==============================
("H1.1", "Kartlägg vem som förvaltar vilka objekt", "H", 35, 36, "K", "L-H1", [], [
 "Öppna `docs/nnk/blankett_forvaltarkunskap_nnk.xlsx`, fliken Blankett.",
 "Be Naturvårdsenheten fylla i kolumn I *Förvaltare* — eller fyll i själv utifrån deras förvaltningsindelning.",
 "Prioritera de sju objekten med Åtgärdas-ytor och de 40 P1-objekten. Resten kan vänta.",
 "När kolumnen är ifylld går blanketten att filtrera per förvaltare och skicka ut i delar.",
]),
("H1.2", "Förankra upplägget med Naturvårdsenhetens chef", "H", 36, 36, "H", "", [], [
 "Boka 30 min. Det är deras personals tid du ber om — förankra innan du kontaktar förvaltarna.",
 "Ta med: `docs/nnk/metodik_forvaltarkunskap.md` avsnitt 1 (citaten som visar att NV godkänner lokalkännedom) och Åtgärdas-fliken i blanketten.",
 "Var konkret om vad du ber om: ca 60 minuter per förvaltare, plus tid att fylla i en blankett.",
 "Erbjud något tillbaka: den kunskap som förs in i NNK blir ett bättre underlag för deras egen skötselplanering, och åtgärdsbehov förs vidare till SkötselDOS.",
]),
("H2.1", "Gå igenom de 141 Åtgärdas-ytorna", "H", 37, 37, "H", "", [], [
 "Öppna `docs/nnk/blankett_forvaltarkunskap_nnk.xlsx`, fliken Åtgärdas-ytor. 30 rader, per objekt och livsmiljötyp.",
 "Fördelning: Skärgårdsreservaten 91 ytor, Strandstuviken 25, Marvikarna 7, Vilsta 6, Rågö 5, Storhultet 4, Tovhulta stormosse 3. Samtliga inom Natura 2000.",
 "Bakgrunden: koden är enligt den publika produktbeskrivningen en äldre kod från basinventeringen som betydde att kompletterande uppgifter behövdes för att bestämma naturtypen. 139 av 141 kommer från BIDOS och redigerades 2007–2008.",
 "Öppna dem i ArcGIS Pro för att se var de ligger: Select By Attributes på NNK-lagret, `KARTERINGS LIKE '5%'`. Zooma till urvalet.",
 "Detta blir öppningsfrågan i förvaltarsamtalen: *\"basinventeringen kunde inte bestämma naturtypen här — vet du vad det är?\"*",
]),
("H2.2", "Kontrollera KOMMENTAR i NNK Ajourhålla", "H", 37, 37, "H", "", ["A1.2"], [
 "Detta är en KÄLLKRITISK kontroll som måste göras innan slutsatser dras om kunskapsläget.",
 "Bakgrund: i den publika NNK är KOMMENTAR, NNK_KOMMEN och REDIGERARE tomma i samtliga 14 830 polygoner — men handledningen 1.3 säger att den publika versionen strippar kommentarer och användaruppgifter. Fälten kan alltså vara ifyllda i Ajourhålla.",
 "Checka ut ett av de sju Åtgärdas-objekten i ArcGIS Pro, förslagsvis SE0220020 Strandstuviken (25 ytor, hanterbart).",
 "Öppna attributtabellen och titta på KOMMENTAR och NNK_KOMMEN för ytorna med KARTERINGS = 5.",
 "Gör samma kontroll för några av de 277 ytorna med fältdata men ej bedömd status.",
 "Notera resultatet i granskningsloggen. Står grunden redan där är en stor del av arbetet redan gjort — då ska det bara läsas in och tillståndet registreras.",
 "Checka in utan ändringar.",
]),
("H2.3", "Kör områdeskopplingen mot NVR-lagret", "H", 43, 43, "K", "", [], [
 "5 221 NNK-ytor ligger utanför Natura 2000 — de finns i naturreservat och nationalpark och saknar områdesidentitet.",
 "Öppna `scripts/analysis/koppla_omraden.py`. Kopiera funktionen `hamta_sci` till en variant som hämtar NVR-lagret från Naturvårdsregistret i stället, och byt fältnamnet SITE_CODE mot NVRID.",
 "NVR-nedladdningen finns på `geodata.naturvardsverket.se/nedladdning/naturvardsregistret/`. `data/sources_sodermanland.csv` har mönstret för URL:erna.",
 "Kör och kontrollera att antalet reservat stämmer mot flik 3 i statistikuttaget.",
 "Resultatet behövs för arbetspaket G och för naturreservatsspåret 2027.",
]),
("H3.1", "Boka förvaltarsamtalen", "H", 37, 37, "K", "", ["H1.1", "H1.2"], [
 "Ca 60 minuter per förvaltare, flera objekt per möte. Fysiskt möte med karta framme är bättre än Teams.",
 "Skicka med i kallelsen: den filtrerade blanketten för deras objekt, plus en rad om vad mötet handlar om.",
 "Be dem titta igenom Åtgärdas-raderna i förväg — det är den fråga som kräver mest eftertanke.",
 "Boka in samtalen mellan v38 och v44 så att svaren hinner påverka fältplaneringen.",
]),
("H3.2", "Genomför förvaltarsamtalen", "H", 38, 44, "HK", "L-H2", ["H3.1", "H2.1"], [
 "FÖRE, ca 30 min per objekt: ta fram objektet i WebbGIS med lagren *LstAB NNK granskning* och *NV Naturtypskartan NNK* tända. Läs bevarandeplanen. Filtrera blanketten. Markera rader med karteringsstatus 3, 4 eller 5 — de har en historia.",
 "UNDER, punkt 1: börja med Åtgärdas-ytorna. Konkret, och den erkänner att kunskapen finns hos dem.",
 "UNDER, punkt 2: gå igenom hävdberoende marker objekt för objekt — hävdas den, av vem, hur länge till, vad är trenden.",
 "UNDER, punkt 3: fråga efter dokument du inte känner till — uppföljningsprotokoll, ÄoB-blanketter, konsultrapporter, gamla skötselplansbilagor, foton. Det ligger ofta på en enhetsmapp ingen letat i.",
 "UNDER, punkt 4: fråga specifikt om utvecklingsmark — vilka ytor är på väg att bli livsmiljötyp, vilka har ni restaurerat.",
 "UNDER, punkt 5: fråga om gränser bara där det rör större arealer. Under minsta karteringsenhet är det inte värt tiden.",
 "UNDER, punkt 6: avsluta med vad som borde kontrolleras i fält, och vilka objekt som kan lämnas som de är.",
 "REGEL R1 att bevaka hela tiden: när förvaltaren säger \"det är ingen äng längre\" — beror det på utebliven skötsel står livsmiljötypen kvar, i icke gott tillstånd.",
 "EFTER: för in i granskningslagret samma vecka. Minnesbilder av andras minnesbilder blir snabbt oanvändbara.",
]),
("H3.3", "Samordna med fältplaneringen", "H", 35, 44, "H", "", ["B1.2"], [
 "Löpande: varje gång en förvaltare kan svara på något, stryk motsvarande objekt ur fältlistan.",
 "Uppdatera fältplanen i `docs/faltprotokoll/faltplan_2026.md` och notera varför objektet ströks.",
 "Detta är den största enskilda tidsbesparingen i hela hösten.",
]),
("H4.1", "Eftersök odokumenterade underlag", "H", 38, 46, "K", "", ["H3.2"], [
 "Leta systematiskt efter det förvaltarna nämner: uppföljningsprotokoll, ÄoB-blanketter, konsultrapporter och PM, skötselplansbilagor, fotodokumentation, gamla inventeringar.",
 "Sök på enhetsmappar, i diariet, och i SkötselDOS. Fråga även dem som slutat, om det går.",
 "Prioritera underlag som rör de 277 ytorna med fältdata men ej bedömd status — där finns det med största sannolikhet ett protokoll någonstans.",
 "Skanna in det som bara finns på papper.",
]),
("H4.2", "Registrera funna underlag i datakälleregistret", "H", 38, 48, "K", "", ["H4.1"], [
 "Lägg in varje funnet underlag i `data/sources_sodermanland.csv` med samma kolumnstruktur som finns där.",
 "Ange: vad det är, vilket objekt eller vilka objekt det gäller, årtal, var det ligger, och om det är digitalt eller papper.",
 "Registret är i sig en leverans — det svarar på FAQ fråga 4 om vad bedömningarna vilar på.",
]),
("H5.1", "För in förvaltarkunskapen i granskningslagret", "H", 38, 46, "HK", "L-H2", ["H3.2"], [
 "Samma vecka som samtalet. Följ stegen i E3.1 för WebbGIS-redigeringen.",
 "Sätt `faltinventerare` = förvaltarens namn, inte ditt.",
 "Sätt `habitat_period_lastdata_end` = det årtal förvaltaren angav.",
 "Skriv `Kommentar_metod` i klartext: *\"Uppgift från NN, förvaltare, samtal 2026-09-24. Bygger på hens fältbesök hösten 2024 samt skötselplan 2019.\"*",
 "Fältmappningen finns i blankettens flik *Fältmappning* — den visar vilken blankettkolumn som hamnar i vilket fält.",
]),
("H5.2", "Registrera i NNK efter avstämning", "H", 41, 48, "H", "L-D", ["H5.1", "D1.2"], [
 "Först efter att du bedömt att underlaget räcker. Granskningslagret är förslagsnivå; NNK är skarpt.",
 "Tillståndsfälten först efter driftsättningen i v40.",
 "Karteringsstatus: 2 Granskad vid skrivbordet för förvaltarkunskap och dokument. 3 Besökt i fält om förvaltaren faktiskt varit där nyligen. 4 Inventerad i fält endast vid standardiserad metodik.",
 "Förändringsorsak: 3 Komplettering i nästan alla fall — kunskapen fanns, den var bara inte registrerad.",
 "Kör toolboxen och checka in per objekt.",
]),
("H5.3", "Skicka avstämning tillbaka till förvaltaren", "H", 38, 48, "H", "", ["H5.1"], [
 "Skicka en kort sammanfattning av vad du fört in, per objekt.",
 "Förvaltaren ska känna igen sin egen uppgift. Gör de inte det har något gått fel i översättningen.",
 "Detta är också det som gör att de svarar nästa gång du frågar.",
]),
]

CHECKLISTA_INCHECKNING = [
 "Kör toolboxen i ArcGIS Pro på det utcheckade området — databasreglerna kontrolleras där, inte vid incheckningen.",
 "Alla obligatoriska attribut ifyllda med godkända värden. Undantag: fritextfälten och de beräknade fälten.",
 "Inga överlapp mellan ytor. Inga glapp eller tomrum. Linjer och ytor korsar inte sig själva.",
 "Topologifel, prioritering enligt handledningen 3.3: undvik nya fel, prioritera överlapp, åtgärda hål större än 0,25 ha och remsor bredare än 10 m, strunta i mindre.",
 "FORANDRING satt på allt du ändrat — 3 Komplettering, 1 Rättning, eller 2 Faktisk förändring.",
 "KARTERINGS uppdaterad så att den speglar underlaget, inte din ansträngning.",
 "Slutdatum senaste inventering ifyllt.",
 "KOMMENTAR ifylld med grund och källa.",
 "Systematiska fel i grundkarteringen anmälda till NNK-kartering@metria.se.",
]

AVGRANSNINGAR = [
 ("Marina livsmiljötyper läggs inte in i NNK", "16 912 ha osäker marin areal lämnas orörd", "FAQ f.16"),
 ("Limniska ytterkanter justeras inte", "Livsmiljötyp anges i befintliga ytor där förekomsten är känd", "FAQ f.16"),
 ("Båvens 4 845 ha okarterat åtgärdas inte", "Limniskt objekt, nationell kartering pågår", "FAQ f.16, f.29"),
 ("Grottor, branter, sandstäpp, inlandssandmarker", "Nationella karteringsunderlag räcker", "FAQ f.16"),
 ("Obetydliga livsmiljötyper inom N2000", "Endast areal redovisas, ingen tillståndsbedömning", "FAQ f.15"),
 ("Standard Data Form / N2000-databasen uppdateras inte", "Uppgifterna hämtas automatiskt ur NNK", "FAQ f.17"),
 ("Tillståndsbedömningar med osäkert underlag görs inte", "Behåll tidigare bedömning eller ange okänt, dokumentera osäkerheten", "FAQ f.22"),
 ("Uppdateringar under minsta karteringsenhet görs inte", "0,25 ha generellt, 1 ha skog och våtmark, 0,5 ha ädellöv", "FAQ f.12"),
 ("Tidigare signifikansbedömningar görs inte om", "Endast nytillkomna livsmiljötyper bedöms", "FAQ f.15"),
 ("Naturreservat utanför N2000 får screening, inte genomgång", "Deadline är 2027", "FAQ f.6"),
]
