# Triconform · směr B „Týden“ · změny šablon a textů

Vrstva 1 (vzhled) je jen CSS a nemění HTML: `rebrand-web.css`, `rebrand-app.css`.
Tento soubor je vrstva 2: úpravy šablon a textů z analýzy. Každý bod je samostatný commit.
Platí pravidla projektu: nikdy neslibovat „shodu/soulad/certifikaci“, ceny neměnit, CSP bez inline stylů.

## A. Web triconform.com

### A1 Úvod: jedno hlavní tlačítko (všechny stránky s `.actions`, hlavička, `.cta-band`)
| Dnes | Nově | Cíl |
|---|---|---|
| Vyzkoušet zdarma (`mailto:`) – primární | **Vyzkoušet ukázku hned** – primární | `https://demo.triconform.com/vyzkouset` |
| Vyzkoušet aplikaci – sekundární | **Požádat o 30 dní zdarma** – sekundární | `/kontakt/?zajem=zkusebni-pristup` (formulář) |
| Domluvit ukázku (`mailto:`) – sekundární | textový odkaz **Domluvit ukázku s průvodcem** | `/kontakt/?zajem=ukazka` |
| Hlavička: Vyzkoušet zdarma | **Vyzkoušet ukázku** | demo |

EN: Try the demo now · Request a 30-day free trial · Book a guided demo · (header) Try the demo.
Poznámka pod tlačítky: „Ukázka běží hned, bez registrace. Zkušební přístup na 30 dní pro vaši firmu založíme do 2 pracovních dnů.“

### A2 Formulář místo `mailto:`
Na `/kontakt/` už formulář je (`.form`). Přidat volbu `zajem` (radio: Zkušební přístup na 30 dní · Ukázka s průvodcem · Jiný dotaz), předvyplnit z URL. `mailto:` nechat jen jako záložní odkaz „nebo napište na info@abuco.cz“.

### A3 Nadpis úvodu
- Dnes: „NIS2, CRA a AI Act v jedné přehledné evidenci“
- Nově: „**Každý týden víte, co udělat pro NIS2, CRA a AI Act**“
- EN: “Every week you know what to do for NIS2, the CRA and the AI Act”
- Perex beze změny.

### A4 Ceník: kalkulačka nad kartami (ceny beze změny)
Nad kartami blok „Kolik zaplatíte“: dvě skupiny přepínačů (radio, bez JS funkční jako odkaz na kotvu) – **Počet zaměstnanců** (10–24 · do 49 · 50–249 · 250–499) a **Roviny** (1 · 2 · všechny 3) → výsledná roční cena z tabulky, „bez DPH“. JS jen zvýrazní odpovídající řádek a vypíše částku do `<output aria-live="polite">`.
Věta „Dvě roviny = cena za 1 rovinu a jedna další rovina“ → „**Každá další rovina má pevnou cenu.** Všechny tři vycházejí levněji.“
Tlačítka „Objednat nebo se zeptat“ (9×) → „**Chci pásmo S**“, „Chci pásmo M“… (odkaz na formulář s `?pasmo=S`).

### A5 Logo a favicony
Inline SVG tří kruhů v hlavičce (každá stránka) nahradit `<img src="/assets/brand/triconform-logo.svg" alt="Triconform" width="168" height="34">` + tmavá varianta přes `<picture>`/`prefers-color-scheme`. Dokud se nezmění, řeší logo CSS (`.brand::before`).
`site/favicon.svg` ← `logo/favicon.svg`, přidat `favicon.ico`, `apple-touch-icon.png`, `og-image.png`.

## B. Aplikace

