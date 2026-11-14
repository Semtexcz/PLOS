# Integrační validační zpráva PLOS v0.3

**Typ:** integrační validační zpráva • **Datum:** 2026-11-14 • **Rozsah:** Iteration 3C.3 • **Stav:** návrhová verifikace, scénářová validace a expertní audit použitelnosti; nikoli empirické ověření.

## 1. Rozsah a meze ověření

Ověřoval jsem uživatelskou dokumentaci v [docs](../docs/README.md), všechny how-to a reference, oba tutorialy a pro sémantickou kontrolu [GLO-01](../glossary.md), [DOM-01](../03-architecture/preliminary-domain-model.md), [ARCH-01](../03-architecture/conceptual-architecture.md), [CO-01](../01-foundations/concept-of-operations.md), [REQ-01](../02-requirements/high-level-requirements.md) a [registr otevřených otázek](../05-decisions/open-questions.md). Historické revizní zprávy jsem nepoužíval jako zdroj současného provozního postupu.

| Vrstva | Co bylo provedeno | Co to dokládá | Co to nedokládá |
| --- | --- | --- | --- |
| Verification | Kontrola pojmů, invariantů, odkazů a vzájemné shody dokumentů | Návrh neodporuje vlastním pravidlům v ověřeném rozsahu | Že je metodika srozumitelná nebo užitečná v životě |
| Scenario Validation | Jeden souvislý průchod E2E-01 a šest hraničních průchodů E2E-02 až E2E-07 | Že lze situace popsat a rozhodnout v navržených krocích | Že tak bude postupovat skutečný člověk |
| Usability Review | Expertní kontrola jazyka, navigace, režie a diagramů | Pravděpodobná místa zvýšené zátěže a nejasnosti | Skutečnou kognitivní zátěž, míru porozumění a přínos |
| Empirical Validation | Neprovedeno | — | Zda PLOS pomáhá člověku v běžném životě |

Simulovaný průchod není empiricky validované použití. Nejde o uživatelský test, pilot ani důkaz přínosu. Časové odhady v této zprávě jsou hypotézy, nikoli naměřená data.

Renderer Mermaid nebyl v prostředí dostupný (`mmdc` chybí). Diagramy jsem proto zkontroloval pouze strukturálně: počet uzlů, popisky, větve a shodu s textem. Vykreslení nebylo ověřeno. Nové balíčky jsem neinstaloval.

## 2. Výsledek E2E-01

Fiktivní člověk má hodnoty autonomie, rodiny, tvořivosti a zdraví; dlouhodobě chce budovat samostatnou odbornou činnost; je zaměstnaný, má rodinné povinnosti, omezenou energii, tři rozpracované projekty a zvažuje strategickou alternativu s neznámou pravděpodobností úspěchu. Následující průchod sleduje pouze rozhodnutí nutná pro ověření integrace.

