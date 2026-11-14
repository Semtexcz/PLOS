# DG-05 — Feedback Control Architecture

**Účel:** vyjádřit několik horizontů učení a lidskou autoritu mezi doporučením a změnou. **Dokumentace:** [FB-01 až FB-04 v ARCH-01](../03-architecture/conceptual-architecture.md), [OP-06/07](../01-foundations/concept-of-operations.md), [ADR-03/05](../05-decisions/decision-log.md).

## Zdrojová definice

```mermaid
flowchart LR
    reference["Reference: hodnoty, záměry, potřeby, závazky"]
    evidence["Pozorování včetně nejistoty a chybějících údajů"]
    review["SS-06 Interpretace a varianty změn"]
    human["Člověk: změnit, pokračovat nebo nerozhodnout"]
    operational["FB-01 Operativní: krok a aktuální alokace"]
    tactical["FB-02 Taktická: portfolio a blízký plán"]
    strategic["FB-03 Strategická: směr a předpoklady"]
    method["FB-04 Metodická: režie a způsob používání"]
    living["Skutečné jednání a životní situace"]
    disturbance["Vnější vlivy a jednání ostatních"]
    reference -->|"co zamýšlíme a proč"| review
    evidence -->|"co se podařilo pozorovat"| review
    review -->|"interpretace a doporučení"| human
    human -->|"volba v dané situaci"| operational
    human -->|"revize výběru a alokací"| tactical
    human -->|"revize směru"| strategic
    human -->|"zjednodušení nebo přerušení metodiky"| method
    tactical -->|"nový rámec aktuálních voleb"| operational
    strategic -->|"aktualizace orientace"| reference
    strategic -->|"podklad nového výběru"| tactical
    operational -->|"podklad pro jednání člověka"| living
    disturbance -->|"neřízené vlivy"| living
    living -->|"zkušenost a dostupné údaje"| evidence
    method -->|"změna rozsahu pozorování a review"| review
    method -->|"zkušenost s režií a používáním"| evidence
    tactical -->|"aktualizované očekávání"| reference
    operational -->|"aktuální záměr"| reference
```

## Prvky a vztahy

Reference nejsou jediný číselný setpoint. Pozorování je omezené a interpretace není kauzální důkaz. FB-01, FB-02 a FB-03 mění odlišné objekty; FB-04 mění způsob používání metodiky. Všechny cesty od doporučení ke změně vedou přes člověka. Rytmy jsou v ARCH-01; událost může vyvolat revizi kdykoli.

## Předpoklady a omezení

Vliv volby na život je částečný a nejistý. Nezobrazuje se přenosová funkce, veličiny regulátoru ani důkaz stability. Model neznamená, že smyčky vždy proběhnou nebo že každé pozorování vyvolá změnu. Zpoždění účinků a riziko nadměrného přeplánování zůstávají OQ-02/OQ-05 a R-06.
