# DG-03 — Framework Responsibility Map

**Účel:** zviditelnit původ metodických příspěvků a jejich přidělení funkčním odpovědnostem. **Dokumentace:** [FW-01 se zdroji a omezeními](../03-architecture/framework-integration.md), [ADR-01 až ADR-05](../05-decisions/decision-log.md).

## Zdrojová definice

```mermaid
flowchart LR
    act["ACT"]
    dyl["Designing Your Life"]
    year["12 Week Year"]
    kanban["Personal Kanban"]
    gtd["GTD"]
    woop["WOOP"]
    values["SS-01 Values & Vision Management"]
    strategy["SS-02 Strategy & Experimentation"]
    portfolio["SS-03 Goal & Portfolio Management"]
    planning["SS-04 Planning & Capacity Management"]
    execution["SS-05 Execution & Commitment Management"]
    review["SS-06 Review & Adaptation"]
    act -->|"hodnoty jako směr"| values
    act -->|"flexibilita při reflexi"| review
    dyl -->|"alternativy a prototypování"| strategy
    year -->|"cíle v horizontu"| portfolio
    year -->|"návaznost taktik a týdne"| planning
    year -->|"pravidelné vyhodnocování"| review
    kanban -->|"viditelnost výběru a WIP"| portfolio
    kanban -->|"viditelnost toku a WIP"| execution
    gtd -->|"vyjasnění a další kroky"| execution
    gtd -->|"revize závazků"| review
    woop -->|"překážka a podmíněná reakce"| planning
```

## Prvky a vztahy

Levé uzly jsou zdrojové frameworky, pravé logické SS. Šipka znamená **příspěvek použitý v návrhu PLOS**. Nepředstavuje závislost programu, výlučnou kompetenci frameworku ani tvrzení o úplné implementaci jeho původní podoby. Přidělení je rozhodnutí PLOS; zdrojové principy jsou doloženy v FW-01.

## Předpoklady a omezení

Mapování nezobrazuje obecné SE/MBSE postupy, které jsou metodou návrhu celého systému. ACT ani GTD se původně neomezují jen na zde přidělené funkce. WOOP má i zkušenostní složku; samotný plán reakce ji nenahrazuje. H-01 až H-05 zůstávají neověřené.
