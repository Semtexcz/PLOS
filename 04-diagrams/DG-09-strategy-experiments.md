# DG-09 — Strategy, Assumptions & Experiments

**Verze:** 0.2 • **Notace:** konceptuální UML class diagram v Mermaid. **Účel:** rozlišit alternativu, poznávací pokus, zkušenost, výklad a volbu. Autorita: [DOM-01, C3](../03-architecture/preliminary-domain-model.md), [GLO-01](../glossary.md). Legenda a validace: [index](README.md).

## Zdrojová definice

```mermaid
classDiagram
    direction TB
    Scenario "0..*" --> "0..*" Strategy : DR-17 informuje
    Strategy "0..*" --> "0..*" Assumption : DR-18 opira se o
    Experiment "0..*" --> "0..*" Assumption : DR-20 zkouma
    Experiment "0..*" --> "0..*" Project : DR-21 provaden pres
    Experiment "0..*" --> "0..*" NextAction : DR-21 provaden pres
    Experiment "0..*" --> "0..*" Observation : DR-22 ziskava
    Metric "0..*" --> "0..*" Observation : DR-28 strukturuje
    Review "0..*" --> "0..*" Observation : DR-23 posuzuje
    Review "1" --> "0..*" Interpretation : DR-24 vytvari
    Review "0..*" --> "0..*" Recommendation : DR-25 pripravuje
    Review "0..*" --> "0..*" Decision : DR-26 podklady pro
    Decision "0..*" --> "0..*" Recommendation : DR-40 prijima meni odmita
    Decision "0..*" --> "0..*" Strategy : DR-27 voli nebo reviduje
    Decision "0..*" --> "0..*" Assumption : DR-27 reviduje
```

## Výklad a omezení

Interpretation je obsah odvozený při jednom původním Review, nikoli autonomní evidence či nová událost. Kandidátní a přijatá Strategy jsou rozlišeny lidskou volbou, ne dědičností. Assumption je volitelná vazba Experiment pouze proto, že pokus smí mít místo tvrzení poznávací otázku; samotný experiment bez otázky i předpokladu je neplatný (INV-09).

Nerozhodný nebo prázdný poznatek nebrání ukončení pokusu. Doporučení není rozhodnutí, rozhodnutí nevyžaduje předchozí review. Vazby Value/Vision jsou v DG-06, vazby WOOP a jejich odvozené role v DOM-01; diagram nenahrazuje celý proces frameworku. INV-02/06/09/10/17/18; UC-01/05/06/07 a SV-05/06.
