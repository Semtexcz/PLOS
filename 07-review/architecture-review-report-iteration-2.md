# Architecture Review Report — Iteration 2

**ID:** REV-02 • **Verze:** 0.2 • **Datum:** 2026-11-14 • **Typ:** interní self-review autora, nikoli nezávislý audit nebo schválení vlastníkem. **Vstupní baseline:** commit `0932933`, Architecture Foundation v0.1. **Verdikt:** Domain Architecture v0.2 je připravena k předání pro I3; žádný otevřený sémantický Blocking pro rozsah I2. Parserová a vizuální validace diagramů zůstává neprovedena, RV-05.

## Rozsah auditu a autorita artefaktů

Prostudovány byly všechny dokumenty baseline: README, CH-01, CO-01, P1–P11, potřeby SN, REQ-01, ARCH-01, FW-01, DOM-01, GLO-01, ADR-01 až ADR-06, OQ/H/R, ROAD-01, REV-01/HANDOFF-01 a DG-01 až DG-06. Audit nejprve posoudil stávající definice, identitu, vztahy a média; následně byly nálezy řešeny v modelu a znovu porovnány napříč artefakty. Původní report a handoff zůstaly historickými záznamy; změny mají návazné ADR.

Závažnost **Blocking** brání smysluplné návaznosti, **Important** vyžaduje řešení v příslušné fázi, **Improvement** zvyšuje použitelnost bez blokování sémantiky. Závažnost nálezu vůči rozsahu I2 neznamená zpětně nesplnění rozsahu I1.

## Domain Model Audit — nálezy proti v0.1 a vypořádání

RV-01 až RV-06 jsou původní ID, dále se nepřidělují jinému významu. Nové nálezy mají pokračující ID.

