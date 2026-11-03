---
title: Výsledky, protokol a uvolnění výsledků
source: https://demo.exam-test.cz/napoveda/lektor/vysledky-a-protokol
lang: cs
---

Přehled výsledků podle rolí a poboček, detail pokusu se záznamem průběhu, protokol PDF, uvolnění výsledků a export XLSX.

## Kdo vidí jaké výsledky

Otevřete **Vyhodnocení → Výsledky**.

- **Lektor** vidí výsledky použití, která sám vytvořil: v pobočkách, kde má roli lektora, a použití bez pobočky.
- **Administrátor pobočky** vidí výsledky všech poboček, které spravuje.
- **Administrátor organizace** vidí všechny výsledky, včetně použití bez pobočky.

Aktivní pobočka v horní liště výsledky nefiltruje. Kdo má roli ve více pobočkách, vidí výsledky ze všech najednou; jednu pobočku si vybere filtrem **Pobočka**. Aktivní pobočka určuje jen, kam se založí nové použití a které dávky ukáže **Tisk**.

Z detailu použití se na výsledky jen tohoto použití dostanete tlačítkem **Výsledky**.

## Filtr a export

- Filtrujte podle testu, pobočky, data, výsledku (**Splněno** / **Nesplněno**) a jména. Klikněte na **Filtrovat**.
- **Export výsledků (XLSX)** stáhne tabulku podle aktuálního filtru: zkoušený, test, způsob, pobočka, variace, časy, body, procenta, výsledek, známka a ověřovací kód.
- Administrátor organizace vidí navíc **Srovnání poboček** (počet osob, počet pokusů, průměr, úspěšnost) a stáhne ho tlačítkem **Export srovnání poboček (XLSX)**.
- U výsledků použití typu odkaz je tlačítko **Srovnat odkazy**. Porovná počet zahájených a odevzdaných pokusů, průměr, medián, úspěšnost a průměrný čas jednotlivých odkazů.
- Když filtrujete jeden test (nebo otevřete výsledky použití), přibudou tlačítka **Záznam o školení (PDF)** a **Záznam o školení (XLSX)**. Popisuje je kapitola [Osvědčení a záznam o školení](osvedceni-a-zaznam-o-skoleni.md). Osvědčení jednoho pokusu stáhnete v detailu výsledku.

## Pohledy podle způsobu zadání

- **Prezenční zkoušky** ukazují výsledky po jednotlivých zkouškách v místnosti.
- **Přidělené testy** ukazují u každého studujícího a skupiny, kdo test splnil, nesplnil nebo ho ještě nezahájil.
- **Platnost školení** ukazuje, kdo má platné osvědčení a komu brzy vyprší (kapitola [Platnost školení a připomínky opakování](platnost-skoleni-a-pripominky.md)).

## Detail pokusu

Klikněte na jméno zkoušeného. Detail obsahuje:

- **Vyhodnocení**: procenta, body, výsledek (splněno nebo nesplněno), čas zahájení a odevzdání a kdo odevzdal (zkoušený, vypršení času, lektor, papírový zápis, automaticky dohledem), prodloužení,
- **Ověřovací kód** a stav ověření záznamu,
- **Otázky a odpovědi** v pořadí variace, s verzí otázky, zvolenými a správnými odpověďmi a body,
- **Průběh testu (záznam)**: časovou osu událostí (zahájení, zobrazení otázek, změny odpovědí, opuštění okna, prodloužení, odevzdání). Události zaznamenané bez spojení (výpadek spojení) dorazí až po jeho obnovení; zařadí se podle času na zařízení zkoušeného, který je u nich uvedený.

Podrobnosti pro odborníky (kontrolní součty) jsou ve sbalené části **Technické údaje**.

## Protokol PDF

V detailu pokusu klikněte na **Protokol PDF**. Protokol obsahuje logo a údaje organizace, časový limit a prodloužení, všechny otázky a odpovědi, výsledek, záznam průběhu, ověřovací kód a QR kód pro ověření pravosti (kapitola [Ověření pravosti protokolu](../zkouseni/overeni-protokolu.md)).

Zkoušený si může stáhnout jen výpis pro zkoušeného: má stejný ověřovací kód, ale otázky jen v rozsahu podle nastavení zobrazení výsledků testu (u úředního testu nikdy se správnými odpověďmi). Výpis je tak označený v záhlaví. Do spisu (například jako přílohu protokolu o zkoušce) proto ukládejte protokol stažený zde, v detailu pokusu.

Každé stažení protokolu se zapíše do auditu.

## Uvolnění výsledků

Má-li test zapnuté **Výsledek zobrazit až po uvolnění lektorem**:

1. V seznamu výsledků zaškrtněte pokusy.
2. Klikněte na **Uvolnit vybrané výsledky zkoušeným**.

Sloupec **Uvolněno** ukazuje datum uvolnění, nebo „ne“. Studující výsledek uvidí v části **Moje výsledky**.

## Osobní údaje

Ochranu záznamu, anonymizaci a export dat provádí administrátor organizace (kapitola Osobní údaje, anonymizace a export dat).

*Pro role: Lektor, Administrátor pobočky, Administrátor organizace*
