# Preliminary Domain Model

**ID:** DOM-01 • **Stav:** předběžný konceptuální model. Autoritativní definice jsou ve [slovníku](../glossary.md), pohled na vztahy v [DG-06](../04-diagrams/README.md#dg-06). Žádná tabulka zde neurčuje databázové entity, atributy, kardinality, dědičnost nebo stavové automaty.

## Koncepty a důvod jejich existence

| Skupina | Koncepty | Rozhodovací hodnota | Vlastník významu |
| --- | --- | --- | --- |
| Orientace | Value, Personal Principle, Life Area, Care Need, Vision | Rozlišit kvalitu jednání, osobní vodítko, kontext péče a představu směru | SS-01 |
| Cesty a nejistota | Strategy, Scenario, Assumption, Experiment | Oddělit volbu cesty od alternativ a od poznávacího pokusu | SS-02 |
| Výběr změn | Objective, zamýšlený Outcome, Portfolio | Rozlišit žádoucí změnu, její zamýšlený výsledek a výběr nároků | SS-03 |
| Provádění | Project, Commitment, Captured Input, Next Action, Routine | Oddělit balík práce, odpovědnost, nevyjasněný vstup a konkrétní jednání | SS-05; výběr projektu do portfolia SS-03 |
| Proveditelnost | Capacity, Allocation, Plan, Conditional Response | Odlišit dostupnost, zamýšlené použití a reakci na změnu | SS-04 |
| Učení | Observation, Metric, Review, Decision | Oddělit evidenci, způsob měření, interpretaci a lidskou volbu | SS-06; pozorování poskytuje člověk a ostatní SS |

Habit a Output jsou rozlišovací pojmy slovníku, nikoli povinné samostatné záznamy. Návyk lze popsat jako pozorovaný vzorec nebo předpoklad; model nepotřebuje katalog všech návyků. Výstup práce lze popsat v projektu nebo pozorování. Podobně Needs v požadavkovém inženýrství nejsou totéž jako konkrétní Care Need v životě uživatele.

Oproti výchozímu seznamu zadání přibyly Strategy a Portfolio, protože bez nich by chyběl význam voleb a společného výběru. Routine odděluje plánované opakování od návyku; Captured Input zabraňuje automatickému přijetí žádosti. Care Need umožňuje samostatný vstup průběžné péče. Plan a Conditional Response mají odlišnou roli od Allocation. Jde o koncepty, nikoli povinné samostatné formuláře (ADR-06, H-01).

## Předběžné sémantické vztahy

Šipka zde znamená pojmenovaný významový vztah, ne dědičnost, povinný vznik ani kauzální garanci. Směr čtení je vždy uveden. Tento seznam zpřesňuje reprezentativní výběr vztahů z DG-06.

| Od → do | Vztah | Význam a hranice |
| --- | --- | --- |
| Value → Vision, Personal Principle | Orientuje | Hodnota může vést k různým představám a vodítkům, není jimi vyčerpána |
| Life Area → Care Need | Dává kontext | Péče není nutně zlepšování ani projekt |
| Vision → Scenario; Scenario → Strategy | Inspiruje alternativy; informuje volbu cesty | Strategie může kombinovat části scénářů; výběr není předpověď |
| Strategy → Assumption | Opírá se o | Zviditelňuje podmíněnost volby |
| Experiment → Assumption | Zkoumá | Zkušenost může předpoklad oslabit, podpořit nebo ponechat otevřený |
| Strategy → Objective | Zdůvodňuje | Přípustná významová návaznost; ne každý cíl musí mít kompletní strategickou hierarchii |
| Objective → Outcome | Vyjadřuje zamýšlený výsledek | Objective je záměr; Outcome jeho obsah nebo následně pozorovaný stav |
| Portfolio → Objective, Project, Experiment | Posuzuje a vybírá | Přijatý výběr neopravňuje ignorovat ostatní nároky |
| Portfolio → Commitment, Care Need | Zohledňuje nárok | Není to nezávislá kopie závazku ani pravomoc jej zrušit |
| Project → Objective | Může přispívat | Dokončený projekt může mít výstup bez požadovaného účinku |
| Experiment → Project nebo Next Action | Může být proveden prostřednictvím | Malý pokus nepotřebuje samostatný projekt; nezdvojuje se jeho práce |
| Captured Input → Commitment | Může být vyjasněn jako | Alternativou je informace, odmítnutí nebo možnost; ne každý vstup je závazek |
| Commitment → Project, Routine nebo Next Action | Může být naplňován prostřednictvím | Závazek je odpovědnost; projekt je organizace práce; krok je jednání |
| Care Need → Routine nebo Next Action | Může být zajišťována | Běžná péče se nemusí měnit na Objective |
| Project → Next Action; Routine → Next Action | Upřesňuje nejbližší krok; může vést k aktuálnímu provedení | Rutina není součet všech budoucích výskytů v evidenci |
| Plan → Allocation; Capacity → Allocation | Uspořádává; omezuje proveditelnost | Zdroje nejsou směnitelné bez zdůvodněného modelu |
| Allocation → Project, Routine nebo Next Action | Vyčleňuje zdroj pro nárok | Na různých úrovních jde o pohled na stejný zdroj, ne o jeho nové přidělení; prevence dvojího započtení je téma I2 |
| Conditional Response → Next Action | Nabízí reakci při dané situaci | Reakce může být i přehodnocení, myšlenka nebo odpočinek; nemusí vytvářet úkol |
| Observation → Outcome, provedení, Capacity | Dokládá dostupnou zkušenost | Pozorovaný výsledek je evidencí skutečnosti s nejistotou, nikoli změnou zamýšleného cíle |
| Metric → Observation | Strukturuje volitelný sběr | Pozorování může existovat bez metriky |
| Review → Observation; Review → Decision | Interpretuje; připravuje podklady pro | Rozhoduje člověk, ne samotné review |
| Decision → Strategy, Portfolio, Plan, Commitment | Může revidovat | Rozhodnutí o přejednání závazku není potvrzení protistrany; změna významu je oddělená od změny reality |

## Kritická rozlišení na příkladech

- **Hodnota versus cíl:** „jednat zvídavě“ může orientovat více cílů. „Ověřit vhodnost nové oblasti“ je posouditelný cíl; jeho dosažením zvídavost nekončí.
- **Cíl versus projekt:** žádoucí lepší orientace v tématu je výsledek, série rozhovorů je organizace práce. Rozhovory mohou být dokončeny bez očekávané orientace.
- **Projekt versus závazek:** přislíbená pomoc je závazek; lze jej naplnit jedním krokem nebo vícečinnostním projektem. Změna projektu sama nemění slib.
- **Výsledek versus aktivita:** uskutečněná návštěva je provedení; získaný poznatek nebo změna vztahu je možný výsledek, který může zůstat nejasný.
- **Jednorázové versus opakované:** konkrétní péče dnes je krok; zvolený opakovaný způsob péče je rutina. Návyk je vzorec chování, ne kalendář opakování.
- **Plán versus skutečnost:** odhad volného času, jeho zamýšlené využití a pozorované využití jsou tři různé věci; poznání skutečné dostupnosti může být neúplné.
- **Pozorování versus rozhodnutí:** „plán nebyl proveden“ je evidence; „zmenším rozsah“ je volba. Příčina nesplnění vyžaduje interpretaci, ne automatický soud o vůli člověka.

## Co zůstává předběžné

Iteration 2 zpřesní identitu a vztahy Project–Commitment–Objective, životní cyklus hypotézy a výsledku experimentu, původ externí povinnosti, vazbu plánované a skutečné kapacity a rozsah minimální trasovatelnosti. Teprve tam budou navrženy detailnější invarianty a kardinality, pokud budou přinášet rozhodovací hodnotu. Stavové automaty patří do Iteration 5. Žádné vyjmenované spojení nezakládá povinné vyplňování všech konceptů.
