# DG-02 — High-Level Functional Architecture

**Účel:** ukázat vlastníky funkcí a hlavní informační vazby. **Dokumentace:** [ARCH-01](../03-architecture/conceptual-architecture.md), [REQ-01](../02-requirements/high-level-requirements.md).

## Zdrojová definice

```mermaid
flowchart TB
    human["Člověk: konečné rozhodnutí ve všech SS"]
    subgraph system["Metodika PLOS: funkční odpovědnosti"]
        values["SS-01 Values & Vision Management"]
        strategy["SS-02 Strategy & Experimentation"]
        portfolio["SS-03 Goal & Portfolio Management"]
        planning["SS-04 Planning & Capacity Management"]
        execution["SS-05 Execution & Commitment Management"]
        review["SS-06 Review & Adaptation"]
        values -->|"IF-02 rámec orientace"| strategy
        values -->|"IF-02 hodnoty a potřeby"| portfolio
        values -->|"IF-03 potřeby péče"| execution
        strategy -->|"IF-04 kandidáti a předpoklady"| portfolio
        portfolio -->|"IF-06 výběr a důvody"| planning
        portfolio -->|"IF-06 vybrané záměry"| execution
        execution -->|"IF-05 závazky a rozpracovanost"| portfolio
        execution -->|"IF-05 nároky a změny"| planning
        planning -->|"IF-07 proveditelnost a konflikty"| portfolio
        planning -->|"IF-07 omezení"| strategy
        planning -->|"IF-08 plán a alokace"| execution
        execution -->|"IF-09 pozorování"| review
        review -->|"IF-11 podnět k revizi směru"| values
        review -->|"IF-11 poznatky k předpokladům"| strategy
        review -->|"IF-11 podnět k revizi výběru"| portfolio
        review -->|"IF-11 podnět k revizi plánu"| planning
        review -->|"IF-11 podnět k úpravě závazků"| execution
    end
    human -->|"IF-01 volby a odhady, platí pro všechny SS"| system
    system -->|"IF-01 podklady a doporučení"| human
```

## Prvky a vztahy

Každý SS odpovídá stejnojmenné kapitole ARCH-01. Hrany jsou hlavní informační předání, nikoli časové pořadí. IF-11 znamená podnět, který se stává změnou až rozhodnutím člověka. Hrana k rámečku PLOS je souhrnná zkratka vztahu člověka se všemi SS.

## Předpoklady a omezení

Pro čitelnost není rozkreslen IF-10: každý SS poskytuje SS-06 platné reference a důvody. Okolí a IF-12 jsou v DG-01. Model není fyzickou dekompozicí do šesti aplikací ani šesti organizací. Vlastnictví konkrétních významů, rozsah invariantů a řešení překryvů jsou normativně vysvětleny v ARCH-01, nikoli geometrickou polohou uzlů.
