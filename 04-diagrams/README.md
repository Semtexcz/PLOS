# Architecture Diagrams

**Stav:** D — DG-01 až DG-05 jsou funkční baseline v0.1 zkontrolovaná v I2; DG-06 až DG-10 jsou doménové pohledy v0.2. Autoritativním zdrojem diagramu je blok `mermaid` v příslušném Markdown souboru. Definice pojmů jsou v [GLO-01](../glossary.md), vztahy/násobnosti/invarianty v [DOM-01](../03-architecture/preliminary-domain-model.md). Render není další zdroj pravdy.

DG-01 až DG-05 používají Mermaid `flowchart`, nejsou UML/SysML. DG-06 až DG-10 používají konceptuální **UML class diagrams** v podmnožině notace Mermaid `classDiagram`: třídy, směrované asociace a násobnosti. Směr je navigace/čtení pojmenovaného vztahu; nevyjadřuje čas, řízení nebo příčinu. Násobnost u konce označuje počet instancí tohoto konce pro jednu instanci protějšího. `0..*` znamená volitelnou vazbu bez obecného horního limitu, `1` právě jeden významový referent, `1..*` alespoň jeden. Nejde o povinné řádky záznamů.

Třída zde pojmenovává koncept, nikoli aplikaci, tabulku nebo povinnou samostatnou identitu. Obsahové a odvozené koncepty mají identitu podle [DOM-01](../03-architecture/preliminary-domain-model.md); role nejsou kresleny jako nezávislé podtřídy. Modely nepoužívají neodůvodněnou kompozici nebo dědičnost. Pro přesné varianty vztahů platí DR-ID. Omezení typu „otázka NEBO předpoklad“ a zákazy dvojího započtení jsou v textových INV, nikoli vymyšlené UML symboly. Zápis asociací byl porovnán s [oficiální dokumentací Mermaid classDiagram](https://mermaid.js.org/syntax/classDiagram.html); to samo není parserová validace.

## DG-01

[System Context](DG-01-system-context.md) — metodika, člověk, skutečné jednání a okolí; [CH-01](../01-foundations/system-charter.md).

## DG-02

[Functional Architecture](DG-02-functional-architecture.md) — šest funkčních odpovědností; [ARCH-01](../03-architecture/conceptual-architecture.md).

## DG-03

[Framework Responsibility Map](DG-03-framework-responsibilities.md) — původ příspěvků šesti metod; [FW-01](../03-architecture/framework-integration.md).

## DG-04

[Information Flow](DG-04-information-flow.md) — strategická i nestrategická cesta k jednání; [ARCH-01](../03-architecture/conceptual-architecture.md), [DOM-01](../03-architecture/preliminary-domain-model.md).

## DG-05

[Feedback Control](DG-05-feedback-control.md) — horizonty reflexe a lidské rozhodování; [ARCH-01](../03-architecture/conceptual-architecture.md), [CO-01](../01-foundations/concept-of-operations.md).

## DG-06

[Domain Architecture](DG-06-domain-concepts.md) — celkový propojující pohled, detailní vztahy následují. Nahrazuje předběžný flowchart v témže ID ([ADR-11](../05-decisions/decision-log.md#adr-11--konceptuální-uml-pohledy-s-explicitní-sémantikou)).

## DG-07

[Goals, Projects & Commitments](DG-07-goals-projects-commitments.md) — práce, odpovědnost a výsledky; [DOM-01](../03-architecture/preliminary-domain-model.md)/[C1](../03-architecture/preliminary-domain-model.md#c1--goals-projects--commitments).

## DG-08

[Care & Routines](DG-08-care-routines.md) — péče, opakování, provedení; [DOM-01](../03-architecture/preliminary-domain-model.md)/[C2](../03-architecture/preliminary-domain-model.md#c2--life-areas-care--routines).

## DG-09

[Strategy & Experiments](DG-09-strategy-experiments.md) — alternativy, pokusy, evidence a volby; [DOM-01](../03-architecture/preliminary-domain-model.md)/[C3](../03-architecture/preliminary-domain-model.md#c3--strategy-scenarios--experiments).

## DG-10

[Capacity & Allocation](DG-10-capacity-allocation.md) — dostupnost, nárok, vyčlenění a překryv; [DOM-01](../03-architecture/preliminary-domain-model.md)/[C4](../03-architecture/preliminary-domain-model.md#c4--capacity-allocation--planning).

## Stav ověření

Ruční sémantické porovnání DR, násobností a významu tříd s [DOM-01](../03-architecture/preliminary-domain-model.md) bylo provedeno pro všech pět doménových pohledů. Strukturální kontroly celého souboru dokumentace vykazuje [review I2](../07-review/architecture-review-report-iteration-2.md). **Úspěšná parserová a vizuální validace renderu nebyla provedena.** Dostupný lokální Mermaid bundle v Node skončil chybou DOM prostředí (`addHook is not a function`); místní Firefox nebylo možné spustit v omezeném prostředí (`unshare(CLONE_NEWPID): EPERM`, snap také vyžadoval zápis mimo povolený rozsah). Stažení CLI nebylo dostupné kvůli DNS (`EAI_AGAIN`). Zdrojové definice zůstávají čitelné v dokumentech. [RV-05](../07-review/architecture-review-report-iteration-2.md#domain-model-audit--nálezy-proti-v01-a-vypořádání) zůstává otevřený; úspěšnost vykreslení ani vizuální čitelnost nejsou tvrzeny.
