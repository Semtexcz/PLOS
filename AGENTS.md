# AGENTS.md — pravidla pro AI agenty v repozitáři PLOS

**Rozsah:** každá významná změna dokumentace, architektury, nástrojů nebo rozsahu iterace v tomto repozitáři.

Tato pravidla neopisují záměr projektu. Kanonický záměr je v [PROJECT_INTENT.md](PROJECT_INTENT.md); přečtěte ho z repozitáře, necitujte ho z paměti.

## Povinný kontext

Před návrhem nebo provedením významné změny:

1. Přečtěte [PROJECT_INTENT.md](PROJECT_INTENT.md) a určete, které jeho části se zadání týká.
2. Respektujte existující autoritativní dokumenty: [System Charter](01-foundations/system-charter.md), [slovník](glossary.md), [doménový model](03-architecture/preliminary-domain-model.md), [konceptuální architekturu](03-architecture/conceptual-architecture.md) a [registr požadavků](02-requirements/high-level-requirements.md). Neměňte jejich obsah ani stav bez rozhodnutí vlastníka.
3. Zkontrolujte, jak zadání souvisí s původním účelem projektu. Zadání, které účel posouvá, označte jako návrh změny záměru.
4. Použijte specializované skills jen podle charakteru úkolu; pro uživatelskou dokumentaci je to [PLOS dokumentace](skills/plos-documentation/SKILL.md). Nové skills, subagenty ani závislosti nepřidávejte bez zadání.

Pokud zadání vyžaduje změnu původního záměru, zastavte provádění a předložte návrh vlastníkovi.

## Intent Alignment Check

Před prací musíte umět odpovědět:

- Který problém původního záměru tato práce řeší?
- Jakou konkrétní schopnost PLOS zlepší?
- Jak uživatel tuto schopnost prakticky využije?
- Jak ověříme, že schopnost funguje?
- Nevytváří řešení zbytečnou evidenci, administrativu nebo další paralelní systém?

Odpovědi uveďte v plánu před implementací. Pokud na některou otázku nelze odpovědět, upozorněte na riziko odchylky a počkejte na rozhodnutí vlastníka; nerozšiřujte projekt ani nepřebalte mezeru do nové dokumentace.

## Completion Gate

Za dokončení významné iterace nestačí:

- existence dokumentů,
- projití strukturálních kontrol,
- správné odkazy,
- formální sémantická konzistence.

Musí existovat konkrétní uživatelský scénář a návrhový důkaz, že nová nebo opravená schopnost řeší zamýšlený problém. Současně musíte pojmenovat, co zůstává neověřené. Empirický přínos lze potvrdit až skutečným používáním; do té doby jej neuvádějte jako doložený.

## Handoff

Na konci významného úkolu uveďte krátkou kontrolu v tomto pořadí:

- **Alignment:** který bod `PROJECT_INTENT.md` byl naplněn.
- **Capability:** co nyní PLOS umí lépe.
- **Evidence:** jak bylo zlepšení ověřeno a čím.
- **Complexity:** co přibylo na režii nebo počtu kroků.
- **Gaps:** co ještě chybí a co zůstává neověřené.

Nepište, že je něco funkčně úplné, pokud to nebylo ověřeno.

## Change Control

- Bez explicitního pokynu vlastníka neprovádějte commit, push ani změnu rozsahu iterace.
- Neměňte [PROJECT_INTENT.md](PROJECT_INTENT.md), [slovník](glossary.md), [doménový model](03-architecture/preliminary-domain-model.md), [konceptuální architekturu](03-architecture/conceptual-architecture.md) ani stav požadavků; takovou změnu navrhněte.
- Při rozporu mezi zadáním, záměrem a architekturou rozpor oznamte, popište dopad a nabídněte varianty. Nerozhodujte místo vlastníka.
- Rozhodnutí o tom, co bude následovat, patří vlastníkovi projektu.
