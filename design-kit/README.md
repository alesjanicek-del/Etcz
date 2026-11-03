# exam-test · design kit 1.0 (směr B „Odpovědní list“)

Podklady pro nový vizuál webu exam-test.cz a aplikace: logo, brand manuál, knihovna komponent a návrhy všech stránek jako hotové HTML/CSS.

Otevřete `index.html` (rozcestník). Odtud vedou odkazy na:
- `logo.html`: logo manuál, varianty, konstrukce a tři kola ověřování. Balíček souborů je `assets/logo/exam-test-logo-balicek.zip`.
- `brand.html`: barvy s ověřenými kontrasty, typografie, mezery, ikony, motivy, obraz, tón komunikace, tiskoviny.
- `komponenty.html`: živé ukázky komponent s HTML ke zkopírování.
- `audit.html`: specifikace každé stránky a výsledky kontrol (WCAG 2.2 AA, UX, UI, srozumitelnost textů).
- `web/`, `app/`, `tisk/`: navržené stránky (seznam je v `sitemap.json`).

## Implementace
1. CSS se načítá v pořadí `assets/fonts.css`, `assets/tokens.css`, `assets/brand.css`. `brand.css` importuje první dva sám.
2. V Tailwindu v4 nahraďte výchozí téma souborem `assets/tailwind-theme.css`. Výchozí barvy a velikosti jsou v něm vypnuté záměrně, aby se do aplikace nevrátil chaos 47 stylů textu.
3. Písma jsou self-hostovaná v `assets/fonts/` (SIL OFL): Schibsted Grotesk 400/700 a IBM Plex Mono 500/600.
4. Ikony jsou v `assets/icons.svg` jako sprite. Návrhy je mají vložené inline, protože externí sprite přes `file://` nefunguje. Na serveru můžete použít `<use href="/assets/icons.svg#i-check">`.
5. Každá stránka obsahuje `<script type="application/json" id="spec">` se specifikací: účel, hlavní akce, stavy, změny UX, přepisy textů a řešení přístupnosti. Stejná data jsou čitelně v `audit.html`.

## Úpravy a kontrola
```bash
npm install                                   # axe-core pro kontrolu
python3 tools/build.py src/app/testy.html     # sestaví stránku z fragmentu (kostra, menu podle role)
node tools/check.js app/testy.html            # WCAG 2.2 AA + pravidla značky + texty
node tools/nahledy.js && python3 tools/kit_build.py   # náhledy, rozcestník a audit
npm run logo                                  # přegeneruje logo z tools/logo_params.json
```
Kontrola hlásí:
- axe-core na 1280 a 375 px;
- vodorovné posouvání při 320 px;
- ovládací prvky menší než 24 px;
- velikosti písma a barvy mimo tokeny;
- chybějící nebo zdvojené H1 a stejné texty odkazů s různým cílem;
- věty delší než 25 slov;
- zastaralé formulace ze slovníku pojmů.

## Angličtina a zavedení
- `node tools/check_en.js` je test délky textu: všechny texty prodlouží o 35 % a zkontroluje šířky 320 a 1280 px.
- Vzorové anglické stránky jsou `web/en-index.html` a `app/en-test-otazka.html`. Kostra webu umí `"lang":"en"` (přepínač CS/EN, `hreflang`).
- Glosář EN v brand manuálu (kapitola 08b) je jen návrh. Při rozporu platí `docs/STYL_A_TERMINOLOGIE.md` v repozitáři aplikace.
- Postup zavedení popisuje brand manuál v kapitole 08c:
  1. Až po go-live SÚJB a zapnutí EN.
  2. Nejdřív vizuál, goldeny obnovit v samostatném commitu.
  3. Potom texty přes katalogy `*.cs.yaml` a zároveň `*.en.yaml`.

## Co ještě zbývá před spuštěním
- Ruční test se čtečkou obrazovky (NVDA + Firefox, VoiceOver + Safari) a jen s klávesnicí na průchodu testem, editoru otázky a živém panelu.
- Ověřit barvy loga v tisku nátiskem. CMYK a Pantone v manuálu jsou orientační.
- Zkrácená znění právních a potvrzovacích textů (potvrzení o školení) nechat odsouhlasit právníkem.
- Nahradit ukázková data a screenshoty skutečnými obrazovkami po nakódování.