| ID / závažnost | Nález a evidence ve v0.1 | Doporučené vypořádání | Stav po interní revizi I2 |
| --- | --- | --- | --- |
| RV-07 / Important | Outcome v GLO-01 a jeden uzel DG-06 nevymezují, co zachovává identitu mezi očekáváním a pozorováním. Hrozí přepis očekávání výsledkem. | Oddělit obsah záměru, původní pozorování a výklad; nevytvářet kopii evidence. | **Vyřešeno:** DC-11/12/27/32, ADR-08, INV-04/05/18; UC-07, SV-09/14. |
| RV-08 / Important | DOM-01 uvádí „může přispívat/naplňovat“, ale neurčuje totožnost a změny Objective–Project–Commitment–Next Action; OQ-04/RV-03. | Rozlišit kontinuitu záměru, práce, odpovědnosti a jednotlivého provedení; připustit mnoho–mnoho a legitimní nepřítomné vazby. | **Vyřešeno:** katalog identity, DR-01 až DR-09, INV-03/06; SV-01/02/06/10/14. |
| RV-09 / Important | „Nárok“ je v GLO-01 neformální; DOM-01 odkládá dvojí započtení projektu a kroků. Portfolio může zdánlivě násobit práci. | Pojmenovat význam rozsahu nároku, rozlišit souhrn, detail a překryv; nepřidávat autonomní pracovní objekt. | **Vyřešeno:** DC-31, DR-29/31/35, ADR-09, INV-14/15; SV-03/10/11. |
| RV-10 / Important | Planned/Actual Capacity existují ve slovníku, ale vztahy k dostupnosti, spotřebě a různým horizontům zůstávají vágní. | Vymezit role časově situovaných posouzení, společné zdroje a pravidla nesrovnatelnosti. | **Vyřešeno:** DC-21 až DC-24, C4, INV-11 až INV-16; SV-08/11/13. |
| RV-11 / Important | DOM-01 odlišuje Routine/Habit, ale nevymezuje výskyt, obnovu po přerušení a vznik „dluhu“. | Zachovat identitu rutiny, oddělit případ jednání a jeho pozorování; péči nepřevést na nekonečný projekt. | **Vyřešeno:** DC-18/19/20, DR-10 až DR-14, INV-07/08; SV-04/07. |
| RV-12 / Important | Strategy/Scenario a Experiment/Project jsou rozlišeny jen rámcově; nejasné hranice přijetí alternativ a potřeby projektu (OQ-06). | Kandidátní strategii odlišit volbou; experiment chápat jako otázku a ohraničení, projekt jako organizaci práce bez početního prahu. | **Vyřešeno:** C3, ADR-10, INV-09/10; UC-01, SV-05/06. |
| RV-13 / Important | Observation v GLO-01 může být „záznam či sdělení“; CH-01 zahrnuje informační záznamy a ASM-03 předpokládá jejich uchování. To je užší než upřesnění SoI v I2. | Oddělit evidenci od média a omezit ASM-03 na potřebu kontinuity explicitních záznamů. | **Vyřešeno minimální změnou:** ADR-07, CH-01, P9, CON-01, DC-27, INV-01. Žádný nový SS. |
| RV-14 / Important | WOOP ve FW-01 je správně omezeno, ale DOM-01 má jen Conditional Response; chybí jednoznačné svázání přání, přínosu a povahy překážky. | Mapovat čtyři role na existující významy a odlišit vnitřní/vnější překážku bez katalogu nových objektů. | **Vyřešeno sémanticky:** C4/WOOP, DC-34/35, ADR-10, SV-12. Úplný proces nebyl posuzován. |
| RV-15 / Improvement | DOM-01 obsahuje mnoho konceptů bez rozlišení nezbytnosti a explicitní evidence; hrozí nadbytečné záznamy. | Klasifikovat všechny významy; odvozené role nepovyšovat na samostatné identity. | **Vyřešeno návrhově:** 36 DC, kategorie a odůvodnění, 12 Core; R-10/H-01 zůstávají praktickým rizikem. |
| RV-16 / Important | Review, poznatek, interpretace a doporučení jsou v ARCH-01 používány, ale poslední dva významy nejsou dostatečně rozlišeny v katalogu; nerozhodnost může působit jako selhání. | Doplnit explicitní rozlišovací pojmy, bez nových povinných objektů; žádná automatická volba. | **Vyřešeno:** DC-32/33, DR-24/25/40, INV-09/10; SV-05, UC-06. |
| RV-17 / Improvement | DG-06 je korektně označený flowchart I1; neumožňuje číst násobnosti a některé pojmy vynechává. Pro přesnost I2 už nestačí. | Změnit notační rozhodnutí explicitním ADR a rozdělit detail do čtyř čitelnějších pohledů. | **Vyřešeno obsahově:** ADR-11, DG-06 až DG-10; rendering zůstává RV-05. |
| RV-18 / Important | Neúplná evidence je dovolena, ale DOM-01 neodlišuje neznámou totožnost, zastaralé posouzení a konfliktní svědectví. | Zavést kvalifikaci poznání a zásady revizí, nikoli automatický stavový model. | **Vyřešeno:** oddíl identity/nejistoty, INV-03/04/11/18; SV-07/13/14. |

Nebyl nalezen důvod rušit hybridní architekturu nebo šest SS. Předběžné diagramy a text v0.1 vykazovaly především odložené nejasnosti, nikoli prokázaný zásadní strukturální rozpor. Změny notace a definic proto nenahrazují ADR-01 až ADR-05.

## Návaznost na požadavky a odpovědnosti

Jedna závazná položka byla upřesněna přímo podle nového explicitního zadání: **CON-01 / Z**, od nezávislosti na konkrétní technologii k absenci předpokladu softwaru vůbec. Původ, důvod a dopad jsou ADR-07 a změnová poznámka REQ-01. Původní historické omezení CON-02 pro I1 nebylo přepsáno na jiný význam. Žádný nový FR/QR není prohlášen za schválený. Následující doplnění kritérií jsou **N — návrhy pro I3**, nikoli závazný text požadavků.

