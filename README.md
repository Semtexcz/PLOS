# PLOS — doménová architektura a provozní návrh

**Doménová baseline:** v0.2 • **Provozní návrh:** v0.3 • **Datum:** 2026-11-15 • **Stav:** doménový model v0.2 zůstává autoritativní doménovou baseline; provozní návrh v0.3 a [integrační validační zpráva](07-review/plos-integration-validation-v0.3.md) jsou novější, návrhově ověřené, nikoli empiricky doložené. Baseline I1: commit `0932933`.

PLOS (Personal Life Operating System) je technologicky nezávislá metodika, která pomáhá člověku převádět hodnoty a záměry do rozhodování a jednání, pečovat o běžný život a učit se ze zkušenosti. Člověk zůstává konečnou autoritou. Úspěchem není počet dokončených úkolů.

Návrh kombinuje hierarchii záměrů s distribuovanými funkčními odpovědnostmi a několika zpětnovazebními smyčkami. Šest subsystémů jsou pohledy na metodiku, nikoli aplikace, týmy nebo povinné oddělené evidence. Běžné závazky a péče o životní oblasti mají vlastní legitimitu vedle strategických změn.

## Původní záměr projektu

[PROJECT_INTENT.md](PROJECT_INTENT.md) je kanonický přehled původního záměru vlastníka: proč PLOS existuje, jaký výsledek sleduje, které schopnosti jsou nezbytné, co je výslovně mimo rozsah a podle čeho se pozná úspěch. Slouží jako kritérium při rozhodování o dalších iteracích. Není náhradou [System Charter](01-foundations/system-charter.md) ani doménové architektury: definice zůstávají ve [slovníku](glossary.md), vztahy v [doménovém modelu](03-architecture/preliminary-domain-model.md) a odpovědnosti v [konceptuální architektuře](03-architecture/conceptual-architecture.md). Záznam je zatím návrh ke schválení vlastníkem.

Pravidla pro práci AI agentů v tomto repozitáři shrnuje [AGENTS.md](AGENTS.md): povinný kontext, Intent Alignment Check, stav záměru, Completion Gate a Change Control.

## Jak dokumentaci číst

**Používáte PLOS, ne architekturu?** [Uživatelská dokumentace](docs/README.md) nabízí návrh provozního postupu: tutorial, denní rozhodování, týdenní plánování a provozní jádro.

