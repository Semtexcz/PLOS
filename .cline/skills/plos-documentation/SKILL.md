---
name: plos-documentation
description: Vytváří, reviduje a audituje uživatelskou dokumentaci PLOS podle typů Diátaxis. Použij při psaní tutorialu, how-to návodu nebo referenční stránky PLOS, při rozhodování, jaký typ dokumentu vzniká, při kontrole srozumitelnosti a při auditu odkazů, terminologie a rozsahu.
---

# PLOS dokumentace

Tento skill shrnuje pravidla pro uživatelskou dokumentaci PLOS. Je nezávislý na poskytovateli LLM a na konkrétním nástroji. Uživatelská dokumentace je v češtině; ustálené anglické názvy konceptů se uvádějí v závorce.

Autoritativní zdroje jsou [GLO-01](../../../glossary.md) pro definice, [DOM-01](../../../03-architecture/preliminary-domain-model.md) pro vztahy a invarianty a [ARCH-01](../../../03-architecture/conceptual-architecture.md) pro odpovědnosti. Uživatelský dokument je provozní pohled, nikoli nový zdroj pravdy.

## 1. Vyberte typ dokumentu

Ptejte se, co čtenář právě dělá: učí se, nebo pracuje? Potřebuje jednat, nebo rozumět?

| Čtenář | Potřeba | Typ | Příklad v PLOS |
| --- | --- | --- | --- |
| učí se | projít bezpečně první zkušenost | tutorial | první týden |
| pracuje | dokončit konkrétní úkol | how-to | denní rozhodování, týdenní plánování |
| pracuje | dohledat pravidlo nebo význam | reference | provozní jádro |
| učí se | pochopit, proč to tak je | explanation | zatím nevzniká |

- Jeden dokument odpovídá na jednu otázku. Pokud odpovídá na dvě, rozdělte ho a propojte odkazy.
- Nevytvářejte prázdné kategorie jen proto, aby byly zastoupené. Explanation vzniká až z konkrétní potřeby.
- Tutorial vede jednu cestu a zaručuje výsledek. How-to předpokládá kompetenci a nabízí podmínky („když X, udělej Y“). Reference popisuje, nevypráví. Explanation vysvětluje souvislosti, nepostup.

## 2. Napište atomický dokument

Jeden dokument řeší jeden úkol nebo jeden vymezený pojem. Držte rozsah: how-to přibližně 400 slov, tutorial přibližně 800 slov.

**How-to** má pouze sekce s informační hodnotou:

1. Co tím čtenář vyřeší.
2. Kdy postup použít.
3. Vstupy a předpoklady.
4. Kroky.
5. Očekávaný výsledek.
6. Co dělat, když to nefunguje.
7. Odkazy na související postupy.

**Tutorial** obsahuje jeden souvislý příklad, viditelný výsledek po klíčových krocích, kontrolu dokončení a postup pro případ, že to nevyjde.

**Reference** obsahuje vstupy, pravidla, výstupy a meze. Nepoužívá vypravěčský tón a nevede čtenáře krok za krokem.

- Každý odstavec má jedno sdělení, zpravidla 2–4 věty.
- Vysvětlujte jen to, co čtenář potřebuje v dané situaci. Hlubší významy odkažte.
- Definici neopisujte do více dokumentů. Uveďte ji jednou v GLO-01 a odkazujte.
- U každého důležitého postupu ukažte konkrétní situaci a očekávaný výsledek.
- Pojmenujte selhání a výjimky. Čtenář musí vědět, co udělat, když postup nejde dokončit.

## 3. Propojte dokument s architekturou

- Uživatelský dokument nesmí předefinovat doménový pojem. Může ho zjednodušit pro danou situaci a odkázat na GLO-01.
- Anglický název uveďte při prvním použití v závorce: „závazek (Commitment)“. Dál používejte český termín.
- Odkazujte relativní cestou a popisným textem. Nepoužívejte odkaz „zde“.
- Rozlišujte normu, návrh a hypotézu. Tři úrovně používání jsou hypotéza; nesmějí být prezentovány jako schválená architektura.
- Nový doménový pojem nevytvářejte. Pokud dokument potřebuje význam, který v GLO-01 chybí, zapište mezeru jako návrh změny, ne jako tichou definici.
- Uživatelský text nesmí být v rozporu s invarianty DOM-01. Ověřte zejména vztah závazku a plánu, význam neznámého údaje a zákaz dvojího započtení.

## 4. Ověřte srozumitelnost

Proveďte ruční reader test. Představte si čtenáře, který PLOS nezná a neumí UML ani systémové inženýrství.

1. Co má udělat jako první?
2. Co má udělat dál?
3. Podle čeho pozná, že je hotov?
4. Co udělá, když mu chybí čas, energie nebo informace?
5. Které pojmy musí znát předem? Pokud ano, dokument je vysvětluje, nebo na ně odkazuje?

