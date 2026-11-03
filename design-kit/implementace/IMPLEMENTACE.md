# Rebrand B: nasazení do aplikace (Symfony, Tailwind v4, AssetMapper)

Cíl: nový vzhled bez úprav šablon Twig. HTML zůstává stejné, takže HTML goldeny i čeština se nemění.

## Kroky (zhruba 30 minut)
1. Písma: `design-kit/assets/fonts/*.woff2` → `assets/fonts/`, `design-kit/assets/fonts.css` → `assets/styles/fonts.css`. V `fonts.css` uprav cestu na `../fonts/`.
2. `design-kit/implementace/rebrand-b.css` → `assets/styles/rebrand-b.css`.
3. V `assets/styles/app.css` hned za `@import "tailwindcss";` přidej:
   `@import "./fonts.css";` a `@import "./rebrand-b.css";`
4. Veřejný web (`layout/public.html.twig`): soubor `rebrand-b.css` musí být až po `web.css`. Buď ho načti tam druhým `<link>`, nebo přesuň sekci 5 (WEB) na konec `web.css`.
5. Logo a favicony: `design-kit/assets/logo/` → `public/images/brand/`. Značku v hlavičce webu i aplikace nahraď za `exam-test-logo.svg`. Favicony vyměň podle logo manuálu.
6. `php bin/console tailwind:build`, pak goldeny a e2e. Vizuální snímky se změní (`GOLDEN_UPDATE=1`, samostatný commit `test(golden)`). Texty se změnit nesmí.

## Co soubor dělá
| Dnes (třída / utilita) | Nově |
|---|---|
| `slate-50…900` | papír #F6F4EC → grafit #22262A, sekundární text #5A6068 |
| `brand-700` (modrá) | propiska #2747A0: odkazy a fokus |
| `btn-primary` | grafit, světlý text, tvrdý žlutý stín 4 px |
| `btn`, `btn-secondary` | bílá, rámeček 2 px grafit |
| `btn-danger` | bílá, červený rámeček i text |
| `badge-*` | mono verzálky 13 px s rámečkem, barva + text |
| `card` | bez zaoblení, rámeček 2 px grafit |
| `text-xs / sm / base / lg / xl / 2xl / 3xl` | 13 / 15 / 17 / 22 / 22 / 30 / 30 px (5 rolí) |
| `rounded-*` | 0 (`rounded-full` zůstává) |
| demo lišta `bg-amber-50 border-amber-300` | žlutý pruh zvýrazňovače |
| boční menu, aktivní položka | plná grafitová |
| `web-*` | hlavička, hero s mřížkou, karty, patička grafit |

## Ručně v šablonách (druhá vlna, nespěchá)
- Logo (krok 5).
- Stavové štítky „splnil(a)/nesplnil(a)“ → „Splněno / Nesplněno“ (pozor: změna textu → goldeny).
- Komponenty, které CSS nedokáže: odpovědní list (`.sheet-box`), kód variace (`.kod`), přepínač jazyka. Vzor je v `design-kit/komponenty.html`.

## Ověření
Náhledy v `nahled/` vznikly vložením souboru do živého webu a dema (bez úprav HTML). Před nasazením na produkci ověř, že neběží žádný pokus.