Průchod záměrně pokrývá všech šest odpovědností: [SS-01](../03-architecture/conceptual-architecture.md#ss-01--values--vision-management) a [SS-02](../03-architecture/conceptual-architecture.md#ss-02--strategy--experimentation) ve fázi A, [SS-03](../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management) v A a B, [SS-04](../03-architecture/conceptual-architecture.md#ss-04--planning--capacity-management) v B a D, [SS-05](../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management) v C, D a E a [SS-06](../03-architecture/conceptual-architecture.md#ss-06--review--adaptation) ve fázi F.

| Fáze | Uživatelský dokument | Rozhodnutí člověka | Významový výstup | Invarianty | Přechod do další fáze |
| --- | --- | --- | --- | --- | --- |
| A — Strategie | [Od hodnot k jednání](../docs/tutorials/from-values-to-action.md), kroky 1–4; [Strategická návaznost](../docs/reference/strategic-bridge.md); [Zpracování nového podnětu](../docs/how-to/process-input.md), odstavec o strategické možnosti | Zvolit cestu nebo experiment s otázkou a mezí ukončení; určit střednědobý výsledek; rozhodnout, zda je kandidátem portfolia | Zvolená cesta s předpoklady; jeden zamýšlený výsledek se způsobem posouzení; kandidát, nikoli alokace | INV-02, INV-05, INV-09, INV-10 | Ano, ale vstup do portfolia nemá samostatný postup (VAL-03). |
| B — Týdenní plán | [Týdenní plánování](../docs/how-to/weekly-planning.md), kroky 1–6; [Denní rozhodování](../docs/how-to/daily-review.md) | Rozpoznat závazky, potřeby péče a kapacitu; zvolit priority; ověřit alokaci; určit další kroky | Seznam platných závazků; jedna až dvě priority; alokace nebo pojmenovaný konflikt; další kroky; rezerva | INV-02, INV-06, INV-11, INV-12, INV-13, INV-16 | Ano, ale potřeby péče nejsou uvedeny mezi vstupy (VAL-04) a krok 4 je jazykově náročný (VAL-01). |
| C — Nová událost | [Zpracování nového podnětu](../docs/how-to/process-input.md), kroky 1–7 | Vyjasnit, zda jde o informaci, odmítnutí, odklad, přijetí odpovědnosti nebo dobrovolné jednání | Vyjasněný podnět; případný závazek s předmětem, původem a podmínkou; žádný automatický závazek | INV-02, INV-03, INV-07, INV-11, INV-12 | Ano. |
| D — Konflikt kapacity | [Denní rozhodování](../docs/how-to/daily-review.md), krok 3; [Týdenní plánování](../docs/how-to/weekly-planning.md), část „Když to nefunguje“; [Řízení rozpracované práce](../docs/how-to/manage-workflow.md), krok 3 | Zmenšit rozsah, odložit, přejednat nebo přiznat konflikt; zachovat existující závazky | Změněný výběr nebo alokace; pojmenovaný konflikt; závazky trvají | INV-06, INV-11, INV-12, INV-16 | Ano, ale týdenní plánování neuvádí spouštěč „změna kapacity“ (VAL-08). |
| E — Přerušení a čekání | [Řízení rozpracované práce](../docs/how-to/manage-workflow.md), kroky 1, 4, 5 a část „Čekání a blokování“; [Výběr práce a WIP](../docs/reference/work-selection-and-wip.md) | Rozlišit celkovou rozpracovanost od aktuální pozornosti; pozastavit, blokovat, dokončit nebo opustit rozsah | Pojmenované čekání s podmínkou návratu; pozastavená práce zůstává zahájená; nic není označeno za dokončené | INV-03, INV-05, INV-11, INV-12, INV-15 | Ano významově; diagram F→E budí dojem automatické reaktivace (VAL-05). |
| F — Reflexe | [První týden](../docs/tutorials/first-week.md), krok 8; [Týdenní plánování](../docs/how-to/weekly-planning.md), krok 6; [Strategická revize](../docs/how-to/strategic-review.md), kroky 1–6 | Oddělit pozorování, interpretaci a rozhodnutí; zvolit změnu dalšího kroku, týdenního výběru nebo strategie | Jedno rozhodnutí s důvodem a spouštěčem návratu; potvrzené závazky, které změna nezasáhla | INV-04, INV-05, INV-06, INV-10, INV-11 | Ano, ale týdenní postup nevede k rozlišení práce a výsledku ani k strategické revizi (VAL-07, VAL-10). |
**Výsledek E2E-01: Conditional.** Všechny fáze lze projít bez přímého rozporu s invarianty. Fáze C a D jsou významově nejčistší: podnět ani plán nevytvářejí závazek a změna plánu závazek neruší. Slabá místa jsou jinde:

- Přechod A→B je implicitní. Dokumenty popisují portfoliového kandidáta, ale žádný how-to neukazuje, jak s ním naložit vedle tří běžících projektů.
- Fáze B nepojmenovává potřeby péče jako vstup. Pokud je člověk nemá jako závazek, týdenní postup ho k nim nepřivede.
- Fáze E je v textu jasná, ale diagram připouští čtení, že se pozastavená práce vrací automaticky.
- Fáze F odděluje pozorování a interpretaci, ale nedává uživateli otázku, která by oddělila dokončenou práci od dosaženého výsledku.

## 3. Výsledky E2E-02 až E2E-07

| Test | Situace | Rozhodující dokumenty | Výsledek | Důkaz a omezení |
| --- | --- | --- | --- | --- |
| E2E-02 Minimum capacity | Extrémně málo energie; bez plánování, rekonstrukce historie a administrativního dluhu | [Denní rozhodování](../docs/how-to/daily-review.md), minimální úroveň; [Provozní jádro](../docs/reference/operational-kernel.md), tabulka úrovní | Pass (návrhově) | Tři otázky, ústně, bez minulosti; „Historii nedoplňujte“ je výslovné. Ověřeno jen jako návrh. |
| E2E-03 No strategy | Žádná vize ani strategie; závazky, vztahy a běžný den | [Týdenní plánování](../docs/how-to/weekly-planning.md), předpoklady; [Denní rozhodování](../docs/how-to/daily-review.md); [Řízení rozpracované práce](../docs/how-to/manage-workflow.md) | Pass (návrhově) | Strategie je volitelná, závazek nepotřebuje cíl ani projekt. Ověřeno jen jako návrh. |
| E2E-04 Priority without capacity | Vysoká priorita, žádná dostupná kapacita | [Týdenní plánování](../docs/how-to/weekly-planning.md), krok 3, krok 4 a „Priorita bez kapacity“ | Pass (návrhově) | Priorita nezaručuje proveditelnost; konflikt se pojmenuje nebo se změní rozsah. Ověřeno jen jako návrh. |
| E2E-05 Overlapping work | Jedna činnost podporuje dva cíle a plní jeden závazek | [Výběr práce a WIP](../docs/reference/work-selection-and-wip.md); [Řízení rozpracované práce](../docs/how-to/manage-workflow.md) | Conditional | Pravidlo jedné identity a jednoho nároku je v referenci, ale how-to je neopakuje; riziko duplicitní WIP (VAL-06). |
| E2E-06 Return after interruption | Dva týdny bez použití PLOS | [Týdenní plánování](../docs/how-to/weekly-planning.md), „Týden vynecháte“; [Denní rozhodování](../docs/how-to/daily-review.md), minimální úroveň; [Provozní jádro](../docs/reference/operational-kernel.md) | Pass (návrhově) | Návrat začíná současným stavem, historie může zůstat neznámá. Objevení je roztroušené (VAL-15). |
| E2E-07 Strategy changed, commitment remains | Strategie i projekt opuštěny, slib vůči jiné osobě trvá | [Strategická revize](../docs/how-to/strategic-review.md), krok 5; [Podněty, závazky a další kroky](../docs/reference/commitment-workflow.md) | Pass (návrhově) | Změna směru závazek neruší; zánik vyžaduje splnění, přejednání nebo skutečný konec odpovědnosti. Ověřeno jen jako návrh. |

## 4. Audit uživatelské použitelnosti

### A. Kognitivní zátěž

| Situace | Přibližný počet samostatných voleb | Pojmy potřebné předem | Poznámka |
| --- | --- | --- | --- |
| Běžný den | 3–4 | závazek, další krok, kapacita, odklad | Denní rozhodování má pět kroků; minimální verze tři otázky. |
| Týdenní plán | 5–6 | navíc záměr, priorita, alokace, nárok, rozpracovanost | Krok 4 přidává doménový slovník. |
| Nový podnět | 4 | navíc podnět, možnost, projekt, čekání | Sedm kroků, obvykle 2–5 minut. |
| Rozpracovanost | 4–5 | navíc WIP, pozastavení, blokace, opuštění | Pět kroků, podle potřeby. |

Tutorial prvního týdne zavádí během 33–45 minut přibližně deset pojmů: závazek, projekt, možnost, týdenní záměr, kapacitu, alokaci, další krok, pozorování, interpretaci a rozhodnutí. Týdenní plánování přidává prioritu, nárok a rozpracovanost. To není chyba sama o sobě, ale je to vysoký vstupní náklad pro metodiku, která slibuje použití bez školení.

Metodika nutí přemýšlet o vlastních pravidlech nejvíce na třech místech: v kroku 4 týdenního plánování (priorita versus nárok versus alokace), v kroku 4 tutorialu (záměr versus priorita) a ve výběru práce podle šesti hledisek. Vstupy jsou jinak běžně dostupné: kalendář, známé závazky a slovní odhad energie. Číselná kapacita není podmínkou.

### B. Jazyk

How-to místy používají doménový slovník, který čtenář nemusí znát. Nejzávažnější je krok 4 v [týdenním plánování](../docs/how-to/weekly-planning.md): „U každé priority porovnejte zdrojový nárok záměru s dostupností. Potom rozhodněte, kterému zdroji, horizontu a kontextu hodláte kapacitu vyčlenit.“ Věta míchá nárok, kapacitu a alokaci a obrací vztah: kapacita se vyčleňuje nároku, ne zdroji. „Zdrojový nárok“ ani „horizont a kontext“ nejsou v uživatelském textu vysvětlené. Podobně [zpracování podnětu](../docs/how-to/process-input.md) vkládá do kroku 3 odkazy na INV-03 a INV-15; uživatel je může ignorovat, ale text tím získává technický tón.

Běžný jazyk lze použít bez ztráty přesnosti: „odhadněte, kolik času a energie to chce; rozhodněte, kdy to uděláte; když se to nevejde, zmenšete rozsah nebo se domluvte jinak“. Význam zůstane stejný a uživatel nemusí znát INV-12.

Rozdíl mezi záměrem a prioritou není v tutorialu plně srozumitelný bez dalšího čtení (VAL-02). Rozdíl mezi nárokem a alokací je v dokumentaci definovaný, ale v how-to krok 4 se ztrácí (VAL-01). Bez DOM-01 je uživatel schopen rozhodnout, ale ne vždy pojmenovat, co přesně porovnal.

### C. Navigace

Start je dobrý: [README](../docs/README.md) nabízí tabulku „Chci…“ s časem a odkazem. Pro běžný den stačí jeden dokument. Při konfliktu uživatel přechází z denního rozhodování do týdenního plánování a případně do řízení rozpracovanosti; při podnětu do zpracování podnětu. To jsou dva až tři dokumenty na jedno rozhodnutí, což je únosné, ale pouze pokud uživatel zná hranice.

Denní rozhodování, týdenní plánování a řízení rozpracovanosti se překrývají v otázce „co teď“. Hranice jsou v záhlavích popsány („Kdy“), ale neexistuje jedna rozhodovací mapa, která by uživateli řekla, který postup zvolit. Považuji to za návrhovou hypotézu, ne za doložený rozpor: v E2E-01 se uživatel rozhodl správně, protože znal dokumenty.

Počet postupů není pro běžné používání zbytečně vysoký: denně jeden, týdně jeden, občas jeden na podnět a jeden na WIP. Pro první týden je ale vysoký; tutorial a pět původních how-to se překrývají v příkladech i krocích.

### D. Režie

PLOS přidává oproti běžnému rozhodování zejména: denní kontrolu závazků a volby (5 minut), týdenní plánování (20–30 minut), vyjasnění podnětů (2–5 minut), posouzení WIP (5–10 minut) a závěrečnou reflexi (10 minut). Souhrnně jde řádově o 1,5–2 hodiny týdně; je to hypotéza z popsaných časů, ne měření.

Nezbytné jsou podle mého posouzení čtyři věci: zkontrolovat, co komu dlužíte; porovnat volbu s kapacitou; určit jeden další krok; na konci týdne oddělit pozorování od rozhodnutí. Volitelné jsou zápis, portfolio, strategie, metriky a přesné kategorie. Dokumenty to většinou říkají, ale denní a týdenní how-to používají „Napište“ a „Zapište“ bez věty, že zápis je volitelný (VAL-09).

Proces lze zkrátit: minimální úroveň denního rozhodování má tři otázky, týden lze vynechat a historie se nedoplňuje. Tlak neustále sledovat projekty, hodnoty nebo čas dokumenty výslovně nevyžadují; přesto věta „Co přestanete sledovat, nezaniká“ může působit jako morální závazek sledovat. To je riziko R-01 a OQ-03, které může rozhodnout až pilot.

### E. Diagramy

| Diagram | Uzly / hrany | Popisky | Logika a shoda s textem | Nález |
| --- | --- | --- | --- | --- |
| [Provozní jádro](../docs/reference/operational-kernel.md) | 5 / 7 | české, krátké | Pět funkcí a tři zpětné vazby; shoda s tabulkou | Bez nálezu. |
| [Od hodnot k jednání](../docs/tutorials/from-values-to-action.md) | 8 / 10 | české, s vysvětlením | Tři horizonty, přerušované zpětné vazby; shoda s textem | Bez nálezu. |
| [Řízení rozpracované práce](../docs/how-to/manage-workflow.md) | 7 / 10 | většina větví popsaná | F→E bez popisku; D→B „ne“ zjednodušuje čtyři reakce | VAL-05, VAL-16. |
| [Zpracování nového podnětu](../docs/how-to/process-input.md) | 11 / 12 | české, převážně jasné | K neobsahuje odmítnutí; odmítnutí je pod F s podmínkou návratu | VAL-11. |
| [Strategická revize](../docs/how-to/strategic-review.md) | 7 / 8 | české | D→Q1 bez popisku; text mluví o odložení s podmínkou | Drobná nejasnost stejného druhu jako VAL-05. |

Počet uzlů je přiměřený; žádný diagram nemá více než jedenáct uzlů. Návratové vazby jsou v tutorialu a provozním jádru popsané a přerušované, takže nečtou jako automatické řízení. Výjimkou je `manage-workflow`: šipka z blokace zpět do rozpracované práce nemá popisek a její titulek říká, že se práce „vrací“. Text přitom žádá podmínku návratu a novou volbu. Doporučuji popisek „podmínka návratu splněna / nová volba“ a větu, že návrat není automatický.

Vykreslení nebylo ověřeno, protože renderer není dostupný. Kontrola byla pouze strukturální.

## 5. Hodnocení AC-01 až AC-07

| Kritérium | Výsledek | Důkaz z dokumentace a scénáře | Omezení a podmínka |
| --- | --- | --- | --- |
| AC-01 Strategic Continuity | Conditional | Cesta hodnota → vize → cesta → výsledek → priorita → krok je v tutorialu a referenci; návrat nabízí strategická revize. E2E-01 fáze A a F. | Portfolio A→B nemá postup (VAL-03); týdenní reflexe nevede k výsledku ani k revizi (VAL-07, VAL-10). Návrhové, nikoli empirické ověření. |
| AC-02 Commitment Integrity | Pass | INV-02 a INV-06 se opakují v podnětech, plánu, WIP i strategické revizi; E2E-07. | Ověřeno jen jako návrh; skutečné dodržení slibu v životě testováno nebylo. |
| AC-03 Capacity Integrity | Pass | Priorita, nárok, kapacita, alokace a spotřeba jsou v textu i referenci odlišné; E2E-04. | „Priorita“ nemá definici v GLO-01 (VAL-12) a krok 4 je jazykově nejasný (VAL-01). Návrhové ověření. |
| AC-04 WIP Integrity | Conditional | Text manage-workflow a reference rozlišují pozastavení, blokaci, dokončení a opuštění; E2E-05 a E2E-06. | Diagram F→E a D→B zjednodušují text (VAL-05, VAL-16); how-to neopakuje pravidlo jedné identity (VAL-06). Návrhové ověření. |
| AC-05 Recovery | Pass | Minimální úroveň, „Týden vynecháte“ a „Historii nedoplňujte“; E2E-02 a E2E-06. | Objevení návratu je roztroušené (VAL-15). Návrhové ověření, nikoli test po skutečné pauze. |
| AC-06 Usability | Conditional | Denní rozhodování je použitelné bez architektury; README vede k prvnímu kroku. | Krok 4 týdenního plánování vyžaduje doménový slovník (VAL-01); tutorial slévá záměr a prioritu (VAL-02). |
| AC-07 Minimal Overhead | Conditional | Zápis je v README a v některých how-to označen za volitelný; minimální režim snižuje zátěž. | Denní a týdenní how-to používají imperativ zápisu (VAL-09); skutečná režie nebyla měřena. |

Souhrn: tři Pass, čtyři Conditional, žádný Fail. Pass znamená shodu návrhu s vlastním pravidlem, ne důkaz přínosu. Conditional znamená, že použití je možné, ale existuje konkrétní omezení uvedené u nálezu.

## 6. Nálezy

**Blocking:** žádný nález. Neexistuje doložený rozpor, který by znemožnil průchod všemi fázemi E2E-01 nebo použití PLOS při nízké kapacitě. Níže uvedené nálezy jsou meze použitelnosti a integrace, ne zhroucení modelu.

Typ nálezu: **rozpor** je doložený nesoulad dvou míst, **mezera** je chybějící krok nebo vstup a **chyba** je doložená nesrovnalost (čas, jazyk). Nálezy nejsou estetické preference; kde jde o hypotézu, je to v textu označeno.

### Important

| ID | Závažnost a typ | Dokument a místo | Problém a důkaz | Dopad | Nejmenší oprava |
| --- | --- | --- | --- | --- | --- |
| VAL-01 | Important — mezera v použitelnosti | [weekly-planning.md](../docs/how-to/weekly-planning.md), krok 4; [process-input.md](../docs/how-to/process-input.md), krok 3 | Krok 4 používá „zdrojový nárok“, „alokace“ a „zdroji, horizontu a kontextu“; věta „kterému zdroji… hodláte kapacitu vyčlenit“ obrací vztah nároku a kapacity. Process-input vkládá INV-ID do 2–5minutového postupu. | Uživatel bez DOM-01 neví, co porovnává, a krok přeskočí nebo zamění prioritu s alokací. | Přepsat krok 4 běžným jazykem („odhadněte, co to chce za čas a energii; rozhodněte, kdy to uděláte; když se to nevejde…“) a INV odkazy přesunout do reference. |
| VAL-02 | Important — rozpor v tutorialu | [first-week.md](../docs/tutorials/first-week.md), kroky 4 a 5; [weekly-planning.md](../docs/how-to/weekly-planning.md), krok 3; [strategic-bridge.md](../docs/reference/strategic-bridge.md), řádek „Týdenní priorita“ | Tutoriál říká, že o přednosti rozhoduje priorita, ale krok 4 volí jen „týdenní záměr“ a krok 5 rovnou alokuje; pojem priorita se v postupu neobjeví. | Uživatel slije záměr, prioritu a alokaci; AC-03 se v praxi rozpadá. | V kroku 4 výslovně pojmenovat rozhodnutí o prioritě, nebo větu o prioritě vypustit a přiznat, že tutoriál prioritu neprocvičuje. |
| VAL-03 | Important — integrační mezera | [from-values-to-action.md](../docs/tutorials/from-values-to-action.md), kroky 4–5; [weekly-planning.md](../docs/how-to/weekly-planning.md), krok 3; [process-input.md](../docs/how-to/process-input.md), „strategická možnost“; [README.md](../docs/README.md), „Co zde zatím není“ | Cesta záměr → portfolio kandidátů není v žádném how-to krokem; týdenní plánování začíná až u „kandidátních záměrů“, ale neříká, jak se tam dostanou. README absenci vícealternativního návodu přiznává. | Fáze A končí implicitně; uživatel se třemi projekty nemá dokumentovaný způsob, jak posoudit, co nový záměr vytlačí. | Přidat krátkou sekci do kroku 3 týdenního plánování nebo samostatný how-to „portfolio kandidátů“: který kandidát, co vytlačí, kdy se vrátí; bez nové evidence. |
| VAL-04 | Important — integrační mezera | [weekly-planning.md](../docs/how-to/weekly-planning.md), vstupy a kroky 1–2; [daily-review.md](../docs/how-to/daily-review.md), vstupy a krok 1; [manage-workflow.md](../docs/how-to/manage-workflow.md), krok 2; [GLO-01](../glossary.md), DC-04 | Opakované postupy neuvádějí potřeby péče mezi vstupy; péče se objevuje jen jako kritérium důležitosti ve WIP a v tutoriálech. DC-04 přitom není automatický závazek. | Fáze B nemusí péči rozpoznat; uživatel ji buď ignoruje, nebo z ní udělá závazek, což odporuje DC-04. | Doplnit „potřeby péče“ do vstupů a jeden prompt v kroku 1 nebo 2 („co potřebuje pravidelnou péči a co se zanedbáním zhorší“). |
| VAL-05 | Important — rozpor diagramu a textu | [manage-workflow.md](../docs/how-to/manage-workflow.md), diagram řádky 21–25 a caption řádek 31; text kroky 3–5 | F→E je bez popisku; caption říká, že se práce „vrací do rozpracované práce“, takže šipka může znamenat automatickou reaktivaci. Text přitom žádá podmínku návratu a novou volbu. | Uživatel může pozastavenou práci považovat za aktivní nebo čekat automatické obnovení; AC-04. | Doplnit popisek „podmínka návratu splněna / nová volba“ a v captionu říci, že návrat není automatický. |
| VAL-06 | Important — integrační mezera | [manage-workflow.md](../docs/how-to/manage-workflow.md), kroky 1–2; [work-selection-and-wip.md](../docs/reference/work-selection-and-wip.md), „Co se započítává do WIP“; INV-15 | How-to neříká, že stejný rozsah práce zůstává jednou položkou, i když podporuje dva záměry nebo plyne ze závazku i projektu; pravidlo je jen v referenci. | E2E-05: riziko duplicitní WIP a dvojího nároku; AC-03 a AC-04. | Přidat jednu větu do kroku 1: „Stejná práce je jedna položka, i když podporuje dva záměry nebo plyne ze závazku i projektu.“ |
| VAL-07 | Important — mezera v návaznosti | [weekly-planning.md](../docs/how-to/weekly-planning.md), krok 6; [first-week.md](../docs/tutorials/first-week.md), krok 8; [work-selection-and-wip.md](../docs/reference/work-selection-and-wip.md), „Dokončení práce a dosažení výsledku“; INV-05 | Týdenní reflexe se ptá „co se stalo / co z toho vyvozuji / co změním“, ale nevede k porovnání zamýšleného výsledku s pozorováním; INV-05 je jen v referenci. | Fáze F snadno zamění dokončenou práci za dosažený výsledek; AC-01 a AC-04. | Doplnit do kroku 6 otázku: „U kterého záměru mám doložený výsledek a kde mám jen provedenou práci?“ |
| VAL-08 | Important — rozpor v navigaci | [weekly-planning.md](../docs/how-to/weekly-planning.md), záhlaví „Kdy“; [daily-review.md](../docs/how-to/daily-review.md), „Související“; [CO-01](../01-foundations/concept-of-operations.md), OP-03 | How-to říká „jednou za týden“, ale denní rozhodování na něj odkazuje při nevyřešeném konfliktu; ConOps připouští „při změně kapacity“. | Fáze D: uživatel neví, zda má plán přepracovat hned, nebo čekat na týden; AC-05. | Upravit hlavičku na „jednou za týden, nebo když se změní kapacita“. |
| VAL-09 | Important — napětí s AC-07 | [daily-review.md](../docs/how-to/daily-review.md), kroky 4–5; [weekly-planning.md](../docs/how-to/weekly-planning.md), kroky 1 a 4; [README.md](../docs/README.md), „PLOS není aplikace“; [process-input.md](../docs/how-to/process-input.md), záhlaví | Denní a týdenní how-to používají „Napište“ a „Zapište“ bez věty, že zápis je volitelný; README přitom říká, že PLOS funguje bez zápisu. | Uživatel může vytvořit administrativní dluh nebo mít pocit povinné evidence; AC-07. | Doplnit „stačí ústně nebo v paměti; zápis je volitelný“ do obou záhlaví. |
| VAL-10 | Important — mezera v návaznosti | [weekly-planning.md](../docs/how-to/weekly-planning.md), krok 6 a „Související“; [strategic-review.md](../docs/how-to/strategic-review.md); [from-values-to-action.md](../docs/tutorials/from-values-to-action.md), krok 7 | Týdenní reflexe neodkazuje na strategickou revizi a její „Související“ ji neuvádí; cesta „vzorec se opakuje → strategie“ je jen v tutoriálu. | Fáze F: uživatel nemusí vědět, kdy změnit strategii; AC-01. | Přidat do kroku 6 a „Související“ odkaz na strategickou revizi s podmínkou „když se vzorec opakuje i po změně taktiky“. |

### Improvement

| ID | Závažnost a typ | Dokument a místo | Problém a důkaz | Dopad | Nejmenší oprava |
| --- | --- | --- | --- | --- | --- |
| VAL-11 | Improvement — rozpor diagramu a textu | [process-input.md](../docs/how-to/process-input.md), diagram K a F; text krok 6; [commitment-workflow.md](../docs/reference/commitment-workflow.md), „Možné výsledky vyjasnění“ | Diagram vede „odmítnout“ do „Možnost nebo odmítnutí s podmínkou návratu“ a u K odmítnutí chybí; krok 6 a tabulka výsledků přitom chápou odmítnutí jako ukončenou záležitost, ne jako čekání. | Menší zmatek u 2–5minutového postupu. | Doplnit „odmítnutí“ do K nebo rozdělit F na možnost a odmítnutí. |
| VAL-12 | Improvement — terminologická mezera | [strategic-bridge.md](../docs/reference/strategic-bridge.md), „Týdenní priorita“; [work-selection-and-wip.md](../docs/reference/work-selection-and-wip.md), „Pracovní pohledy“; [GLO-01](../glossary.md), DC-21 | „Týdenní priorita“, „kandidátní práce“ a „připravená práce“ nejsou v GLO-01; DC-21 jen říká, co kapacita není. | Termíny se mohou v dalších dokumentech rozejít; není to rozpor, ale chybí autoritativní opora. | Označit je jako provozní zkratky a odkázat na nejbližší pojmy GLO-01; případné doplnění GLO-01 jen po rozhodnutí. |
| VAL-13 | Improvement — chyba v odhadu | [first-week.md](../docs/tutorials/first-week.md), záhlaví a kroky 1–6; [README.md](../docs/README.md), tabulka | Kroky 1–6 sčítají 33 minut, hlavička a README uvádějí 40–45 minut první den. | Menší nesoulad očekávání; odhad je hypotéza, ne měření. | Sjednotit na „přibližně 35–45 minut“ nebo uvést, že zahrnuje úvod a rezervu. |
| VAL-14 | Improvement — jazyková chyba | [first-week.md](../docs/tutorials/first-week.md), krok 4 | „rozpočet odeslaný do pátku“ zní jako hotový stav; závazek je „odeslat do pátku“. | Může mást rozlišení závazku a dokončené práce. | Změnit na „rozpočet odeslat do pátku“. |
| VAL-15 | Improvement — navigační mezera | [README.md](../docs/README.md), odstavec o nízké kapacitě; [daily-review.md](../docs/how-to/daily-review.md), minimální úroveň; [weekly-planning.md](../docs/how-to/weekly-planning.md), „Týden vynecháte“; [first-week.md](../docs/tutorials/first-week.md), „Když to nevyjde“; [operational-kernel.md](../docs/reference/operational-kernel.md), tabulka úrovní | Návrat po přerušení je popsán na čtyřech místech, ale README na něj neodkazuje; uživatel po dvou týdnech nemá jeden vstupní bod. | E2E-06 projde, ale objevení je pomalejší; AC-05. | Přidat jeden řádek do README „Po přerušení začněte současným stavem“ s odkazem na denní a týdenní plánování. |
| VAL-16 | Improvement — rozpor diagramu a textu | [manage-workflow.md](../docs/how-to/manage-workflow.md), diagram D→B; text krok 3 | D→B „ne“ vrací jen k výběru, ale text nabízí zmenšení rozsahu, odklad, přejednání a přiznání konfliktu. | Diagram zjednodušuje rozhodnutí a může vést k opakovanému výběru bez změny podmínek. | Doplnit do diagramu nebo captionu čtyři přípustné reakce. |

## 7. Doporučení

**Accept with conditions.** Návrh je sémanticky konzistentní v tom, co je pro v0.3 podstatné: závazek nevzniká zachycením ani plánem, změna směru ho neruší, priorita nepřidává kapacitu, pozastavení není dokončení a neznámé není nula. Žádný nález není Blocking. Podmínky se týkají použitelnosti a několika chybějících přechodů, ne změny architektury.

1. **Před pilotem provést malé textové opravy** bez nových pojmů: VAL-01, VAL-02, VAL-04, VAL-05, VAL-06, VAL-07, VAL-08, VAL-09 a VAL-10. Jde o doplnění vět, popisků a jednoho odkazu, ne o přepis dokumentace.
2. **Pilot lze spustit i bez oprav**, ale známé mezery mohou zkreslit výsledek. Facilitátor má při pilotu sledovat právě tato místa a neslibovat, že PLOS sám vyřeší portfolio nebo péči.
3. **O VAL-03 a VAL-12 rozhodnout až po pilotu.** Zda uživatel potřebuje samostatný portfolio postup a zda mu provozní zkratky stačí, je otázka skutečného používání, ne dalšího teoretického návrhu.
4. **Neměnit GLO-01, DOM-01, ARCH-01 ani ADR** bez doloženého protipříkladu a nového rozhodnutí. Tato zpráva žádné takové rozhodnutí nenavrhuje.

## 8. Co může rozhodnout až skutečný pilot

Následující tvrzení zůstávají neověřená a žádný scénář je neuzavírá:

- Zda PLOS pomůže vybrat smysluplné jednání v běžném týdnu, nebo jen vytvoří další vrstvu rozhodování. Otevřené H-01, H-03, H-05 a OQ-03.
- Zda uživatel rozumí rozdílu mezi záměrem, prioritou, nárokem a alokací bez čtení DOM-01. To ověří jen skutečný člověk, ne audit.
- Zda je režie přiměřená přínosu a které kroky lidé sami vypustí. Otevřené H-01, R-01 a OQ-03.
- Zda se dlouhodobý směr skutečně promítne do dne, nebo zůstane samostatným rituálem. Otevřené H-03.
- Zda člověk udrží závazky bez průběžného sledování a zda se po přerušení vrátí bez rekonstrukce. Otevřené H-04.
- Zda potřeby péče vstoupí do plánování samy, nebo je uživatel převede na závazky. To je hypotéza, kterou tento audit jen pojmenoval.

Pilotní návod je v [Pilot PLOS — sedm dní](../docs/how-to/pilot-plos.md). Neobsahuje povinný formulář ani novou evidenci.

## 9. Technické kontroly

| Kontrola | Výsledek | Poznámka |
| --- | --- | --- |
| `python3 tools/check_docs.py` | Prošlo bez chyb | Strukturální kontrola odkazů, kotev, tabulek a identifikátorů; není to renderer ani validátor Mermaid. |
| `git diff --check` | Prošlo bez chyb | Žádné koncové mezery ani poškození bílých znaků. |
| Platnost odkazů nových dokumentů | Ověřena nástrojem | Všechny relativní odkazy a kotvy v obou nových dokumentech. |
| Duplicitní autoritativní definice | Nenalezena | Nové dokumenty neobsahují definice DC, DR ani INV; používají existující odkazy. |
| Historické dokumenty jako současný postup | Nepoužity | Report vychází z aktuálních uživatelských a autoritativních dokumentů. |

Ověření je návrhové. Skutečný přínos, srozumitelnost a režie zůstávají předmětem pilotu.
