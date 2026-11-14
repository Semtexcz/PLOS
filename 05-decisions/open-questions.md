# Open Questions, Hypotheses & Risks

**Stav:** otevřený registr v0.1. Žádná položka neblokuje konceptuální předání I1; položky Important však omezují závěry a musí být řešeny před příslušnou další branou. Předpoklady ASM-01 až ASM-05 jsou v [charteru](../01-foundations/system-charter.md).

## Návrhové hypotézy

| ID | Hypotéza, nikoli fakt nebo požadavek | Jak ji zkoumat | Kdy / vlastník rozhodnutí |
| --- | --- | --- | --- |
| H-01 | Šest funkčních odpovědností umožní srozumitelnost bez nepřijatelné režie | Případy s minimálním záznamem, hledání duplicit; následně kvalitativní pilot | I2 a I8; ST-05 a ST-01 |
| H-02 | Hrubý vícezdrojový obraz kapacity stačí pro užitečné rozhodování o konfliktech | Srovnat rozhodnutí při neznámé energii, proměnlivém času a omezených financích; sledovat, co zůstalo skryté | I6–I8; ST-01 |
| H-03 | Pravidelný rámec doplněný událostní revizí ochrání směr lépe než pouze reaktivní volby | Zkoumat případy vytlačení strategie i přehnaného přeplánování | I5 a I8; ST-01 |
| H-04 | Omezený režim bez doplňování minulosti usnadní návrat | Scénář po přerušení, poté dobrovolný pilot s hodnocením režie a přehlédnutých povinností | I5 a I8; ST-01 |
| H-05 | Kvalitativní review přinese užitečné rozhodnutí i bez povinných skóre | Případy aktivity bez výsledku a neúplné evidence; hledat situace, kdy měření chybí | I7 a I8; ST-01 |

## Otevřené otázky

| ID / závažnost | Co je nutné rozhodnout | Dočasné zacházení v I1 | Cílová iterace / kdo |
| --- | --- | --- | --- |
| OQ-01 / Important | Co je kritická povinnost a minimální rozsah omezeného režimu? | Význam určuje člověk podle skutečných důsledků; žádný univerzální seznam | I3 a I5; ST-01, návrh ST-05 |
| OQ-02 / Important | Jak volit kadenci a spouštěče mimořádné revize bez nestability? | Pravidelný rámec i událostní vstup, bez číselných prahů | I5; ST-01 |
| OQ-03 / Important | Jaká režie a hloubka trasovatelnosti je pro uživatele přijatelná? | Zaznamenávat významné volby přiměřeně kapacitě; hranice významnosti zatím neurčena | I3, validace I8; ST-01 |
| OQ-04 / Important | Jak přesně rozlišit identitu cíle, projektu, závazku a jejich změny? | Rozlišení významu v DOM-01; žádné kardinality ani duplicitní entity pro každý pohled | I2; ST-05 |
| OQ-05 / Important | Jak vyhodnotit výsledek se zpožděním, chybějící evidencí a vnějšími vlivy? | Připustit „neznámé“ a neslibovat kauzální závěr | I7; ST-05 a ST-01 |
| OQ-06 / Improvement | Kdy postačí Next Action pro experiment a kdy je užitečný Project? | Volba podle složitosti koordinace; bez prahu počtu kroků | I2; ST-05 |
| OQ-07 / Important | Jak omezit sdílení, delegaci a přístup podpůrných osob? | Žádná výchozí přístupová oprávnění; explicitní dohoda mimo tuto iteraci | I3 před jakýmkoli zapojením třetích osob; ST-01 |
| OQ-08 / Improvement | Kdy je vhodná přesnější modelovací notace než Mermaid? | Konceptuální grafy s vysvětlenou sémantikou | I4; ST-05 |

## Rizika návrhu

Závažnost je kvalitativní odhad autora. Nejde o statistické pravděpodobnosti ani definitivní analýzu rizik.

| ID / závažnost | Riziko a signál | Navržené omezení dopadu | Zbylé riziko / vazba |
| --- | --- | --- | --- |
| R-01 / Important | Metodika spotřebuje více kapacity než poskytne; evidence se hromadí | Společné review, volitelné metriky a omezený režim | Přijatelnou režii ověří až uživatel; H-01, OQ-03 |
| R-02 / Important | Falešná přesnost nebo sebeobviňování podle čísel | Oddělit aktivitu a výsledek, nepoužít skóre osoby | I kvalitativní pravidlo může vytvářet tlak; H-05 |
| R-03 / Important | Operativa trvale vytlačuje směr | Viditelný dopad na portfolio a taktické review | Vnější okolnosti skutečně mohou znemožnit strategii; neslibovat řešení každého konfliktu |
| R-04 / Important | Změna směru skryje platný závazek | Samostatná evidence závazků a potvrzení přejednání | Neúplná původní evidence může něco vynechat; FR-10, QR-06 |
| R-05 / Important | Nedostatek zdrojů se interpretuje jako vnitřní překážka či nedostatek vůle | Oddělit WOOP od posouzení vnějších omezení | Posouzení zůstává subjektivní; FR-14, QR-03 |
| R-06 / Important | Příliš časté změny plánu zničí kontinuitu nebo rigidní rytmus brání adaptaci | Více horizontů, vědomá volba okamžité versus pozdější revize | Chybí ověřené spouštěče; OQ-02 |
| R-07 / Important | Osobní záznamy nebo role podpory omezí soukromí a autonomii | Žádná automatická oprávnění; minimalizovat sdílený obsah | Podrobné požadavky zatím nejsou definovány; OQ-07 |
| R-08 / Improvement | Čtenář zamění konceptuální diagram za formální model nebo integraci za ověřenou intervenci | Výslovné limity notace, zdroje a stavy F/D/H | Vyžaduje důslednost při dalších revizích; ADR-06 |

Řešení otevřené otázky může změnit ADR i požadavky N. Nová norma se zapíše s důvodem a vazbou na potřebu, nesmí vzniknout pouze přejmenováním hypotézy.
