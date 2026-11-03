# Zadání: překlad do angličtiny (exam-test, design kit + obsah)

Pracuješ v `/home/user/Etcz/design-kit/`. Nejdřív si přečti `_sablony/ZADANI.md` (formát fragmentů, build, kontrola) a kapitolu 08b v `brand.html` (glosář EN).

## Výstup podle typu
**A. Stránky design kitu.** Z českého fragmentu `src/<oddil>/<x>.html` vytvoř `src/<oddil>/en-<x>.html`.
- Do meta doplň `"lang":"en"` a `"cs_verze":"<x>.html"`; ostatní pole meta zůstanou (sablona, role, aktivni).
- Přelož veškerý viditelný text i `alt`, `aria-label`, `title`, `placeholder`, `<caption>` a `.sr-only`.
- Interní odkazy veď na `en-*.html` ve stejném oddílu (`testy.html` → `en-testy.html`, `../web/cenik.html` → `../web/en-cenik.html`).
- Specifikaci (`<!--spec … -->`) přelož do angličtiny.
  - `texty`: `dnes` = český text návrhu, `nove` = anglický text, `proc` = důvod volby termínu (glosář).
  - `zmeny_ux`: jen to, co se liší od české verze (délka, jiné zalomení, jiná slova). Ostatní odkaž na českou stránku.
- Vlastní jména, ukázkové osoby, názvy organizací a kódy nech. Ukázkový obsah otázek přelož. Obsah, který v EN zůstává česky (např. závazný právní text), obal do `lang="cs"`.
- Postup: `python3 tools/build.py src/<oddil>/en-<x>.html`, pak `node tools/check.js <oddil>/en-<x>.html` (0 chyb, kontrola hlídá i češtinu v EN), pak `node tools/check_en.js <oddil>/en-<x>.html` (délka). Opravuj, dokud vše neprojde. U každé stránky jeden screenshot na 375 px (`node tools/shot.js … 375`) a prohlédnout.

**B. Právní texty (neoficiální překlad).** Stránka EN začíná upozorněním `.alert--info`: „Unofficial translation. The Czech version is legally binding. [link to Czech version]“. Text přelož věrně, nezkracuj, zachovej číslování článků. Blok „V kostce“ přelož jako „At a glance“.

**C. Nápověda (Markdown).** Pro každý článek vytvoř `content/napoveda/en/<kategorie>/<slug>.md` a k němu českou předlohu `content/napoveda/cs/<kategorie>/<slug>.md`, převedenou z crawlu do Markdownu (podklad pro porovnání).
- Front matter `--- title: … / source: https://demo.exam-test.cz/napoveda/<kategorie>/<slug> / translation: unofficial-draft ---`.
- Nadpisy `##`, seznamy, tabulky Markdown. Názvy prvků rozhraní (tlačítka, menu) piš **tučně** přesně podle glosáře a anglického názvu v design kitu.
- Struktura se při převzetí do repozitáře aplikace přizpůsobí `content/napoveda/` (tam je zdroj pravdy).

## Styl angličtiny
- Britský pravopis (organisation, centre, licence), apostrof ’, uvozovky “ ”.
- Krátké věty (kontrola hlásí > 25 slov), druhá osoba, aktivní rod, sloveso první v tlačítkách. Žádné „please“ v tlačítkách.
- Čísla číslicemi, `15&nbsp;min`, `80&nbsp;%` → v EN `80%` bez mezery, data `3 Nov 2026`, čas `17:41`, desetinná tečka `83.3%`, měna `CZK 9,900`.
- Nepoužívat: proctoring, examinee v rozhraní pro zkoušené (oslovujeme „you“), dashboard, click here, please submit.

## Glosář (závazný pro tento úkol)
| CS | EN |
|---|---|
| zkoušený | test taker (v textech o úředních zkouškách smí být „candidate“) |
| lektor | instructor |
| autor otázek | question author |
| administrátor pobočky / organizace | branch administrator / organisation administrator |
| pobočka | branch |
| pokus | attempt |
| variace | test version |
| soubor otázek | question bank |
| seznam štítků / štítek | tag list / tag |
| test, sekce testu | test, test section |
| použití testu | test assignment |
| prezenční zkouška | supervised in-room exam |
| osobní kódy · veřejný odkaz · přidělení skupině · tisk | personal access codes · public link · assigned to a group · print |
| živý panel | live monitor |
| čekárna · promítací plocha | waiting room · projector screen |
| kód pro převzetí | handover code |
| dohled | monitoring |
| protokol (o výsledku) | result report |
| ověřovací kód · kód variace · přístupový kód | verification code · version code · access code |
| osvědčení · záznam o školení · platnost školení | certificate · training record · training validity |
| cvičný test · zkouška nanečisto | practice test · trial run |
| splněno · nesplněno | Passed · Not passed |
| zpřístupnit výsledky · zkoušený vidí | release results · visible to test taker |
| ke schválení · schválit · vrátit do konceptu | pending approval · approve · return to draft |
| koncept | draft |
| koš | Deleted items |
| záznam změn | change log |
| tarif · zálohová faktura | plan · proforma invoice |
| Vyzkoušet demo · Ukázka s průvodcem | Try the demo · Book a guided demo |
| Další otázka · Vrátit se později · Zkontrolovat a odevzdat · Odevzdat test | Next question · Flag for review · Review and submit · Submit test |
| Nápověda k této stránce · Můj účet · Odhlásit | Help for this page · My account · Sign out |
| ověření ve dvou krocích | two-step verification |

Výraz, který v glosáři chybí a opakuje se, zapiš do spec `poznamky_pro_kodera` jako „Glossary gap: cs → en“. Na konci ho uveď i v hlášení.

## Pravidla
- Neměň české stránky, `assets/*`, `tools/*`, `_sablony/*`, `sitemap.json` ani soubory jiných agentů.
- Nic neodesílej na exam-test.cz. Demo smíš jen číst.
- Na konci vrať tabulku: soubor → kontrola ✓/✗ → délka ✓/✗. K ní seznam mezer v glosáři a míst, kde si překladem nejsi jistý.
