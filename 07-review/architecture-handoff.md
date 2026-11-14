# Architecture Handoff

> Historický artefakt I1 / v0.1, ponechaný jako záznam tehdejšího předání. Aktuální výsledek je v [Iteration 2](architecture-handoff-iteration-2.md). Tehdejší otevřené položky a stop podmínka se čtou v historickém kontextu.

**ID:** HANDOFF-01 • **Datum:** 2026-11-14 • **Předávaná verze:** 0.1 — Architecture Foundation, Iteration 1. **Stav:** návrh připravený k revizi vlastníkem; další iterace nebyla zahájena.

## Co je navrženo

Technologicky nezávislá metodika s vymezením člověka, řídicích praktik a okolí; sedm provozních režimů; potřeby a předběžné požadavky; šest funkčních odpovědností s hlavními rozhraními; předběžný doménový model a šest konceptuálních diagramů. [README](../README.md) je vstupní index všech artefaktů.

Hodnoty orientují, strategie navrhuje možné cesty, portfolio vybírá nároky, plánování posuzuje kapacitu a operativa udržuje závazky a nejbližší kroky. Péče a povinnosti mohou vstupovat samostatně. Zpětná vazba vede přes interpretaci a lidské rozhodnutí zpět ke správnému vlastníkovi významu.

## Přijatá návrhová rozhodnutí

[ADR-01 až ADR-06](../05-decisions/decision-log.md) doporučují hybridní architekturu, samostatnou legitimitu péče a povinností při společném posuzování kapacity, přizpůsobitelnou kadenci, rozlišení zdrojů bez univerzálního skóre, přiměřenou evidenci s omezeným režimem a lehké textové modely. Alternativy, výhody, nevýhody a podmínky revize jsou uvedeny v každém ADR.

Jsou to rozhodnutí autora pro pracovní návrh. Požadavky explicitně převzaté ze zadání mají stav Z; nové požadavky mají stav N a čekají na validaci. Self-review není jejich uživatelským schválením.

## Otevřené předpoklady a rizika

ASM-01 až ASM-05 předpokládají alespoň občasnou ochotu reflektovat, hrubou dostupnost informací o kapacitě a závazcích, možnost uchovat minimum záznamů, alespoň částečně ovlivňovat nároky a únosnost šesti funkcí. Tyto předpoklady nebyly ověřeny s uživatelem.

H-01 až H-05 se týkají režie architektury, užitečnosti hrubého obrazu kapacity, kadence, obnovy a kvalitativní reflexe. Významná rizika jsou přetížení evidencí, tlak na výkon, vytlačení strategie operativou, ztráta závazku při změně směru a zaměňování vnějších omezení za vnitřní překážky. Přehled vlastníků a cílových iterací je v [registru otevřených otázek](../05-decisions/open-questions.md).

Nejbližší sémantické riziko: hranice projektu, závazku a cíle a dvojí započtení nároků při pohledu na projekt i jeho kroky. Před praktickým používáním bude třeba navíc vymezit kritičnost, přijatelnou režii a rozsah sdílení.

## Co je připraveno pro pokračování

Slovník, předběžné vztahy a osm scénářů poskytují konkrétní podklad pro detailnější modelování. Požadavky mají ID, původ, zdůvodnění, předběžné ověření a odpovědnou funkci. Diagramy mají textový zdroj, význam hran a omezení; nejsou označeny za formální SysML ani strojově ověřený model.

Výsledek kontrol, nálezy a hranice jistoty jsou v [Architecture Review Report](architecture-review-report.md). Provozní přínos PLOS, spokojenost uživatele ani empirická účinnost kombinace frameworků zatím nejsou ověřeny.

## Doporučené zadání Iteration 2

**Zpřesnit doménový model pouze ve čtyřech skupinách:** (1) cíl–výsledek–projekt–závazek–další krok, (2) oblast–péče–rutina–návyk, (3) strategie–scénář–předpoklad–experiment–pozorování–rozhodnutí a (4) kapacita–alokace–plán. Doplnit odůvodněné vztahy a nezbytné kardinality/invarianty, příklady a protipříklady, vyřešit OQ-04 a ohraničit OQ-06. Aktualizovat pouze dotčený slovník, model, diagramy a rozhodnutí; posoudit dopad na požadavky.

Dokončení I2 vyžaduje konzistentní vyjádření UC-01 až UC-08 bez fiktivních cílů, záměny odpovědnosti a činnosti a dvojího započtení kapacity. Přesné vstupy, výstupy, závislosti a výluky jsou v [roadmapě](../06-roadmap/architecture-roadmap.md). Implementace, úplné workflow, algoritmy a finální metriky do I2 nepatří.

**Tímto předáním práce končí v Iteration 1.**
