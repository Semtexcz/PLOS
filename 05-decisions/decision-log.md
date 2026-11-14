# Architecture Decision Log

**Stav ADR-01 až ADR-06:** D — přijato autorem pro návrh v0.1 dne 2026-11-14 v rámci zadání. ADR-07 až ADR-11 jsou rozhodnutí pro v0.2 se stavem u každého záznamu. ADR-11 částečně nahrazuje notační část ADR-06; ostatní rozhodnutí I1 zůstávají platná. Doporučení vlastníkovi k revizi, nikoli tvrzení o jeho dodatečném schválení. Rozhodnutí lze změnit novým ADR s odkazem na nahrazený záznam. Otevřené hypotézy nejsou potichu povýšeny na mandát.

## ADR-01 — Hybridní architektura funkčních odpovědností

**Kontext:** P2, P3, P6, P7; je třeba spojit směr s jednáním a zachovat operativní reakci. **Alternativy:** čistý hierarchický rozklad je přehledný, ale vnucuje péči falešné cíle; plně autonomní procesy jsou pružné, ale mohou vést k soupeřícím prioritám; šest modulů podle frameworků usnadňuje původ metod, ale duplikuje review a plánování.

**Rozhodnutí:** šest funkčních SS, hierarchie záměrů a průběžné obousměrné vazby. Člověk je společná rozhodovací autorita. **Důvod:** oddělit významy a vlastníky bez šesti nezávislých systémů. **Důsledky:** potřeba explicitních rozhraní a disciplíny jediného vlastníka významu; větší pojmová složitost než jeden seznam. **Revize:** pokud H-01 neobstojí nebo vzniknou neodstranitelné duplicity. Vazba: FR-12, QR-07, ARCH-01, DG-02/05.

## ADR-02 — Péče a závazky mají samostatný vstup, kapacita společný pohled

**Kontext:** běžný život není jen portfolio strategických projektů. **Alternativy:** vše odvozovat z cílů zlepšuje formální dohledatelnost, ale vytváří fiktivní cíle; oddělit strategickou a provozní evidenci zjednodušuje lokální přehled, ale skrývá společné přetížení.

**Rozhodnutí:** SS-05 spravuje závazky a provádění péče; SS-03 je zohledňuje v portfoliovém pohledu, SS-04 při alokaci. Evidence a aktivní rozpracovanost jsou různé pojmy. **Důvod:** jedna realita zdrojů, různé legitimní zdroje nároků. **Důsledky:** nutno odlišit referenci od duplicitního záznamu a nevytvářet projektu dvě alokace za stejnou práci. **Revize:** při modelování identity v I2. Vazba: FR-03/05/08/09, QR-06, DG-04/06.

## ADR-03 — Revidovatelná kadence a kontinuita při změně

**Kontext:** 12 Week Year nabízí pravidelný horizont; P5 a P10 vyžadují adaptaci. **Alternativy:** pevný cyklus má jednoduchá očekávání, ale může být nepoužitelný při nepravidelnosti; pouze událostní řízení je pružné, ale může ztratit strategický odstup.

**Rozhodnutí:** nabídnout pravidelné krátké, střední a delší horizonty a doplnit je událostní revizí; délka je přizpůsobitelná. Dvanáct týdnů je inspirace. Při změně strategie se závazky přezkoumají, ne automaticky zruší. **Důsledky:** nižší uniformita a nutnost později určit pravidla spouštění review. Nenabízíme kompletní původní 12 Week Year. **Revize:** H-03, OQ-02, pilot kadence. Vazba: FR-10/12/13, FB-01 až FB-04.

## ADR-04 — Vícezdrojová kapacita bez univerzálního skóre priorit

**Kontext:** různé nároky soutěží o čas, energii a jiné zdroje. **Alternativy:** čistá intuice má malou režii, ale skryté konflikty; vážené skóre je srovnatelné, ale předstírá směnitelnost a přesnost; detailní optimalizace vyžaduje neobhajitelné vstupy.

**Rozhodnutí:** udržovat kontextový obraz zdrojů a jejich nejistoty, oddělit dostupnost od alokace a skutečnosti. Konflikty předkládat jako lidské volby s důvody, včetně nevyřešeného konfliktu. Nealokovaný prostor je platný. **Důsledky:** méně automatické srovnatelnosti, větší nárok na interpretaci; žádný univerzální WIP limit ani procento rezervy. **Revize:** H-02 a I6; kvalitativní model lze zpřesnit jen tam, kde to pomáhá. Vazba: FR-04/07/14, QR-02/03.

## ADR-05 — Pozorování pro rozhodnutí a omezený režim

