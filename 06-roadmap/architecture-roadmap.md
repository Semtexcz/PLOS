# Architecture Roadmap

**ID:** ROAD-01 • **Stav:** doporučený postup, nikoli automatické zahájení dalších iterací. Iteration 1 vytváří výchozí návrh v0.1. Každá další iterace uzavírá soubor konkrétních otázek, promítá změny do návazných artefaktů a končí revizí. Zjištěný rozpor může vrátit návrh do předchozího kroku; číslování není nevratný vodopád.

## Přehled iterací

| Iterace / cíl | Předpoklady a závislosti | Očekávané výstupy | Kritérium dokončení |
| --- | --- | --- | --- |
| **I2 — Detailní doménové modelování**: zpřesnit význam a identitu konceptů | Přezkoumané DOM-01, GLO-01, ADR-02/06 a UC-01 až UC-08; případné výhrady vlastníka zaznamenány | Doménový model v0.2, vztahy a jejich odůvodnění, přiměřené kardinality a invarianty, příklady a protipříklady, aktualizovaný slovník a ADR | UC lze vyjádřit bez falešného cíle pro rutinu, záměny slibu s krokem a dvojího započtení nároků; OQ-04 rozhodnuta, OQ-06 vyřešena nebo jasně ohraničena; žádný nevyřešený sémantický Blocking |
| **I3 — Požadavková specifikace a trasovatelnost**: potvrdit skutečné potřeby a normativní rozsah | I2; dostupnost vlastníka pro validaci potřeb, dosud neověřené SN a N | Revidované potřeby, rozhodnutí o přijetí/změně/odložení požadavků N, úplnější obousměrná matice, ověřovací případy, omezení sdílení a minimálního režimu | Každý závazný požadavek má původ, vlastníka a rozlišitelné kritérium; odmítnuté návrhy zůstávají dohledatelné; OQ-01/03 mají pracovní vymezení a OQ-07 pravidla před zapojením třetích osob |
| **I4 — Logická architektura a rozhraní**: specifikovat odpovědnosti a kontrakty předávání | I2 a I3; ARCH-01, IF-01 až IF-12 | Architektura v0.2, význam a platnost vstupů/výstupů, odpovědnost za aktualizaci, pravidla nekonzistentních a chybějících podkladů, nové pohledy dle potřeby | Každý požadavek má alokaci; každý význam má jednoho vlastníka; konflikty a chybějící informace mají adresáta; OQ-08 rozhodnuta bez předčasné volby runtime technologie |
| **I5 — Workflow a stavové modely**: vyjádřit běžný i omezený provoz a přerušení | I3 a I4; OP-01 až OP-07 | Vybrané workflow, přechody závazku a záměru, návrat po přerušení, spouštěče review, výjimky a odpovědnosti | UC-01 až UC-08 mají průchod, podmínky zastavení a obnovy; čekání není splnění; změna plánu nemaže povinnost; OQ-01/02 rozpracovány do ověřitelných pravidel |
| **I6 — Rozhodovací a plánovací pravidla**: navrhnout transparentní pomoc při výběru | I2–I5; popis skutečných konfliktů a nejistot, H-02 | Porovnání heuristik, vysvětlitelné pravidlo výběru/odkladu, nakládání s WIP, kapacitními konflikty a rezervou, slovní či matematické modely jen s oporou | Pravidla respektují P1/P4/P5, umějí vrátit „neřešitelný konflikt“, dovolují override a nesčítají nesrovnatelné zdroje; žádná heuristika není označena za vědecký zákon |
| **I7 — Zpětná vazba a pozorování**: určit minimální evidenci pro rozhodnutí | I3–I6; FB-01 až FB-04 a H-05 | Pozorovací otázky, případné kandidátní metriky, zacházení se zpožděním a nejistotou, plán review a ochrana před nadměrným měřením | Každá metrika má rozhodovací účel a podmínku vypnutí; aktivita není zaměněna s výsledkem; OQ-05 má pracovní řešení; kvalitativní review zůstává možné |
| **I8 — Verifikace a validace**: ověřit shodu návrhu a přínos použití | Konzistentní I2–I7; předem dohodnutý rozsah dobrovolného pilotu a zacházení se soukromými údaji | Scénářové verifikace, ověření uživatelských potřeb, pilot metodiky bez nutné aplikace, zjištění k H-01 až H-05, seznam změn a zbylých rizik | Všechny závazné požadavky mají výsledek a důkaz nebo odůvodněné omezení; uživatel posoudí SC-01 až SC-06; žádný Blocking zůstává otevřený; neprokázaný přínos se přizná |
| **I9 — Konsolidace reference**: vydat udržovatelnou výchozí architekturu | Zapracované nálezy I8 a rozhodnutí o zbylých rizicích | Jednotná dokumentace, stabilizovaný slovník, konzistentní diagramy, matice, ADR, historie změn a pravidla budoucí správy | Stejná definice ve všech pohledech, funkční odkazy, oddělení normy/hypotéz, explicitní limity a akceptace vlastníkem; implementace zůstává samostatným budoucím zadáním |

## Přesný doporučený rozsah Iteration 2

Vstupem je stávající sada I1 a připomínky k ní. Cílem není rozšířit počet modulů, ale odstranit sémantické nejasnosti, které by se později proměnily v rozporné procesy.

1. Zpřesnit **Objective–Outcome–Project–Commitment–Next Action**: identitu, přípustné vztahy, změnu cíle při trvání slibu a případ jednoho kroku bez projektu.
2. Zpřesnit **Life Area–Care Need–Routine–Habit**: opakovanou péči, konkrétní výskyt, rozdíl rutiny a návyku, péči bez cíle změny.
3. Zpřesnit **Strategy–Scenario–Assumption–Experiment–Observation–Decision**: co je předpoklad, co poznatek a co volba, včetně nerozhodného výsledku experimentu.
4. Zpřesnit **Capacity–Allocation–Plan**: společný horizont a zdroj, odhad versus skutečná dostupnost versus spotřeba, neznámé a prevence dvojího započtení projektu a jeho kroků.
5. U každé skupiny určit pouze nutné vztahy, příklady/protipříklady, případné kardinality a sémantické invarianty. Evidovat důvody existence nebo sloučení konceptů; nepředepisovat fyzické uložení.
6. Provést průchody UC-01 až UC-08 na úrovni pojmů. Změny promítnout do GLO-01, DOM-01, DG-06 a dotčených ADR; dopady na požadavky uvést jako návrhy pro I3.

**Výstupní sada I2:** aktualizovaný slovník a doménový model, revidovaný DG-06, katalog ilustračních případů a protipříkladů, rozhodnutí o OQ-04/06, záznam změn a krátký review/handoff. Měřítkem dostatečnosti je odstranění nejasností v uvedených případech, nikoli počet diagramů.

**Mimo I2:** software a aplikace, databázové schéma, UI, kompletní workflow a stavové automaty, algoritmus priorit, konečné metriky, číselné WIP limity, předepsaná časová rezerva, plošná personalizace nebo zahájení pilotu. Tyto práce mají vlastní závislosti výše.

Samotné předání I1 nedává pokyn I2 spustit. Další iterace začne až novým zadáním uživatele.
