# Glossary

**ID:** GLO-01 • **Verze:** 0.2 • **Stav:** D — autoritativní definice Domain Architecture, Iteration 2, 2026-11-14. Anglické názvy a DC-ID jsou stabilní. Klasifikace, identita, vztahy a invarianty patří do [DOM-01](03-architecture/preliminary-domain-model.md); zde je jediný zdroj definic. Koncept není předepsaný záznam ani softwarová třída.

## Doménové koncepty

| ID | Pojem | Význam v PLOS | Nezaměňovat s |
| --- | --- | --- | --- |
| DC-01 | Value / Hodnota | Člověkem volená kvalita či směr jednání, který lze žít průběžně. | Dokončitelným cílem či skóre osoby. |
| DC-02 | Personal Principle / Osobní princip | Přijaté, revidovatelné vodítko člověka pro opakované rozhodování. | Architektonickými [P1](01-foundations/design-principles.md)–[P11](01-foundations/design-principles.md). |
| DC-03 | Life Area / Životní oblast | Trvající kontext života pro rozlišování potřeb péče a změn; oblasti se mohou překrývat. | Projektem či povinnou taxonomií života. |
| DC-04 | Care Need / Potřeba péče | Rozpoznaná potřeba udržování či obnovování podmínek života, nezávislá na volbě konkrétního způsobu péče. | Automatickým závazkem, úkolem nebo cílem zlepšování. |
| DC-05 | Vision / Vize | Revidovatelná představa žádoucího celkového směru života. | Předpovědí nebo závazným plánem. |
| DC-06 | Scenario / Scénář budoucnosti | Možný vývoj okolností a cest používaný při zvažování alternativ; nemusí být žádoucí ani zvolený. | Scénářem UC/SV, strategií nebo slibem. |
| DC-07 | Strategy / Strategie | Provizorní soubor voleb o směru, cestách a tom, čemu se nevěnovat, s důvody a předpoklady; může být kandidátní nebo člověkem přijatý pro určitý rozsah. | Každým scénářem či pouhým seznamem cílů. |
| DC-08 | Assumption / Předpoklad | Nejisté tvrzení o podmínkách či souvislostech, používané nebo zkoumané při rozhodování. | Pozorováním; ASM jsou předpoklady návrhu, nikoli tyto doménové předpoklady. |
| DC-09 | Experiment / Experiment | Ohraničený poznávací záměr s otázkou nebo zkoumaným předpokladem a rozpoznatelnou mezí ukončení získávání zkušenosti. | Organizací práce, zárukou poznatku nebo změny života. |
| DC-10 | Objective / Cíl | Rozlišitelný záměr dosáhnout konkrétní žádoucí změny s horizontem a způsobem posouzení, který může být kvalitativní a postupně zpřesňovaný. | Projektem či pouhým výkonem činnosti. |
| DC-11 | Intended Outcome / Zamýšlený výsledek | Obsah žádoucího stavu nebo změny v kontextu a horizontu, včetně smyslu, podle něhož má být posouzen; může vyjadřovat i očekávaný přínos záměru. | Pozorováním, jistou předpovědí úspěchu či vykonanou prací. |
| DC-12 | Observed Outcome / Pozorovaný výsledek | Role Observation, která popisuje pozorovaný stav či změnu relevantní pro posuzovaný záměr nebo potřebu, včetně nečekaného účinku. | Vyhodnocením dosažení cíle či kauzálním vysvětlením. |
| DC-13 | Output / Výstup práce | Artefakt, poskytnutá služba nebo dokončená činnost rozpoznaná v popisu provedení. | Účinkem této práce; dokončení služby nedokazuje prospěch. |
| DC-14 | Portfolio / Portfolio | Rozhodovací pohled na kandidátní a vybrané záměry i ostatní nároky, jejich souběh a důvody výběru. | Dalšími kopiemi projektů či pravomocí rušit povinnosti. |
| DC-15 | Project / Projekt | Ohraničená organizace související práce se samostatně rozpoznatelným rozsahem a kritériem dokončení práce. | Cílem, experimentální otázkou, závazkem nebo trvalou péčí. |
| DC-16 | Commitment / Závazek | Rozpoznaná odpovědnost něco vykonat, zajistit nebo udržovat, založená dobrovolným přijetím nebo existující povinností; má předmět, původ a podmínky splnění či zániku, i když jsou známy jen částečně. | Žádostí, alokací či interním přáním zrušit vnější povinnost. |
| DC-17 | Captured Input / Zachycený podnět | Ještě nevyjasněný obsah žádosti, informace, nápadu či signálu, který člověk zachytil. | Automaticky přijatým závazkem; zachycení nevyžaduje zápis. |
| DC-18 | Next Action / Další krok | Konkrétní zamýšlené jednotlivé jednání, které je při splnění známých podmínek kontextu přímo proveditelné bez dalšího rozkladu. | Skutečným provedením, čekáním, slibem nebo celým opakovaným vzorcem. |
| DC-19 | Routine / Rutina | Vědomě zvolený opakovaný způsob činnosti či péče s rozpoznatelným účelem a podmínkami opakování. | Součtem všech budoucích výskytů nebo automatickým návykem. |
| DC-20 | Habit / Návyk | Interpretovaný ustálený vzorec chování v kontextu, žádoucí i nežádoucí; pravidelnost sama nedokazuje automatizaci. | Vědomým plánem opakování. |
| DC-21 | Capacity / Kapacita | Dostupnost konkrétního zdroje v určitém horizontu a kontextu, posuzovaná s přiznanou mírou poznání. | Nárokem, alokací, spotřebou či prioritou. |
| DC-22 | Planned Capacity / Plánovaná kapacita | Role posouzení Capacity jako odhadu dostupnosti použitého při přípravě určitého plánu. | Plánovaným využitím nebo garantovanou dostupností. |
| DC-23 | Actual Capacity / Skutečná kapacita | Role posouzení Capacity jako aktuální či zpětně zjišťované dostupnosti na základě zkušenosti; může zůstat nejistá. | Skutečnou spotřebou nebo dokonale známou realitou. |
| DC-24 | Allocation / Alokace | Zamýšlené vyčlenění zdroje pro vymezený nárok v horizontu a kontextu, jako návrh nebo člověkem zvolená součást plánu. | Dostupností zdroje, spotřebou či přijetím závazku. |
| DC-25 | Plan / Plán | Revidovatelná hypotéza o výběru a uspořádání jednání a alokací pro horizont a kontext, i s vědomě nealokovaným prostorem. | Slibem, strategií či přepisem minulých skutečností. |
| DC-26 | Conditional Response / Podmíněná reakce | Člověkem zvolená možná odpověď na rozpoznatelnou situaci či překážku ve vztahu k záměru; může být jednáním, myšlenkou či přehodnocením. | Automatickou instrukcí nebo celou metodou WOOP. |
| DC-27 | Observation / Pozorování | Dostupné svědectví zkušenosti, události, provedení nebo stavu s kontextem, časovým určením a omezenou jistotou, i pouze v paměti člověka. | Médiem záznamu, absolutní pravdou nebo vysvětlením příčiny. |
| DC-28 | Metric / Metrika | Volitelně vymezený způsob získání nebo porovnávání opakovatelných údajů pro konkrétní rozhodovací otázku. | Údajem, cílem systému nebo automatickým výkladem příčiny. |
| DC-29 | Review / Reflexe a přezkoumání | Ohraničené posouzení pozorování, záměrů a okolností, při kterém člověk vytváří či reviduje interpretace a podklady další volby. | Reportem, automatickým rozhodnutím nebo povinným rituálem. |
| DC-30 | Decision / Rozhodnutí | Volba člověka v rozsahu a kontextu s relevantním důvodem, včetně pokračování, odmítnutí doporučení nebo odložení věcné volby. | Doporučením nebo potvrzením protistrany. |
| DC-31 | Resource Demand / Zdrojový nárok | Potřeba konkrétního zdroje vyvolaná vymezeným rozsahem práce či péče v horizontu a kontextu; může být odhadnutá, kvalitativní či neznámá. | Samostatnou kopií práce, alokací či automaticky aditivním číslem. |
| DC-32 | Interpretation / Interpretace | Odvozený, člověkem učiněný výklad pozorování ve vztahu k záměrům, předpokladům a okolnostem, včetně závěru „nelze rozhodnout“. | Pozorováním, jistým kauzálním důkazem nebo závaznou volbou. |
| DC-33 | Recommendation / Doporučení | Návrh možné volby s důvody k posouzení člověkem. | Decision; zdrojem může být sám člověk, nikoli nutně jiná osoba či stroj. |
| DC-34 | Internal Obstacle / Vnitřní překážka | Role popisu vlastního prožívání či chování jako něčeho, co brání určitému záměru; rozpoznání může být pozorováním nebo nejistým předpokladem. | Vnějším omezením, diagnózou či nedostatkem vůle. |
| DC-35 | External Constraint / Vnější omezení | Role popisu okolností mimo přímou volbu člověka, které omezují proveditelnost záměru. | Vnitřní překážkou odstranitelnou pouhou podmíněnou reakcí. |
| DC-36 | WIP / Rozpracovanost | Odvozený pohled na aktuálně zahájenou a dosud neukončenou práci ve vymezeném rozsahu. | Všemi zachycenými možnostmi nebo univerzálním limitem. |

