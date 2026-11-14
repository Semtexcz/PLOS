# Výběr práce a WIP

**Typ dokumentu:** reference • **Stav:** návrh pro Iteration 3C.2; provozní pohled na [SS-03](../../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management) až [SS-06](../../03-architecture/conceptual-architecture.md#ss-06--review--adaptation), nikoli nová architektura • **Rozsah:** pracovní pohledy, výběr práce, kapacita, blokování a dokončení

Stránka popisuje, jak se kandidátní práce stává zahájenou a co znamená rozpracovanost (WIP). Definice obsahuje [GLO-01](../../glossary.md), vztahy a invarianty [DOM-01](../../03-architecture/preliminary-domain-model.md). Rozpracovanost je odvozený pohled [DC-36](../../glossary.md#doménové-koncepty), ne nová evidence, stavový automat ani univerzální limit. Postup popisuje [Řízení rozpracované práce](../how-to/manage-workflow.md).

## Pracovní pohledy

| Pohled | Význam | Co to není |
| --- | --- | --- |
| Kandidátní práce | možnost nebo projekt nevybraný k provedení | nárok na kapacitu ani zahájená práce |
| Připravená práce | vybraný záměr nebo krok, u kterého se posuzuje proveditelnost | ještě zahájená práce |
| Rozpracovaná práce | skutečně zahájená práce vyžadující pozornost nebo kapacitu | každá vybraná nebo odložená věc |
| Čekání nebo blokování | práce nemůže pokračovat za současných podmínek | dokončení ani automatický důvod k nové práci |
| Dokončení | skutečně dokončený rozsah práce | důkaz dosažení zamýšleného výsledku |

Pohledy popisují situaci; nejsou to nové entity ani přechody.

## Co se započítává do WIP

Do rozpracovanosti patří zahájená a neuzavřená práce ve stejném rozsahu. Stejný rozsah zůstává jedním záznamem, i když podporuje dva záměry, plyne ze závazku a zároveň z projektu, nebo se objeví v jiném pohledu ([INV-03](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)/15).

Nezapočítává se zachycený podnět, kandidát, informace ani dokončená práce; připravená práce se započítá až zahájením. Rozsah WIP závisí na pohledu: portfoliový ([SS-03](../../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management)) nebo operativní ([SS-05](../../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management)).

## Výběr práce

Při výběru rozlišujte čtyři věci: důležitost (co se zanedbáním zhorší), naléhavost (tlak času nebo okolí), závaznost (co jste slíbili nebo co plyne z povinnosti) a proveditelnost (zda je práce možná). Ani jedno samo nerozhoduje.

- Vyšší priorita nevytváří kapacitu; neslučitelné nároky se nesmějí prohlásit za proveditelné změnou pořadí ([INV-16](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).
- Strategie automaticky nepřeváží existující povinnost; vytlačení dlouhodobého směru je vědomé rozhodnutí.
- Naléhavý podnět může změnit dnešní volbu, ale jen po posouzení závazků a kapacity.
- Rozpracovanou práci lze dokončit, zmenšit nebo uvolnit; uvolnění je platná volba.
- Nevyřešený konflikt je přípustný stav. Bodování, pořadí ani pevné limity výběr nenahrazují.

## Blokování a čekání

Blokovaná práce není dokončená a sama nezakládá novou práci. Pokud k ní držíte odpovědnost nebo pozornost, zůstává v rozpracovanosti, i když nepokročí. Bez odpovědnosti jde o nezávazné čekání.

U blokace hledejte krok nezávislý na překážce. Každé čekání doplňte podmínkou návratu. Druhy čekání popisuje [Podněty, závazky a další kroky](commitment-workflow.md#čekání-a-kapacitní-nároky).

## Dokončení práce a dosažení výsledku

Dokončení uzavírá vymezený rozsah práce, ne zamýšlený výsledek ([INV-05](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)). Pozorovaný výsledek je samostatné pozorování ([DC-12](../../glossary.md#doménové-koncepty)), může být nejistý či rozporný.

Dokončení uvolňuje pozornost i kapacitu, ne zamýšlený účinek.

## Vztah ke kapacitě

Zdrojový nárok (Resource Demand) je potřeba zdroje, kapacita (Capacity) dostupnost zdroje a alokace (Allocation) rozhodnutí zdroj vyčlenit; pozorovaná spotřeba je samostatný údaj ([INV-12](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)). Projekt může mít nenulový nárok, i když není aktivní nebo nemá přidělenou kapacitu. Neaktivita nespotřebovává plánovanou kapacitu ani neruší nárok ([INV-11](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).

Rozpracovanost není alokace: zahájená práce nemusí být v plánu alokována a alokace není slib ani skutečnost. Stejný nárok se nezapočítá dvakrát kvůli dvěma záměrům ([INV-15](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).

## Návaznosti na architekturu

| Odpovědnost | Co přebírá |
| --- | --- |
| [SS-03](../../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management) portfolio | výběr práce a portfoliová rozpracovanost |
| [SS-04](../../03-architecture/conceptual-architecture.md#ss-04--planning--capacity-management) kapacita | ověření proveditelnosti, konflikty a alokace |
| [SS-05](../../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management) provádění | operativní rozpracovanost, čekání a dokončení |
| [SS-06](../../03-architecture/conceptual-architecture.md#ss-06--review--adaptation) reflexe | posouzení přetížení a rozdíl práce a výsledku |

Ověřované invarianty: [INV-03](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)/15, [INV-05](../../03-architecture/preliminary-domain-model.md#katalog-invariantů), [INV-11](../../03-architecture/preliminary-domain-model.md#katalog-invariantů), [INV-12](../../03-architecture/preliminary-domain-model.md#katalog-invariantů) a [INV-16](../../03-architecture/preliminary-domain-model.md#katalog-invariantů).

## Limity a otevřené otázky

- Neexistuje univerzální počet sloupců, WIP limit ani prahová hodnota přetížení ([ADR-04](../../05-decisions/decision-log.md#adr-04--vícezdrojová-kapacita-bez-univerzálního-skóre-priorit)).
- Vizualizace je mentální, textová nebo grafická; tabule ani aplikace nejsou podmínkou.
- Kdy je rozpracovanost vysoká, zůstává na úsudku člověka ([OQ-03](../../05-decisions/open-questions.md#otevřené-otázky)).
- Otevřené zůstávají prahy a spouštěče review ([OQ-01](../../05-decisions/open-questions.md#otevřené-otázky), [OQ-02](../../05-decisions/open-questions.md#otevřené-otázky)).

## Autoritativní zdroje

[GLO-01](../../glossary.md) pro definice, [DOM-01](../../03-architecture/preliminary-domain-model.md) pro identitu, vztahy a invarianty, [ARCH-01](../../03-architecture/conceptual-architecture.md) pro odpovědnosti SS-03 až SS-06, [provozní jádro](operational-kernel.md) a [strategická návaznost](strategic-bridge.md) pro provozní rámec.
