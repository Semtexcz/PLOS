# Podněty, závazky a další kroky

**Typ dokumentu:** reference • **Stav:** návrh pro Iteration 3C.1; provozní pohled na [SS-03](../../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management) až [SS-06](../../03-architecture/conceptual-architecture.md#ss-06--review--adaptation), nikoli nová architektura • **Rozsah:** vyjasnění podnětu, možné výsledky a návaznost na existující doménu

Pravidla vyjasnění. Definice obsahuje [GLO-01](../../glossary.md), vztahy a invarianty [DOM-01](../../03-architecture/preliminary-domain-model.md). Postup popisuje [Zpracování nového podnětu](../how-to/process-input.md).

## Vstupy vyjasnění

Vstupem je zachycený podnět (Captured Input): žádost, informace, nápad, signál nebo povinnost, která není vyjasněná. Může být neúplný, rozporný nebo zastaralý. Vyjasnění je krátké posouzení, ne formulář: co podnět znamená, zda vyžaduje jednání a zda už existuje závazek, projekt nebo krok.

## Možné výsledky vyjasnění

| Výsledek | Co vzniká | Co nevzniká |
| --- | --- | --- |
| Neakční informace | Uzavřený nebo uložený obsah | Závazek, projekt ani krok |
| Nezávazná možnost | Kandidát s podmínkou návratu | Nárok na kapacitu ani aktivní práce |
| Existující závazek nebo projekt | Odkaz na tutéž věc | Nová identita ani duplicitní závazek |
| Nový závazek | Odpovědnost s předmětem, původem a podmínkami | Automatický projekt, termín ani alokace |
| Projekt | Koordinace práce s kritériem dokončení | Závazek, cíl ani nárok na kapacitu |
| Další krok | Konkrétní jednání s časem nebo podmínkou | Dokončení závazku ani projektu |
| Čekání | Závislost s podmínkou návratu | Dokončení ani zrušení odpovědnosti |
| Odmítnutí nebo zánik | Ukončená záležitost s důvodem | Zrušení odpovědnosti, která trvá jinde |

Výsledky jsou přípustné možnosti, ne povinný katalog. Jeden podnět může vyústit ve víc výsledků, například v závazek a projekt.

## Podnět, závazek, projekt a další krok

- **Podnět** je nevyjasněný obsah. **Závazek** je rozpoznaná odpovědnost. **Projekt** je organizace práce s rozpoznatelným dokončením. **Další krok** je konkrétní jednání, přímo proveditelné za známých podmínek.
- Závazek nepotřebuje projekt ani cíl; projekt může existovat bez závazku; krok nemusí patřit k projektu ([INV-07](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).
- Projekt nevzniká z počtu kroků, ale z potřeby koordinovat rozsah nebo závislosti.
- Žádost, doporučení, výběr ani zařazení do plánu závazek nevytváří ([INV-02](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)). Vzniká přijetím odpovědnosti nebo existující povinností.

## Čekání, odklad, dokončení a zánik

| Situace | Co se děje | Co platí dál |
| --- | --- | --- |
| Čekání | Jednání závisí na druhém nebo vnější události | Odpovědnost a podmínka návratu; čekání není dokončení |
| Odklad | Vědomé rozhodnutí odložit provedení s důvodem | Odpovědnost trvá; odklad je samostatné rozhodnutí |
| Dokončení | Předmět je splněn a doložen pozorováním | Závazek může skončit; práce nedokládá zamýšlený výsledek ([INV-05](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)) |
| Zánik | Platné přejednání, souhlas protistrany nebo jiný skutečný konec povinnosti | Odpovědnost končí; úmysl ani změna plánu nestačí ([INV-06](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)) |

Čekání na odpověď není dokončení. Dokud nedorazí odpověď nebo jiná rozhodná událost, odpovědnost trvá; podmínka návratu je součástí vyjasnění. Neznámý stav není dokončený ani zrušený ([INV-11](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).

## Identita a odpovědnost

Opakovaný podnět odkazuje na tutéž věc, pokud má společný původ. Více pohledů — denní přehled, portfolio, plán — nezvyšuje počet závazků ani práci ([INV-03](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)/15). Revize zachová původ a důvod odpovědnosti ([INV-04](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)).

Změna projektu, cíle, strategie ani plánu závazek neruší ([INV-06](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)). Nejasná totožnost zůstane nerozhodnutá, ne sloučená ani zdvojená.

## Návaznost na SS-03 až SS-06

| Odpovědnost | Co přebírá z vyjasnění |
| --- | --- |
| [SS-03](../../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management) výběr a portfolio | Závazek, projekt nebo možnost posoudí jako kandidáta; výběr není alokace |
| [SS-04](../../03-architecture/conceptual-architecture.md#ss-04--planning--capacity-management) proveditelnost a kapacita | Nový nebo ohrožený závazek může vyvolat nové posouzení kapacity |
| [SS-05](../../03-architecture/conceptual-architecture.md#ss-05--execution--commitment-management) zachycení a provedení | Vyjasnění, další kroky, projekty, čekání a potřeba přejednání |
| [SS-06](../../03-architecture/conceptual-architecture.md#ss-06--review--adaptation) reflexe a adaptace | Nevyjasněné podněty, pozorování a rozhodnutí k přehodnocení |

Portfolio ani plán nevytváří druhou evidenci; strategická možnost sama nespotřebovává kapacitu.

## Invarianty

- [INV-02](../../03-architecture/preliminary-domain-model.md#katalog-invariantů) — zachycení ani doporučení nevytváří závazek.
- [INV-03](../../03-architecture/preliminary-domain-model.md#katalog-invariantů)/15 — více pohledů nezakládá novou identitu ani dvojí započtení.
- [INV-06](../../03-architecture/preliminary-domain-model.md#katalog-invariantů) — změna plánu, projektu či strategie závazek neruší.
- [INV-07](../../03-architecture/preliminary-domain-model.md#katalog-invariantů) — závazek, projekt a krok jsou vzájemně volitelné.
- [INV-11](../../03-architecture/preliminary-domain-model.md#katalog-invariantů) — neznámé není dokončené, zrušené ani nula.

## Výjimky a neúplné informace

- Původ závazku nemusí být jasný. Přiznejte nejistotu a držte odpovědnost do vyjasnění.
- Závazek lze splnit částečně nebo přejednat pro část rozsahu.
- Odpovědnost může existovat bez vašeho přijetí, například ze zákona; rozpoznání nevytváří vznik.
- Vyjasnění může skončit „zatím nerozhodnuto“ s podmínkou návratu.
- Odmítnutí po prvotním zájmu je rozhodnutí, ne ztráta přehledu.

## Meze

Text nezavádí nové entity, povinné stavy ani univerzální workflow engine. Nepředepisuje zápis, aplikaci ani databázi. Pojmenování výsledků je popis možností, ne katalog. Otevřené zůstávají [OQ-02](../../05-decisions/open-questions.md#otevřené-otázky) a [OQ-03](../../05-decisions/open-questions.md#otevřené-otázky).

## Autoritativní zdroje

[GLO-01](../../glossary.md) pro definice, [DOM-01](../../03-architecture/preliminary-domain-model.md) pro identitu, vztahy [DR-03](../../03-architecture/preliminary-domain-model.md#katalog-vztahů)/04/08 a invarianty, [ARCH-01](../../03-architecture/conceptual-architecture.md) pro odpovědnosti [SS-03](../../03-architecture/conceptual-architecture.md#ss-03--goal--portfolio-management) až [SS-06](../../03-architecture/conceptual-architecture.md#ss-06--review--adaptation), [provozní jádro](operational-kernel.md) a [strategická návaznost](strategic-bridge.md) pro provozní rámec.
