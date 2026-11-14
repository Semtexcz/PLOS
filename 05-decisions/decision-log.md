# Architecture Decision Log

**Stav všech ADR:** D — přijato autorem pro návrh v0.1 dne 2026-11-14 v rámci zadání. Doporučení vlastníkovi k revizi, nikoli tvrzení o jeho dodatečném schválení. Rozhodnutí lze změnit novým ADR s odkazem na nahrazený záznam. Otevřené hypotézy nejsou potichu povýšeny na mandát.

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
