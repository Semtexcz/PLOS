# High-Level Requirements

**ID:** REQ-01 • **Stav:** předběžná specifikace. Z znamená explicitní mandát zadání, N nově odvozený návrh. Žádný požadavek N zatím nebyl uživatelem schválen. Kritéria jsou předběžná, ale formulovaná pro rozlišitelný výsledek; číselné tolerance se bez evidence nezavádějí.

„PLOS musí“ označuje požadované chování metodiky. Odpovědným vykonavatelem může být člověk; neimplikuje to automatizaci. Alokace SS určuje primárního vlastníka funkce, ne rozhodovací autoritu. Definice SS viz [architektura](../03-architecture/conceptual-architecture.md), UC viz [ConOps](../01-foundations/concept-of-operations.md), SN viz [potřeby](stakeholder-needs.md).

## Funkční požadavky

| ID / stav | Požadavek | Zdůvodnění / zdroj | Předběžné kritérium ověření | Primární alokace |
| --- | --- | --- | --- | --- |
| FR-01 / N | PLOS musí umožnit vyjádřit hodnoty, vizi a potřeby péče o životní oblasti jako rozlišitelné podklady rozhodování. | SN-01, SN-05; P2, P6 | Inspekce UC-01/02: hodnota není dokončitelný cíl a oblast nepotřebuje datum dokončení. | SS-01 |
| FR-02 / N | PLOS musí umožnit porovnat strategické alternativy pomocí předpokladů a navrhnout jejich ověření experimentem. | SN-01, SN-06; P5, DYL | UC-01: lze uvést dvě alternativy, nejistotu a experiment s otázkou, očekávaným poznatkem a možností skončit. | SS-02 |
| FR-03 / N | PLOS musí umožnit rozhodnout o výběru, odložení nebo ukončení kandidátních záměrů s ohledem na ostatní nároky a rozpracovanost. | SN-03; P4, P6 | UC-03: nový záměr se nestane aktivním bez viditelné volby člověka a posouzení dopadu na existující nároky. | SS-03 |
| FR-04 / N | PLOS musí podporovat revidovatelnou alokaci nároků do blízkého horizontu podle odhadované kapacity. | SN-03; P4, P5 | UC-03: dvě neslučitelné alokace jsou označitelné jako konflikt; neznámá energie není interpretována jako neomezená. | SS-04 |
| FR-05 / N | PLOS musí rozlišit zachycený podnět, možnost, neakční informaci a přijatý nebo uznaný závazek. | SN-04; operativa a GTD | UC-02: stejný typ podnětu lze vyjasnit jako informaci, odmítnutou žádost nebo skutečný závazek; zachycení samo nezakládá slib. | SS-05 |
| FR-06 / N | PLOS musí umožnit u závazku určit aktuální další krok nebo důvod, proč se zatím nejedná. | SN-04; spolehlivost závazků | UC-02/05: je rozlišitelné provedení, čekání na druhého a záměrný odklad; odklad není vykázán jako dokončení. | SS-05 |
| FR-07 / Z | PLOS musí umožnit člověku odmítnout doporučení, změnit plán a ponechat prostor pro odpočinek či spontánní jednání. | SN-02; P1, P5, otázka 10 | UC-06: existuje přípustná volba nealokovat nebo přestat plánovat, bez povinného strategického cíle a bez sankce metodiky. | SS-04; průřezově všechny SS |
| FR-08 / Z | PLOS musí umožnit vysvětlit návaznost důležitých strategických záměrů a konkrétních činností, aniž ji vyžaduje pro každou povinnost. | SN-01; P7 | UC-01 má dohledatelnou významovou cestu; UC-02 je validní bez Objective. | SS-03; vazby spravují vlastníci artefaktů |
| FR-09 / N | PLOS musí podporovat průběžnou péči jako samostatný zdroj činností a kapacitních nároků. | SN-05; P6, P7 | UC-02: rutina je opakovatelná, není trvale otevřeným projektem a její nároky vstupují do plánování. | SS-05; potřeby péče SS-01 |
| FR-10 / N | PLOS musí při změně strategie zachovat rozlišitelnost dosavadních závazků a jejich původního odůvodnění. | SN-06; P5, P7 | UC-05: cíl je opuštěn, ale závazek zůstává viditelný do samostatného rozhodnutí o jeho řešení; původní důvod se nepřepisuje novým. | SS-03; závazek SS-05 |
| FR-11 / N | PLOS musí rozlišit pozorování provedených činností, pozorování výsledků a jejich interpretaci při review. | SN-07; P3, P11 | UC-07: „kroky provedeny“ nedokazuje „výsledek nastal“; chybějící údaj je přiznatelný a interpretace může být revidována. | SS-06 |
| FR-12 / Z | PLOS musí uzavírat zpětnovazební smyčky na operativním, taktickém a strategickém horizontu. | SN-07; P3 | Pro každou FB-01 až FB-03 lze identifikovat referenci, pozorování, interpretaci, lidskou volbu a místo účinku změny. | SS-06; účinek podle cílového SS |
| FR-13 / Z | PLOS musí umožnit omezené fungování a návrat po přerušení plánování. | SN-08; P10 | UC-04: lze začít aktuálními potřebami a známými kritickými závazky bez doplnění všech starých záznamů. | SS-04; SS-05, SS-06 spolupracují |
| FR-14 / N | PLOS musí umožnit připravit podmíněnou reakci na rozpoznanou překážku zvoleného záměru. | SN-11; WOOP | UC-01/03: lze vyjádřit „pokud nastane X, zkusím Y“, odlišit vnitřní překážku od vnějšího omezení a přehodnotit nereálný záměr. | SS-04; proveditelný krok SS-05 |

