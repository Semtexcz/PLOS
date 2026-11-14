# Architecture Handoff — Iteration 2

**ID:** HANDOFF-02 • **Verze:** 0.2 • **Datum:** 2026-11-14 • **Předmět:** Domain Architecture & Semantic Model. **Stav:** dokončený návrh po interní sémantické revizi, k revizi vlastníkem; nikoli empiricky validovaná metodika nebo schválená specifikace požadavků N. Baseline v0.1 je commit `0932933`.

## Co se předává

[DOM-01](../03-architecture/preliminary-domain-model.md) je stabilizovaný sémantický základ: katalog 36 konceptů s klasifikací, důvodem a identitou, 40 vztahů s nutností/násobnostmi a 18 invariantů. [GLO-01](../glossary.md) je autoritou definic. [DG-06 až DG-10](../04-diagrams/README.md) zobrazují celkovou doménu a čtyři detailní skupiny. [SEM-01](semantic-validation-report.md) dokládá 22 ručních průchodů: UC-01 až UC-08 a SV-01 až SV-14. [REV-02](architecture-review-report-iteration-2.md) obsahuje audit baseline, vypořádání, dopady na požadavky a quality gates.

Šest funkčních SS, hybridní architektura a hranice člověka vůči metodice zůstávají baseline. PLOS je samostatně člověkem vykonatelná metodika bez předpokladu nynější nebo budoucí softwarové implementace. Evidence je významový podklad, nikoli médium; nemusí být úplná, průběžná ani explicitně zaznamenaná. Nebyla navržena žádná konkrétní provozní forma.

## Přijatá architektonická rozhodnutí a změny proti v0.1

Všechna nová ADR mají stav **D — rozhodnuto pro návrh**, nikoli dodatečné schválení vlastníkem. Alternativy, důvody, dopady a podmínky revize jsou v [decision logu](../05-decisions/decision-log.md).

| Rozhodnutí | Změna a dopad |
| --- | --- |
| ADR-07 | Upřesněn SoI, P9 a CON-01 podle explicitního zadání; ASM-03 je podmíněný potřebou uchování záznamů. Nejde o přechod k softwarové architektuře. |
| ADR-08 | Intended Outcome je obsah záměru, Observed Outcome role původního Observation; výklad patří do Review. Objective, Project, Commitment a Next Action mají oddělenou identitu a přípustné vazby mnoho–mnoho. |
| ADR-09 | Resource Demand pojmenovává rozsah potřeby zdroje bez další identity práce. Pravidla rozlišují souhrn/detail, částečný překryv, alternativy a skutečný konflikt. Planned/Actual Capacity jsou role posouzení dostupnosti, ne spotřeba. |
| ADR-10 | WOOP pokryto významovými rolemi včetně vnitřní/vnější překážky; nevznikají čtyři nové objekty. Experiment nepotřebuje Project podle počtu kroků; rozhoduje samostatná potřeba organizovat práci. |
| ADR-11 | DG-06 nahrazen konceptuálním UML třídním pohledem, doplněny DG-07 až DG-10. Nahrazena pouze notační část ADR-06; ostatní rozhodnutí I1 platí. |

Nejasnosti výsledku, přijetí strategie, nerozhodného experimentu, odmítnutí doporučení, identity rutiny po přerušení, zachování slibu a dvojího započtení jsou vypořádány v DOM-01. Tytéž významy se nekopírují do různých subsystémů. Změna plánu nesmí přepsat skutečnost, změna cíle původní očekávání ani změna strategie platný závazek.

## Nezbytný konceptuální základ a volitelnost

**12 Core významů:** Value, Care Need, Intended Outcome, Commitment, Next Action, Capacity, Resource Demand, Allocation, Plan, Observation, Review a Decision. Jsou nutné k vysvětlení základního rozhodování, omezení a učení, nikoli k založení dvanácti záznamů. Jedno konkrétní použití nemusí mít instanci každého Core konceptu; například volba nic nealokovat nevytváří Allocation a člověk nemusí mít v dané situaci závazek.

**9 Contextual:** Life Area, Strategy, Assumption, Experiment, Objective, Portfolio, Project, Captured Input a Routine. Jsou potřebné podle situace; základní péče nemusí mít strategii, cíl, projekt ani explicitní členění oblastí.

**6 Optional:** Personal Principle, Vision, Scenario, Conditional Response, Metric a Recommendation. Zlepšují některé postupy, nejsou univerzální vstupní podmínkou. Je-li volitelně použit celý WOOP, významy jeho čtyř rolí se přesto musí rozlišit.

**9 Derived bez nové identity:** Observed Outcome, Output, Habit, Planned Capacity, Actual Capacity, Interpretation, Internal Obstacle, External Constraint a WIP. Odvození používá dostupné podklady a lidský úsudek; Actual Capacity nelze odvodit jen z plánu a Interpretation nemusí být jednoznačná. Klasifikace není návrhem formulářů ani evidenčních struktur.

