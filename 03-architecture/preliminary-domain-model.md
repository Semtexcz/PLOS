# Domain Architecture v0.2 — stabilizovaný konceptuální model

**ID:** DOM-01 • **Iterace:** 2 • **Datum:** 2026-11-14 • **Stav:** D — stabilizováno pro návrhovou návaznost, nikoli empiricky validováno nebo schváleno vlastníkem. Cesta souboru zůstává kvůli kontinuitě v0.1. Definice jsou výhradně v [GLO-01](../glossary.md); tento dokument je autoritou pro klasifikaci, identitu, vztahy a invarianty. [Audit a review](../07-review/architecture-review-report-iteration-2.md), [sémantické případy](../07-review/semantic-validation-report.md), [diagramy](../04-diagrams/README.md).

## Rozsah a pravidla čtení

PLOS je metodika vykonávaná člověkem. Koncepty mohou být pouze rozlišeny v úvaze; zápis, identifikátor instance, databáze ani automatizace nejsou předpokladem. Identity níže odpovídají otázce „je to stále tentýž záměr, slib nebo případ?“, nikoli primárnímu klíči. [SS-01](conceptual-architecture.md#ss-01--values--vision-management) až [SS-06](conceptual-architecture.md#ss-06--review--adaptation) zůstávají funkčními odpovědnostmi [ADR-01](../05-decisions/decision-log.md#adr-01--hybridní-architektura-funkčních-odpovědností). Člověk rozhoduje, i když je vlastníkem významu určitý SS.

**Core** je význam nezbytný pro základní orientaci, volbu a učení; všechny jeho instance nemusí být přítomny v každé situaci. **Contextual** je potřebný až v určité situaci či režimu. **Optional** zlepšuje některé postupy. **Derived** je odvozený pohled, role nebo výklad jiných konceptů bez nové samostatné identity. Odvození výkladu vyžaduje lidský úsudek a nemusí být jednoznačné; neznamená automatický výpočet ani jistotu. Derived neříká, že podklad lze vymyslet: Actual Capacity vyžaduje zkušenost, nikoli pouhé převzetí Planned Capacity.

## Katalog konceptů: nutnost, identita a důvod

Identita **I** = samostatná významová kontinuita; **V** = obsah rozlišený významem a kontextem, bez autonomní kontinuity; **R** = role/pohled s identitou podkladu. „Rozlišit“ v posledním sloupci není požadavek samostatně zapisovat. Žádný koncept nemá univerzálně povinnou explicitní evidenci; významné původy a změny musí být vysvětlitelné v rozsahu dostupných informací (INV-03/04). Přijatelná hloubka zůstává [OQ-03](../05-decisions/open-questions.md#otevřené-otázky).

| ID / koncept (definice [GLO-01](../glossary.md)) | Kategorie a proč | Identita / hranice kontinuity | Vlastník / konceptuální potřeba explicitnosti |
| --- | --- | --- | --- |
| [DC-01](../glossary.md#doménové-koncepty) Value | Core — důvod voleb přesahující výkon | I: význam volené kvality; přejmenování ji nemění, jiná kvalita je jiná hodnota | [SS-01](conceptual-architecture.md#ss-01--values--vision-management); může zůstat implicitní |
| [DC-02](../glossary.md#doménové-koncepty) Personal Principle | Optional — zkracuje opakované rozhodování | I: vodítko pro tutéž otázku; změna pravidla je rozlišitelná revize | [SS-01](conceptual-architecture.md#ss-01--values--vision-management); žádný povinný seznam |
| [DC-03](../glossary.md#doménové-koncepty) Life Area | Contextual — širší přehled různých kontextů péče | I: rozsah kontextu; přejmenování zachová, rozdělení vytvoří nové kontexty | [SS-01](conceptual-architecture.md#ss-01--values--vision-management); péče nevyžaduje pojmenovanou oblast |
| [DC-04](../glossary.md#doménové-koncepty) Care Need | Core — legitimita udržování života | I: co potřebuje péči a proč; změna rutiny potřebu nenahradí | [SS-01](conceptual-architecture.md#ss-01--values--vision-management); rozpoznání potřeby stačí |
| [DC-05](../glossary.md#doménové-koncepty) Vision | Optional — sjednocuje dlouhodobou orientaci | I: uvažovaná představa směru; alternativní představy mohou koexistovat | [SS-01](conceptual-architecture.md#ss-01--values--vision-management); není vstupní podmínkou |
| [DC-06](../glossary.md#doménové-koncepty) Scenario | Optional — zviditelní možné budoucnosti | I: uvažovaný vývoj a podmínky; změna zásadních podmínek odliší variantu | [SS-02](conceptual-architecture.md#ss-02--strategy--experimentation); nevyžadovat úplný soubor |
| [DC-07](../glossary.md#doménové-koncepty) Strategy | Contextual — vědomá volba dlouhodobé cesty | I: soubor voleb pro vymezenou rozhodovací otázku; přijetí nemění identitu kandidáta | [SS-02](conceptual-architecture.md#ss-02--strategy--experimentation); přijetí se odliší od návrhu |
| [DC-08](../glossary.md#doménové-koncepty) Assumption | Contextual — práce s rozhodovací nejistotou | I: tvrzení a podmínky platnosti; změna důvěry není nové tvrzení | [SS-02](conceptual-architecture.md#ss-02--strategy--experimentation); explicitní jen pro potřebné rozlišení |
| [DC-09](../glossary.md#doménové-koncepty) Experiment | Contextual — cílené zjišťování | I: poznávací otázka a ohraničený pokus; nový pokus není přepsání předchozího | [SS-02](conceptual-architecture.md#ss-02--strategy--experimentation); otázka a mez ukončení musí být srozumitelné |
| [DC-10](../glossary.md#doménové-koncepty) Objective | Contextual — řízení konkrétní změny | I: záměr změny, kontext a smysl úspěchu; pravidla změny níže | [SS-03](conceptual-architecture.md#ss-03--goal--portfolio-management); základní péče se obejde bez něj |
| [DC-11](../glossary.md#doménové-koncepty) Intended Outcome | Core — rozliší chtěné od zjištěného | V: obsah záměru a kontext posouzení, nikoli další samostatný cíl | [SS-03](conceptual-architecture.md#ss-03--goal--portfolio-management) pro cíle; jinde vlastník příslušného záměru |
| [DC-12](../glossary.md#doménové-koncepty) Observed Outcome | Derived — Observation v roli pozorovaného účinku | R: totožné pozorování, žádný další „výsledek“ | [SS-06](conceptual-architecture.md#ss-06--review--adaptation); označení role, ne kopie |
| [DC-13](../glossary.md#doménové-koncepty) Output | Derived — rozpoznaný výstup v popisu provedení | R: předmět Observation / rozsahu dokončení Project | [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management); samostatný registr není potřebný |
| [DC-14](../glossary.md#doménové-koncepty) Portfolio | Contextual — společné posouzení více záměrů | I: rozsah rozhodovacího pohledu a horizont; obsah se mění bez klonování členů | [SS-03](conceptual-architecture.md#ss-03--goal--portfolio-management); může být pouze úvahou |
| [DC-15](../glossary.md#doménové-koncepty) Project | Contextual — koordinace ohraničené práce | I: rozsah a rozpoznatelné dokončení práce; změna cílové vazby jej sama nemění | [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management); neodvozovat z počtu kroků |
| [DC-16](../glossary.md#doménové-koncepty) Commitment | Core — zachová odpovědnost vůči sobě i okolí | I: původ odpovědnosti, předmět, dotčené strany a podmínky; nikoli název projektu | [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management); nejasný původ lze přiznat |
| [DC-17](../glossary.md#doménové-koncepty) Captured Input | Contextual — ochrana před nechtěným přijetím | I: zachycený podnět v jeho původu; opakovaná zpráva může odkazovat na totéž | [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management); může být krátce držen v paměti |
| [DC-18](../glossary.md#doménové-koncepty) Next Action | Core — rozliší volbu konkrétního jednání | I: zamýšlené jednotlivé provedení a rozsah; opakování po provedení je nový případ | [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management); ne všechny skutečné činnosti musí být předem zachyceny |
| [DC-19](../glossary.md#doménové-koncepty) Routine | Contextual — opakovaná péče či jednání | I: opakovaný způsob a účel; přerušení a obnovení nezakládají automaticky novou rutinu | [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management); není povinná generace výskytů |
| [DC-20](../glossary.md#doménové-koncepty) Habit | Derived — lidský výklad opakovaných pozorování | R: vzorec z Observation a Interpretation, může být jen předpokládaný | [SS-06](conceptual-architecture.md#ss-06--review--adaptation); žádný katalog návyků |
| [DC-21](../glossary.md#doménové-koncepty) Capacity | Core — hranice proveditelnosti | V: posouzení zdroje, horizontu, kontextu a znalosti k určité době | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); může být slovní či neznámá |
| [DC-22](../glossary.md#doménové-koncepty) Planned Capacity | Derived — role Capacity použitá v Plan | R: příslušné posouzení dostupnosti, ne nová zásoba | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); odhad není spotřeba |
| [DC-23](../glossary.md#doménové-koncepty) Actual Capacity | Derived — role Capacity opřená o zkušenost | R: posouzení s podkladem Observation; neodvozuje se z plánu | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); může zůstat neznámá |
| [DC-24](../glossary.md#doménové-koncepty) Allocation | Core — odliší dostupnost a zamýšlené užití | V: vyčlenění pro vymezený nárok, zdroj a horizont v dané variantě plánu | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); bez povinného čísla |
| [DC-25](../glossary.md#doménové-koncepty) Plan | Core — revidovatelný rámec volby | I: kontext a horizont plánovací otázky; revize zůstává odlišena od skutečnosti | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); přípustný i bez alokací |
| [DC-26](../glossary.md#doménové-koncepty) Conditional Response | Optional — připravená odpověď na překážku | V: podmínka, záměr a reakce; změnou vzniká jiný obsah reakce | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); sama nestačí pro WOOP |
| [DC-27](../glossary.md#doménové-koncepty) Observation | Core — odliší zkušenost a očekávání | I: svědectví s původem, časem a předmětem; kopie není další pozorování | [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management)/člověk poskytuje, [SS-06](conceptual-architecture.md#ss-06--review--adaptation) spravuje význam evidence |
| [DC-28](../glossary.md#doménové-koncepty) Metric | Optional — opakovatelné srovnání pro otázku | I: způsob získání a význam údaje; změna měřítka musí být odlišena | [SS-06](conceptual-architecture.md#ss-06--review--adaptation); lze zcela vynechat |
| [DC-29](../glossary.md#doménové-koncepty) Review | Core — možnost poučit se a přehodnotit | I: konkrétní případ posouzení v rozsahu a kontextu, i krátká úvaha | [SS-06](conceptual-architecture.md#ss-06--review--adaptation); žádný povinný report |
| [DC-30](../glossary.md#doménové-koncepty) Decision | Core — odliší skutečnou lidskou volbu | I: konkrétní akt volby; pozdější opačná volba je nové rozhodnutí | [SS-06](conceptual-architecture.md#ss-06--review--adaptation) drží důvod, obsah mění příslušný SS |
| [DC-31](../glossary.md#doménové-koncepty) Resource Demand | Core — rozliší potřebu zdroje a překryv práce | V: rozsah téže práce/péče, zdroj, horizont a kontext; žádná nová identita práce | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); původ nároku dodává [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management)/[SS-03](conceptual-architecture.md#ss-03--goal--portfolio-management) |
| [DC-32](../glossary.md#doménové-koncepty) Interpretation | Derived — výklad, nikoli další skutečnost | R: obsah úsudku v Review nad uvedenými podklady; revize není nové pozorování | [SS-06](conceptual-architecture.md#ss-06--review--adaptation); lze přiznat nerozhodnost |
| [DC-33](../glossary.md#doménové-koncepty) Recommendation | Optional — alternativa před rozhodnutím | V: návrh volby a důvody; přijetím vzniká Decision, ne „stav“ doporučení | SS podle předmětu; lze odmítnout bez sankce |
| [DC-34](../glossary.md#doménové-koncepty) Internal Obstacle | Derived — role popisu vnitřního bránění záměru | R: Observation nebo Assumption a jeho vztah k záměru | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); nevyžaduje novou psychologickou entitu |
| [DC-35](../glossary.md#doménové-koncepty) External Constraint | Derived — role omezení z okolí | R: popis okolnosti v Observation/Assumption; zdrojová mez v Capacity | [SS-04](conceptual-architecture.md#ss-04--planning--capacity-management); ne každé omezení je kapacita |
| [DC-36](../glossary.md#doménové-koncepty) WIP | Derived — pohled na zahájenou práci | R: vybrané Project/Next Action a známá provedení, se stejnou identitou práce | [SS-03](conceptual-architecture.md#ss-03--goal--portfolio-management) rozsah portfolia, [SS-05](conceptual-architecture.md#ss-05--execution--commitment-management) operativa |

**Minimální konceptuální základ (12 Core):** Value, Care Need, Intended Outcome, Commitment, Next Action, Capacity, Allocation, Plan, Observation, Review, Decision a Resource Demand jsou nezbytné významy. Základní fungování znamená rozpoznat důvody a potřeby, odlišit slib od možné činnosti, posoudit nároky proti dostupnosti, zvolit i nic nealokovat a odlišit zkušenost od očekávání. Core není povinný seznam položek ani nutnost každý význam při každém použití aktivovat.

Contextual jsou Life Area, Strategy, Assumption, Experiment, Objective, Portfolio, Project, Captured Input a Routine. Optional jsou Personal Principle, Vision, Scenario, Conditional Response, Metric a Recommendation. Devět Derived konceptů využívá významy podkladů. Tato redukce je konceptuální, nikoli návrh praktického provozu.

## Identita, změna a neúplná informace

- Stejný název neprokazuje totožnost; různé názvy či pohledy neprokazují rozdíl. Při nejasnosti zůstane totožnost **nerozhodnutá**, ne automaticky sloučená či zdvojená. Rozpoznaný společný původ dovoluje odkazovat na tutéž věc bez nového záznamu.
- **Objective:** upřesnění stejné změny či posun horizontu může zachovat identitu, ale mění referenci pro posouzení. Nahrazení smyslu úspěchu jinou změnou vytváří nový cíl s návazností na původní. Původní očekávání se nesmí zpětně upravit tak, aby se neúspěch změnil na úspěch.
- **Project:** přeplánování kroků při zachování rozpoznatelného dokončení je revize; výměna předmětu práce či rozdělení do nezávislých celků zakládá nové projekty s původem. Sdílený krok se nekopíruje při přiřazení dvěma projektům.
- **Commitment:** nezávislé důvody odpovědnosti znamenají různé závazky, i když je splní jedna činnost. Přejednání může měnit podmínky téhož závazku, pokud je kontinuita původu zachována. Náhradní dohoda může původní ukončit a vytvořit nový. Samotný úmysl přejednat nedokládá změnu vnější povinnosti; relevantní souhlas protistrany či jiný skutečný důvod zániku je samostatný podklad. Nejde o právní model platnosti dohod.
- **Next Action:** ztráta aktuální proveditelnosti nemění automaticky identitu zamýšleného případu; případ může čekat. „Next“ popisuje přímost jednání za splněných podmínek, nikoli záruku dostupnosti nyní. Provedení dokládá Observation. Skutečné spontánní jednání lze pozorovat bez dodatečně vytvořeného Next Action.
- **Observation:** dvě nezávislá svědectví o téže události jsou dvě pozorování, nikoli dvě události. Oprava omylu je rozpoznatelná korekce; rozporná svědectví se mohou zachovat vedle sebe. Není předepsán auditní log.
- Každé relevantní tvrzení má rozlišit **co se posuzuje**, **k jakému času/kontextu** a **s jakou jistotou**. Neznámé, nepotvrzené, rozporné, zastaralé a nevztahující se nejsou totéž. Jde o kvalifikátory poznání, nikoli povinný stavový automat. Neznámý vztah není prokázaná absence vztahu.
- Změna má zachovat dostupný původ a důvod tam, kde ovlivní odpovědnost či výklad výsledku; nevyžaduje úplnou historii. Po přerušení se minulost může ponechat neznámou. Rozlišení revize a náhrady činí člověk podle významu, nikoli podle změny textu nebo počtu polí.

## Katalog vztahů

DR-ID jsou autoritativní. Čte se **zdroj → cíl** podle slovesa; šipka neznamená časový tok, automatický vznik ani kauzalitu. Pokud není v řádku uvedeno jinak, vazba je **volitelná, 0..* na obou koncích**: žádný obecný horní limit nemá doménové odůvodnění. Rozsahy „A, B“ znamenají samostatné přípustné typy cílů, nikoli povinnost všech. Povinnost se vztahuje na význam, ne zápis. Chybějící znalost vazby je neúplný popis, nikoli tvrzení, že invariant neplatí. Diagramy zobrazují jen vybrané DR.

### C1 — Goals, Projects & Commitments

| ID | Od → do / sloveso | Význam, nutnost a meze |
| --- | --- | --- |
| DR-01 | Objective → Intended Outcome / vyjadřuje | Pro každý Objective alespoň 1 zamýšlený obsah; tentýž obsah může být relevantní pro 0..* cílů. Totožnost obsahu neslučuje záměry. |
| DR-02 | Project → Objective / přispívá | 0..* v obou směrech: jeden projekt může podporovat dva cíle; jeden cíl může mít několik projektů i žádný. Příspěvek je záměr, ne prokázaný účinek. |
| DR-03 | Commitment → Project, Routine, Next Action / je naplňován prostřednictvím | 0..* každého typu; čekající závazek může nemít žádnou zvolenou cestu. Jedna činnost může naplňovat více závazků. |
| DR-04 | Project → Next Action / rozpracovává | 0..* v obou směrech. Projekt může čekat, být kandidátní či dokončený; nevyžaduje aktuální krok. Členství není vlastnictví výskytu. |
| DR-05 | Next Action → Objective / přispívá | Volitelná přímá návaznost bez Project; více cílů nevytváří více provedení. |
| DR-06 | Portfolio → Objective, Project, Experiment / posuzuje | Kandidát a vybraný záměr se liší volbou, ne identitou. Prázdný výběr je přípustný. |
| DR-07 | Portfolio → Commitment, Care Need / zohledňuje | Reference na odpovědnost či potřebu, nikoli vlastnictví nebo nové vytvoření nároku. |
| DR-08 | Captured Input → Commitment / vyjasňuje jako | Vstup může odkazovat na více závazků a více vstupů na stejný závazek; také na žádný. Obsah může zůstat informací, možností či odmítnutou žádostí. |
| DR-09 | Observation → Intended Outcome / je relevantní pro posouzení | Pozorování může informovat více očekávání a očekávání může mít nula či více pozorování. Není to vztah „potvrzuje“. Pozorování účinku má roli Observed Outcome. |

**Příklad:** projekt rozhovorů přispívá k cíli porozumět oboru i rozšířit spolupráci. Slib poslat shrnutí lze splnit dvěma kroky; po opuštění cíle trvá. **Protipříklad:** dokončení rozhovorů automaticky označí oba cíle jako dosažené. To porušuje INV-05. **Přípustná výjimka z hierarchie:** závazek poskytnout slíbenou informaci nemá strategii, cíl ani projekt. Výjimka není porušením pravidla: DR-02/03 jsou úmyslně volitelné.

### C2 — Life Areas, Care & Routines

| ID | Od → do / sloveso | Význam, nutnost a meze |
| --- | --- | --- |
| DR-10 | Life Area → Care Need / dává kontext | Oběma směry 0..*: stejná potřeba může zasahovat více oblastí; rozpoznání péče nepotřebuje pojmenovanou taxonomii. |
| DR-11 | Care Need → Routine, Next Action / je zajišťována prostřednictvím | Potřeba může být zatím nenaplněná, realizovaná jednorázově či opakovaně; cesta není garancí pokrytí. |
| DR-12 | Routine → Next Action / konkretizuje provedení | 0..* v obou směrech; jeden zamýšlený výskyt může sloužit více rutinám. Nevzniká povinná nekonečná množina výskytů. |
| DR-13 | Observation → Next Action, Routine, Project / dokládá zkušenost s provedením | Dokládá uskutečnění, neuskutečnění či nejistotu pro daný případ nebo období; samotný plán není podklad provedení. |
| DR-14 | Routine → Intended Outcome / sleduje | Volitelný výslovný žádoucí přínos, ne povinný strategický cíl. |

Péče udržuje či obnovuje podmínky; změna může mít Objective a ohraničený Project, ale jejich dokončení neukončuje nutně Care Need. Rutina může být přerušena nebo obnovena se zachováním účelu a identity. Úprava rytmu je revize, zásadně jiný způsob péče může být nová rutina pro tutéž potřebu. Z přerušení nevzniká automatický součet dlužných výskytů; nezávislé skutečné závazky však mohou trvat. Habit je výklad pozorovaného vzorce, nikoli důkaz vědomě zvolené Routine.

**Příklad:** potřeba obyvatelné domácnosti vede k rutině úklidu bez cíle. Konkrétní společný úklid se dotýká dvou oblastí, ale má jeden rozsah práce. **Protipříklad:** oblast „domácnost“ musí mít stále otevřený projekt a všechny zmeškané úklidy se po návratu přičtou. Porušení INV-07/08/15. **Přípustné:** oblast nemá aktivní projekt; péče zatím nemá rutinu; rutina slouží učení místo péče. Její nároky vždy podléhají stejným zdrojovým mezím jako projekt (DR-29).

### C3 — Strategy, Scenarios & Experiments

| ID | Od → do / sloveso | Význam, nutnost a meze |
| --- | --- | --- |
| DR-15 | Value → Vision, Personal Principle / orientuje | Volitelné vyjádření návaznosti, nikoli vyčerpání hodnoty jednou vizí. |
| DR-16 | Vision → Scenario / inspiruje | Alternativy mohou vzniknout i bez vize, například změnou okolností. |
| DR-17 | Scenario → Strategy / informuje | Strategie může kombinovat části scénářů; scénář není kandidátní strategie automaticky. |
| DR-18 | Strategy → Assumption / opírá se o | Rozpoznané podmínky cesty; nulová explicitní vazba neprokazuje cestu bez nejistoty. |
| DR-19 | Strategy → Objective / zdůvodňuje | Cíl může mít více strategických důvodů, nebo legitimně žádný takto vyjádřený. |
| DR-20 | Experiment → Assumption / zkoumá | 0..*; každý experiment ale musí mít alespoň jednu rozpoznatelnou otázku NEBO zkoumaný předpoklad. Otázka je obsah pokusu, ne nový objekt. |
| DR-21 | Experiment → Project, Next Action / je prováděn prostřednictvím | Volitelné 0..*: kandidát nebo ukončený pokus nemusí mít aktuální provádění; malý pokus postačí krokem. |
| DR-22 | Experiment → Observation / získává | 0..* v obou směrech; pokus může skončit bez použitelných údajů, jedno pozorování může informovat více pokusů. |
| DR-23 | Review → Observation / posuzuje | 0..*; chybění evidence může být předmětem review, nikoli důvodem ji vymyslet. |
| DR-24 | Review → Interpretation / vytváří | Jeden případ review může vyprodukovat nula či více výkladů; každý vyjádřený výklad má právě jeden původní případ posouzení. Další review jej může revidovat novým výkladem. |
| DR-25 | Review → Recommendation / připravuje | Volitelný návrh; review smí skončit otázkou bez doporučení. |
| DR-26 | Review → Decision / připravuje podklady pro | 0..* v obou směrech, Decision může vzniknout bez formálního review. Ani review s doporučením nevynucuje volbu. |
| DR-27 | Decision → Strategy, Objective, Portfolio, Plan, Commitment, Routine, Assumption / volí nebo reviduje | Volitelné vazby jednotlivých typů; každý akt má rozpoznatelný předmět volby, i „ponechat otevřené“. Změna externího závazku podléhá INV-06. |
| DR-28 | Metric → Observation / strukturuje získání či porovnání | Metrika není nutná pro Observation ani jeho interpretaci. |

Kandidátní a přijatá strategie jsou týž typ konceptu; přijetí je důsledek Decision v určeném rozsahu, nikoli přejmenování Scenario. Více otevřených alternativ smí existovat současně. Neslučitelné kandidáty nelze bez vědomého řešení považovat za současně přijatý plán v témže rozsahu. Přehodnocení strategie nemění odpovědnost Commitment.

Experiment a Project nejsou podtypy jeden druhého. První určuje, co se chceme dozvědět a kdy pokus ukončíme; druhý organizuje práci a její dokončení. Projekt je účelný, když má organizace práce samostatný smysl pro koordinaci rozsahu, závislostí či dokončení. Počet kroků není práh: i několik přímých činností může sloužit experimentu bez projektu. Jeden Project může podporovat několik Experiment; jde stále o tutéž práci. Nová otázka nebo nový nezávislý pokus se nesmí tvářit jako zpětně změněný původní pokus.

**Příklad:** dvě alternativy změny oboru zůstanou otevřené; pokusný rozhovor skončí bez jasné odpovědi. Observation zachycuje zkušenost, Interpretation říká „nerozhodné“, Decision může ponechat alternativy. **Protipříklad:** dokončený pokus automaticky potvrdí Assumption a přijme Strategy (INV-09/10). **Přípustné:** experiment nemá hypotézu k potvrzení, pouze otázku; doporučení z review člověk odmítne; závazek z pokusu trvá po jeho ukončení.

### C4 — Capacity, Allocation & Planning

| ID | Od → do / sloveso | Význam, nutnost a meze |
| --- | --- | --- |
| DR-29 | Project, Routine, Next Action, Commitment, Care Need, Experiment → Resource Demand / vyvolává nebo shrnuje | Jednotlivé zdroje mohou mít 0..* nároků. Nárok musí odkazovat na rozpoznatelný rozsah práce/péče; nemusí mít podrobný rozklad. Vazby na různé účely nejsou různé nároky automaticky. |
| DR-30 | Plan → Allocation / uspořádává | 0..* v obou směrech: nealokovaný plán je platný; totéž vyčlenění lze referovat v dílčím i širším plánu. Příslušnost ke dvěma pohledům nezdvojuje zdroj. |
| DR-31 | Allocation → Resource Demand / vyčleňuje pro | Každá alokace má právě 1 vymezený nárok, ten může být souhrnný; jeden nárok může mít 0..* dílčích či alternativních alokací. Nárok může zůstat nepokrytý. |
| DR-32 | Capacity → Allocation / omezuje proveditelnost | Oběma směry 0..*: více posouzení může informovat alokaci; nesčítají se jako nezávislé zásoby. Neznámá dostupnost neznamená neomezenost. |
| DR-33 | Plan → Capacity / používá posouzení | Posouzení dostupnosti použité při přípravě má roli Planned Capacity. Chybějící posouzení neprokazuje proveditelnost plánu. |
| DR-34 | Observation → Capacity / informuje posouzení dostupnosti | Podklad pro Actual Capacity; poznání může zůstat neúplné. Pozorovaná spotřeba není totožná s dostupností. |
| DR-35 | Resource Demand → Resource Demand / zahrnuje | Souhrn → zahrnutá část téhož zdroje/horizontu. 0..* na obou koncích; vztah je bez cyklů a nereflexivní. Části se mohou překrývat, nelze je pak prostě sčítat. |
| DR-36 | Plan → Conditional Response / zahrnuje | Volitelné podmíněné reakce, které mohou existovat i bez širšího plánu. |
| DR-37 | Conditional Response → Next Action / může navrhnout jako reakci | Volitelné: reakce může být také myšlenka, odpočinek či přehodnocení, bez nového kroku. |
| DR-38 | Conditional Response → Assumption, Observation / vztahuje podmínku k popisu překážky | Volitelné explicitní vazby; obsah reakce ale musí mít rozpoznatelnou podmínku, záměr a odpověď. |
| DR-39 | Care Need, Next Action → Intended Outcome / sleduje | Volitelný přínos nebo žádoucí stav bez Objective; umožňuje Wish a Outcome WOOP bez falešného cíle. |
| DR-40 | Decision → Recommendation / přijímá, mění nebo odmítá | 0..* v obou směrech; doporučení může zůstat bez rozhodnutí, rozhodnutí může být bez doporučení. |

Kapacita je **dostupnost**, nárok je **potřeba**, alokace je **zamýšlené využití**, spotřeba je **pozorované použití**. Planned/Actual Capacity jsou role různých časově situovaných posouzení téhož druhu dostupnosti; nejsou vzájemně odvoditelné přejmenováním. Zpětná zkušenost může opravovat odhad, ale nevymaže, z čeho plán původně vycházel.

Čas se vztahuje k intervalu, peníze k relevantnímu rozpočtovému rozsahu, energie či pozornost mohou být pouze slovní a kontextové. Kvalitativní stupně nemají automaticky sčitatelnost. Ani dvě časové veličiny nejsou srovnatelné bez shodného rozsahu, například osobní hodina a hodina čekání nejsou totéž. Dostupnost druhého člověka není vlastní ovládaná kapacita. Různé zdroje se neslévají do jednoho skóre. Neurčitý interval, hrubý odhad, rozmezí a „neznámo“ jsou přípustné; nula je tvrzení, nikoli náhrada chybějících údajů.

**Prevence dvojího započtení (sémantika, nikoli algoritmus):**

1. Každé posouzení vymezí zdroj, horizont, kontext a variantu plánu. Alternativní varianty nejsou současně platnými alokacemi pouze proto, že existují.
2. Rozpoznává se rozsah skutečné práce či péče, ne počet jejích cílů, závazků nebo zobrazení. Nárok téhož výskytu sdílený dvěma cíli je stále jeden.
3. Souhrnný nárok a jeho zahrnuté části se v témže posouzení započtou buď jako souhrn, nebo jako nepřekrývající se rozklad včetně zbytku. Nikdy jako souhrn plus již zahrnuté části. Neznámý zbytek není nula.
4. Částečný překryv není totožnost. Dva různé rozsahy práce se musí rozlišit na společnou část a odlišné části, nebo zůstat označené jako nejistý překryv. Neznalost překryvu neumožňuje tvrdit přesný součet ani vše sloučit.
5. Totéž platí pro alokace souhrnu a kroků, společné zdroje i překrývající se horizonty (týden/den). Jedna dostupnost není násobena počtem plánů. Nesčítá se navíc „požadováno“ a „alokováno“ jako dvě různé spotřeby.
6. Překročení či neslučitelnost může existovat jako rozpoznaný konflikt; model jej nesmí vydávat za proveditelný plán. Člověk může přijmout riziko nebo ponechat konflikt bez řešení, ale tím kapacitu nezvýší.

Formálně pouze k objasnění: pokud rozsah nároku B je obsažen v A, pak A a B nejsou nezávislé sčítance. Při částečném překryvu se uvažuje sjednocení rozsahů, nikoli součet velikostí; množiny jsou významová pomůcka, ne požadavek zaznamenat elementární práci.

**Příklad:** odhad projektu 6 hodin již zahrnuje dva kroky po 2 hodinách a zbytek 2 hodiny. Nárok je 6, nikoli 10; pokud zbytek neznáme, nesmíme tvrdit, že projekt stojí jen 4 hodiny. **Protipříklad:** sdílený dvouhodinový krok má dva cíle, proto plán spotřebuje 4 hodiny (INV-15). **Jiný případ:** dvě odlišné dvouhodinové činnosti potřebují stejné úterní odpoledne — není to duplicita, ale konflikt (INV-16). Další případy v [SV-03](../07-review/semantic-validation-report.md#cílené-sv-01-až-sv-10)/08/10 a [SV-11](../07-review/semantic-validation-report.md#doplňující-hraniční-případy).

## WOOP: sémantické pokrytí bez návrhu procesu

Kontrola vychází z [oficiální WOOP Practice](https://woopmylife.org/en/practice) a [Written WOOP Guide](https://www.woopmylifetoolbox.org/static1.squarespace.com/static/58a10eca725e25197ec58037/t/5ac36c591ae6cf15a4c49328/1522756697159/4-%2BWritten%2BWOOP%2BGuide%2B%281%29.pdf); původní integrace viz [FW-01](framework-integration.md). Mapování níže je rozhodnutí PLOS ([ADR-10](../05-decisions/decision-log.md#adr-10--woop-pomocí-významových-rolí-a-experiment-bez-povinného-projektu)), nikoli tvrzení autorů WOOP o tomto modelu.

| Role WOOP | Vyjádření v PLOS | Rozlišení |
| --- | --- | --- |
| Wish | Konkrétní zvolený záměr v roli Objective nebo záměru péče/jednání | Samotná obecná oblast ani závazek bez vlastního záměru nejsou přáním; potřebné zpřesnění je obsah, ne nová entita. |
| Outcome | Intended Outcome navázaný na tentýž záměr (DR-01/14/39) | Očekávaný nejlepší přínos, nikoli Observed Outcome či pouhý opis činnosti. |
| Obstacle | Observation nebo Assumption v roli Internal Obstacle vztahované ke stejnému záměru | Pozorované odkládání a hypotéza o jeho příčině se oddělují. Nejasná povaha překážky může zůstat nejistá. |
| Plan | Conditional Response s podmínkou téže překážky a možnou reakcí (DR-38/37) | Není totožný s kapacitním Plan; reakce se stále posuzuje podle dostupnosti. |

Jedno použití musí významově spojovat stejné přání, jeho přínos, relevantní vnitřní překážku a odpověď na ni. Vazba překážky ke konkrétnímu záměru je součást její role, ne povinná globální taxonomie. **External Constraint** umožňuje odlišit nedostupnou dopravu od vlastní obavy; obojí může působit současně. Nedostatek zdroje je Capacity, jiná vnější okolnost je popis Observation/Assumption. Pouhý if–then není celé WOOP; zkušenostní představování a pořadí nejsou předmětem této iterace. Nové samostatné objekty Wish, Obstacle nebo WOOP Session nejsou nutné. Rozšíření spočívá v pojmenování rolí a povinném významovém svázání, bez praktické šablony.

## Katalog invariantů

Invarianty jsou D — pravidla konzistence modelu, ne nově schválené FR. Platí při příslušném použití konceptů. Neúplná znalost je přípustná; tvrzení v rozporu s invariantem nikoli. Zmíněné přípustné varianty nejsou výjimkami, které by dovolovaly pravidlo obejít.

| ID | Pravidlo | Meze / přípustná varianta | Hlavní vazba |
| --- | --- | --- | --- |
| INV-01 | Pojem a vztah musí být smysluplné bez softwaru, fyzického záznamu a nepřetržitého sledování. | Člověk může zapomenout; model nezaručuje dokonalou paměť. | [CON-01](../02-requirements/high-level-requirements.md#omezení-návrhu), [P8](../01-foundations/design-principles.md)/[P9](../01-foundations/design-principles.md); všechny C |
| INV-02 | Doporučení, pozorování, výběr a alokace samy nezakládají přijatý závazek ani lidské rozhodnutí. | Vnější povinnost může existovat bez přijetí uživatelem; její rozpoznání není její vznik. | [FR-05](../02-requirements/high-level-requirements.md#funkční-požadavky)/07, [QR-01](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu); C1/C3 |
| INV-03 | Více pohledů na stejnou věc nesmí vytvářet nové identity; neprokázaná totožnost se nesmí předstírat. | Dva sliby mohou být různé, i když je splní jedna práce. | [QR-07](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu), [ADR-02](../05-decisions/decision-log.md#adr-02--péče-a-závazky-mají-samostatný-vstup-kapacita-společný-pohled); všechny C |
| INV-04 | Revize nesmí zpětně zaměnit původní záměr, podklad či důvod závazku za nový. | Neznámá historie může zůstat neznámá; není nutný úplný archiv. | [FR-10](../02-requirements/high-level-requirements.md#funkční-požadavky)/11/13; všechny C |
| INV-05 | Dokončení Project/Next Action či existence Output neimplikuje dosažení Intended Outcome. | Účinek lze posoudit pouze s relevantními pozorováními a výkladem; může být neznámý. | [FR-11](../02-requirements/high-level-requirements.md#funkční-požadavky); C1/C3 |
| INV-06 | Změna Strategy, Objective, Project, Plan či Routine sama neruší Commitment. | Splnění, platné přejednání či jiný skutečný zánik odpovědnosti mohou závazek ukončit; úmysl nestačí. | [FR-10](../02-requirements/high-level-requirements.md#funkční-požadavky), [QR-06](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu); C1/C3 |
| INV-07 | Care Need, Routine, Commitment a Next Action nepotřebují strategický Objective ani Project; Life Area může mít nula projektů. | Dobrovolná strategická vazba je možná; péče nesmí vyžadovat nekonečný projekt. | [FR-08](../02-requirements/high-level-requirements.md#funkční-požadavky)/09; C2 |
| INV-08 | Opakovaný záměr Routine není konkrétní provedení ani důkaz Habit; přerušení negeneruje automatický dluh všech výskytů. | Skutečná trvající povinnost se posuzuje nezávisle. | [FR-09](../02-requirements/high-level-requirements.md#funkční-požadavky)/13; C2 |
| INV-09 | Experiment má poznávací otázku nebo Assumption a mez ukončení; jeho ukončení nemusí přinést rozhodný poznatek. | Bez údajů, rozporné údaje i nerozhodný výklad jsou přípustné výsledky pokusu. | [FR-02](../02-requirements/high-level-requirements.md#funkční-požadavky)/11; C3 |
| INV-10 | Observation, Assumption, Interpretation a Decision se nesmějí směšovat; výklad příčiny není pozorovaný fakt. | Dvě interpretace mohou koexistovat; člověk může doporučení odmítnout či ponechat alternativy. | [FR-11](../02-requirements/high-level-requirements.md#funkční-požadavky), [QR-01](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu)/04; C3 |
| INV-11 | Neznámé, nepotvrzené, zastaralé a rozporné není nula, neomezenost ani prokázané splnění. | Neúplný plán či neznámá historie mohou být přiznány bez rekonstrukce. | [FR-13](../02-requirements/high-level-requirements.md#funkční-požadavky), [QR-04](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu)/05; všechny C |
| INV-12 | Capacity, Resource Demand, Allocation a pozorovaná spotřeba jsou odlišné významy; Actual Capacity se neodvozuje jen z plánu či nečinnosti. | Odhad i aktuální poznání mohou být kvalitativní a nejisté. | [FR-04](../02-requirements/high-level-requirements.md#funkční-požadavky), [QR-03](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu); C4 |
| INV-13 | Porovnání nároků a dostupnosti musí mít kompatibilní zdroj, jednotku/škálu, horizont a kontext. | Bez srovnatelnosti je možné slovní posouzení omezení, nikoli falešný číselný součet. | [QR-03](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu), [ADR-04](../05-decisions/decision-log.md#adr-04--vícezdrojová-kapacita-bez-univerzálního-skóre-priorit); C4 |
| INV-14 | V jednom posouzení se souhrnný nárok nesčítá s jeho již zahrnutými částmi; rozklad zachová i neznámý zbytek. | Souhrn a detail mohou být současně přítomné jako pohledy; DR-35 je bez cyklů. | [FR-04](../02-requirements/high-level-requirements.md#funkční-požadavky), [ADR-02](../05-decisions/decision-log.md#adr-02--péče-a-závazky-mají-samostatný-vstup-kapacita-společný-pohled); C4 |
| INV-15 | Stejný rozsah práce a stejná dostupnost se nezapočtou vícekrát kvůli cílům, závazkům, experimentům, pohledům nebo překrývajícím se horizontům. | Částečný překryv se nesmí vydávat za úplnou totožnost ani nezávislost. Alternativy se odliší od souběhu. | [QR-03](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu), [ADR-02](../05-decisions/decision-log.md#adr-02--péče-a-závazky-mají-samostatný-vstup-kapacita-společný-pohled)/04; C1/C4 |
| INV-16 | Neslučitelné nároky nesmějí být prohlášeny za proveditelné jen změnou priority nebo přijetím rizika. | Rozpoznaný nevyřešený konflikt je validní stav poznání; model negarantuje řešení. | [FR-04](../02-requirements/high-level-requirements.md#funkční-požadavky)/07, [QR-03](../02-requirements/high-level-requirements.md#požadavky-na-kvalitu); C4 |
| INV-17 | Vnitřní překážka není automaticky vnější omezení ani naopak; samotná Conditional Response nedokládá celé WOOP. | Smíšené a nejisté příčiny se mohou přiznat. | [FR-14](../02-requirements/high-level-requirements.md#funkční-požadavky), [R-05](../05-decisions/open-questions.md#rizika-návrhu); C3/C4 |
| INV-18 | Pozorovaný výsledek sdílí identitu Observation; více interpretací či návazností nevytváří nové události ani další důkazy. | Jedna událost může mít několik nezávislých svědectví, která mohou být v rozporu. | [FR-11](../02-requirements/high-level-requirements.md#funkční-požadavky), [ADR-05](../05-decisions/decision-log.md#adr-05--pozorování-pro-rozhodnutí-a-omezený-režim); C1/C3 |

## Návaznost a uzavření modelu

[ADR-07](../05-decisions/decision-log.md#adr-07--metodika-bez-předpokladu-implementace-a-povinných-záznamů) až [ADR-11](../05-decisions/decision-log.md#adr-11--konceptuální-uml-pohledy-s-explicitní-sémantikou) zaznamenávají upřesnění SoI, výsledek/identitu, nároky/kapacitu, WOOP a změnu notace. [ADR-01](../05-decisions/decision-log.md#adr-01--hybridní-architektura-funkčních-odpovědností) až [ADR-05](../05-decisions/decision-log.md#adr-05--pozorování-pro-rozhodnutí-a-omezený-režim) zůstávají platnou baseline. [ADR-11](../05-decisions/decision-log.md#adr-11--konceptuální-uml-pohledy-s-explicitní-sémantikou) nahrazuje pouze část [ADR-06](../05-decisions/decision-log.md#adr-06--lehký-konceptuální-model-a-textové-diagramy) o notaci [DG-06](../04-diagrams/README.md#dg-06); autoritativní zdroje zůstávají zachovány.

Požadavky N zůstávají N. Konkrétní dopady a návrhy kritérií pro I3 jsou v review reportu, bez přidání závazných FR. Stavové automaty, prahy, workflow, praktické evidence a rozhodovací algoritmy nejsou z tohoto modelu odvozovány jako hotová specifikace. [OQ-04](../05-decisions/open-questions.md#otevřené-otázky)/06 jsou pro sémantický rozsah rozhodnuté; provozní volba přiměřené podrobnosti zůstává [OQ-03](../05-decisions/open-questions.md#otevřené-otázky). Scénáře UC/SV ověřují konzistenci návrhu, nikoli přínos PLOS v životě.