## Aliasy a pojmy architektonického jazyka

**Outcome / Výsledek** z v0.1 zůstává pouze souhrnným názvem rodiny významů, bez samostatné identity a dalšího DC. V každém tvrzení se určí Intended Outcome nebo Observed Outcome. Zamýšlený obsah a jeho pozorování jsou různé sémantické koncepty, nikoli zaměnitelné stavy jedné položky. Experimentální „výsledek“ se rozlišuje na Observation a Interpretation. „Skutečné provedení / spotřeba“ je předmět Observation, nikoli nový druh plánu.

WOOP **Wish** je role zvoleného záměru (Objective, Care Need nebo konkrétního záměru jednání); **Outcome** je Intended Outcome vyjadřující očekávaný přínos tohoto přání; **Obstacle** je Internal Obstacle a **Plan** je Conditional Response. Nejde o další čtyři identity ani automatické zavedení Objective pro péči. Přesné vazby a omezení jsou v [DOM-01](03-architecture/preliminary-domain-model.md).

„Úkol“ je neformální výraz; místo něj se rozlišuje Commitment a Next Action. „Nárok“ znamená DC-31, pokud jde o zdroj; „taktika“ 12 Week Year podle kontextu znamená krok, rutinu nebo dílčí plán. „Evidence“ znamená dostupný podklad poznání nebo orientace; není synonymem úložiště a nemusí být úplná ani zapsaná. Zdroj, horizont, kontext a jednotka jsou významové kvalifikátory, ne další povinné objekty.

| Pojem mimo katalog domény | Význam |
| --- | --- |
| Design Principle / Návrhový princip | Pravidlo návrhu metodiky, zde [P1](01-foundations/design-principles.md)–[P11](01-foundations/design-principles.md); nikoli osobní přesvědčení. |
| Rolling Horizon / Posuvný horizont | Postupné zpřesňování nejbližšího plánu a revize vzdálenějších záměrů; nikoli automatický přesun restů. |
| Traceability / Trasovatelnost | Schopnost vysvětlit relevantní původ a návaznost volby, požadavku či činnosti; nikoli povinný kompletní strom. |
| Verification / Verifikace | Posouzení souladu artefaktů nebo systému se specifikací; není důkazem životního přínosu. |
| Validation / Validace | Posouzení potřeb a fungování v zamýšleném použití; nenahrazuje ji kontrola odkazů nebo návrhových scénářů. |

Klasifikace všech 36 DC v [DOM-01](03-architecture/preliminary-domain-model.md) pokrývá i rozlišovací a odvozené pojmy. Aliasy a pojmy jazyka návrhu nejsou dalšími doménovými koncepty.
