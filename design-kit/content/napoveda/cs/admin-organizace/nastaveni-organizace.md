---
title: Nastavení organizace
source: https://demo.exam-test.cz/napoveda/admin-organizace/nastaveni-organizace
translation: unofficial-draft
---

Název a logo, procesy (schvalování, ověření ve dvou krocích, odkazy), výchozí parametry testů, doba uchování, texty pro zkoušené a údaje prohlášení o přístupnosti.

Otevřete **Správa** → **Nastavení organizace**. Změny uložíte tlačítkem **Uložit nastavení**. Každá změna se zapíše do auditu: ve sloupci **Podrobnosti** uvidíte, co se změnilo, z jaké hodnoty na jakou. Delší texty se v auditu zkracují, e-maily jsou zkrácené na první písmeno a doménu.

## Organizace

- **Název organizace**: zobrazuje se v aplikaci, na protokolech a v tiskových sestavách.
- **Kontaktní e-mail**.
- **Logo**: PNG, JPEG nebo WebP do 2 MB. Zobrazuje se v aplikaci, v protokolu i v tisku.

## Procesy a oprávnění

- **Schvalování otázek**: do testů jde jen schválená verze otázky (kapitola [Schvalování otázek](../autor/schvalovani-otazek.md)).
- **Otázky smí schvalovat i administrátoři poboček**.
- **Povinné ověření ve dvou krocích i pro lektory**. Pro administrátory, autory otázek a lektory, kteří vlastní nebo smí upravovat soubor otázek nebo test, je povinné vždy.
- **Lektoři smí zakládat soubory otázek** a **Lektoři smí zakládat testy**.
- **Povolit použití testu přes odkaz (anonymní zkoušení)**. Vypnutí zakáže nové odkazy.

## Přihlášení

- **Povolit přihlášení odkazem z e-mailu**: uživatelé se mohou přihlásit jednorázovým odkazem místo hesla. Ve výchozím stavu vypnuto. Kdy funkci zapnout, popisuje kapitola [Přihlášení odkazem z e-mailu](prihlaseni-odkazem.md).

## Výchozí parametry nových testů

**Časový limit (minuty)**, **Maximální počet pokusů**, **Co zkoušený uvidí po odevzdání**, **Reakce na odpověď** a další. Lektor je může u testu změnit.

## Připomínky opakování školení

**Posílat připomínky konce platnosti osvědčení**, **Kolik dní před koncem platnosti připomenout** (výchozí „30, 7“), **Připomenout i po vypršení platnosti** a **Komu posílat souhrn připomínek**. Podrobnosti popisuje kapitola [Platnost školení a připomínky opakování](../lektor/platnost-skoleni-a-pripominky.md).

## Data a texty

- **Doba uchování výsledků (měsíce)**: po jejím uplynutí se osobní údaje zkoušených anonymizují. Protokoly zůstanou ověřitelné. Výchozí je 60 měsíců. Pokus s platným osvědčením se anonymizuje až 30 dní po konci platnosti osvědčení.
- **Úvodní text před testem**: zkoušení ho uvidí na úvodní stránce testu.
- **Patička protokolu o zkoušce**.
- **Informace o zpracování osobních údajů**: zkoušení je otevřou odkazem z úvodní stránky testu. Když text nevyplníte, použije se výchozí text s kontaktem organizace a dobou uchování.

## Prohlášení o přístupnosti

Údaje pro [prohlášení o přístupnosti](/prohlaseni-o-pristupnosti), které se zobrazuje na adrese vaší organizace:

- **Jsme povinný subjekt podle zákona č. 99/2019 Sb., o přístupnosti**: zaškrtněte, je-li vaše organizace úřadem, obcí, krajem, školou nebo jinou veřejnoprávní institucí. Prohlášení pak vydáváte jako své. Jako dozorový orgán v něm bude uvedeno Ministerstvo vnitra. U tarifu Veřejná správa je zaškrtnuto předem. Když políčko nezaškrtnete, prohlášení uvede, že ho vydáváte dobrovolně.
- **Datum vypracování nebo schválení prohlášení**: datum, kdy jste prohlášení zkontrolovali a schválili. Když ho nevyplníte, uvede se datum, kdy návrh připravil provozovatel aplikace.
- **Odkaz na prohlášení nebo web organizace**: adresa, na které prohlášení zveřejňujete na svém webu.
- **E-mail pro podněty k přístupnosti**: když ho nevyplníte, použije se **Kontaktní e-mail**.

Seznam nedostatků aplikace a jejich odstranění doplňuje provozovatel.

## Přístup podpory

Viz kapitola [Přístup technika podpory](pristup-podpory.md).

*Pro role: Administrátor organizace*
