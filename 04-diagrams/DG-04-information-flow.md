# DG-04 — Strategic-to-Operational Information Flow

**Účel:** ukázat převod směru k jednání a stejně legitimní vstup průběžné péče a povinností. **Dokumentace:** [ARCH-01](../03-architecture/conceptual-architecture.md), [DOM-01](../03-architecture/preliminary-domain-model.md), [UC-01 až UC-06](../01-foundations/concept-of-operations.md).

## Zdrojová definice

```mermaid
flowchart TB
    values["Hodnoty a vize"]
    strategy["Strategie, scénáře a předpoklady"]
    candidates["Kandidátní cíle a experimenty"]
    care["Potřeby péče o životní oblasti"]
    inputs["Nové podněty a vnější povinnosti"]
    clarify["Vyjasnění: informace, možnost nebo závazek"]
    portfolio["SS-03 Výběr portfolia a přehled nároků"]
    capacity["Odhad kapacity a aktuální kontext"]
    planning["SS-04 Plán a kapacitní posouzení"]
    decision["Člověk: přijetí, změna, odklad nebo volný prostor"]
    execution["SS-05 Závazky, rutiny a další kroky"]
    living["Člověk: jednání nebo odpočinek"]
    observation["Pozorování a reflexe"]
    values -->|"orientují"| strategy
    strategy -->|"zdůvodňuje"| candidates
    candidates -->|"navrhované nároky"| portfolio
    inputs -->|"zachycení bez automatického přijetí"| clarify
    clarify -->|"rozpoznané závazky"| execution
    care -->|"péče bez povinného cíle"| execution
    execution -->|"IF-05 stávající nároky"| portfolio
    execution -->|"IF-05 operativní změny"| planning
    portfolio -->|"výběr a důvody"| planning
    capacity -->|"omezení a nejistota"| planning
    planning -->|"alokace a případný konflikt"| decision
    decision -->|"schválený nebo upravený plán"| execution
    decision -->|"přehodnocení výběru"| portfolio
    execution -->|"podklady pro aktuální volbu"| living
    living -->|"dostupná zkušenost"| observation
    observation -->|"podklad pro lidskou revizi"| strategy
    observation -->|"podklad pro přehodnocení kapacity"| capacity
```

## Prvky a vztahy

Hrany označují předání významu a informace, nikoli povinný workflow. Již existující závazek může být rozpoznán přímo v operativě; významné nároky se vracejí do společného posouzení. Konkrétní Project může organizovat provádění cíle nebo experimentu uvnitř [SS-05](../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management); uzel zde není zvlášť kvůli čitelnosti.

## Předpoklady a omezení

Není nutné projít všechny horní uzly před běžným jednáním. Rozhodovací uzel zvýrazňuje konflikt kapacity, ale konečná autorita člověka platí i jinde. Rutina bez cíle a volný prostor jsou validní cesty. Reflexe může vracet podnět i k hodnotám, jak ukazuje [DG-05](README.md#dg-05); diagram není úplný graf všech zpětných vazeb.