| Dotčená baseline | Dopad domény v0.2 a navržené doplnění kritéria | Odpovědnost / důkaz |
| --- | --- | --- |
| FR-01/08/09, QR-05 | Výslovně rozlišit nezbytný význam od záznamu; péče může být bez pojmenované oblasti, cíle i projektu. | SS-01/03/05; INV-01/07/08, UC-02/04/08, SV-04 |
| FR-02/14 | Doplnit nerozhodný experiment a sémantické mapování všech čtyř rolí WOOP; FR-14 zůstává požadavkem na podmíněnou reakci, nikoli skrytým mandátem celého procesu WOOP. | SS-02/04; SV-05/12, ADR-10 |
| FR-03/04, QR-03 | Doplnit souhrn/detail, sdílenou práci, částečný překryv, alternativy a překrývající se horizonty. Dostupnost se nesmí násobit počtem plánů. | SS-03/04; INV-12 až INV-16, SV-03/08/10/11/13 |
| FR-05/06/10, QR-06 | Doplnit mnoho kroků na jeden závazek, nezávislé sliby pro tutéž práci a kontinuitu při změně strategie. Rozlišit úmysl a skutečný podklad změny vnější povinnosti. | SS-05/03; INV-02/03/06, SV-02/06/14 |
| FR-07/11/12, QR-01/04 | Doplnit role pozorování versus obsah očekávání, revizi interpretace bez přepsání reference a odmítnutí doporučení. | SS-06 + vlastník cílového významu; UC-06/07, SV-09/14 |
| FR-13, QR-05/07 | Doplnit neznámou historii, zachování známých závazků a obnovu rutiny bez automatického dluhu. Reálný minimální rozsah stále vyžaduje OQ-01/03. | SS-04/05/06; SV-07, UC-08 |

SS a IF nedostaly nové funkce. Resource Demand zpřesňuje kapacitní význam SS-04, Interpretation/Recommendation rozlišují již existující výstupy SS-06 a jiných SS. Jediný autoritativní slovník obsahuje definice; DOM-01 drží identitu, DR a INV; diagramy je pouze zobrazují. Výjimka vlastníka Intended Outcome mimo cíle je výslovně uvedena v DOM-01 a ARCH-01.

## Architecture Quality Gates

„Splněno pro I2“ znamená doloženou návrhovou konzistenci v deklarovaném rozsahu. Neznamená empirickou účinnost, potvrzení požadavků N ani formální důkaz úplnosti.

| Gate | Konkrétní evidence a provedená kontrola | Výsledek a meze |
| --- | --- | --- |
| QG-01 — Semantic Consistency | Porovnání všech 36 DC v GLO-01 s katalogem DOM-01, důvody kategorií; řešení RV-07/11/12/14/16. Outcome není zaměnitelný stav jedné položky. | **Splněno pro I2.** Významy mají definici a důvod; přijatelnost terminologie s uživatelem neověřena. |
| QG-02 — Identity Integrity | Katalog I/V/R a pravidla revize/náhrady; DR-01 až DR-09, INV-03 až INV-06/18; SEM-01: SV-01/02/06/09/14. | **Splněno pro I2.** Nejistou totožnost lze přiznat; žádné technické ID nebo úplný archiv se nevyžadují. |
| QG-03 — Relationship Integrity | Ruční porovnání asociací DG-06 až DG-10 s DR-01 až DR-40, konců násobností a povinných podmínek. Experiment má otázku NEBO předpoklad; nejde o povinnou vazbu 1 na Assumption. | **Splněno sémanticky.** Parser/render není tímto gate tvrzen; limit v QG-08. |
| QG-04 — Capacity Integrity | C4, DR-29 až DR-35, INV-11 až INV-16; konkrétní průchody SV-03/08/10/11/13. Souhrn, částečný překryv a skutečný konflikt se chovají odlišně. | **Splněno pro I2.** Pravidla dovolují rozpoznat problém, nezaručují lidskou detekci ani optimální řešení. |
| QG-05 — Human Executability | CH-01/P9/CON-01 a INV-01; všechny UC/SV vysvětleny bez úložiště, API, agenta či automatického výpočtu. Review může být lidská úvaha a evidence paměť. | **Splněno konceptuálně.** Žádná praktická provozní forma, uživatelský test ani pilot nebyly provedeny. |
| QG-06 — Minimum Sufficient Complexity | Klasifikace 12 Core / 9 Contextual / 6 Optional / 9 Derived; každé DC má důvod. Resource Demand nemá autonomní identitu práce; role výsledku, kapacity a překážek nevytvářejí nové záznamy. | **Splněno návrhově.** Skutečná režie a srozumitelnost zůstávají H-01/OQ-03/R-10. |
| QG-07 — Scenario Coverage | SEM-01 obsahuje 8 UC a 14 SV, vždy konkrétní vztahy, INV, očekávání, protipříklad, výsledek a otevřenost. Všech 18 INV je uplatněno alespoň jednou. | **Splněno.** 22 ručních sémantických průchodů; nejde o empirickou validaci. |
| QG-08 — Documentation Integrity | Kontrola relativních odkazů/kotev, tabulek, zdrojových bloků, unikátních definic a odkazovaných DC/DR/INV/SV; ruční revize README, ADR, OQ, roadmapy a historických verzí. | **Splněno s omezením:** zdrojová a sémantická konzistence zkontrolována, úspěšná parserová a vizuální kontrola renderu **neprovedena**, RV-05. |

