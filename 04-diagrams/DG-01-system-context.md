# DG-01 — System Context Diagram

**Účel:** vymezit System-of-Interest a dvojí roli člověka jako rozhodovací autority a vykonavatele praktik. **Dokumentace:** [CH-01](../01-foundations/system-charter.md), [ADR-01](../05-decisions/decision-log.md#adr-01--hybridní-architektura-funkčních-odpovědností).

## Zdrojová definice

```mermaid
flowchart LR
    human["Člověk: autorita a vykonavatel praktik"]
    others["Další lidé a instituce"]
    environment["Životní prostředí a vnější vlivy"]
    living["Skutečné jednání a prožívání"]
    support["Volitelný podpůrný člověk"]
    subgraph plos["Hranice SoI: metodika PLOS"]
        guidance["Příprava voleb a plánování"]
        records["Orientace v závazcích a záměrech"]
        reflection["Reflexe a adaptace"]
        records -->|"podklady"| guidance
        reflection -->|"návrhy aktualizace"| guidance
        reflection -->|"podněty ke změně záznamů"| records
    end
    human -->|"hodnoty, potřeby, rozhodnutí"| guidance
    guidance -->|"varianty a jejich důsledky"| human
    human -->|"podněty a uznané závazky"| records
    records -->|"přehled a další kroky"| human
    human -->|"jednání"| living
    living -->|"zkušenost a pozorování"| human
    human -->|"dostupná evidence"| reflection
    reflection -->|"interpretace k posouzení"| human
    others -->|"žádosti a povinnosti"| human
    human -->|"dohody a přejednání"| others
    environment -->|"okolnosti a omezení"| human
    environment -->|"vlivy na výsledky"| living
    support -->|"dohodnutá pomoc"| human
```

## Prvky a vztahy

Uvnitř hranice jsou skupiny funkcí metodiky, nikoli úplné členění na SS. Člověk funkce vykonává, ale zůstává jako osoba mimo SoI. Šipky označují pojmenované interakce; nevyjadřují automatizaci ani kontrolu druhých lidí. Dohoda s protistranou a její následky vznikají mimo PLOS, který drží jejich rozpoznanou reprezentaci.

## Předpoklady a omezení

[ASM-01](../01-foundations/system-charter.md#předpoklady-a-omezení) až [ASM-04](../01-foundations/system-charter.md#předpoklady-a-omezení); model nezobrazuje všechny stakeholdery jednotlivě. Podpůrná role nemá automatický přístup k záznamům. Budoucí software není zakreslen, protože není součástí současné systémové hranice. „Skutečné jednání“ není technický regulovaný objekt.