**Kontext:** měření může pomáhat i zvyšovat tlak a režii. **Alternativy:** úplné skórování nabízí konzistentní časové řady, ale hrozí falešná přesnost; žádná evidence minimalizuje režii, ale oslabuje učení a kontinuitu.

**Rozhodnutí:** pozorování mohou být kvalitativní a neúplná; metrika má konkrétní rozhodovací účel. Oddělit provedení a výsledek. Při omezené kapacitě zachovat jen aktuálně potřebnou orientaci a známé kritické závazky, bez povinného doplňování minulosti. **Důsledky:** někdy nelze vyhodnotit trend; přípustné „nevíme“ má přednost před vymyšlenou přesností. **Revize:** H-04/H-05, OQ-01/03/05. Vazba: FR-11/13, QR-04/05, UC-04/07/08.

## ADR-06 — Lehký konceptuální model a textové diagramy

**Kontext:** I1 má umožnit další modelování bez implementace a falešné formálnosti. **Alternativy:** plný SysML může později zlepšit formální model, ale vyžaduje konkrétní verzi, nástroje a ověření; samotná próza má malou bariéru, ale skrývá vazby; databázový model by předčasně uzamkl významy.

**Rozhodnutí:** Markdown jako referenční dokumentace, šest lokálních Mermaid flowchartů s explicitní sémantikou hran. Pojmy definovat v jednom slovníku, doménové vztahy v DOM-01. Diagramy nejsou UML třídní model ani SysML a nevyjadřují kardinality. **Důsledky:** nelze z nich odvozovat strojový důkaz konzistence, simulaci nebo kód. Syntax a sémantika se ověřují odděleně; provedené kontroly se uvedou pravdivě. **Revize:** I2/I4 podle potřeby přesnějšího jazyka. Vazba: CON-01/02, QR-07.

## ADR-07 — Metodika bez předpokladu implementace a povinných záznamů

**Stav:** D pro v0.2, 2026-11-14; vychází z explicitního upřesnění SoI v zadání I2. **Kontext:** CH-01 zmiňoval informační záznamy jako součást SoI a „budoucí software“; ASM-03 mohl působit jako univerzální podmínka. P9 už technologickou nezávislost vyžaduje.

**Alternativy:** ponechat formulaci s rizikem implementačního výkladu; předefinovat celou architekturu; minimálně upřesnit hranici a oddělit význam evidence od média. **Rozhodnutí:** třetí možnost. PLOS je samostatně člověkem vykonatelná metodika i bez jakéhokoli softwaru nyní či v budoucnu; konceptuální nezbytnost nezakládá povinné záznamy. **Dopady:** malé změny CH-01, P9 a CON-01; ASM-03 platí podmíněně pro kontinuitu explicitních záznamů, nikoli existenci metodiky. Nevznikají nové funkční požadavky, SS ani provozní formy. **Vazby:** ADR-01/05/06, INV-01, UC-04/08. **Revize:** pouze novým zadáním měnícím SoI; volba média sama rozhodnutí neruší.

## ADR-08 — Oddělené významy výsledku, práce a odpovědnosti

**Stav:** D pro v0.2, 2026-11-14. **Kontext:** Outcome v GLO-01/DG-06 v0.1 rozlišoval zamýšlené a pozorované použití slovně, ale neměl hranici identity; OQ-04. **Alternativy:** jedna identita Outcome měnící se z očekávání na skutečnost (riziko přepsání reference); dvě nezávislé evidence výsledků (duplicitní pozorování); oddělený obsah Intended Outcome a role Observation pro Observed Outcome.

**Rozhodnutí:** třetí varianta. Intended Outcome je samostatný sémantický koncept bez autonomní identity; Observed Outcome nese identitu původního Observation. Interpretace dosažení či příčiny patří do Review. Objective, Project, Commitment a Next Action mají vlastní významovou kontinuitu podle DOM-01; jejich vazby jsou referenční a dovolují mnoho–mnoho. Žádná hierarchie není univerzálně povinná.

**Dopady:** nahrazuje neúplné rozlišení Outcome v DOM-01/GLO-01/DG-06 v0.1, zachovává ADR-02/03/05. Outcome zůstává pouze aliasem rodiny významů. Změna strategie nezruší závazek; přejednání a rozpoznání skutečného zániku nejsou totéž. Klasifikace Core nevyžaduje explicitní evidenci. **Vazby:** INV-03 až INV-10/18, SV-01/02/05/06/09, FR-10/11 a QR-06 zůstávají N. **Revize:** pokud se objeví případ, kde role Observation nedokáže odlišit pozorování a výklad bez ztráty původu. OQ-04 uzavřena pro konceptuální identitu, stavy zůstávají I5.

