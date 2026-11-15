# AGENTS.md — pravidla pro AI agenty v repozitáři PLOS

**Rozsah:** každá změna dokumentace, architektury, nástrojů nebo rozsahu iterace v tomto repozitáři. Povinnosti se liší podle druhu úkolu: významná změna vyžaduje plný Intent Alignment Check, rutinní údržba jen potvrzení, že se nemění význam.

Tato pravidla neopisují záměr projektu. Kanonický záměr je v [PROJECT_INTENT.md](PROJECT_INTENT.md); přečtěte ho z repozitáře, necitujte ho z paměti.

## Druhy úkolů

**Významná změna** mění metodické schopnosti, architekturu, požadavky, zavádí nové workflow, mění rozsah iterace nebo zasahuje do zásadních uživatelských postupů.

**Rutinní údržba** je oprava překlepu, odkazu nebo formátování a drobná technická oprava bez změny významu.

Pokud úkol nelze jednoznačně zařadit, považujte ho za významnou změnu.

## Povinný kontext

Před návrhem nebo provedením významné změny:

1. Přečtěte [PROJECT_INTENT.md](PROJECT_INTENT.md) a určete, které jeho části se zadání týká.
2. Respektujte existující autoritativní dokumenty: [System Charter](01-foundations/system-charter.md), [slovník](glossary.md), [doménový model](03-architecture/preliminary-domain-model.md), [konceptuální architekturu](03-architecture/conceptual-architecture.md) a [registr požadavků](02-requirements/high-level-requirements.md). Neměňte jejich obsah ani stav bez rozhodnutí vlastníka.
3. Zkontrolujte, jak zadání souvisí s původním účelem projektu. Zadání, které účel posouvá, označte jako návrh změny záměru.
4. Použijte specializované skills jen podle charakteru úkolu; pro uživatelskou dokumentaci je to [PLOS dokumentace](skills/plos-documentation/SKILL.md). Nové skills, subagenty ani závislosti nepřidávejte bez zadání.

U rutinní údržby stačí ověřit, že úprava nemění účel, významy ani projektový rozsah. Autoritativní dokumenty čtěte v plném rozsahu jen tehdy, když oprava zasahuje do jejich významu.

## Intent Alignment Check

U významné změny odpovězte před implementací:

- Který problém původního záměru tato práce řeší?
- Jakou konkrétní schopnost PLOS zlepší?
- Jak uživatel tuto schopnost prakticky využije?
- Jak ověříme, že schopnost funguje?
- Nevytváří řešení zbytečnou evidenci, administrativu nebo další paralelní systém?

Odpovědi uveďte v plánu před implementací. Otázku, která se na zadání nevztahuje, označte jako N/A s krátkým důvodem. Nic nerozšiřujte a mezeru nepřebalujte do nové dokumentace.

U rutinní údržby stačí jedna věta: co se opravuje a že se nemění účel, významy ani projektový rozsah. Pětibodový plán se nevyžaduje.

### Kdy zastavit

Zastavte a předložte věc vlastníkovi pouze tehdy, když:

- existuje skutečný rozpor s původním záměrem,
- zadání vyžaduje změnu původního záměru bez schválení vlastníka,
- významná nejasnost rozsahu může vést k nevratné nebo zásadní odchylce.

Zastavení není náhradou za odborný úsudek. Chybí-li odpověď, ale nejde o rozpor se záměrem ani o nevratnou odchylku, upozorněte na riziko a pokračujte v rozsahu zadání.

## Stav PROJECT_INTENT.md

Stav dokumentu čtěte vždy z hlavičky [PROJECT_INTENT.md](PROJECT_INTENT.md), ne z předpokladu ani z předchozí konverzace.

**Dokud dokument není schválen vlastníkem:**

- Je návrhová reference, nikoli mandát ani zdroj povinností.
- Agent jej používá k posouzení souladu zadání s původním záměrem.
- Agent z něj nevytváří nové schválené požadavky.
- Rozpory hlásí vlastníkovi a nevyřeší je sám.

**Po schválení vlastníkem:**

- Dokument je autoritativní pro účel projektu.
- Agent nesmí jeho význam tiše změnit.
- Změna účelu vyžaduje výslovné rozhodnutí vlastníka.

Stav dokumentu nemění agent; mění jej pouze vlastník.

## Completion Gate

Rozsah důkazu závisí na druhu úkolu.

**Významná metodická změna** vyžaduje:

- konkrétní uživatelský scénář,
- návrhový důkaz, že nová nebo opravená schopnost řeší zamýšlený problém,
- kontrolu složitosti a režie,
- přiznání toho, co zůstává empiricky neověřené.

Existence dokumentů, projití strukturálních kontrol, správné odkazy ani formální sémantická konzistence samy o sobě nestačí. Empirický přínos lze potvrdit až skutečným používáním; do té doby jej neuvádějte jako doložený.

**Technická nebo dokumentační údržba** vyžaduje odpovídající kontrolu: regresní test, strukturální kontrolu, ověření odkazů nebo potvrzení, že se nezměnila sémantika. Umělý životní scénář se pro opravu překlepu ani pro validační skript nevyžaduje.

## Handoff

Na konci významného úkolu uveďte krátkou kontrolu v tomto pořadí:

- **Alignment:** který bod `PROJECT_INTENT.md` byl naplněn.
- **Capability:** co nyní PLOS umí lépe.
- **Evidence:** jak bylo zlepšení ověřeno a čím.
- **Complexity:** co přibylo na režii nebo počtu kroků.
- **Gaps:** co ještě chybí a co zůstává neověřené.

Nepište, že je něco funkčně úplné, pokud to nebylo ověřeno. U rutinní údržby stačí uvést změněné soubory, způsob ověření a případný dopad na význam; pořadí Alignment až Gaps použijte, jen když je co vyplnit.

## Change Control

- Z vlastní iniciativy agent nemění [PROJECT_INTENT.md](PROJECT_INTENT.md), [slovník](glossary.md) (GLO-01), [doménový model](03-architecture/preliminary-domain-model.md) (DOM-01), [konceptuální architekturu](03-architecture/conceptual-architecture.md) (ARCH-01) ani normativní znění a stav [registru požadavků](02-requirements/high-level-requirements.md).
- Měnit je smí, jen když konkrétní změna leží v rozsahu výslovně schváleného zadání vlastníka. Výslovný mandát k jedné změně neznamená oprávnění k dalším.
- Před změnou identifikujte dopady na související dokumentaci: odkazy, odpovědnosti, scénáře, diagramy a ADR.
- Význam se nemění nepřímo, přes návody, diagramy ani reference. Nejasný mandát není oprávněním měnit architekturu.
- Bez explicitního pokynu vlastníka neprovádějte commit, push ani změnu rozsahu iterace.
- Při rozporu mezi zadáním, záměrem a architekturou rozpor oznamte, popište dopad a nabídněte varianty. Nerozhodujte místo vlastníka.
- Rozhodnutí o tom, co bude následovat, patří vlastníkovi projektu.
