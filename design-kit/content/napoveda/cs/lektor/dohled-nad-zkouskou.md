---
title: Dohled nad zkouškou
source: https://demo.exam-test.cz/napoveda/lektor/dohled-nad-zkouskou
lang: cs
---

Volitelný lehký dohled bez kamery: záznam opuštění okna, celá obrazovka, blokace kopírování, rychlé odpovědi a odevzdání po opakovaném opuštění okna.

Dohled nad zkouškou zaznamená, když zkoušený během testu opustí okno. Podle nastavení ho také upozorní, nebo po opakovaném opuštění okna test odevzdá. Je to lehký dohled: bez kamery, mikrofonu, záznamu obrazovky a bez umělé inteligence. Aplikace nesleduje jiné aplikace ani zařízení zkoušeného.

Události jsou informace pro vás. Neznamenají automaticky podvádění. Okno se může přepnout i kvůli upozornění systému, slabé baterii nebo pomůcce pro zdravotně znevýhodněné. O tom, co událost znamená a co dál, rozhoduje vždy člověk.

## Nastavení u testu

Otevřete test → **3. Parametry** → část **Dohled nad zkouškou**. Pole **Dohled nad zkouškou** má čtyři možnosti:

- **Vypnuto** (výchozí): opuštění okna se zaznamená jen v záznamu průběhu.
- **Jen zaznamenat**: zaznamenají se všechny události dohledu, zkoušený upozornění nevidí.
- **Zaznamenat a upozornit zkoušeného**: po návratu do okna se zkoušenému zobrazí upozornění „Opustili jste okno testu. Zaznamenali jsme to.“ Upozornění nic neblokuje a přečte ho i čtečka obrazovky.
- **Ukončit po opakovaném opuštění okna**: v poli **Ukončit po tolika opuštěních okna** nastavíte počet (výchozí 3). Pole se zobrazí po výběru tohoto režimu. Když zkoušený okno opustí tolikrát, test se odevzdá s dosud uloženými odpověďmi a vyhodnotí se jako běžné odevzdání. Zkoušený vidí počítadlo opuštění a na stránce výsledku se dozví, proč se test odevzdal.

Doplňkové volby (zobrazí se a fungují jen se zapnutým dohledem):

- **Nabízet celou obrazovku a zaznamenat její opuštění**: zkoušený dostane tlačítko **Přejít na celou obrazovku**. Když z ní odejde, zaznamená se to a nabídne se mu návrat. Kdo celou obrazovku nemá (některé telefony, prohlížeče nebo pomůcky), píše test normálně a nic se mu nezapisuje.
- **Blokovat kopírování textu otázek a vkládání do odpovědí**: zablokuje jen kopírování zadání a odpovědí. Výběr textu, zvětšení ani čtečka obrazovky omezené nejsou. Kopírování se zaznamená i bez blokace.
- **Nezvykle rychlá odpověď (sekund)**: zaznamená první odpověď na otázku, která přišla dřív, než uplynul nastavený počet sekund od zobrazení otázky. Prázdné pole znamená, že se to nesleduje. Čas měří aplikace, ne zařízení zkoušeného.

Změna nastavení platí pro pokusy zahájené po uložení. Běžící a odevzdané pokusy si nesou nastavení z okamžiku zahájení. Dohled můžete měnit i u testu, který už byl použit u skutečné zkoušky.

Každý typ události se zapisuje nejvýše několikrát za minutu, aby záznam nezahltila zaseknutá klávesa nebo opakované přepínání.

## Úřední test

U úředního testu smí **Ukončit po opakovaném opuštění okna** zapnout jen administrátor organizace nebo administrátor pobočky, do které test patří. Uložením nastavení tento režim schválí. Jeho jméno a čas schválení se uvedou u testu a zapíšou do auditu. Když režim nebo počet později změní někdo jiný, schválení se zruší a test se uložit nedá. Kopie úředního testu schválení nepřebírá. Dokud ho administrátor neschválí, zkoušený se jen upozorňuje.

## Co zkoušený ví předem

Na úvodní stránce testu zkoušený před zahájením uvidí, že je dohled zapnutý, co se zaznamenává a kdy se test odevzdá sám. Informace o zpracování osobních údajů pro zkoušené mají část „Dohled nad zkouškou“.

Během testu je nad otázkami trvalá informace o dohledu s odkazem **Informace o dohledu a zpracování údajů**. Ten i odkazy v patičce (informace o zpracování, prohlášení o přístupnosti) se otevřou v okně přímo na stránce testu, takže se jejich přečtení nepočítá jako opuštění okna.

Prodloužení času pro zkoušené se zdravotním znevýhodněním funguje i s dohledem. Používá-li zkoušený pomůcku, která přebírá okno (například diktování, samostatnou lupu nebo některé čtečky obrazovky a ovládání hlasem), nastavte mu výjimku (viz níže). Ukončování by u něj mohlo test odevzdat bez jeho vůle a znevýhodnit ho kvůli zdravotnímu postižení. O pomůcce stačí vědět, diagnózu nevyžadujte.

## Výjimka z dohledu pro jednoho zkoušeného

Otevřete použití testu (přístupové kódy, přidělení nebo prezenční zkouška) → **Výjimky z dohledu**. Vyberte zkoušeného a zvolte režim. **Jen zaznamenat** vypne upozornění, automatické odevzdání, celou obrazovku i blokaci kopírování, události ale dál uvidíte. **Bez dohledu** funguje jako test bez dohledu. Nakonec napište důvod bez diagnózy, například „asistivní technologie“. U prezenční zkoušky nastavte výjimku účastníkovi v čekárně, než ho vpustíte.