## ADR-09 — Zdrojový nárok jako význam, nikoli další pracovní objekt

**Stav:** D pro v0.2, 2026-11-14. **Kontext:** ADR-02/04 požadují společné posouzení bez dvojího započtení; v0.1 nechal pojem nárok neformální. **Alternativy:** sčítat odhady všech projektů a kroků (duplicity); vést nezávislé entity nároků s povinným úplným rozkladem (režie a implementační tlak); rozlišit Resource Demand podle rozsahu práce, zdroje, horizontu a kontextu bez nové identity práce.

**Rozhodnutí:** třetí možnost; souhrn a zahrnuté části nejsou nezávislé sčítance. Shodné nároky, částečné překryvy, alternativní plány a skutečné konflikty se rozlišují. Nejasný překryv zůstává nejistý. Planned/Actual Capacity jsou role posouzení dostupnosti; spotřeba je předmět Observation, nikoli Actual Capacity.

**Dopady:** zpřesnění DR-29 až DR-35 a INV-11 až INV-16; nárok je nově pojmenován v GLO-01, nikoli nově zavedená povinná evidence. Ani kvalita života, ani energie se nemění na univerzální skóre. **Vazby:** ADR-02/04, SV-03/08/10/11, FR-04 a QR-03. **Revize:** konkrétní protipříklad neřešeného překryvu; numerická či rozhodovací pravidla až I6. H-02 zůstává neověřena.

## ADR-10 — WOOP pomocí významových rolí a experiment bez povinného projektu

**Stav:** D pro v0.2, 2026-11-14. **Kontext:** FW-01 správně neztotožňuje if–then s WOOP; chybí svázání čtyř rolí. OQ-06 nevymezuje hranici Experiment/Project. **Alternativy WOOP:** čtyři nové samostatné objekty; pouze Conditional Response; existující koncepty s přesně vymezenými rolemi. **Alternativy experimentu:** povinný projekt; práh podle počtu kroků; rozlišovat poznávací záměr a organizační potřebu.

**Rozhodnutí:** WOOP využije záměr v roli Wish, jeho Intended Outcome, Observation/Assumption v roli Internal Obstacle a odpovídající Conditional Response. External Constraint je odlišná role; ne každé omezení je kapacitní. Nový objekt WOOP ani povinný strategický cíl nevzniká. Experiment se může realizovat přes jeden či několik Next Action. Project je účelný, pokud je potřeba samostatně koordinovat ohraničenou práci; Experiment ani Project není podtyp druhého. Nerozhodný poznatek je přípustný.

**Dopady:** pouze upřesnění rolí DC-34/35 a vazeb v DOM-01; nepřidává celý proces WOOP ani katalog překážek. OQ-06 uzavřena sémanticky, individuální únosnost rozkladu zůstává OQ-03. **Vazby:** ADR-02/05/08, INV-09/17, UC-01, SV-05/12, FR-02/14 zůstávají N. **Revize:** případ vyžadující další identitu, který nelze vyjádřit existujícími rolemi; behaviorální úplnost až I5.

## ADR-11 — Konceptuální UML pohledy s explicitní sémantikou

**Stav:** D pro v0.2, 2026-11-14. **Kontext:** zpřesnění vztahů a několika nutných násobností přesahuje významové flowcharty I1. **Alternativy:** ponechat DG-06 flowchart (slabé rozlišení násobností); úplný SysML/UML model s nástrojovým úložištěm (neodůvodněná režie); omezená notace UML tříd a asociací ve zdrojových Mermaid blocích.

**Rozhodnutí:** třetí varianta. DG-06 je celkový pohled, DG-07 až DG-10 detaily čtyř skupin. Nepoužívá se dědičnost ani kompozice pro role či reference. GLO-01 drží definice, DOM-01 vztahy a invarianty; diagramy jsou navazující pohledy, ne další zdroj pravidel.

**Dopady:** částečně nahrazuje ADR-06 pouze v rozhodnutí o flowchart notaci DG-06 a počtu diagramů; DG-01 až DG-05 a ostatní pravidla ADR-06 platí. Parser/render a sémantická kontrola se vykazují odděleně. **Vazby:** QG-03/08, RV-05, OQ-08. OQ-08 je vyřešena pro doménové pohledy I2, potřeba další notace v I4 zůstává otevřená. **Revize:** pokud potřebné vztahy nelze přesně vyjádřit v této podmnožině nebo dostupné renderery brání použitelnosti.