Dokument projde, když čtenář odpoví bez čtení architektury a bez dohadování. Zvlášť ověřte minimální úroveň používání: musí být použitelná bez rekonstrukce minulosti.

Při pochybnostech zkraťte, ne přidejte. Odstraňte věty, které by platily v libovolném projektu („je důležité mít přehled“), a nahraďte je konkrétní instrukcí, příkladem nebo odkazem.

## 5. Auditujte dokumentaci

Při auditu projděte dokument po dokumentu a zkontrolujte:

- odpovídá typ dokumentu skutečné potřebě čtenáře,
- dokument řeší jednu otázku a nemá prázdné sekce,
- kroky mají vstupy, pořadí, výsledek a řešení selhání,
- termíny odpovídají GLO-01 a jsou v celé sadě stejné,
- definice nejsou duplikované,
- příklady jsou konkrétní, fiktivní a označené jako ilustrativní,
- relativní odkazy a kotvy fungují,
- dokument neodporuje invariantům DOM-01,
- hypotézy nejsou vydávány za schválená rozhodnutí,
- dokument nepředpokládá software, aplikaci ani povinný zápis.

Audit je read-only, dokud uživatel neschválí opravy. Nálezy pište jako konkrétní místo a konkrétní změnu, ne jako obecné hodnocení.

## 6. Diagramy, příklady a odkazy

- Diagram použijte jen tehdy, když zkrátí vysvětlení rozhodnutí nebo posloupnosti. Jeden malý diagram na dokument je zpravidla dost.
- Uživatelský diagram pište s českými popisky a minimum uzlů. Zobrazuje rozhodnutí nebo posloupnost, ne doménový model ani UML schéma.
- Preferujte Mermaid nebo D2 ve zdrojovém bloku, aby byl text čitelný i bez rendereru.
- Diagram nesmí zavádět nový vztah, pojem nebo povinnost. Musí být v souladu s textem a s DOM-01.
- Popište, co diagram zobrazuje a co ne. Šipka neznamená automatické řízení ani časový tok, pokud to text neříká.
- Příklad uvádějte jako jeden souvislý případ s výsledkem. U složitějšího postupu přidejte i případ, kdy se krok nepovede.
- Odkazy pište relativně, s popisným textem. Ověřte existenci souboru i kotvy. Externí zdroj citujte jen tehdy, když je ověřený a relevantní.

## 7. Jazyk a styl

- Pište ve druhé osobě a činném rodě. Podmínku dejte před instrukci.
- Používejte krátké věty a krátké odstavce. Vyhýbejte se marketingu, slibům a abstraktním úvahám.
- Číslovaný seznam používejte pro posloupnost, odrážky pro ostatní výčty.
- Nepoužívejte skóre, metafory výkonu ani moralizování. Odpočinek a odklad jsou platné volby.
- Nadpisy pište větou s velkým písmenem jen na začátku, ne v titulkovém stylu.
- Název souboru nemusí vyjadřovat typ dokumentu; typ uveďte v záhlaví.

## 8. Co nedělat

- Nevytvářejte dokument jen kvůli symetrii čtyř kategorií.
- Nepřenášejte cizí skill ani šablonu do repozitáře. Pište původní adaptaci a citujte zdroj.
- Nepřidávejte doménové koncepty, ID ani nové režimy bez rozhodnutí a záznamu.
- Nepředpokládejte aplikaci, databázi, API ani povinné měření.
- Neopravujte text tak, že zeslabíte invariant nebo překryjete rozpor formulací.

## Zdroje a licence

Tento skill je původní adaptace. Nepřebírá doslovný text cizích skillů ani šablon.

| Zdroj | Co bylo použito | Licence nebo podmínka |
| --- | --- | --- |
| [Diátaxis](https://diataxis.fr/) | čtyři typy dokumentace a kompas volby | obsah © Daniele Procida; použita pouze myšlenka, bez kopírování |
| [writing-documentation-with-diataxis](https://github.com/lukehsiao/dotfiles/blob/main/dot_claude/skills/writing-documentation-with-diataxis/SKILL.md) | rozlišení tutorial, how-to, reference, explanation | repozitář pod Blue Oak 1.0; vendored skill má podle LICENSE.md upstream licenci Apache-2.0; použit koncept |
| [writing-technical-documentation](https://github.com/ramkumar-r-goml/agent-skills/blob/main/skills/writing-technical-documentation/SKILL.md) | evidence-based writing, atomicita, audit, odkazy, terminologie | MIT |
| [doc-coauthoring](https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md) | reader testing a iterativní zpřesnění | repozitář uvádí Apache-2.0 u mnoha skillů, samostatný kořenový LICENSE nalezen nebyl; použit koncept, bez subagentů |
| [The Good Docs Project — templates](https://github.com/thegooddocsproject/templates) | struktura tutorialu, how-to a reference | Zero-Clause BSD |
| [Google developer documentation style guide](https://developers.google.com/style) | srozumitelnost, skenovatelnost, krátké věty, konzistentní terminologie | CC BY 4.0 |
