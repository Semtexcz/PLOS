# PLOS — Domain Architecture, Iteration 2

**Verze:** 0.2 • **Datum:** 2026-11-14 • **Stav:** dokončený a interně revidovaný návrh druhé iterace, určený k revizi vlastníkem systému. Baseline I1: commit `0932933`.

PLOS (Personal Life Operating System) je technologicky nezávislá metodika, která pomáhá člověku převádět hodnoty a záměry do rozhodování a jednání, pečovat o běžný život a učit se ze zkušenosti. Člověk zůstává konečnou autoritou. Úspěchem není počet dokončených úkolů.

Návrh kombinuje hierarchii záměrů s distribuovanými funkčními odpovědnostmi a několika zpětnovazebními smyčkami. Šest subsystémů jsou pohledy na metodiku, nikoli aplikace, týmy nebo povinné oddělené evidence. Běžné závazky a péče o životní oblasti mají vlastní legitimitu vedle strategických změn.

## Jak dokumentaci číst

| Artefakt | Obsah |
| --- | --- |
| [System Charter](01-foundations/system-charter.md) | Problém, účel, hranice, aktéři, předpoklady a úspěch |
| [ConOps](01-foundations/concept-of-operations.md) | Sedm provozních režimů a ilustrativní scénáře |
| [Design Principles](01-foundations/design-principles.md) | Normativní principy P1–P11 ze zadání |
| [Stakeholder Needs](02-requirements/stakeholder-needs.md) | Potřeby a jejich původ |
| [High-Level Requirements](02-requirements/high-level-requirements.md) | Požadavky, stav, odůvodnění, ověření a alokace |
| [Conceptual Architecture](03-architecture/conceptual-architecture.md) | Odpovědnosti, rozhraní a zpětné vazby |
| [Framework Integration](03-architecture/framework-integration.md) | Šest frameworků, zdroje, překryvy a vlastní adaptace |
| [Domain Architecture v0.2](03-architecture/preliminary-domain-model.md) | Katalog 36 konceptů, 40 vztahů, identita a 18 invariantů |
| [Diagramy](04-diagrams/README.md) | Pět zachovaných architektonických a pět doménových pohledů, zdroje Mermaid |
| [Decision Log](05-decisions/decision-log.md) | Architektonická rozhodnutí s alternativami a důsledky |
| [Open Questions](05-decisions/open-questions.md) | Hypotézy, otázky a rizika |
| [Architecture Roadmap](06-roadmap/architecture-roadmap.md) | Iterace 2–9, závislosti a kritéria dokončení |
| [Architecture Review — Iteration 2](07-review/architecture-review-report-iteration-2.md) | Audit v0.1, quality gates, dopady a meze ověření |
| [Semantic Validation Report](07-review/semantic-validation-report.md) | UC-01 až UC-08, SV-01 až SV-14 |
| [Review Iteration 1](07-review/architecture-review-report.md) | Historický výsledek baseline I1 |
| [Architecture Handoff — Iteration 2](07-review/architecture-handoff-iteration-2.md) | Rozhodnutí, rizika a přesný rozsah I3 |
| [Handoff Iteration 1](07-review/architecture-handoff.md) | Historické předání v0.1 |
| [Glossary](glossary.md) | Autoritativní slovník |

## Pravidla čtení a změn

- **Z — zadáno:** závazek explicitně stanovený uživatelem v kickoff zadání. Neznamená schválení celého nového návrhu.
- **N — navrženo:** odvozená potřeba nebo požadavek k potvrzení. Je podkladem současného návrhu, dosud bez uživatelské validace.
- **D — rozhodnuto pro příslušnou verzi návrhu:** architektonická volba autora v rámci zadání; vratná a podléhající revizi vlastníkem.
- **H — hypotéza:** tvrzení o vhodnosti nebo účinku návrhu, které vyžaduje ověření.
- **O — otevřeno:** nerozhodnutá otázka. **F — zdrojový princip:** parafráze doloženého frameworku; není důkazem účinnosti PLOS.

Prefixy: SN potřeba, FR funkční požadavek, QR kvalitativní požadavek, CON omezení, ASM předpoklad, SC kritérium úspěchu, OP provozní režim, UC scénář, SS subsystém, IF rozhraní, FB zpětnovazební smyčka, ADR rozhodnutí, H hypotéza, OQ otázka, R riziko, DG diagram, RV nález, DC doménový koncept, DR doménový vztah, INV invariant, SV sémantický případ, QG quality gate. P1–P11 jsou původní identifikátory principů. ID se při změně nepřečíslují a nepřidělují znovu jinému významu.

Definice pojmů se mění ve slovníku, význam vztahů v doménovém modelu, normativní znění v požadavcích. Architektura a diagramy jsou navazující pohledy; nesmějí zavádět skryté nové požadavky. Změna musí posoudit dopad na odkazy, odpovědnosti, scénáře a ADR. Aktuální doména má verzi v0.2. Nezměněné funkční pohledy I1 zůstávají baseline; review a handoff I1 jsou výslovně historické. Stav N požadavků se bez schválení nemění.

**Rozsah ověření:** strukturální kontroly souborů a odkazů, ruční sémantická revize a průchody fiktivními scénáři. Nejde o validaci životního přínosu s uživatelem ani o formálně ověřený MBSE model. Podrobnosti uvádí review report.

**Stop podmínka:** Iteration 2 je uzavřena interní revizí a předáním. Iteration 3 nebyla zahájena; vyžaduje nové zadání. Software, praktický provoz, workflow ani pilot nebyly navrženy.

Základní orientaci tvoří 12 Core významů v DOM-01; ani ty neznamenají povinné samostatné záznamy. Klasifikace ostatních konceptů vysvětluje, co je situační, volitelné či odvozené. PLOS musí být vykonatelný člověkem bez jakékoli softwarové implementace, nyní i v budoucnu.
