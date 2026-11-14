# Conceptual Architecture

**ID:** ARCH-01 • **Stav:** D — doporučená logická architektura v0.1. Konkrétní účinnost a únosnost jsou H-01 až H-05. Oporou jsou [požadavky](../02-requirements/high-level-requirements.md), [ADR](../05-decisions/decision-log.md) a [DG-02](../04-diagrams/README.md#dg-02).

## Základní uspořádání

PLOS je **kombinace hierarchie záměrů a distribuovaných funkčních procesů** (ADR-01). Hodnoty orientují směr, strategie navrhuje cesty a portfolio vybírá omezené nároky. Nejde o povinný strom rozkladu: běžná péče a externí povinnosti vstupují samostatně, poznatky mohou měnit vyšší úrovně a jeden projekt může přispívat více záměrům.

Strategické řízení určuje „proč a jakým směrem“, taktické „co teď vybereme a uneseme“, operativní „co má smysl udělat v dané situaci“. Průběžná péče vede napříč horizonty jako samostatný zdroj potřeb, ne jako čtvrtá úroveň hierarchie. Člověk může učinit lokální volbu bez předchozí kompletní strategické revize. Při významném dopadu na závazky nebo portfolio vznikne podnět k příslušné revizi.

Subsystémy níže jsou logické odpovědnosti. Je možné vykonávat více funkcí v jednom rozhovoru nebo záznamu. „Vlastník“ určuje, kde je informace vyjasňována a udržována; rozhodovací pravomoc má stále člověk.

## SS-01 — Values & Vision Management

**Účel:** udržovat srozumitelnou orientaci v hodnotách, vizi a potřebách životních oblastí. **Odpovědnosti:** význam hodnot a osobních principů, vyjádření vize, rozlišení průběžné péče a žádoucí změny, uchování důvodu změny směru.

**Vstupy:** lidská reflexe, potřeby a okolnosti, poznatky SS-06. **Výstupy:** orientační rámec hodnot a vize; vyjádřené potřeby péče. **Závislosti:** člověk je zdrojem významu; SS-06 přináší podněty, SS-02 a SS-03 rámec používají, SS-05 rozpracovává péči.

**Hranice:** neurčuje psychologicky „správné“ hodnoty, nevybírá projekty a nespravuje jednotlivé rutiny. **Invarianty:** hodnota není dokončitelný cíl; životní oblast nemusí mít projekt; zapsaná vize nevytváří závazek. **Požadavky:** FR-01, podpůrně FR-09 a QR-01.

## SS-02 — Strategy & Experimentation

**Účel:** formulovat možné cesty od orientace k žádoucí změně a snižovat rozhodovací nejistotu. **Odpovědnosti:** scénáře, strategické volby, předpoklady, návrh experimentů a interpretace jejich významu pro strategii.

**Vstupy:** rámec SS-01, pozorované okolnosti, poznatky SS-06 a omezení ze SS-04. **Výstupy:** navržená strategie, kandidátní cíle a experimenty, otázky k ověření. **Závislosti:** SS-03 rozhodovací podklady přebírá do portfolia; SS-05 organizuje provedení vybraných experimentů; SS-06 dodává reflexi.

**Hranice:** neautorizuje kapacitu experimentu a nevede druhou evidenci provádění. **Invarianty:** scénář není předpověď; experiment má poznávací účel a možnost ukončení; získaný poznatek neslibuje dosažení cíle. **Požadavky:** FR-02, podpora FR-11.

## SS-03 — Goal & Portfolio Management

**Účel:** udržovat vědomý výběr záměrů a přehled konkurenčních nároků. **Odpovědnosti:** konkretizace cílů a zamýšlených výsledků, rozhodování o výběru projektů a experimentů, viditelnost ostatních nároků, omezení rozpracovanosti na úrovni portfolia, významové vazby na strategii.

**Vstupy:** kandidáti SS-02, rámec SS-01, závazky a nároky péče SS-05, proveditelnost SS-04, reflexe SS-06. **Výstupy:** vybrané a odložené záměry, odůvodněné priority, požadavky na alokaci, návrhy změn rozsahu. **Závislosti:** SS-04 poskytuje společné kapacitní posouzení; SS-05 zachovává skutečné závazky.

**Hranice:** neplánuje konkrétní den a nepřepisuje dohody s druhými. Portfolio je rozhodovací pohled i na nároky, které nelze libovolně odmítnout. **Invarianty:** vybrat neznamená naplánovat; odložit projekt neznamená zrušit povinnost; opuštěný cíl nemaže původ závazků. **Požadavky:** FR-03, FR-08, FR-10, QR-02.

## SS-04 — Planning & Capacity Management

**Účel:** převádět vybrané nároky do revidovatelných a kontextově proveditelných alokací. **Odpovědnosti:** společný obraz kapacity, střednědobý rámec a blízký plán, konflikty zdrojů, prostor pro regeneraci a nealokovaný čas, podmíněné plány reakcí, zjednodušení rozsahu při omezené kapacitě.

**Vstupy:** priority SS-03, závazky a rozpracovanost SS-05, aktuální odhad člověka, pozorování SS-06. **Výstupy:** plán a alokace, nezajištěné nároky a konflikty, návrhy redukce, podmíněné reakce, rozsah omezeného režimu. **Závislosti:** SS-03 znovu posoudí výběr při konfliktu; SS-05 použije plán jako podklad; SS-06 poskytne zpětnou vazbu.

**Hranice:** nezvyšuje skutečnou kapacitu změnou odhadu, nesčítá energii a peníze do jediného skóre, nerozhoduje o správnosti hodnot. **Invarianty:** alokace není skutečnost ani slib; neznámá kapacita není volná kapacita; plný plán není povinný; snížení kapacity nevyvolává automatický dluh. **Požadavky:** FR-04, FR-07, FR-13, FR-14, QR-03, QR-05.

## SS-05 — Execution & Commitment Management

**Účel:** udržovat důvěryhodný přehled podnětů, závazků a možností nejbližšího jednání. **Odpovědnosti:** zachycení a vyjasnění, další kroky, rutiny, čekání a závislosti, operativní rozpracovanost, evidence skutečného provedení a potřeb přejednání.

**Vstupy:** nové podněty z okolí, potřeby péče SS-01, vybrané záměry SS-03, plán SS-04, rozhodnutí a zprávy člověka o skutečnosti. **Výstupy:** přehled závazků a nároků, další kroky, stav provádění, pozorování pro SS-06 a konflikty pro SS-04. **Závislosti:** člověk jedná mimo SoI; SS-03 posuzuje širší dopad, SS-04 kapacitu, SS-06 zkušenost.

**Hranice:** nezaručuje provedení ani reakce druhých, nepřiděluje skrytě strategickou prioritu podle naléhavosti. **Invarianty:** zachycení není přijetí; čekání není dokončení; povinnost může existovat i bez cíle; záznam zrušení plánu není zrušení vnější dohody. **Požadavky:** FR-05, FR-06, FR-09, QR-06, podpora FR-10 a FR-13.

## SS-06 — Review & Adaptation

**Účel:** spojit zkušenost s interpretací a návrhy změn na odpovídajícím horizontu. **Odpovědnosti:** review, rozlišení aktivity a výsledku, posouzení nejistot, návrhy změn vlastníkům, evidování významných rozhodnutí a kontrola režie metodiky.

**Vstupy:** pozorování člověka a SS-05, záměry a reference ostatních SS, odhad versus skutečnost kapacity. **Výstupy:** poznatky, doporučení, rozhodnutí člověka s důvody, podněty k aktualizaci. **Závislosti:** všichni vlastníci provádějí změny ve svém významovém rozsahu; ST-05 řeší změny referenční metodiky.

**Hranice:** neřídí ostatní SS samočinně a nevytváří druhé portfolio; nevyvozuje kauzalitu bez podkladu. **Invarianty:** pozorování není rozhodnutí; neznámé není nula; metrika je volitelný prostředek; rozhodnutí pokračovat či nic neměnit je platný výstup. **Požadavky:** FR-11, FR-12, QR-04, QR-07, průřezově QR-01.

## Hlavní rozhraní a toky

Rozhraní je významová dohoda o předání informací, nikoli API. **I** = informující tok; **N** = návrh; **R** = člověkem přijaté rozhodnutí nebo vymezení. Všechna R mají lidský původ. Tabulka zachycuje hlavní toky; detailní smlouvy a validace vstupů patří do Iteration 4.

| ID | Zdroj → příjemce | Obsah a význam | Typ / hranice |
| --- | --- | --- | --- |
| IF-01 | Člověk ↔ všechny SS | Hodnoty, odhady a volby dovnitř; varianty, stav a důsledky ven | I, N, R; žádný SS nepřebírá autoritu |
| IF-02 | SS-01 → SS-02, SS-03 | Hodnoty, vize, životní oblasti a orientační principy | I/R; rámec, nikoli seznam příkazů |
| IF-03 | SS-01 → SS-05 | Potřeby průběžné péče | I/N; nezakládají povinně projekty |
| IF-04 | SS-02 → SS-03 | Strategie, kandidátní cíle, experimenty, předpoklady | N/R; kandidát není aktivní práce |
| IF-05 | SS-05 → SS-03, SS-04 | Existující závazky, péče, naléhavé nároky, rozpracovanost | I; vnější povinnost nelze prostým odmítnutím zneplatnit |
| IF-06 | SS-03 → SS-04, SS-05 | Vybrané záměry, priority, důvody a omezení výběru | R; autorizace směru není automatická alokace |
| IF-07 | SS-04 → SS-03, SS-02 | Proveditelnost, konflikty a nejistoty kapacity | I/N; žádost o redukci či změnu předpokladů |
| IF-08 | SS-04 → SS-05 | Alokace, blízký plán, podmíněné reakce a rozsah omezeného režimu | R/N; revidovatelný podklad jednání |
| IF-09 | SS-05 a člověk → SS-06 | Provedení, výsledky, zkušenost, dostupná a využitá kapacita | I; oddělit pozorování od interpretace |
| IF-10 | SS-01 až SS-05 → SS-06 | Platné záměry, očekávání, předpoklady a důvody voleb | I; reference pro review, ne cílové skóre života |
| IF-11 | SS-06 → člověk → příslušný SS | Doporučení, lidské rozhodnutí, důvod a podklad změny | N → R; změnu provádí vlastník dotčeného významu |
| IF-12 | Okolí ↔ člověk ↔ SS-05 | Žádosti, existující povinnosti, vyjednávání a potvrzení změn | I/R; rozhodnutí druhých zůstávají mimo SoI |

SS-03 vlastní portfoliový limit rozpracovanosti; SS-05 operativní přehled souběžných činností. SS-04 ověřuje jejich společnou proveditelnost. Nejde o dva soupeřící seznamy priorit. Hodnoty limitů se v této iteraci nestanovují. Jeden závazek se v portfoliu a plánu zobrazuje v různém pohledu, nevznikají jeho nezávislé kopie (ADR-02).

## Kapacita a konflikt priorit

Kapacita je kontextové omezení pro daný horizont, rozlišené podle zdroje. Čas či peníze mohou mít jednotky, energie může být pouze slovně popsaná. Odhadovaná dostupnost, pozorovaná dostupnost a skutečná spotřeba se nesmějí zaměnit. Nevyužitý čas nedokazuje, že byla dostupná energie.

Allocation vyjadřuje zamýšlené použití zdroje, nikoli rezervaci garantovaného výsledku. Pro srovnatelné zdroje lze později ověřovat nároky vůči dostupnosti ve stejném horizontu a jednotce; mezi nesrovnatelnými zdroji se neprovádí součet. V I1 jde o sémantický závazek, ne o matematický model nebo algoritmus (ADR-04).

Při konfliktu SS-04 ukazuje nesoulad a alternativy, SS-03 posuzuje výběr, SS-05 důsledky pro dohody. Člověk rozhodne o rozsahu, odkladu, přejednání, pomoci nebo přijetí nevyřešeného konfliktu. Samotná vyšší priorita kapacitu nevytvoří. Ochrana strategie spočívá ve viditelném rozhodnutí při jejím vytlačení a návratu tématu do review, nikoli v pevné procentní kvótě. Regenerace je legitimní potřeba; spontánní čas nemusí být evidován jako projekt.

## Zpětnovazební architektura

Jde o kvalitativní model řízení s člověkem v rozhodovací smyčce. Život není deterministický řízený objekt; jiné osoby a prostředí nejsou ovladače PLOS. Diagram [DG-05](../04-diagrams/README.md#dg-05) popisuje informační vazby, ne důkaz stability řízení.

| ID / horizont | Reference | Pozorování a interpretace | Možný účinek lidské volby | Omezení |
| --- | --- | --- | --- | --- |
| FB-01 Operativní, podle situace | Bezprostřední potřeby, známé povinnosti, blízký plán | SS-05 a člověk rozpoznají změnu okolností; SS-06 může být krátká reflexe | Upravit další krok v SS-05 nebo alokaci v SS-04; nic nedělat | Neúplné údaje, kolísání energie; není nutný denní report |
| FB-02 Taktická, obvykle týdně a při konfliktu | Portfolio, zamýšlené výsledky a kapacitní rámec | SS-06 porovná pokrok, péči, rozpracovanost a únosnost | Změnit výběr SS-03 a plán SS-04, iniciovat přejednání SS-05 | Výsledek se může projevit později; jeden týden neprokazuje chybnou strategii |
| FB-03 Strategická, na konci horizontu či při změně | Hodnoty, vize, strategické předpoklady | SS-06 se SS-01/SS-02 interpretuje výsledky a zkušenost experimentů | Změnit strategii, cíle či vyjádření směru; zachovat jej | Nelze redukovat význam života na odchylku od čísla |
| FB-04 Metodická, při nadměrné režii nebo opakovaných potížích | Účel PLOS a P1–P11 | SS-06 posoudí užitečnost záznamů, rytmu a pravidel | Zjednodušit používání; změnu reference předat ST-05 | Vypnutí evidence nemá skrýt trvající povinnosti |

Žádné automatické „dohánění“ zmeškaných taktik. Uživatel může reagovat ihned na významnou událost; opakované přehazování plánu podle každého kolísání je riziko R-06. Konkrétní pravidla stabilizace budou navržena až s kontextem a ověřena, ne přenesena z technického regulátoru.

## Kontrola odpovědností a mezer

| Rozhodovací objekt | Jediný vlastník významu | Kdo dodává podklad | Proč nejde o duplicitu |
| --- | --- | --- | --- |
| Hodnoty, vize, potřeby oblastí | SS-01 | Člověk, SS-06 | SS-02 navrhuje cesty, nepředefinuje hodnoty |
| Strategie, scénář, předpoklad a návrh experimentu | SS-02 | SS-01, SS-04, SS-06 | Provádění experimentu má evidenci v SS-05 |
| Cíl, zamýšlený výsledek a výběr portfolia | SS-03 | SS-02, SS-04, SS-05 | SS-04 alokuje; nevytváří druhý výběr záměrů |
| Plán, kapacitní obraz a alokace | SS-04 | Člověk, SS-03, SS-05, SS-06 | Skutečnost je evidencí, ne přepsaným plánem |
| Projekt jako organizace práce, závazek, rutina, další krok a stav provádění | SS-05 | Člověk, okolí, SS-01, SS-03, SS-04 | SS-03 vlastní výběr projektu do portfolia; SS-05 jeho provádění, portfolio pouze odkazuje na tytéž nároky |
| Review, interpretace evidence a záznam významného rozhodnutí | SS-06 | Všechny SS, člověk | Obsah rozhodnutí vykoná příslušný vlastník; SS-06 je nenařizuje |

Podněty bez akce, externí povinnosti, péče, experimentování, konflikty, odklad i obnova mají přiřazenou funkci. Soukromí, delegace, detailní kritičnost a minimální rozsah záznamů nejsou dopracované; jsou explicitně ponechány v OQ-01, OQ-03 a OQ-07. CON-01 až CON-03 omezují všechny funkce.