Výjimka platí pro pokusy, které zkoušený zahájí od uložení; běžící pokus se nezmění. Do záznamu pokusu (a protokolu) se zapíše jen to, že výjimka platila a v jakém režimu, důvod je jen u použití a v auditu. Výjimku můžete zrušit; zrušení se také zapíše do auditu. V živém panelu má pokus s výjimkou značku „Výjimka: jen záznam“ nebo „Výjimka: bez dohledu“.

## Než dohled zapnete: osobní údaje a přiměřenost

Za zapnutí dohledu a za rozhodnutí o důsledcích odpovídá vaše organizace jako správce osobních údajů (obchodní podmínky čl. 8.3, zpracovatelská smlouva čl. 4.3). Doporučení:

- **Zapínejte jen tam, kde je to potřeba.** U cvičných testů a běžných školení obvykle stačí **Vypnuto** nebo **Jen zaznamenat**. Ukončování nechte na zkoušky, na jejichž výsledku něco závisí, a jen když jiný dozor nemáte.
- **Zaměstnanci.** U testů pro vlastní zaměstnance informujte předem o rozsahu kontroly a způsobu jejího provádění (§ 316 odst. 3 zákoníku práce). Úvodní stránka testu to říká každému zkoušenému, ale zmínit to můžete i v pozvánce nebo ve vnitřním předpisu.
- **Posouzení vlivu (DPIA).** Před plošným zapnutím ukončování, zejména u úřadů, zaměstnanců nebo velkého počtu zkoušených, zvažte posouzení vlivu na ochranu osobních údajů (čl. 35 GDPR) a poraďte se se svým pověřencem. Popis funkce vám na požádání dodá provozovatel.
- **O automatickém odevzdání rozhoduje program, ne člověk.** Pokud na výsledku zkoušky něco závisí (zaměstnání, oprávnění, úřední zkouška), musí mít zkoušený možnost požádat o přezkoumání člověkem (čl. 22 GDPR). Informace pro zkoušené to uvádějí, žádosti ale vyřizuje vaše organizace.
- **Vlastní text informací o zpracování.** Část „Dohled nad zkouškou“ se zobrazí i pod vaším vlastním textem. Právní základ v ní odkazuje na váš text. Proto ve svém textu uveďte i technický záznam průběhu testu.

## Když zkoušený nesouhlasí s automatickým odevzdáním

Odevzdaný pokus nejde vrátit ani změnit. Přezkoumání proto znamená, že člověk posoudí okolnosti a rozhodne, zda výsledek platí. Pokus odevzdaný dohledem má v detailu výsledku upozornění „Odevzdáno dohledem, čeká na posouzení“ a v živém panelu značku **Čeká na posouzení**.

1. Otevřete detail výsledku a projděte časovou osu událostí dohledu (kdy a jak dlouho byl zkoušený mimo okno).
2. Vyslechněte zkoušeného: technický problém, upozornění systému, pomůcka.
3. V části **Dohled nad zkouškou → Posoudit odevzdání dohledem** zvolte:
   - **Uznat výsledek**: výsledek zůstává platný;
   - **Zneplatnit a povolit náhradní pokus**: pokus přestane platit (nepočítá se do výsledků, statistik ani exportů a osvědčení z něj neplatí). Zkoušený může test napsat znovu stejným kódem nebo v části **Moje testy**; náhradní pokus se nezapočítá do maximálního počtu pokusů. Použití musí být v tu dobu ještě otevřené.
4. Napište důvod (alespoň 5 znaků, bez údajů o zdraví) a uložte.

Rozhodnutí je jen jedno a nejde vrátit. Důvod, jméno a čas se zapíšou k výsledku, do protokolu PDF a do auditu. Zkoušený dostane e-mail, pokud má e-mail u účtu nebo u přístupového kódu. Jinak mu rozhodnutí sdělte sami. Na veřejném ověření protokolu se ukáže jen stav (výsledek uznán / pokus zneplatněn s odkazem na náhradní pokus), ne důvod ani události. Zneplatněný pokus zůstává v neměnném záznamu a najdete ho přes živý panel použití; náhradní pokus na něj odkazuje.

U úředního testu posuzuje odevzdání dohledem jen administrátor organizace nebo administrátor pobočky. Lektor uvidí, že rozhodnutí patří administrátorovi.

O dalších důsledcích (například disciplinárních) aplikace nerozhoduje a sama z událostí podvod nevyvozuje.

## Kde události uvidíte

- **Živý panel** použití: ve sloupci **Upozornění** u každého zkoušeného značka s textem, například „Dohled: 2 události (okno 1×, kopírování 1×)“. Zelená značka „Dohled: bez událostí“ znamená, že se nic nestalo. Žlutá znamená události pod limitem, červená „zkontrolujte“ dosažení limitu. Samostatná značka „Odevzdáno dohledem“ označuje pokus, který odevzdal dohled. Více v kapitole [Živý panel](zivy-panel.md).
- **Detail výsledku**: část **Dohled nad zkouškou** s režimem, souhrnem a časovou osou událostí.
- **Protokol PDF**: řádek **Dohled nad zkouškou** v hlavičce a tabulka událostí dohledu.
- **Statistiky testu**: kolik pokusů má události dohledu, podle typu, a kolik jich odevzdal dohled. Více v kapitole [Statistiky](statistiky.md).

Události se ukládají do neměnného záznamu o zkoušce stejně jako ostatní průběh. Dodatečně je nikdo nesmaže ani nezmění.

*Pro role: Lektor, Administrátor pobočky, Administrátor organizace*
