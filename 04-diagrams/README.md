# Architecture Diagrams

Všechny modely mají stav **D — konceptuální návrh v0.1**. Zdrojový blok `mermaid` v příslušném dokumentu je jediná autoritativní textová definice daného diagramu. Lze jej zobrazit v prostředí podporujícím Mermaid; render není samostatným zdrojem pravdy.

Používáme Mermaid `flowchart`, protože v I1 potřebujeme kontext, odpovědnosti, toky a významové vztahy. Nejde o SysML, UML diagram tříd, procesní exekuční model, ERD nebo databázové schéma. Směr šipky má význam uvedený u každého pohledu; mezi pohledy jej nelze automaticky přenášet. Rámeček seskupuje, nevyjadřuje dědičnost nebo vlastnictví osoby systémem.

## DG-01

[System Context Diagram](DG-01-system-context.md) — hranice metodiky, člověka, okolí a skutečného jednání. Dokumentace: CH-01.

## DG-02

[High-Level Functional Architecture](DG-02-functional-architecture.md) — rozdělení šesti odpovědností a jejich hlavní spolupráce. Dokumentace: ARCH-01.

## DG-03

[Framework Responsibility Map](DG-03-framework-responsibilities.md) — příspěvek šesti frameworků funkcím PLOS, bez zaměnění metod za subsystémy. Dokumentace: FW-01.

## DG-04

[Strategic-to-Operational Information Flow](DG-04-information-flow.md) — návaznost záměrů, samostatný vstup péče a povinností, kapacitní posouzení. Dokumentace: ARCH-01, DOM-01.

## DG-05

[Feedback Control Architecture](DG-05-feedback-control.md) — uzavření informačních smyček přes interpretaci a lidské rozhodnutí. Dokumentace: ARCH-01, CO-01.

## DG-06

[Preliminary Domain Concept Diagram](DG-06-domain-concepts.md) — reprezentativní významové vztahy bez kardinalit a atributů. Dokumentace: DOM-01, GLO-01.

**Validace:** zdroje byly ručně zkontrolovány proti dokumentaci a strukturálně kontrolovány na přítomnost ID, metadat a jednoho zdrojového bloku. Parser Mermaid ani renderer nebyly spuštěny. Syntaktická a vizuální správnost v konkrétní verzi rendereru nejsou strojově potvrzeny. Podrobnosti viz [review report](../07-review/architecture-review-report.md).