## Technická verifikace dokumentace a její omezení

Provedena lokální jednorázová strukturální kontrola Markdown (nikoli implementace PLOS): relativní odkazy včetně kotev, uzavření bloků, šířky tabulek, identifikátory konceptů/vztahů/invariantů/scénářů, shoda asociací a násobností s katalogem. Výsledky závěrečného běhu jsou uvedeny níže. Kontrolní skript pracuje pouze se soubory dokumentace; katalog `/mnt/Data/automation/agent-tools/README.md` neobsahoval podobný nástroj.

**Diagramy:** porovnána ručně notace asociací/násobností s dokumentací Mermaid. Dostupný lokální bundle se v Node nepodařilo inicializovat pro úspěšné parsování kvůli DOM API (`addHook is not a function`). Firefox nelze spustit v omezeném prostředí (user namespaces: `EPERM`, snap vyžaduje zápis mimo workspace); získání CLI z npm selhalo na DNS `EAI_AGAIN`. Úspěšný průchod parserem a kontrola vykreslených diagramů proto nebyly provedeny. Není tvrzena ani úplná validace UML metamodelu; použitá podmnožina má výslovnou legendu a textové invarianty. Omezení je přijatelné pro sémantické předání s čitelnými zdroji, neznamená uzavření RV-05.

**Neprovedeno:** empirická validace, rozhovory s vlastníkem/stakeholdery, potvrzení N, pilot, numerická optimalizace, simulace, detailní workflow/stavy, konkrétní evidence či provozní návrh. H-01 až H-05 zůstávají hypotézami.

## Dispozice původních nálezů a zbývající rizika

| Původní ID | Stav po I2 |
| --- | --- |
| RV-01 | Zůstává uzavřen; vlastník Project je SS-05, výběr v SS-03. |
| RV-02 | Otevřen: schválení potřeb/požadavků N je I3. |
| RV-03 | **Uzavřen sémanticky:** ADR-08/09, OQ-04, katalog identity a invarianty, SV-01/02/03/06/10/14. |
| RV-04 | Otevřen: únosnost režie a minimálního režimu, OQ-01/03, H-01/H-04. |
| RV-05 | **Otevřen:** úspěšná parserová a vizuální validace Mermaid neprovedena; neblokuje sémantický rozsah I2, musí být znovu prověřena při dostupném rendereru. |
| RV-06 | Otevřen: sdílení a delegace, OQ-07 v I3 před zapojením třetích osob. |

OQ-04/06 uzavřeny pro konceptuální rozsah, OQ-08 částečně vyřešena pro doménovou notaci. OQ-01/02/03/05/07 a všechny H zůstávají otevřené. R-09 připomíná nedokonalé lidské rozpoznání překryvu, R-10 riziko převzetí katalogu jako povinné evidence. Žádný otevřený sémantický Blocking; stav celého PLOS není „hotovo“.

## Závěrečná strukturální kontrola

Závěrečný běh lokální strukturální kontroly nad kompletní sadou včetně tohoto reportu a handoffu: **29 Markdown dokumentů, 108 relativních odkazů včetně kotev, 10 Mermaid bloků; bez nálezů.** Ověřeno 36 jedinečných definic DC, 40 DR, 18 INV, 14 SV a pokrytí 22 scénářů. Klasifikace odpovídá 12 Core / 9 Contextual / 6 Optional / 9 Derived. Všech 67 zobrazených asociací v pěti doménových pohledech má odpovídající DR, přípustné konce a shodné násobnosti. Kontrola `git diff --check` prošla bez nálezů.

Kontrolní příkaz: `python3 tools/check_docs.py` (pomocný skript pro kontrolu dokumentace v repozitáři, není součástí metodiky; volitelně `--json PATH`). Kontroluje strukturu a deklarované asociace, **ne gramatiku Mermaid, render nebo UML metamodel**. Ruční sémantická revize navíc posoudila příklady/protipříklady SEM-01, změny ADR, stavy OQ a historické artefakty. Autoritativní předání je [HANDOFF-02](architecture-handoff-iteration-2.md).