### B1 Menu: jedno místo = jedno jméno
| Dnes (menu / podmenu / H1) | Nově |
|---|---|
| Co musíme mít / Opatření / „Opatření“ | **Opatření** (H1 „Opatření podle vyhlášky 410“) |
| Dodavatelé a software / Software | dvě položky: **Dodavatelé**, **Software** |
| Pro odběratele a kontrolu / Doklady pro odběratele | **Doklady** (H1 „Doklady pro odběratele a kontrolu“) |
| Podstránky „Co musíme mít“ se stejným H1 | H1 = název podstránky (Rizika, Směrnice, Roční přehled…) |
Pořadí menu: Tento týden · Úkoly · Opatření · Incidenty · Dodavatelé · Software · Výrobky · AI · Doklady · Další.
U položek rovin malá ikona tvaru (čtverec = Organizace, trojúhelník = Výrobek, kruh = AI), `aria-hidden`, název zůstává textem.

### B2 „Tento týden“: jedna kostra pro každou položku
Každá položka v „Co udělat“ = řádek `[štítek naléhavosti] [datum] [co] [jedna akce vpravo]`:
- skupiny **Hned · Tento týden · Později** jako nadpisy `h3` s pruhem vlevo (signál / jedle / listí) – třídy `urg urg-hned|urg-tyden|urg-pozdeji` (styl níže);
- akce vždy tlačítko `btn btn-sm btn-secondary` vpravo (na mobilu pod textem, zarovnané vlevo), nikdy střídavě tlačítko a odkaz;
- „Vyřešit“ → **Rozhodnout** (zranitelnost: aktualizovat / netýká se / odložit), **Otevřít** (úkol), **Potvrdit** (hlášení CVD);
- emoji ⚠ ⛔ nahradit SVG ikonami (`aria-hidden`), význam nese text štítku („Zneužívá se“, „Po termínu 40 dní“);
- počet položek v nadpisu skupiny: „Hned · 4“.

```css
/* do app.css @layer components */
.urg { border-left: 6px solid var(--color-listi); padding-left: 12px; }
.urg-hned { border-left-color: var(--color-signal); }
.urg-tyden { border-left-color: var(--color-ink); }
```

### B3 „Stav po oblastech“: pruh se všemi stavy
Pruh složit ze 4 úseků (Zavedeno jedle · V procesu `brand-600` · Nezavedeno signál · Neposouzeno `slate-200`), pod ním legenda se slovy a čísly (už je). Úseky `role="img"` s `aria-label="Zavedeno 4, v procesu 2, nezavedeno 1, neposouzeno 14 z 21"`.

### B4 Opatření: upozornění do jednoho řádku
Tři odstavce před seznamem → jeden řádek „Platí pro vás vyhláška 410/2025 Sb. (nižší povinnosti). **Jak číst tento přehled**“ – `<details>` s dosavadním textem. Kartu „AI ve firmě“ ze stránky Opatření přesunout do roviny AI.

### B5 Formáty a žargon (z auditu kola 2)
Měsíce „2027-04“ → „duben 2027“, „Q2/2027“ → „2. čtvrtletí 2027“. Žargon (token, modul A, OSV) → slova z glosáře.

### B6 Logo
`app/templates/_logo.html.twig` → `<img src="{{ asset('images/brand/triconform-logo.svg') }}" alt="Triconform" width="150" height="30">` (tmavý motiv: `triconform-logo-negativ-pruhledne.svg`). Do té doby logo řeší CSS. Favicon `public/favicon.svg` ← `logo/favicon.svg`.

## C. Doklad pro odběratele (PDF)
Hlavička dokladu: logo B, název dokladu Source Serif 4. Ověřovací blok vpravo dole jako **razítko**: rámeček 2 px jedle, text „OVĚŘENO · kód 7F3K-29QD · 3. 11. 2026“ (IBM Plex Mono není nutné, stačí Public Sans tabulková čísla). Bez červené.

## Pořadí nasazení
1. Vrstva 1 (CSS + písma + logo soubory) → test → produkce.
2. A1, A2, A3, B1 (texty a menu) → test → produkce.
3. A4, B2, B3, B4 → test → produkce.
4. A5, B6, C.
