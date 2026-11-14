# Concept of Operations

**ID:** CO-01 • **Stav:** návrh provozní koncepce. Vazby: [charter](system-charter.md), [architektura](../03-architecture/conceptual-architecture.md).

Člověk vstupuje do PLOS podle aktuální potřeby. Režimy nejsou povinné po sobě jdoucí kroky ani úplný stavový automat. Mohou se překrývat a být přerušeny. „Výsledek režimu“ je informační výstup nebo rozhodnutí; nelze jej zaměňovat s výsledkem v životě.

| ID / režim | Účel z pohledu člověka | Základní vstupy | Očekávané výstupy | Podnět / odpovědné funkce |
| --- | --- | --- | --- | --- |
| OP-01 Strategické rozhodování | Ujasnit směr, alternativy a co zatím nevím | Hodnoty, životní oblasti, vize, změny okolností, dosavadní poznatky | Zvolená strategie nebo vědomě ponechané alternativy, předpoklady a návrhy experimentů | Významná změna či potřeba revize; [SS-01](../03-architecture/conceptual-architecture.md#ss-01--values--vision-management), [SS-02](../03-architecture/conceptual-architecture.md#ss-02--strategy--experimentation) |
| OP-02 Střednědobé plánování | Vybrat omezený soubor změn a ověřování na nejbližší období | Strategie, kandidátní cíle, experimenty, péče, závazky, hrubá kapacita | Vybrané portfolio, odložené možnosti s důvodem, zamýšlené výsledky a rámec alokací | Začátek horizontu či zásadní konflikt; [SS-03](../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management), [SS-04](../03-architecture/conceptual-architecture.md#ss-04--planning--capacity-management) |
| OP-03 Týdenní plánování | Převést vybrané nároky do uskutečnitelného blízkého plánu | Portfolio, dostupnost, termíny, regenerace, rozpracovanost, skutečnost předchozího období | Revidovatelný plán, prostor bez alokace, pojmenované konflikty a potřebná přejednání | Obvykle týden, případně při změně kapacity; [SS-04](../03-architecture/conceptual-architecture.md#ss-04--planning--capacity-management) |
| OP-04 Každodenní realizace | Rozhodnout, čemu se věnovat teď | Další kroky, aktuální kontext a kapacita, důležité povinnosti | Volba jednat, odpočívat nebo neplánovat; stav závazků a významná pozorování | Podle situace; [SS-05](../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management), člověk provádí skutečnou činnost |
| OP-05 Průběžné zpracování nových závazků | Nezaměnit zachycený podnět s přijatým slibem | Žádosti, nápady, nové povinnosti a informace | Vyjasněný podnět: informace, odmítnutí, možnost k pozdějšímu zvážení nebo závazek; další krok či čekání | Průběžně podle kapacity; [SS-05](../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management), významné nároky do [SS-03](../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management)/[SS-04](../03-architecture/conceptual-architecture.md#ss-04--planning--capacity-management) |
| OP-06 Reflexe a adaptace | Porozumět zkušenosti a zvolit změnu nebo pokračování | Pozorování, zamýšlené výsledky, nejistoty, subjektivní zkušenost | Interpretace oddělená od evidence, rozhodnutí a návrhy aktualizace příslušnému vlastníkovi | Blízké, střednědobé a strategické horizonty nebo událost; [SS-06](../03-architecture/conceptual-architecture.md#ss-06--review--adaptation) |
| OP-07 Krizové nebo kapacitně omezené fungování | Zachovat orientaci v bezprostředních potřebách s minimální režií | Aktuálně známé kritické povinnosti, základní potřeby, dostupná pomoc a kapacita | Zúžený rozsah, odklady či návrhy přejednání, ochrana regenerace; později postupný návrat | Vlastní volba člověka, přetížení či přerušení; [SS-04](../03-architecture/conceptual-architecture.md#ss-04--planning--capacity-management), [SS-05](../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management), [SS-06](../03-architecture/conceptual-architecture.md#ss-06--review--adaptation) |

Střednědobý horizont může vycházet z 12 Week Year, ale dvanáct týdnů není v PLOS povinné. Týden je orientační kontrolní rytmus, ne předpoklad pravidelného pracovního režimu. PLOS nevyžaduje každodenní vyplňování záznamů. Volba kratšího nebo nepravidelného rytmu je adaptace PLOS ([ADR-03](../05-decisions/decision-log.md#adr-03--revidovatelná-kadence-a-kontinuita-při-změně)).

## Omezený režim a návrat

Člověk může kdykoli zúžit používání metodiky na současné základní potřeby, známé neodkladné závazky a nejbližší zvládnutelnou volbu. Strategické rozpracování, podrobné záznamy a měření lze přerušit. PLOS má uchovat dostupné informace o odložených závazcích; nic se nepovažuje za splněné jen proto, že se přestalo sledovat. Ani tento režim nezaručuje zajištění všech potřeb.

Návrat začíná současným stavem. Starý plán je podklad k přehodnocení, nikoli seznam povinného dohánění. Neznámá historie může zůstat neznámá. Člověk podle kapacity obnovuje širší přehled; návrat nevyžaduje kompletní inbox, skóre ani pravidelný týden. Podrobné přechody a pravidla pro kritičnost patří do pozdějších iterací ([OQ-01](../05-decisions/open-questions.md#otevřené-otázky)).

## Ilustrativní scénáře pro návrhovou verifikaci

Scénáře nejsou popisem uživatele. Údaje jsou záměrně fiktivní. Kritérium „lze“ znamená, že návrh obsahuje odpovědnost a informační cestu; ne že už proběhl provozní test.

| ID | Situace | Co musí být v návrhu možné ukázat |
| --- | --- | --- |
| UC-01 Od záměru k jednání | Hodnota učení vede k cíli zjistit, zda nový obor dává smysl | Směr → předpoklad → malý experiment → výběr → alokace → další krok → pozorování → review; možnost zastavit po zjištění nesouladu |
| UC-02 Péče bez projektu | Pravidelná péče o domácnost a jednorázové splnění povinnosti | Životní oblast a závazek mohou vést přímo k rutině nebo dalšímu kroku; cíle ani projekty nejsou povinné |
| UC-03 Konflikt kapacity | Dvě věci vyžadují stejný časový prostor a energie je nejasná | Rozpor je viditelný; člověk může zmenšit rozsah, odložit, vyjednat nebo přiznat nesplnitelnost; priority nepřičítají čas |
| UC-04 Přerušení a návrat | Po období nízké kapacity zůstal neaktuální plán | Omezený režim jde použít ihned; návrat nevyžaduje doplnit historii; známé povinnosti nezmizí |
| UC-05 Změna strategie | Člověk opouští cíl, ale již něco slíbil druhému | Strategická vazba se změní, závazek a původní důvod zůstanou čitelné; přejednání je zvláštní rozhodnutí |
| UC-06 Nesouhlas a spontánnost | Člověk odmítne doporučení a chce volné odpoledne | Lze nealokovat kapacitu či doporučení změnit bez penalizace nebo povinného cíle pro odpočinek |
| UC-07 Aktivita bez výsledku | Kroky byly provedeny, očekávaná změna se neprojevila a část údajů chybí | Review oddělí provedení od účinku, připustí zpoždění i neznámé a navrhne revizi předpokladu |
| UC-08 Režie bez hodnoty | Evidence spotřebovává pozornost a nepomáhá rozhodnout | Lze vypustit metriku a zjednodušit praxi při zachování kritických závazků; vznikne podnět ke změně metodiky |

Tyto scénáře jsou společným základem [kritérií požadavků](../02-requirements/high-level-requirements.md) a [self-review](../07-review/architecture-review-report.md).
