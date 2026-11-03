# Zadání pro návrhy stránek – exam-test, směr B („Odpovědní list“)

Navrhuješ stránky v **novém designu značky exam-test**. Výstup slouží kodérovi jako hotové HTML/CSS. Pracuj v `/home/user/Etcz/design-kit/`.

## 1. Co odevzdáš
Pro každou svou stránku ze `sitemap.json` (pole `skupina` = tvoje skupina):
1. Fragment `src/<oddil>/<soubor>.html` (oddíl = web | app | tisk). Sestavení: `python3 tools/build.py src/<oddil>/<soubor>.html` → vznikne `<oddil>/<soubor>.html`.
2. Kontrola: `node tools/check.js <oddil>/<soubor>.html`. Opakuj, dokud **axe nemá žádné serious/critical** a **„vlastní“ chyby = 0**. Varování buď oprav, nebo je zdůvodni ve specifikaci (`pristupnost` nebo `poznamky_pro_kodera`).
3. Vizuální kontrola: `node tools/shot.js <oddil>/<soubor>.html /tmp/…png 1280` a totéž s `375`. Obrázek si prohlédni (Read) a oprav rozbité rozvržení (přetékání, zalomení tlačítek, prázdná místa). U každé stránky aspoň jednou desktop i mobil.
4. Na konci vrať stručný seznam: soubor → stav kontroly (✓/✗), nejdůležitější změny, chybějící komponenty.

**Neupravuj** `assets/*.css`, `tools/*`, `_sablony/*`, `sitemap.json` ani stránky jiných skupin. Když komponenta chybí, použij existující + inline `style` **jen s tokeny** (`var(--s-3)`, `var(--c-…)`) pro rozvržení (gap, grid-template-columns, max-width). Nové barvy, velikosti písma ani stíny nevymýšlej. Chybějící komponentu zapiš do spec `chybi_komponenta`.

## 2. Formát fragmentu
```
<!--meta {"titulek":"Testy","sablona":"app","role":"lektor","aktivni":"testy.html","demo":false} -->
<!--spec { …JSON… } -->
<section>…obsah <main>…</section>
```
- `sablona`: `web` (veřejný web, `aktivni` = odkaz v hlavní navigaci) · `app` (aplikace s bočním menu podle `role`: lektor|autor|admin|zkouseny; `aktivni` = položka menu) · `exam` (průchod testem – bez menu, vlastní hlavička `.exam-head` píšeš do obsahu; meta `skip` = text odkazu přeskočení) · `cisty` (přihlášení, chyby, projektor – bez menu; `body_class` volitelně) · `a4` (tiskové dokumenty, obsah v `<div class="a4">`).
- Obsah fragmentu je to, co patří do `<main>`. U `exam`/`cisty`/`a4` musí fragment obsahovat vlastní `<main id="obsah">`.
- Ikony: `{{I:nazev}}` (seznam v `assets/icons.json`). Ikona je vždy dekorace vedle textu; samostatná ikona v tlačítku potřebuje `aria-label` na tlačítku.
- Odkazy mezi stránkami: relativně podle `sitemap.json` (`testy.html`, `../web/cenik.html`). Neexistující cíl = `#`.

**Specifikace (povinná pole):**
```json
{"route":"/testy","nazev":"Testy","role":"lektor","sablona":"app",
 "ucel":"1–2 věty: proč stránka existuje",
 "hlavni_akce":"co má uživatel nejčastěji udělat",
 "komponenty":["page-head","table","…"],
 "stavy":["prázdný stav: …","chyba: …","načítání: …","bez oprávnění: …"],
 "zmeny_ux":["konkrétní změna oproti dnešku a proč"],
 "texty":[{"dnes":"doslovně z dnešní aplikace","nove":"nový text","proc":"pravidlo/důvod"}],
 "pristupnost":["konkrétní řešení: labely, popisky tabulek, aria-live, pořadí fokusu…"],
 "poznamky_pro_kodera":["data, chování, co je dynamické"],
 "chybi_komponenta":[]}
```
`stavy` popiš u každé stránky (prázdný, chyba, načítání, oprávnění). Hlavní stav nakresli; další stavy nakresli jako samostatné bloky pod nadpisem **„Další stavy stránky“** (H2, za hlavním obsahem, `class="no-print"`), pokud se vzhledově liší (např. prázdný seznam, chyba formuláře, neplatný kód).

## 3. Zdroje obsahu (dnešní stav)
- Texty a screenshoty webu: `/tmp/claude-0/-home-user-Etcz/55de0f84-554c-5f5c-ac5b-96e089e53363/scratchpad/crawl/web/*.txt|png`
- Aplikace (role lektor, zkoušený, autor, admin): `…/scratchpad/crawl/<role>_<route>.txt|png` a `…/scratchpad/crawl/index*.json` (seznam route + H1).
- Starší měření a obrazovky testu: `…/scratchpad/measure/*.txt|png`, tisk: `…/scratchpad/tisk/*` (skutečná PDF zadání, listů a klíčů + `zapis2.txt`).
- Hotové referenční návrhy směru B (obrázky): `…/scratchpad/mock/b/*.png` a zdroje `*.html` (start, otazka, odevzdani, vysledek, m_*, l_prehled, l_vysledky, l_panel, list2, zadani, klic, zapis). **Drž se jich**, ale přepiš je do komponent `assets/brand.css`.
- Hotový vzor fragmentu: `src/web/index.html`.
- Smíš si otevřít živý web `https://exam-test.cz` a demo `https://demo.exam-test.cz` (Playwright; demo spustíš na `https://exam-test.cz/vyzkouset`, výběr role `#demo-role-lektor|autor|admin|zkouseny`, tlačítko „Spustit demo“). **Nikdy neodesílej formuláře na exam-test.cz** (poptávka, kontakt – šly by skutečné firmě). V demu smíš klikat a vytvářet data. Nic nemaž.
- Obsah nevymýšlej: funkce, čísla, ceny a lhůty ber z dnešních textů. Ukázková data (jména, testy) přeber z dema. Když je něco nové (návrh), napiš to do `zmeny_ux` jako návrh.

