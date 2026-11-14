# System Charter

**ID:** CH-01 • **Stav:** návrh v0.2, minimální upřesnění SoI v I2 (ADR-07); normativní původ rozlišuje [README](../README.md).

## Problém, mise a účel

Člověk může vědět, co je pro něj důležité, aniž má spolehlivý způsob převodu tohoto směru do využití omezené kapacity. Operativní nároky, proměnlivé okolnosti a nejasné závazky mohou vytlačit důležité záměry. Naopak příliš rigidní plán může poškozovat regeneraci, vztahy a schopnost přehodnotit vlastní směr.

**Mise:** vytvořit referenční metodiku pro propojení hodnot, vize, strategie, cílů, portfolia, plánování, jednání, reflexe a adaptace. **Účel:** podpořit vědomá a vysvětlitelná rozhodnutí v reálných životních podmínkách, nikoli maximalizovat výkon. Jde o návrhový záměr, nikoli o doložený účinek.

## System-of-Interest a hranice

**System-of-Interest (SoI):** PLOS jako soustava pravidel, pojmů, dostupných podkladů poznání a člověkem vykonávaných řídicích praktik. Zahrnuje rozpoznání potřeb, přípravu voleb, plánování, sledování závazků a vyhodnocování zkušeností. Nezahrnuje celý život člověka.

Člověk je vůči metodice externí rozhodovací autoritou a zároveň vykonavatelem jejích praktik. Tato dvojí role je záměrná: funkce patří do metodiky, člověk jako osoba se nestává její komponentou. Samotná životní činnost a její následky probíhají mimo hranici SoI. Subsystém Execution & Commitment Management organizuje jednání a zachycuje jeho stav; nevykonává život za člověka.

| Uvnitř PLOS | Překračuje hranici | Mimo PLOS |
| --- | --- | --- |
| Vyjádření hodnot, oblastí a záměrů | Člověkem zvolené hodnoty, potřeby a změny směru | Prožívání, identita, zdraví a autonomie osoby |
| Varianty, doporučení, odůvodnění, evidence rozhodnutí | Doporučení ven; rozhodnutí a souhlas člověka dovnitř | Konečná volba a odpovědnost člověka |
| Zpracování podnětů a sledování závazků | Požadavky jiných lidí, dohody, termíny, informace o důsledcích | Protistrany, jejich rozhodování, skutečné povinnosti |
| Posouzení kapacity a alokací | Odhady, subjektivní pozorování a zpětná vazba | Fyzická dostupnost zdrojů a skutečné jednání |
| Reflexe, návrhy změn a kontinuita záznamů | Zkušenost a pozorované výsledky | Nepředvídatelné události, společenské a přírodní podmínky |

PLOS nevyžaduje software nyní ani v budoucnu. Je samostatně vykonatelný člověkem; případné analogové, digitální či kombinované prostředky neurčují jeho doménovou sémantiku. Evidence je významový podklad oddělený od média a může existovat pouze v lidské paměti. Konceptuální nezbytnost neznamená povinný samostatný záznam. Reference, kalendář nebo papír jsou možné nosiče informací, nikoli předepsané komponenty. PLOS neovládá jiné lidi a nezaručuje výsledky.

## Stakeholdeři a aktéři

| ID | Role | Zájem a oprávnění | Působení |
| --- | --- | --- | --- |
| ST-01 | Uživatel / vlastník PLOS | Smysl, autonomie, únosnost; konečná rozhodovací autorita | Hlavní aktér ve všech režimech |
| ST-02 | Blízcí a další dotčení lidé | Dopady na vztahy, dohody a společnou kapacitu | Zdroje potřeb, dohody a zpětné vazby; žádný automatický přístup k osobním záznamům |
| ST-03 | Protistrany závazků, instituce | Spolehlivost dohod, termínů a případných změn | Vnější požadavky a odpovědi; PLOS jejich pravidla nemění |
| ST-04 | Volitelný podpůrný člověk | Pomoc při reflexi nebo obnově režimu | Jedná jen v rozsahu výslovné dohody s uživatelem |
| ST-05 | Správce referenční metodiky | Sémantická konzistence, změny a návaznost verzí | Návrhová role; bez autority nad životními volbami ST-01 |

Role se mohou překrývat. Žádné rozhovory s těmito stakeholdery zatím neproběhly. Jejich potřeby jsou odvozeny ze zadání, ne z terénního výzkumu.

## Provozní kontext