## Požadavky na kvalitu

| ID / stav | Požadavek | Zdůvodnění / zdroj | Předběžné kritérium ověření | Alokace |
| --- | --- | --- | --- | --- |
| QR-01 / Z | Konečná rozhodovací autorita musí zůstat člověku. | SN-02; P1 | Inspekce všech řídicích toků: žádné doporučení ani metrika samy nemění závazek nebo strategii. | Všechny SS |
| QR-02 / Z | Zdůvodnění významné prioritizace musí být interpretovatelné ve vztahu k hodnotám, potřebám a závazkům. | SN-01; P2 | UC-01/03: člověk může pojmenovat důvod a dotčený kompromis bez znalosti skrytého skóre. | SS-03 |
| QR-03 / Z | Posouzení proveditelnosti musí respektovat čas, energii, finance a další relevantní omezené zdroje. | SN-03; P4 | UC-03: dostupný čas nekompenzuje chybějící peníze či energii; relevantní nejistota zůstává explicitní. | SS-04 |
| QR-04 / Z | Vyhodnocování musí připouštět kvalitativní a neúplnou evidenci bez povinného souhrnného skóre člověka. | SN-07, SN-09; P11 | UC-07/08: review lze provést slovně, uvést „neznámé“ a zrušit nepotřebnou metriku. | SS-06 |
| QR-05 / N | Minimální použitelný režim nesmí vyžadovat kompletní evidenci ani plnou plánovací kadenci. | SN-08, SN-09; P8, P10 | UC-04/08: zachování orientace v přítomnosti je možné bez strategické revize a bez vyčištění všech podnětů. | SS-04 |
| QR-06 / N | Změna interního plánu nesmí být reprezentována jako automatické zrušení externí povinnosti. | SN-04, SN-06; hranice SoI | UC-05: „navrženo přejednat“ se nezamění s „protistrana přijala změnu“; neovlivnitelná povinnost zůstává rozpoznatelná. | SS-05 |
| QR-07 / N | Každý základní koncept a funkční celek musí mít samostatnou rozhodovací hodnotu a autoritativní definici. | SN-09, SN-10; P6, P8 | Inspekce slovníku a SS: pro každý je uvedena potřeba existence a vlastník, bez duplicitního řízení téhož výstupu. | SS-06 a ST-05 |

## Omezení návrhu

| ID / stav | Omezení | Zdůvodnění / zdroj | Kritérium ověření | Alokace |
| --- | --- | --- | --- | --- |
| CON-01 / Z | Metodika ani její logická specifikace nesmějí předpokládat softwarovou implementaci, databázi, API či automatizovaného agenta; musí být vykonatelné člověkem nezávisle na podpůrném médiu. | SN-10; P9; explicitní upřesnění SoI v zadání I2, ADR-07 | Každý UC lze vysvětlit bez technologického produktu; žádné rozhraní nepředepisuje API nebo úložiště. | Všechny SS, ST-05 |
| CON-02 / Z | Iteration 1 musí zůstat u architektonických základů bez implementace a detailních algoritmů, stavů či personalizace. | SN-10; rozsah zadání §4 a §9 | Inspekce dodávky proti seznamu necílů charteru a roadmapě; pouze dokumentace a zdroje diagramů. | ST-05 |
| CON-03 / Z | Integrace musí pokrýt všech šest frameworků a rozlišit jejich principy od návrhových adaptací PLOS. | SN-10; zadání §2 | Každý framework má doložený zdroj, roli, hranici a popsanou adaptaci; žádný claim o validaci celé kombinace. | ST-05, všechny SS |

## Trasovatelnost a schvalování

Tabulky jsou primární maticí **SN / P → požadavek → SS → ověřovací scénář nebo inspekce**. Opačný pohled poskytují tabulky potřeb a odpovědností v architektuře. SC v charteru mapují systémový přínos na stejné scénáře; diagramy jsou ilustrací, nikoli náhradou normativního znění.

Schváleným mandátem jsou pouze explicitní položky Z a P1–P11. Při potvrzení N vlastníkem se zaznamená datum a podklad rozhodnutí; bez toho stav zůstává N. Hypotézy H-01 až H-05 ani ADR se nestávají požadavky přidáním slova „musí“. Otevřené hranice rozhodování a kritéria přijatelné režie viz [registr](../05-decisions/open-questions.md).

V této iteraci byla provedena návrhová kontrola pokrytí, nikoli realizace nebo validace všech požadavků. Důkazy a zbylá omezení jsou v [review reportu](../07-review/architecture-review-report.md).

## Dopad Iteration 2

CON-01 / Z byl zpřesněn podle explicitního zadání I2 a ADR-07: nestačí nezávislost na konkrétním produktu, nesmí být předpokládán software vůbec. Původní CON-02 zůstává omezením historického rozsahu I1; rozsah I2 vymezuje zadání a DOM-01. Žádné FR/QR ve stavu N nebyly schváleny ani přidány jako závazné. [Review I2](../07-review/architecture-review-report-iteration-2.md) uvádí dopady a návrhy doplnění ověřovacích kritérií pro I3; invarianty DOM-01 mají stav D.
