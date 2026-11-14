# Framework Integration

**ID:** FW-01 • **Stav:** zdrojové principy F a návrhové adaptace D jsou oddělené. Zdroje byly konzultovány 2026-11-14; jde o primární veřejné materiály autorů nebo organizací, ne o systematickou rešerši účinnosti. Integrace PLOS jako celek není vědecky validována.

## Původ principů a přidělení rolí

| Framework | F — původní princip a zdroj | D — role v PLOS / rozhraní | Omezení integrace |
| --- | --- | --- | --- |
| ACT | Hodnoty vyjadřují volené kvality jednání, ne dosažitelné objekty. Psychologická flexibilita zahrnuje schopnost přetrvat i změnit jednání ve službě hodnotám; hodnoty a angažované jednání jsou součástí širšího modelu šesti procesů. [ACBS: Six Core Processes](https://contextualscience.org/six_core_processes_act) | Orientace SS-01 a způsob reflexe SS-06; IF-02, IF-11. Žádná metrika nesmí být zaměněna s hodnotou osoby. | PLOS nepřebírá terapeutický protokol a netvrdí, že evidencí hodnot realizuje celé ACT. |
| Designing Your Life | Odyssey Plans zkoumají alternativní budoucnosti; prototypování používá rozhovory a zkušenostní experimenty před velkým závazkem. [DYL: Prototyping Three Futures](https://designingyour.life/insights/the-magic-of-odysseys-prototyping-your-future-with-designing-your-life/) | SS-02 navrhuje scénáře a experimenty; IF-04 předává kandidáty do portfolia, IF-09/11 poznatky zpět. | V PLOS není předepsán počet scénářů ani délka jejich horizontu. Experiment zabírá kapacitu a není bezplatnou paralelní aktivitou. |
| 12 Week Year | Dvanáctitýdenní plán převádí vizi do cílů a taktik; týdenní plán obsahuje příslušné taktiky a pravidelné hodnocení provedení. [Oficiální Field Guide](https://12weekyear.com/wp-content/uploads/2018/09/Road-Map-to-the-12-Week-Year-Field-Guide.pdf), [Participant Workbook](https://academy.12weekyear.com/wp-content/uploads/2021/08/Participant_Workbook_New_New_Cover.pdf) | SS-03/SS-04 převádějí vybrané cíle do blízkých alokací; SS-06 porovnává plán a zkušenost. IF-06, IF-08, IF-10/11. | PLOS přebírá návaznost horizontů, nikoli povinný výkonový cíl, skórovací práh nebo neměnný cyklus. Variabilní kadence je vlastní adaptace ADR-03. |
| Personal Kanban | Dvě základní pravidla jsou zviditelnit práci a omezit rozpracovanost. [Personal Kanban — autoři metodiky](https://personalkanban.com/) | SS-03 zviditelňuje výběr a portfoliovou rozpracovanost; SS-05 probíhající činnosti; SS-04 posuzuje kapacitu. IF-05 až IF-08. | Tok činností není sám strategií. PLOS nestanovuje univerzální limit WIP ani povinnou vizuální aplikaci. |
| GTD | Zachytit, vyjasnit, organizovat, revidovat a jednat. Vyjasnění rozlišuje akční a neakční vstupy; pro akční obsah hledá další krok a případně projekt. [David Allen Company: What is GTD](https://gettingthingsdone.com/what-is-gtd/) | SS-05 udržuje důvěryhodnou evidenci a další kroky; revize je koordinována přes SS-06. IF-05, IF-09, IF-12. | Přidělení operativní role v PLOS neříká, že GTD neobsahuje vyšší horizonty. Nevzniká samostatný konkurenční strategický systém ani druhá týdenní revize. |
| WOOP | Wish, Outcome, Obstacle, Plan pracuje se zvoleným přáním, představou výsledku, vnitřní překážkou a reakcí „pokud–pak“. [WOOP Practice](https://woopmylife.org/en/practice), [Written WOOP Guide](https://www.woopmylifetoolbox.org/static1.squarespace.com/static/58a10eca725e25197ec58037/t/5ac36c591ae6cf15a4c49328/1522756697159/4-%2BWritten%2BWOOP%2BGuide%2B%281%29.pdf) | SS-04 nabízí volitelný podmíněný plán; SS-05 jej převádí do dostupné reakce, SS-06 posuzuje zkušenost. IF-08/09/11. | Vnější nedostatek zdrojů není automaticky vnitřní psychologická překážka. Pouhé pravidlo „pokud–pak“ není celá praxe WOOP. |

Poznámka k dostupnosti: u 12 Week Year byly dostupné indexované výňatky oficiálních PDF a web autora. Přímé otevření jiné verze týmového workbooku na doméně academy vrátilo 403. Dokumentace proto nečiní tvrzení o kompletním znění knih nebo neveřejných materiálů. Ostatní citované webové stránky byly otevřeny; Written WOOP Guide byl dostupný ve výňatku vyhledávání.

## Překryvy, konflikty a rozhodnutí o integraci

| Překryv či napětí | Rozlišení v PLOS | Důsledek / vazba |
| --- | --- | --- |
| ACT hodnotový směr × cílové plánování | Hodnota orientuje kvalitu jednání; Objective je konkrétní žádoucí změna | Dosažení cíle „nedokončí“ hodnotu. ADR-05, FR-01 |
| DYL objevování × závazek k taktikám | Experiment má poznávací účel; taktika slouží již zvolené cestě | Výsledek experimentu může legitimně zrušit plán. ADR-03, FR-02 |
| GTD přehled závazků × Kanban limit aktivity | Evidováno neznamená rozpracováno; závazek může čekat nebo potřebovat přejednání | Limit nesmí skrýt existující sliby. ADR-02, FR-05/06 |
| 12 Week Year strategické taktiky × každodenní povinnosti | Jeden kapacitní pohled zahrnuje obojí, ale zachovává rozdílný původ | Týdenní plán PLOS je širší adaptace; operativa strategii nevytlačí nepozorovaně. ADR-02/04 |
| Revize ve více metodách | SS-06 sjednocuje rozhodovací výstupy, jednotlivé otázky mohou mít jiný horizont | Není nutné absolvovat šest samostatných rituálů. ADR-01/05 |
| WOOP vnitřní překážka × objektivní kapacitní omezení | Před navržením reakce je rozlišena povaha omezení | Pokud reakce nezajistí zdroje, řeší se rozsah nebo směr. ADR-04 |
| Tlak na provedení × flexibilita a regenerace | Evidence výkonu nesmí morálně klasifikovat člověka | Skórování a pevná kadence nejsou povinné. ADR-03/05 |

Doporučená dělba GTD–Kanban–12 Week Year: **GTD pomáhá vyjasnit, co existuje a co znamená další krok; Kanban pomáhá vidět a omezit souběh; 12 Week Year inspiruje návaznost vybraných cílů a pravidelného plánování.** Společné kapacitní posouzení a pravidla konfliktu jsou návrhem PLOS, nikoli tvrzením původních autorů o této kombinaci.

Metody jsou prostředky funkcí, ne povinných šest subsystémů nebo šest samostatných evidencí. [DG-03](../04-diagrams/README.md#dg-03) je mapa příspěvků, nikoli tabulka plné implementace jednotlivých metod. Empirické přínosy této integrace zůstávají H-01 až H-05.

## Sémantická kontrola WOOP v Iteration 2

[DOM-01](preliminary-domain-model.md) mapuje Wish, Outcome, Obstacle a Plan na existující záměr, Intended Outcome, roli Internal Obstacle a Conditional Response. External Constraint je oddělená role. ADR-10 nevytváří čtyři nové identity ani netvrdí, že if–then nebo samotné mapování uskutečňuje celou praxi WOOP. Oficiální Practice a Written WOOP Guide byly v I2 znovu otevřeny 2026-11-14; průchod SV-12 je návrhová sémantická kontrola, nikoli test účinnosti frameworku.
