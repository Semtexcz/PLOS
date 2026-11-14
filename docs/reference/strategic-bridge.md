# Strategická návaznost

**Typ dokumentu:** reference • **Stav:** návrh pro Iteration 3B; provozní pohled na [SS-01](../../03-architecture/conceptual-architecture.md#ss-01--values--vision-management) až [SS-06](../../03-architecture/conceptual-architecture.md#ss-06--review--adaptation), nikoli nová architektura • **Rozsah:** hodnota → vize → strategie → zamýšlený výsledek → týdenní priorita → další krok

Tato stránka popisuje horizonty a jejich předávání. Cesta je orientační, ne povinná hierarchie; běžná péče a závazky strategické zdůvodnění nepotřebují ([INV-07](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).

## Tři horizonty

| Horizont | Rozsah | Hlavní otázka |
| --- | --- | --- |
| Strategický | měsíce až roky | Jakou kvalitu jednání rozvíjím, jakou budoucnost si představuji a jakou cestou se vydám? |
| Taktický | týdny až měsíce | Jakou změnu nyní uskutečním a co se vejde do kapacity? |
| Operativní | dny | Jak začnu jednat a co dnes nesmím minout? |

Reflexe je společná ([SS-06](../../03-architecture/conceptual-architecture.md#ss-06--review--adaptation)); cestu znázorňuje [tutorial](../tutorials/from-values-to-action.md#diagram-cesta-od-hodnoty-k-dalšímu-kroku), volbu při nejistotě [strategická revize](../how-to/strategic-review.md#volba-při-strategické-nejistotě).

## Co se předává

| Prvek | Význam | Co vzniká předáním |
| --- | --- | --- |
| Hodnota | kvalita jednání, kterou rozvíjím; není dokončitelná | směr a měřítko volby, ne cíl |
| Vize | revidovatelná představa žádoucího stavu | obraz budoucnosti, ne plán |
| Strategie | volba cesty včetně toho, čemu se nevěnuji, s předpoklady | kandidátní cíle a experimenty |
| Projekt nebo experiment | organizace práce, nebo ověření otázky s mezí ukončení | další kroky; poznatek může cestu potvrdit, změnit i nechat otevřenou |
| Cíl a zamýšlený výsledek | konkrétní změna s horizontem a způsobem posouzení | zdrojový nárok; priorita rozhodne o přednosti při výběru |
| Týdenní priorita | čemu dát přednost při výběru práce vedle závazků | alokace ověřená proti kapacitě, další krok a pojmenované odklady |
| Další krok | konkrétní jednání s časem nebo podmínkou | provedení, nebo vědomá volba nejednat |

Dokončení práce nedokládá zamýšlený výsledek ([INV-05](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).

## Rozhodovací body

Vstupem je pozorování a dosavadní volba; výstupem rozhodnutí s důvodem a podklad pro nižší horizont.

| Přechod | Otázka | Výstup |
| --- | --- | --- |
| Hodnota → vize | Jak by vypadal běžný týden, kdybych žil podle hodnoty? | věta o žádoucí budoucnosti |
| Vize → strategie | Která cesta hodnotu podporuje a co kvůli ní vylučuji? | zvolená cesta nebo alternativy |
| Strategie → výsledek | Jakou změnu a do kdy poznám? | jeden zamýšlený výsledek s posouzením |
| Výsledek → priorita | Čemu dát přednost vedle závazků a co odložím s podmínkou? | jedna nebo dvě týdenní priority; alokace se ověřuje zvlášť |
| Priorita → krok | Jaká činnost začne a kdy? | další krok |

Při volbě alternativ se ptejte: Podporuje cesta hodnotu? Co vylučuje? Jak velký omyl unesu? Odpovědi jsou kvalitativní, bez bodování. Při nejistotě volte menší krok.

## Zpětná vazba

| Úroveň | Co se posuzuje | Otázka | Co se může změnit |
| --- | --- | --- | --- |
| [FB-01](../../03-architecture/conceptual-architecture.md#zpětnovazební-architektura) operativní | dnešní jednání a okolnosti | Co změnit v aktuálním jednání? | další krok, dnešní volba |
| [FB-02](../../03-architecture/conceptual-architecture.md#zpětnovazební-architektura) taktická | týden, portfolio, kapacita | Co změnit v týdnu nebo ve výběru? | priority, rozsah, výběr záměrů |
| [FB-03](../../03-architecture/conceptual-architecture.md#zpětnovazební-architektura) strategická | hodnoty, vize, předpoklady | Je zvolená cesta stále vhodná? | strategie, výsledek, vyjádření směru |

[FB-04](../../03-architecture/conceptual-architecture.md#zpětnovazební-architektura) se týká režie metodiky, ne směru života. Strategickou revizi otevřete, když se vzorec opakuje v dalších týdnech navzdory změně taktiky, když experiment vyvrátil klíčový předpoklad, když se trvale změnily okolnosti, nebo když se hodnota přestala objevovat i po zmenšení rozsahu. Počet týdnů není univerzální pravidlo; záleží na délce vzorce, kontextu a vaší zkušenosti, kdy už nejde o náhodu.

Jeden den ani nedostatek kapacity strategii nemění; řeší se rozsahem nebo odkladem. Kadence je příklad, ne povinnost; zpětná vazba nemusí projít všemi úrovněmi.

## Vazby na architekturu

- [SS-01](../../03-architecture/conceptual-architecture.md#ss-01--values--vision-management) vlastní hodnoty a vizi, [SS-02](../../03-architecture/conceptual-architecture.md#ss-02--strategy--experimentation) navrhuje cesty a experimenty, [SS-03](../../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management) vybírá záměry, [SS-04](../../03-architecture/conceptual-architecture.md#ss-04--planning--capacity-management) posuzuje kapacitu, [SS-05](../../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management) vede závazky a kroky, [SS-06](../../03-architecture/conceptual-architecture.md#ss-06--review--adaptation) interpretuje a doporučuje.
- [IF-02](../../03-architecture/conceptual-architecture.md#hlavní-rozhraní-a-toky) předává rámec hodnot a vize jako orientaci, [IF-04](../../03-architecture/conceptual-architecture.md#hlavní-rozhraní-a-toky) strategie, cíle a experimenty jako kandidáty, [IF-06](../../03-architecture/conceptual-architecture.md#hlavní-rozhraní-a-toky) vybrané záměry jako autorizaci směru (ne alokaci), [IF-11](../../03-architecture/conceptual-architecture.md#hlavní-rozhraní-a-toky) doporučení člověku; změnu provádí vlastník významu.
- Platí invarianty [DOM-01](../../03-architecture/preliminary-domain-model.md): změna strategie, cíle ani plánu neruší závazek ([INV-06](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)); péče, závazek ani krok nepotřebují strategický cíl ([INV-07](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)); experiment má otázku a mez ukončení ([INV-09](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)); pozorování, předpoklad, interpretace a rozhodnutí se nesměšují ([INV-10](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)); neznámé není nula ([INV-11](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)); vnitřní překážka není vnější omezení ([INV-17](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).

## Povinné a volitelné

| Prvek | Stav | Poznámka |
| --- | --- | --- |
| Lidské rozhodnutí a důvod | povinné při volbě | rozhoduje člověk |
| Závazek a jeho stav | povinné, pokud existuje | platí i bez strategie |
| Další krok | potřebný pro jednání | stačí ústně |
| Hodnota, vize, strategie, scénáře | volitelné | lze začít týdenním plánem |
| Cíl, portfolio, experiment | volitelné | při změně směru nebo nejistotě |
| Zápis, metrika, kadence | volitelné | nikdy podmínkou použití |

Každá činnost nemusí být trasovatelná ke strategickému cíli. Trasovatelnost znamená vysvětlit původ volby, ne udržovat strom.

## Meze

- Nejde o bodovací model; rozhodnutí zůstávají kvalitativní a vratná.
- Dvanáct týdnů je jedna z možných délek horizontu, ne norma.
- Návaznost nezakládá nový formulář, evidenci, aplikaci ani softwarovou komponentu.
- [Tutorial prvního týdne](../tutorials/first-week.md) i tato reference používají oba pojmy ve stejném smyslu: týdenní záměr je kandidátní zamýšlený výsledek, týdenní priorita rozhoduje o přednosti při výběru a alokace vyčleňuje konkrétní zdroj. Ani priorita, ani alokace nezakládají nový závazek.
- Otevřené: spouštěče revizí ([OQ-02](../../05-decisions/open-questions.md#otevřené-otázky)), hloubka záznamu ([OQ-03](../../05-decisions/open-questions.md#otevřené-otázky)).

## Autoritativní zdroje

- [GLO-01](../../glossary.md), [DOM-01](../../03-architecture/preliminary-domain-model.md), [ARCH-01](../../03-architecture/conceptual-architecture.md), [provozní jádro](operational-kernel.md).