| Artefakt | Obsah |
| --- | --- |
| [Původní záměr projektu](PROJECT_INTENT.md) | Účel, North Star, osm nezbytných schopností, non-goals a správa záměru |
| [Pravidla pro AI agenty](AGENTS.md) | Povinný kontext, Intent Alignment Check, Completion Gate a Change Control |
| [System Charter](01-foundations/system-charter.md) | Problém, účel, hranice, aktéři, předpoklady a úspěch |
| [ConOps](01-foundations/concept-of-operations.md) | Sedm provozních režimů a ilustrativní scénáře |
| [Design Principles](01-foundations/design-principles.md) | Normativní principy [P1](01-foundations/design-principles.md)–[P11](01-foundations/design-principles.md) ze zadání |
| [Stakeholder Needs](02-requirements/stakeholder-needs.md) | Potřeby a jejich původ |
| [High-Level Requirements](02-requirements/high-level-requirements.md) | Požadavky, stav, odůvodnění, ověření a alokace |
| [Conceptual Architecture](03-architecture/conceptual-architecture.md) | Odpovědnosti, rozhraní a zpětné vazby |
| [Framework Integration](03-architecture/framework-integration.md) | Šest frameworků, zdroje, překryvy a vlastní adaptace |
| [Domain Architecture v0.2](03-architecture/preliminary-domain-model.md) | Katalog 36 konceptů, 40 vztahů, identita a 18 invariantů |
| [Diagramy](04-diagrams/README.md) | Pět zachovaných architektonických a pět doménových pohledů, zdroje Mermaid |
| [Uživatelská dokumentace](docs/README.md) | Tutorialy, how-to postupy a reference pro používání PLOS |
| [Decision Log](05-decisions/decision-log.md) | Architektonická rozhodnutí s alternativami a důsledky |
| [Open Questions](05-decisions/open-questions.md) | Hypotézy, otázky a rizika |
| [Architecture Roadmap](06-roadmap/architecture-roadmap.md) | Iterace 2–9, závislosti a kritéria dokončení |
| [Architecture Review — Iteration 2](07-review/architecture-review-report-iteration-2.md) | Audit v0.1, quality gates, dopady a meze ověření |
| [Semantic Validation Report](07-review/semantic-validation-report.md) | [UC-01](01-foundations/concept-of-operations.md#ilustrativní-scénáře-pro-návrhovou-verifikaci) až [UC-08](01-foundations/concept-of-operations.md#ilustrativní-scénáře-pro-návrhovou-verifikaci), [SV-01](07-review/semantic-validation-report.md#cílené-sv-01-až-sv-10) až [SV-14](07-review/semantic-validation-report.md#doplňující-hraniční-případy) |
| [Integrační validace v0.3](07-review/plos-integration-validation-v0.3.md) | E2E-01 až E2E-07, audit použitelnosti a meze ověření |
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

Prefixy: [SN](02-requirements/stakeholder-needs.md) potřeba, [FR](02-requirements/high-level-requirements.md#funkční-požadavky) funkční požadavek, [QR](02-requirements/high-level-requirements.md#požadavky-na-kvalitu) kvalitativní požadavek, [CON](02-requirements/high-level-requirements.md#omezení-návrhu) omezení, [ASM](01-foundations/system-charter.md#předpoklady-a-omezení) předpoklad, [SC](01-foundations/system-charter.md#předběžná-kritéria-úspěchu) kritérium úspěchu, [ST](01-foundations/system-charter.md#stakeholdeři-a-aktéři) aktér, [OP](01-foundations/concept-of-operations.md) provozní režim, [UC](01-foundations/concept-of-operations.md#ilustrativní-scénáře-pro-návrhovou-verifikaci) scénář, [SS](03-architecture/conceptual-architecture.md) subsystém, [IF](03-architecture/conceptual-architecture.md#hlavní-rozhraní-a-toky) rozhraní, [FB](03-architecture/conceptual-architecture.md#zpětnovazební-architektura) zpětnovazební smyčka, [ADR](05-decisions/decision-log.md) rozhodnutí, [H](05-decisions/open-questions.md#návrhové-hypotézy) hypotéza, [OQ](05-decisions/open-questions.md#otevřené-otázky) otázka, [R](05-decisions/open-questions.md#rizika-návrhu) riziko, [DG](04-diagrams/README.md) diagram, [RV](07-review/architecture-review-report-iteration-2.md#domain-model-audit--nálezy-proti-v01-a-vypořádání) nález, [QG](07-review/architecture-review-report-iteration-2.md#architecture-quality-gates) quality gate, [DC](glossary.md#doménové-koncepty) doménový koncept, [DR](03-architecture/preliminary-domain-model.md#katalog-vztahů) doménový vztah, [INV](03-architecture/preliminary-domain-model.md#katalog-invariantů) invariant, [C1–C4](03-architecture/preliminary-domain-model.md#katalog-vztahů) doménová asociace, [SV](07-review/semantic-validation-report.md) sémantický případ. [P1](01-foundations/design-principles.md)–[P11](01-foundations/design-principles.md) jsou původní identifikátory principů. ID se při změně nepřečíslují a nepřidělují znovu jinému významu.

Definice pojmů se mění ve slovníku, význam vztahů v doménovém modelu, normativní znění v požadavcích. Architektura a diagramy jsou navazující pohledy; nesmějí zavádět skryté nové požadavky. Změna musí posoudit dopad na odkazy, odpovědnosti, scénáře a ADR. Aktuální doména má verzi v0.2. Nezměněné funkční pohledy I1 zůstávají baseline; review a handoff I1 jsou výslovně historické. Stav N požadavků se bez schválení nemění.

**Rozsah ověření:** strukturální kontroly souborů a odkazů, ruční sémantická revize a průchody fiktivními scénáři. Nejde o validaci životního přínosu s uživatelem ani o formálně ověřený MBSE model. Podrobnosti uvádějí review report a [integrační validační zpráva](07-review/plos-integration-validation-v0.3.md).

**Stop podmínka:** Doménová baseline v0.2 je uzavřena interní revizí a předáním. Navazující provozní návrh, uživatelská dokumentace a jejich integrační validace vznikly jako v0.3; doménový model zůstává ve verzi v0.2. Empirické ověření přínosu, pilot ani softwarová implementace neproběhly a nejsou doloženy.

Základní orientaci tvoří 12 Core významů v [DOM-01](03-architecture/preliminary-domain-model.md); ani ty neznamenají povinné samostatné záznamy. Klasifikace ostatních konceptů vysvětluje, co je situační, volitelné či odvozené. PLOS musí být vykonatelný člověkem bez jakékoli softwarové implementace, nyní i v budoucnu.