## 4. Vizuální systém (závazné)
- Pořadí: `assets/brand.css` (importuje fonts + tokens). Čti ho celý, používej jeho třídy.
- **Typografie, 5 rolí v aplikaci:** `.t-titulek` 30 (H1 stránky), `.t-nadpis` 22 (H2 sekce, otázka v testu), běžný text 17, `.t-maly` 15 šedá (metadata, nápovědy), `.t-stitek` 13 mono verzálky. Web navíc `.t-display` (H1 hero) a `.t-sekce` (H2 sekce) a `.t-perex`. **Žádné jiné velikosti.** Hierarchie řezem (700), ne velikostí.
- **Barvy textu:** grafit, šedá (`.t-maly`/`.t-stitek`), odkaz propiska, stavy jen přes `.stav--ok|ne|pise|info|neutral` a `.alert--…`. Žlutá nikdy jako text; na žluté jen grafit.
- Čísla, kódy, časy, procenta: `.t-cislo` / `.t-kod` / `.num` v tabulce.
- Stav vždy **ikonou + slovem**: splněno = `{{I:check}}`, nesplněno = `{{I:minus-kruh}}` (**nikdy ✕** – koliduje se značkou), pozor = `{{I:pozor}}`, info = `{{I:info}}`.
- Tlačítka: 3 druhy (`.btn--hlavni` max. 1 na obrazovku/formulář, `.btn`, `.btn--tiche`), plus `.btn--male`, `.btn--nebezpecne`. Text tlačítka = sloveso + co („Uložit test“, ne „OK“).
- Tabulky: `.table-wrap > table.table.table--stack` s `<caption>` (může být `.sr-only`) a `data-label` u každé `td` (mobil). Čísla `.num`. Akce v řádku jako odkazy s účelem („Upravit: BOZP – cvičný test“ – nebo vizuálně „Upravit“ + `<span class="sr-only">: název</span>`).
- Formuláře: `.field > .label + (.hint) + .input`; povinné pole bez hvězdiček, nepovinné označ `<span class="volitelne">(nepovinné)</span>`; chyba = `aria-invalid="true"` + `.error` s `id` v `aria-describedby`; nahoře `.error-summary` s odkazy na pole. Skupiny voleb ve `fieldset/legend`.
- Mezery: `.stack*`, `.row`, `.grid-*`, `.layout-aside`, `.page-head`. Rohy 0. Stín jen `.card--papir` a vybraná volba.
- Mobil od 320 px bez vodorovného posouvání (kromě `.table-wrap`). Cíle min. 44 px (komponenty to mají).

## 5. Texty – pravidla a slovník
Pravidla: (1) jednou a na jednom místě, (2) tlačítko říká, co se stane, (3) důležité nikdy drobně (nevratné/právní věci v běžném textu), (4) jedna věc = jedno slovo, (5) krátce, vykáním, činně – věta do 20 slov (kontrola hlásí > 25), (6) čísla číslicemi.
České typografické uvozovky „…“, pomlčka –, nedělitelná mezera mezi číslem a jednotkou (`15&nbsp;min`, `80&nbsp;%`), jednopísmenné předložky (`v&nbsp;učebně`).

| Pojem (závazně) | Nepoužívat |
|---|---|
| Vyzkoušet demo (samoobsluha) · Ukázka s průvodcem (schůzka) | Prohlédnout demo, Domluvit ukázku |
| Prezenční zkouška (v učebně) · Osobní kódy · Přidělení skupině / Přiděleno · Veřejný odkaz · Tisk | Odkaz (anonymní), Přístupové kódy pro osoby, Přidělení studujícím / skupině |
| Zkoušený vidí výsledek · Zpřístupnit výsledky | Uvolnit, Uvolněno |
| Další otázka · Vrátit se později · Zkontrolovat a odevzdat · Odevzdat test | Uložit a další, Označit k pozdějšímu návratu, Přejít k odevzdání testu |
| Pokus (jedno vyplnění) · Variace · Soubor otázek · Seznam štítků · Pobočka · Použití testu | — |
| Dohled (zapnutý) · Živý panel · Čekárna · Promítací plocha · Kód pro převzetí | 👁, proctoring |
| Ověřovací kód (protokolu) · Kód variace (tisk) · Přístupový kód (vstup do testu) | — |

Odpovídá-li dnešní text pravidlům, nech ho. Každou změnu textu zapiš do spec `texty` (dnes → nově → proč).
