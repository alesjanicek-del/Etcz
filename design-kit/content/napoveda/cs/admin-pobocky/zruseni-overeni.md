---
title: Zrušení ověření ve dvou krocích
source: https://demo.exam-test.cz/napoveda/admin-pobocky/zruseni-overeni
translation: unofficial-draft
---

Když uživatel ztratí telefon i záložní kódy. Nejdřív ověřte jeho totožnost.

## Postup

1. Ověřte totožnost žadatele, například telefonicky na známé číslo. Nikdy nerušte ověření jen na základě e-mailu.
2. V menu **Správa** → **Uživatelé** otevřete detail uživatele.
3. V části **Zrušit ověření ve dvou krocích** vyplňte **Důvod (povinné)**.
4. Klikněte na **Zrušit ověření** a potvrďte.

Administrátor pobočky zruší ověření jen uživateli, který má všechny role ve spravovaných pobočkách. Autorovi otázek a uživateli s rolí v jiné pobočce ho zruší administrátor organizace. Důvod musí mít alespoň 5 znaků.

## Co se stane

- Uživatel bude odhlášen a dostane e-mail.
- Při dalším přihlášení si ověření nastaví znovu.
- Akce se zapíše do auditu.

Má-li uživatel ještě záložní kód, zrušení nepotřebuje. Přihlásí se záložním kódem a ověření si nastaví znovu sám (kapitola [Ověření ve dvou krocích](../zaciname/overeni-ve-dvou-krocich.md)).

*Pro role: Administrátor pobočky, Administrátor organizace*
