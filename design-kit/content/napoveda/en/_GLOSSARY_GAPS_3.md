# Glossary gaps 3: admin-pobocky, admin-organizace

Terms used in the branch and organisation administrator help that are missing from the binding glossary (`_sablony/PREKLAD_EN.md`, brand.html 08b). Proposed EN in the second column. Please confirm or replace them in the app’s `docs/STYL_A_TERMINOLOGIE.md`.

## Roles and people

| CS | EN (proposed) | Note |
|---|---|---|
| studující | learner | App role: a person with an account who can be assigned a test. Kept apart from “test taker” (zkoušený = anyone taking a test). The lektor agent uses the same term. |
| skupina studujících | learner group | Menu item **Learner groups**. |
| Objednatel (zmocněnec) | Customer (authorised representative) | Role line. Matches the lektor articles. |
| zmocněnec objednatele | customer’s authorised representative | Contact role. |
| pověřenec pro ochranu osobních údajů | data protection officer | Standard GDPR term (DPO). |
| technik podpory Abuco | Abuco support technician | Also the audit label “Abuco support technician”. |
| provozovatel (aplikace) | app operator / operator | |
| pracovníci (administrátoři, lektoři, autoři) | staff users | Plan limit on non-learner accounts. |
| osobní číslo | staff number | Field **Staff number**. |

## Menus and screens

| CS | EN (proposed) | Note |
|---|---|---|
| Správa (menu) | **Administration** | Not yet in any EN design-kit page. Check against the app’s EN catalogue. |
| Audit (menu item), audit | **Change log**, change log | Glossary has “záznam změn → change log”. The CS menu says “Audit”. The article title keeps “Change log (audit)”. Confirm the menu label. |
| Nastavení organizace | **Organisation settings** | |
| Kontakty organizace | **Organisation contacts** | |
| Tarif a využití | **Plan and usage** | |
| Autoři otázek | **Question authors** | |
| Způsoby hodnocení / způsob hodnocení | **Grading methods** / grading method | Aligned with the lektor agent (“grading method”). |
| Objednávky | **Orders** | |

## Concepts

| CS | EN (proposed) | Note |
|---|---|---|
| zrušení ověření ve dvou krocích / Zrušit ověření | resetting two-step verification / **Reset verification** | “Reset” describes the effect (the user sets it up again). “Remove” would also work. |
| záložní kódy | backup codes | |
| zrušení pobočky (s převodem) / Zrušit pobočku a převést | closing a branch / **Close branch and transfer** | “Cancel” sounds wrong for a branch. |
| cílová pobočka | **Target branch** | |
| přihlášení odkazem z e-mailu | sign-in with an email link | Button **Email me a sign-in link**, as in en-prihlaseni.html. |
| doba uchování výsledků | result retention period | |
| ochrana záznamu (legal hold) | record protection | Used in the audit list. |
| informace o zpracování osobních údajů | privacy notice | |
| prohlášení o přístupnosti | accessibility statement | |
| povinný subjekt (zákon 99/2019 Sb.) | public sector body | Field **We are a public sector body under Act No. 99/2019 Coll., on Accessibility**. |
| práh úspěšnosti | pass mark | Also “threshold” in the grading type names. |
| pásma známek / nejhorší známka, se kterou … splnil | grade bands / **Lowest passing grade** | |
| částečné body | partial points | |
| úspěšnost (v %) | score | “Score is 70%”. |
| připomínky opakování školení | refresher training reminders | |
| zkušební provoz (stav tarifu) | trial | Status value. |
| daňový doklad | tax invoice | |
| odběratel | customer | Billing details. |
| registr smluv | Register of Contracts | Act No. 340/2015 Coll. |
| příspěvková organizace | state-funded organisation | Approximation; no exact UK equivalent. |
| předplatné | subscription | |

## Plan names

| CS | EN (proposed) | Note |
|---|---|---|
| tarif Síť | Síť (Network) plan | Product name kept in Czech with a gloss. Decide whether plans get EN names. |
| tarif Veřejná správa | Veřejná správa (Public Administration) plan | Same as above. |

## Uncertain points

- **Visible to test taker after submission** (Co zkoušený uvidí po odevzdání) is a default-settings label. The test editor uses a different CS label, translated by the lektor agent as **Results visible to test taker**. If the app uses one key for both, use one EN label.
- The grading example `90 1`, `75 2`, `50 3`, `0 4` follows the Czech scale, where 1 is the best grade. EN readers may need a note.
- Link targets not in the crawl: “Osobní údaje, anonymizace a export dat” and “Hlášení vady a požadavku na podporu”. Both are plain text with an HTML comment to add the link.
- Links to other categories use the slug only. Their EN titles (“Two-step verification”, “Question approval”, “Training validity and refresher reminders”) must match the titles the other agents choose.
