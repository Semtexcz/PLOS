# Open Questions, Hypotheses & Risks

**Stav:** registr v0.2 po Iteration 2 (2026-11-14). OQ-04/06 jsou uzavřeny pro sémantický rozsah, OQ-08 částečně vyřešena. Žádná položka neblokuje konceptuální předání I2; položky Important však omezují závěry a musí být řešeny před příslušnou další branou. Předpoklady [ASM-01](../01-foundations/system-charter.md#předpoklady-a-omezení) až [ASM-05](../01-foundations/system-charter.md#předpoklady-a-omezení) jsou v [charteru](../01-foundations/system-charter.md).

## Návrhové hypotézy

| ID | Hypotéza, nikoli fakt nebo požadavek | Jak ji zkoumat | Kdy / vlastník rozhodnutí |
| --- | --- | --- | --- |
| H-01 | Šest funkčních odpovědností umožní srozumitelnost bez nepřijatelné režie | Případy s minimálním záznamem, hledání duplicit; následně kvalitativní pilot | I2 a I8; [ST-05](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) a [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| H-02 | Hrubý vícezdrojový obraz kapacity stačí pro užitečné rozhodování o konfliktech | Srovnat rozhodnutí při neznámé energii, proměnlivém času a omezených financích; sledovat, co zůstalo skryté | I6–I8; [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| H-03 | Pravidelný rámec doplněný událostní revizí ochrání směr lépe než pouze reaktivní volby | Zkoumat případy vytlačení strategie i přehnaného přeplánování | I5 a I8; [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| H-04 | Omezený režim bez doplňování minulosti usnadní návrat | Scénář po přerušení, poté dobrovolný pilot s hodnocením režie a přehlédnutých povinností | I5 a I8; [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| H-05 | Kvalitativní review přinese užitečné rozhodnutí i bez povinných skóre | Případy aktivity bez výsledku a neúplné evidence; hledat situace, kdy měření chybí | I7 a I8; [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |

## Otevřené otázky

| ID / závažnost | Co je nutné rozhodnout | Stav a zacházení po I2 | Cílová iterace / kdo |
| --- | --- | --- | --- |
| OQ-01 / Important | Co je kritická povinnost a minimální rozsah omezeného režimu? | Význam určuje člověk podle skutečných důsledků; žádný univerzální seznam | I3 a I5; [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři), návrh [ST-05](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| OQ-02 / Important | Jak volit kadenci a spouštěče mimořádné revize bez nestability? | Pravidelný rámec i událostní vstup, bez číselných prahů | I5; [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| OQ-03 / Important | Jaká režie a hloubka trasovatelnosti je pro uživatele přijatelná? | Zaznamenávat významné volby přiměřeně kapacitě; hranice významnosti zatím neurčena | I3, validace I8; [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| OQ-04 / Important | Jak přesně rozlišit identitu cíle, projektu, závazku a jejich změny? | **Uzavřeno sémanticky v I2, 2026-11-14:** [DOM-01](../03-architecture/preliminary-domain-model.md) katalog identity a změny, [DR-01](../03-architecture/preliminary-domain-model.md#katalog-vztahů) až [DR-09](../03-architecture/preliminary-domain-model.md#katalog-vztahů), [INV-03](../03-architecture/preliminary-domain-model.md#katalog-invariantů) až [INV-06](../03-architecture/preliminary-domain-model.md#katalog-invariantů)/18; [ADR-08](decision-log.md#adr-08--oddělené-významy-výsledku-práce-a-odpovědnosti). [SEM-01](../07-review/semantic-validation-report.md): [SV-01](../07-review/semantic-validation-report.md#cílené-sv-01-až-sv-10)/02/06/09/14. Detailní stavy nejsou součástí této odpovědi. | I2 dokončeno; [ST-05](../01-foundations/system-charter.md#stakeholdeři-a-aktéři). Navazující stavy I5, přijatelná hloubka OQ-03. |
| OQ-05 / Important | Jak vyhodnotit výsledek se zpožděním, chybějící evidencí a vnějšími vlivy? | Připustit „neznámé“ a neslibovat kauzální závěr | I7; [ST-05](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) a [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| OQ-06 / Improvement | Kdy postačí Next Action pro experiment a kdy je užitečný Project? | **Uzavřeno sémanticky v I2, 2026-11-14:** Experiment nese otázku a mez ukončení; jeden či více přímých kroků nepotřebují Project. Ten má smysl při samostatné potřebě koordinovat rozsah, závislosti a dokončení práce. Žádný početní práh. [ADR-10](decision-log.md#adr-10--woop-pomocí-významových-rolí-a-experiment-bez-povinného-projektu), [DR-20](../03-architecture/preliminary-domain-model.md#katalog-vztahů)/21, [UC-01](../01-foundations/concept-of-operations.md#ilustrativní-scénáře-pro-návrhovou-verifikaci) a [SV-05](../07-review/semantic-validation-report.md#cílené-sv-01-až-sv-10). | I2 dokončeno; [ST-05](../01-foundations/system-charter.md#stakeholdeři-a-aktéři). Individuální únosnost rozkladu OQ-03, nikoli chybějící identita. |
| OQ-07 / Important | Jak omezit sdílení, delegaci a přístup podpůrných osob? | Žádná výchozí přístupová oprávnění; explicitní dohoda mimo tuto iteraci | I3 před jakýmkoli zapojením třetích osob; [ST-01](../01-foundations/system-charter.md#stakeholdeři-a-aktéři) |
| OQ-08 / Improvement | Kdy je vhodná přesnější modelovací notace než Mermaid? | **Částečně vyřešeno:** I2 používá podmnožinu UML tříd/asociací v Mermaid, [ADR-11](decision-log.md#adr-11--konceptuální-uml-pohledy-s-explicitní-sémantikou). Jazyk notace je odlišen od textového nástroje. Potřeba jiné notace pro kontrakty I4 dosud neposouzena. | I4; [ST-05](../01-foundations/system-charter.md#stakeholdeři-a-aktéři). Není uzavřena globální volba notací. |

## Rizika návrhu

Závažnost je kvalitativní odhad autora. Nejde o statistické pravděpodobnosti ani definitivní analýzu rizik.

| ID / závažnost | Riziko a signál | Navržené omezení dopadu | Zbylé riziko / vazba |
| --- | --- | --- | --- |
| R-01 / Important | Metodika spotřebuje více kapacity než poskytne; evidence se hromadí | Společné review, volitelné metriky a omezený režim | Přijatelnou režii ověří až uživatel; H-01, OQ-03 |
| R-02 / Important | Falešná přesnost nebo sebeobviňování podle čísel | Oddělit aktivitu a výsledek, nepoužít skóre osoby | I kvalitativní pravidlo může vytvářet tlak; H-05 |
| R-03 / Important | Operativa trvale vytlačuje směr | Viditelný dopad na portfolio a taktické review | Vnější okolnosti skutečně mohou znemožnit strategii; neslibovat řešení každého konfliktu |
| R-04 / Important | Změna směru skryje platný závazek | Samostatný význam závazků a rozlišení návrhu/potvrzení přejednání ([INV-06](../03-architecture/preliminary-domain-model.md#katalog-invariantů)) | Neúplná původní evidence může něco vynechat; [FR-10](../02-requirements/high-level-requirements.md#funkční-požadavky), [QR-06](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu) |
| R-05 / Important | Nedostatek zdrojů se interpretuje jako vnitřní překážka či nedostatek vůle | Oddělit WOOP od posouzení vnějších omezení | Posouzení zůstává subjektivní; [FR-14](../02-requirements/high-level-requirements.md#funkční-požadavky), [QR-03](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu) |
| R-06 / Important | Příliš časté změny plánu zničí kontinuitu nebo rigidní rytmus brání adaptaci | Více horizontů, vědomá volba okamžité versus pozdější revize | Chybí ověřené spouštěče; OQ-02 |
| R-07 / Important | Osobní záznamy nebo role podpory omezí soukromí a autonomii | Žádná automatická oprávnění; minimalizovat sdílený obsah | Podrobné požadavky zatím nejsou definovány; OQ-07 |
| R-08 / Improvement | Čtenář zamění konceptuální diagram za formální model nebo integraci za ověřenou intervenci | Výslovné limity notace, zdroje a stavy F/D/H | Vyžaduje důslednost při dalších revizích; [ADR-06](decision-log.md#adr-06--lehký-konceptuální-model-a-textové-diagramy) |

Řešení otevřené otázky může změnit ADR i požadavky N. Nová norma se zapíše s důvodem a vazbou na potřebu, nesmí vzniknout pouze přejmenováním hypotézy.

## Dopad Iteration 2

OQ-01/02/03/05/07 zůstávají otevřené. OQ-05 získala rozlišení Intended Outcome, Observation a Interpretation, nikoli metodu kauzálního vyhodnocení. H-01 až H-05 zůstávají neověřené: návrhové průchody nejsou pilot. OQ-04/06 lze znovu otevřít konkrétním protipříkladem proti [DOM-01](../03-architecture/preliminary-domain-model.md); nesmí se tím potichu změnit autoritativní definice.

| ID / závažnost | Nově zpřesněné riziko | Omezení dopadu | Co zůstává nejisté |
| --- | --- | --- | --- |
| R-09 / Important | Člověk nerozpozná totožnost nebo částečný překryv práce a uvede falešně přesný součet | [INV-03](../03-architecture/preliminary-domain-model.md#katalog-invariantů)/14/15, [SV-03](../07-review/semantic-validation-report.md#cílené-sv-01-až-sv-10)/10/11/14; neznámý překryv zůstane neznámý | Sémantická pravidla nezaručují spolehlivé lidské rozpoznání; H-02, I6/I8 |
| R-10 / Important | Katalog konceptů bude mylně převzat jako povinný katalog evidence | Klasifikace 12 Core / 9 Contextual / 6 Optional / 9 Derived; [INV-01](../03-architecture/preliminary-domain-model.md#katalog-invariantů); žádná povinná samostatná evidence | Srozumitelnost a únosnost se musí ověřit s vlastníkem, OQ-03/H-01 |

Stávající R-01 až R-08 nezanikají; R-04/05/08 mají přesnější sémantická opatření, nikoli prokázané odstranění rizika.
