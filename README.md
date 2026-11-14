# PLOS — Architecture Foundation, Iteration 1

**Verze:** 0.1 • **Datum:** 2026-11-14 • **Stav:** dokončený návrh první iterace, určený k revizi vlastníkem systému.

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
| [Preliminary Domain Model](03-architecture/preliminary-domain-model.md) | Koncepty a význam vztahů bez implementačního schématu |
| [Diagramy](04-diagrams/README.md) | Šest konceptuálních modelů a zdrojové definice Mermaid |
| [Decision Log](05-decisions/decision-log.md) | Architektonická rozhodnutí s alternativami a důsledky |
| [Open Questions](05-decisions/open-questions.md) | Hypotézy, otázky a rizika |
| [Architecture Roadmap](06-roadmap/architecture-roadmap.md) | Iterace 2–9, závislosti a kritéria dokončení |
| [Architecture Review Report](07-review/architecture-review-report.md) | Quality gates, nálezy a meze ověření |
| [Architecture Handoff](07-review/architecture-handoff.md) | Předání a přesný rozsah další iterace |
| [Glossary](glossary.md) | Autoritativní slovník |

## Pravidla čtení a změn

- **Z — zadáno:** závazek explicitně stanovený uživatelem v kickoff zadání. Neznamená schválení celého nového návrhu.
- **N — navrženo:** odvozená potřeba nebo požadavek k potvrzení. Je podkladem současného návrhu, dosud bez uživatelské validace.
- **D — rozhodnuto pro návrh v0.1:** architektonická volba autora v rámci zadání; vratná a podléhající revizi vlastníkem.
- **H — hypotéza:** tvrzení o vhodnosti nebo účinku návrhu, které vyžaduje ověření.
- **O — otevřeno:** nerozhodnutá otázka. **F — zdrojový princip:** parafráze doloženého frameworku; není důkazem účinnosti PLOS.

Prefixy: SN potřeba, FR funkční požadavek, QR kvalitativní požadavek, CON omezení, ASM předpoklad, SC kritérium úspěchu, OP provozní režim, UC scénář, SS subsystém, IF rozhraní, FB zpětnovazební smyčka, ADR rozhodnutí, H hypotéza, OQ otázka, R riziko, DG diagram, RV nález. P1–P11 jsou původní identifikátory principů. ID se při změně nepřečíslují a nepřidělují znovu jinému významu.

Definice pojmů se mění ve slovníku, význam vztahů v doménovém modelu, normativní znění v požadavcích. Architektura a diagramy jsou navazující pohledy; nesmějí zavádět skryté nové požadavky. Změna musí posoudit dopad na odkazy, odpovědnosti, scénáře a ADR. Dokumenty sdílejí tuto verzi a stav, pokud výslovně neuvádějí jinak.

**Rozsah ověření:** strukturální kontroly souborů a odkazů, ruční sémantická revize a průchody fiktivními scénáři. Nejde o validaci životního přínosu s uživatelem ani o formálně ověřený MBSE model. Podrobnosti uvádí review report.

**Stop podmínka:** Iteration 1 je uzavřena předáním. Žádná další iterace, software, infrastruktura ani výběr aplikací nejsou zahájeny.
