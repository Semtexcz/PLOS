# Design Principles

**Stav:** Z — principy explicitně stanovené zadáním. Následující tabulka je jejich návrhová interpretace, nikoli sada samostatných měřitelných požadavků. Normativní operacionalizace je v [registru požadavků](../02-requirements/high-level-requirements.md).

| ID | Princip | Důsledek pro návrh | Signál porušení |
| --- | --- | --- | --- |
| P1 | Human Agency First | Člověk volí, mění i odmítá doporučení | Doporučení samo vytváří závazek |
| P2 | Values-Driven | Důležité volby mají vysvětlitelný důvod v hodnotách, potřebách nebo závazcích | Jediné skóre nahrazuje důvody |
| P3 | Closed-Loop Control | Pozorování vede k interpretaci a vědomé úpravě na více horizontech | Report bez možnosti změny |
| P4 | Capacity Awareness | Všechny druhy nároků soutěží o tutéž omezenou kapacitu | Nové priority pouze přibývají |
| P5 | Adaptive Planning | Plán je revidovatelná hypotéza | Neaktuální plán je závazný bez ohledu na okolnosti |
| P6 | Separation of Concerns | Oddělit volbu směru, výběr portfolia, alokaci a zpracování závazků | Dva procesy mění tutéž věc bez koordinace |
| P7 | Traceability | Přiměřená návaznost důležitých záměrů; legitimní nestrategická operativa | Rutina potřebuje fiktivní strategický cíl |
| P8 | Minimal Sufficient Complexity | Koncept existuje jen při samostatné rozhodovací hodnotě | Evidence existuje jen kvůli evidenci |
| P9 | Technology Independence | Pojmy a rozhraní mají smysl bez aplikace | Pole nebo API určuje význam konceptu |
| P10 | Graceful Degradation | Omezený režim a návrat bez administrativního dluhu | Nejprve je nutné doplnit všechny záznamy |
| P11 | Observability without Overmeasurement | Pozorování může být slovní, neúplné a volitelné podle rozhodnutí | Počet úkolů je zaměněn za kvalitu života |

Při konfliktu se nejprve vyjasní dotčená potřeba a důsledek. Autonomii nelze převést na váhu v optimalizačním vzorci. Kapacitní limit nelze obejít vyšší prioritou. Nárok na trasovatelnost musí být přiměřený významu rozhodnutí a dostupné kapacitě. Konkrétní pravidla tohoto vyvažování zůstávají návrhovými rozhodnutími ADR-02, ADR-04 a ADR-05.