## Otevřené otázky a rizika

[Registr OQ/H/R](../05-decisions/open-questions.md) je aktuální autorita stavů. **OQ-04 a OQ-06 jsou uzavřeny sémanticky**; neuzavírají návrh workflow, stavů a individuální granularity. **OQ-08 je částečně vyřešena** pro doménovou notaci; volba dalších modelů pro I4 zůstává otevřená.

Otevřené zůstávají OQ-01 (kritičnost a minimální rozsah), OQ-02 (kadence/spouštěče), OQ-03 (režie a hloubka trasovatelnosti), OQ-05 (zpoždění, chybějící evidence a příčiny výsledku) a OQ-07 (sdílení/delegace). H-01 až H-05 ani praktická použitelnost nejsou ověřeny. Požadavky N zůstaly N; pouze CON-01 / Z byl upřesněn přímým mandátem zadání I2. Návrhy změn ověřovacích kritérií pro I3 jsou v REV-02.

Hlavní zbylá rizika: režie a tlak na evidenci (R-01/02/10), ztráta známé odpovědnosti při změně či přerušení (R-04), záměna vnějších mezí za vnitřní překážky (R-05), falešné součty při nerozpoznaném překryvu (R-09) a přecenění formálnosti diagramů (R-08). Pravidla modelu pomáhají chybu pojmenovat; nezaručují bezchybné lidské používání.

## Stav quality gates a verifikace

QG-01 až QG-07 jsou splněny v deklarovaném návrhovém rozsahu; každá brána má konkrétní evidence v REV-02. **QG-08 je splněna s technickým omezením:** strukturální a ruční sémantická kontrola dokumentace proběhla, úspěšná parserová a vizuální kontrola renderu diagramů nebyla provedena kvůli omezením lokálního prostředí a nedostupnosti stažení CLI. RV-05 zůstává otevřený. Zdrojové definice jsou součástí dokumentace; není tvrzen formální UML důkaz ani zaručené vykreslení.

Neprovedeny byly empirická validace, praktický pilot, schválení N, workflow, detailní stavové automaty, numerická optimalizace a návrh konkrétní evidence. Toto omezení je součástí předání, nikoli chybějící skrytá implementace.

## Přesný doporučený rozsah Iteration 3

**Cíl:** požadavková specifikace a trasovatelnost nad stabilizovanou doménou; bez opakovaného definování základních pojmů, pokud nevznikne doložený protipříklad.

1. Validovat s vlastníkem SN-01 až SN-11 a jejich skutečný původ/nezbytnost; nezaměnit autorův návrh s potvrzenou potřebou.
2. U každého FR/QR se stavem N rozhodnout přijetí, změnu, odložení či odmítnutí a zaznamenat podklad. Zachovat ID a oddělit normu, návrh, ADR a hypotézu.
3. Zpřesnit ověřovací kritéria podle dopadové tabulky REV-02: význam versus záznam, totožnost, výsledek versus práce, kontinuita závazků, nejistota a kapacitní překryvy. Nové požadavky z invariantů vytvářet pouze s doloženým původem a výslovným schválením, nikoli automaticky.
4. Doplnit obousměrnou trasovatelnost SN/P → FR/QR/CON → SS/IF → DC/DR/INV → UC/SV. Nevyžadovat, aby každý doménový koncept založil nový požadavek.
5. Vymezit na požadavkové úrovni OQ-01 a OQ-03: co má metodika umožnit při nízké kapacitě, jak poznat významné důsledky a co se od ní nesmí vyžadovat. OQ-07 rozhodnout před jakýmkoli sdílením či zapojením třetích osob.
6. Revidovat konzistenci dopadů do ARCH-01, ADR a OQ; pokud je dostupný renderer, uzavřít RV-05 syntaxí a vizuální kontrolou. Nový sémantický protipříklad řešit změnovým návrhem s dopadem, nikoli tichým přejmenováním.

**Vstupy:** DOM-01/GLO-01 v0.2, SEM-01, REV-02, REQ-01 se zachovanými N, ADR-01 až ADR-11 a otevřený registr. **Výstupy:** potvrzené či odmítnuté potřeby/požadavky, rozlišitelná kritéria, aktualizovaná matice, rozhodnutí OQ-01/03/07 v potřebném rozsahu, review a handoff I3. **Výstupní brána:** každý závazný požadavek má původ, schvalovací podklad, vlastníka a ověřovací případ; odmítnuté návrhy jsou dohledatelné a žádná nová norma nevzniká z diagramu.

**Mimo I3:** konkrétní provozní forma, software/UI/databáze, úplné workflow a stavy (I5), pravidla priorit a optimalizace (I6), finální metriky (I7), personalizovaný provoz a pilot (I8). Logické kontrakty se detailně rozpracují v I4. Případné nástroje nejsou předpokládaným cílem metodiky.

**Stop:** Iteration 2 tímto končí. Iteration 3 nebyla zahájena a nezačne bez nového zadání.