Jedna osoba pracuje s proměnlivým časem, energií, financemi, pozorností a závislostmi na druhých. Život obsahuje činnosti strategické, udržovací, neodkladné i spontánní. Část výsledků je opožděná nebo obtížně pozorovatelná. Plánování je přerušitelné; neexistuje předpoklad stabilního týdne, úplné evidence ani denního používání. Pravidelné horizonty doplňují revize vyvolané událostí.

## Cíle a necíle

| Cíl systému | Co tento cíl neznamená |
| --- | --- |
| Vysvětlit důležité volby vzhledem k hodnotám, potřebám a závazkům | Povinně odvozovat každou činnost ze strategického cíle |
| Převést záměry do proveditelných voleb a zohlednit náklady obětované příležitosti | Najít jediný matematicky optimální život |
| Zachovat běžnou péči a důvěryhodné závazky při změně strategie | Automaticky rušit závazky nebo vymazávat historii |
| Učit se a měnit plány bez morálního hodnocení člověka | Léčit, diagnostikovat nebo nahradit odbornou péči |
| Fungovat i s omezenou kapacitou a po přerušení | Povinně dokončit resty před návratem |

Necíle Iteration 1 a 2: software, UI, technologie, datové schéma, úplná procesní a stavová specifikace, číselné optimalizační algoritmy, definitivní metriky a personalizace podle skutečného života uživatele.

## Předpoklady a omezení

| ID | Neověřený předpoklad | Dopad neplatnosti / postup |
| --- | --- | --- |
| ASM-01 | Uživatel chce alespoň někdy vědomě reflektovat své volby | Metodiku lze odložit; nelze vynucovat adopci ani tvrdit účinek |
| ASM-02 | Lze získat alespoň hrubou informaci o kapacitě a kritických závazcích | Pracovat s „neznámé“, omezit nové plánované nároky; H-02 |
| ASM-03 | Pokud člověk potřebuje kontinuitu explicitních záznamů, má dostupný způsob jejich uchování; nejde o podmínku používání PLOS | Bez záznamů může orientace i obnova vycházet z aktuálního poznání; historie nemusí být rekonstruovatelná |
| ASM-04 | O některých nárocích lze vyjednávat nebo je odkládat | Rozlišit ovlivnitelné a neovlivnitelné; přiznat neřešitelný konflikt, nikoli vyrábět kapacitu |
| ASM-05 | Šest navržených funkcí lze vykonávat s únosnou režií | Zjednodušit formu a četnost; H-01 a R-01 |

Omezení jsou normativně evidována jako CON-01 až CON-03 v [požadavcích](../02-requirements/high-level-requirements.md). P1–P11 platí napříč systémem. PLOS nemůže změnou záznamu odstranit vnější povinnost nebo její důsledky.

## Předběžná kritéria úspěchu

| ID | Kritérium | Jak se posoudí a kdy |
| --- | --- | --- |
| SC-01 | Člověk umí vysvětlit vazbu důležité volby na vlastní důvody a může ji změnit | UC-01 a UC-06 při návrhové verifikaci; srozumitelnost později s uživatelem |
| SC-02 | Návrh připustí běžnou péči bez strategického cíle a ukáže konflikt kapacity | UC-02 a UC-03; žádné skryté předpoklady neomezených zdrojů |
| SC-03 | Přerušení plánování nebrání zjednodušenému návratu | UC-04; praktickou únosnost ověřit v pilotu |
| SC-04 | Nová strategie nepřepisuje existující dohody a důvody minulých voleb | UC-05; změnu lze vysledovat bez fiktivního zrušení povinnosti |
| SC-05 | Review rozliší vykonanou činnost od změny v životě a dovolí nejistotu | UC-07; nelze tvrdit kauzalitu jen z korelace |
| SC-06 | Režie metodiky je pro uživatele přijatelná a nevytěsňuje regeneraci | UC-08 + budoucí kvalitativní validace; mez přijatelnosti zatím OQ-03 |

Splnění dokumentačních quality gates není splněním SC-01 až SC-06 v reálném životě. Současný stav zachycuje [review report](../07-review/architecture-review-report.md). Kontext viz [DG-01](../04-diagrams/README.md#dg-01).

**Změna I2:** ADR-07 zpřesňuje SoI a podmíněnost ASM-03 podle zadání. Mise, hranice skutečného jednání, role člověka a šest funkčních odpovědností se nemění. Konkrétní provozní forma není navržena.
