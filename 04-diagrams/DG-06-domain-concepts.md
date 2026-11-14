# DG-06 — Preliminary Domain Concept Diagram

**Účel:** ukázat reprezentativní významové vztahy hlavních konceptů. **Dokumentace:** [DOM-01](../03-architecture/preliminary-domain-model.md), [GLO-01](../glossary.md), [ADR-06](../05-decisions/decision-log.md#adr-06--lehký-konceptuální-model-a-textové-diagramy).

## Zdrojová definice

```mermaid
flowchart TB
    subgraph orientation["Orientace a cesty"]
        value["Value"]
        vision["Vision"]
        scenario["Scenario"]
        strategy["Strategy"]
        assumption["Assumption"]
        experiment["Experiment"]
        value -->|"orientuje"| vision
        vision -->|"inspiruje alternativy"| scenario
        scenario -->|"informuje"| strategy
        strategy -->|"opírá se o"| assumption
        experiment -->|"zkoumá"| assumption
    end
    subgraph selection["Změna a výběr"]
        objective["Objective"]
        outcome["Outcome: zamýšlený nebo pozorovaný"]
        portfolio["Portfolio"]
        project["Project"]
        objective -->|"vyjadřuje zamýšlený"| outcome
        portfolio -->|"posuzuje a vybírá"| objective
        portfolio -->|"posuzuje a vybírá"| project
        project -->|"může přispívat"| objective
    end
    subgraph operation["Péče, odpovědnost a provádění"]
        area["Life Area"]
        care["Care Need"]
        input["Captured Input"]
        commitment["Commitment"]
        routine["Routine"]
        action["Next Action"]
        area -->|"dává kontext"| care
        care -->|"může být zajišťována"| routine
        input -->|"může být vyjasněn jako"| commitment
        commitment -->|"může být naplňován"| action
        commitment -->|"může být naplňován"| routine
        routine -->|"může vést k aktuálnímu"| action
    end
    subgraph feasibility["Proveditelnost a učení"]
        capacity["Capacity"]
        plan["Plan"]
        allocation["Allocation"]
        observation["Observation"]
        metric["Metric"]
        review["Review"]
        decision["Decision člověka"]
        capacity -->|"omezuje proveditelnost"| allocation
        plan -->|"uspořádává"| allocation
        metric -->|"volitelně strukturuje sběr"| observation
        review -->|"interpretuje"| observation
        review -->|"připravuje podklady pro"| decision
    end
    strategy -->|"zdůvodňuje"| objective
    portfolio -->|"posuzuje a vybírá"| experiment
    portfolio -->|"zohledňuje nárok"| commitment
    portfolio -->|"zohledňuje nárok"| care
    experiment -->|"lze provést prostřednictvím"| action
    commitment -->|"může být naplňován"| project
    project -->|"upřesňuje nejbližší"| action
    allocation -->|"vyčleňuje zdroj pro"| action
    observation -->|"dokládá pozorovaný"| outcome
    observation -->|"dokládá zkušenost s"| capacity
    decision -->|"může revidovat"| strategy
    decision -->|"může revidovat"| plan
```

## Prvky a vztahy

Uzly jsou pojmy, nikoli třídy nebo tabulky. Šipky se čtou podle popisků a nejsou časovým tokem. „Může“ znamená přípustnou vazbu, nikoli povinnost nebo stanovenou kardinalitu. Outcome je zobrazen jedním konceptem s rozlišeným použitím, ne sloučením očekávání a evidence. Základní rozdíly rozvádí DOM-01.

## Předpoklady a omezení

Kvůli čitelnosti nejsou zakresleny Personal Principle a Conditional Response ani všechny vazby alokací, experimentů a rozhodnutí; jsou popsány v DOM-01. Habit a Output jsou rozlišovací pojmy bez povinné samostatné evidence. Neexistuje předpoklad, že každý krok má cíl nebo projekt. Kardinality, detailní invarianty, atributy a stavy tento model nezachycuje.
