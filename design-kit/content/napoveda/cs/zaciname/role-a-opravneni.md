---
title: Role a oprávnění
source: https://demo.exam-test.cz/napoveda/zaciname/role-a-opravneni
---

# Role a oprávnění

Co smí administrátor organizace, administrátor pobočky, lektor, autor otázek, studující a zkoušený bez účtu.

## Role

Každý uživatel může mít více rolí, i v různých pobočkách. Role autora otázek se obvykle kombinuje s rolí lektora.

| Co lze dělat | Administrátor organizace | Administrátor pobočky | Lektor | Autor otázek | Studující | Zkoušený bez účtu |
|---|---|---|---|---|---|---|
| Nastavení organizace, logo, texty, uchování dat | ano | — | — | — | — | — |
| Pobočky | zakládá a upravuje | vidí své | — | — | — | — |
| Uživatelé, role, skupiny, zrušení ověření ve dvou krocích | ano | ve svých pobočkách (u uživatelů jen se svými pobočkami) | — | — | — | — |
| Soubory otázek | vše | ve své pobočce a podle práv | podle práv k souboru | podle práv k souboru | — | — |
| Schvalovat otázky | ano | jen když to organizace povolí | — | — | — | — |
| Testy | vše | ve své pobočce a podle práv | podle práv k testu | — | — | — |
| Použít test (kód, odkaz, přidělení, prezenční zkouška, tisk) | ano | ve své pobočce | ve své pobočce, smí-li test číst | — | — | — |
| Živý panel, prodloužení času, ukončení pokusu | ano | ve své pobočce | u svých použití | — | — | — |
| Tiskové dávky, klíče, zápis papírových odpovědí | ano | dávky své pobočky | dávky své pobočky | — | — | — |
| Výsledky, protokol, export | vše | ve své pobočce | u svých použití | — | vlastní výsledek | vlastní výsledek |
| Statistiky | ano | ano | podle práv k souboru | podle práv k souboru | — | — |
| Audit | ano | akce uživatelů svých poboček | — | — | — | — |
| Povolit přístup technika podpory | ano | — | — | — | — | — |
| Vyplnit test | — | — | — | — | přidělené testy | podle kódu nebo odkazu |
| Ověřit protokol | každý, i bez přihlášení | | | | | |

Administrátor pobočky nesmí jmenovat administrátora organizace.

## Práva k souborům otázek a k testům

Kromě role rozhoduje i právo ke konkrétnímu souboru otázek nebo testu:

- **Vlastník** má plný přístup, přiděluje práva ostatním, může soubor nebo test přesunout do koše a převést vlastnictví.
- **Editace** dovoluje upravovat obsah, vidět statistiky a u souboru otázek ho použít v testech.
- **Čtení** dovoluje použít ho v testech (u testu náhled a použití) a vidět statistiky, ale nic měnit.

Právo lze dát jednomu uživateli, celé pobočce nebo celé organizaci. Administrátor organizace má plný přístup ke všemu.

Jak práva přidělit, popisují kapitoly [Soubory otázek](../autor/soubory-otazek.md) a [Sestavení testu](../lektor/sestaveni-testu.md).

## Kdo smí co v pobočkách

- **Lektor** pracuje v pobočkách, kde má roli. Může jich mít víc a přepíná mezi nimi přepínačem **Aktivní pobočka**.
- **Administrátor pobočky** spravuje lektory, studující a skupiny své pobočky. Cizí pobočky nevidí.
- **Administrátor organizace** vidí všechny pobočky i výsledky bez pobočky.

*Pro role: všichni*
