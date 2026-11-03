---
title: Přihlášení odkazem z e-mailu
source: https://demo.exam-test.cz/napoveda/admin-organizace/prihlaseni-odkazem
translation: unofficial-draft
---

Uživatelé se mohou přihlásit jednorázovým odkazem z e-mailu místo hesla. Funkce je ve výchozím stavu vypnutá.

## Co funkce dělá

Po zapnutí přibude na přihlašovací stránce organizace volba **Poslat přihlašovací odkaz e-mailem**. Uživatel zadá svůj e-mail a přijde mu odkaz, kterým se přihlásí bez hesla.

- Odkaz platí **15 minut** a lze ho použít **jen jednou**.
- Odkaz nahrazuje heslo, **ne ověření ve dvou krocích**. Kdo má ověření zapnuté nebo povinné, zadá po otevření odkazu kód z telefonu stejně jako po zadání hesla.
- Odkaz platí jen pro vaši organizaci. Do jiné organizace se jím přihlásit nelze.
- Odkaz zneplatní změna hesla, odhlášení ze všech zařízení i každé další přihlášení.
- Odkaz dostane jen aktivní účet, který už má nastavené heslo. Nově pozvaný uživatel nejdřív dokončí pozvánku.
- Odpověď na žádost je vždy stejná, i když účet neexistuje. Podle ní nejde zjistit, kdo u vás má účet.
- Vydání odkazu i přihlášení odkazem se zapisují do auditu. Odkaz samotný se nikam neukládá.

## Jak funkci zapnout

1. Otevřete **Správa** → **Nastavení organizace**.
2. V části **Přihlášení** zaškrtněte **Povolit přihlášení odkazem z e-mailu**.
3. Klikněte na **Uložit nastavení**.

Změna se zapíše do auditu. Stejným postupem funkci vypnete. Po vypnutí přestanou platit i odkazy, které už byly odeslané.

Funkci může na vaši žádost zapnout nebo vypnout i provozovatel. Dostanete o tom e-mail a změna je v auditu organizace s důvodem.

## Kdy přihlášení odkazem nezapínat

S přihlášením odkazem závisí bezpečnost účtu na zabezpečení e-mailové schránky. Kdo získá přístup do schránky uživatele, může se přihlásit za něj.

- **Úřední zkoušky:** funkci je vhodné nechat vypnutou, nebo ji zapnout jen spolu s volbou **Povinné ověření ve dvou krocích i pro lektory**. Administrátoři a autoři mají ověření povinné vždy.
- **Sdílené schránky:** pokud lektoři používají společnou schránku oddělení, funkci nezapínejte.
- Bez fungující pošty odkaz nedorazí. Uživatelé se pak přihlásí heslem jako dosud.

*Pro role: Administrátor organizace*
