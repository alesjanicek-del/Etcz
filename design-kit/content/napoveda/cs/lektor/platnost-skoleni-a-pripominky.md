---
title: Platnost školení a připomínky opakování
source: https://demo.exam-test.cz/napoveda/lektor/platnost-skoleni-a-pripominky
lang: cs
---

Přehled, kdo má platné osvědčení, komu brzy vyprší a kdo má prošlé, export XLSX a e-mailové připomínky před koncem platnosti.

Testy, které vydávají osvědčení s omezenou platností, se dají sledovat v přehledu **Platnost školení**. Před koncem platnosti aplikace pošle připomínku e-mailem.

## Přehled Platnost školení

Otevřete **Vyhodnocení → Platnost školení**.

- Za každou osobu a test se počítá poslední splněné osvědčení. Když osoba test zopakuje a znovu splní, platí nové datum.
- Stav je **platné**, **brzy vyprší** (platnost skončí dřív, než za kolik dní chodí první připomínka; výchozí 30 dní) nebo **prošlé**.
- Filtrujte podle testu, pobočky a stavu a klikněte na **Filtrovat**.
- Tlačítko **Export platnosti (XLSX)** stáhne tabulku podle filtru.

Kdo co vidí, je stejné jako u výsledků: lektor osoby z použití, která vytvořil, administrátor pobočky svou pobočku a administrátor organizace všechny.

## Kdo v přehledu a v připomínkách není

Aplikace zatím nevede trvalou evidenci osob napříč zkouškami. Pokusy jedné osoby proto spojuje jen:

- podle uživatelského účtu (studující s přiděleným testem, **Moje testy**),
- podle e-mailu u přístupového kódu (kódy rozeslané e-mailem).

Pokusy z kódů bez e-mailu, z odkazů a z prezenčních zkoušek nejde spolehlivě přiřadit stejné osobě. Do přehledu ani připomínek se nedostanou. Přehled uvede jejich počet a jejich osvědčení najdete ve **Výsledcích**. Pokud chcete platnost sledovat, zadávejte opakovaná školení přidělením studujícím nebo kódy s e-mailem.

## Připomínky e-mailem

Nastavení je v **Správa → Nastavení organizace → Připomínky opakování školení**:

- **Posílat připomínky konce platnosti osvědčení**: zapne nebo vypne celé připomínky.
- **Kolik dní před koncem platnosti připomenout**: výchozí „30, 7“. Prázdné pole znamená, že přijde jen připomínka po vypršení.
- **Připomenout i po vypršení platnosti**: jednou, nejpozději 30 dní po konci platnosti.
- **Komu posílat souhrn připomínek**: lektorovi, který použití testu vytvořil (pokud už nemá aktivní účet, administrátorům organizace), administrátorům organizace nebo nikomu.

Jak připomínky chodí:

- Aplikace je kontroluje jednou denně ráno.
- Zkoušený dostane e-mail na adresu svého účtu nebo na e-mail u přístupového kódu. Příjemce souhrnu (lektor nebo administrátor organizace) dostane jeden souhrn za den se seznamem osob.
- Každá připomínka se pošle jen jednou. Aplikace si odeslané připomínky eviduje, takže opakovaná kontrola duplicitní e-mail nepošle. Když kontrola nějaký den neproběhne, pošle se jen nejnaléhavější připomínka.
- Krátké osvědčení nedostane připomínku hned po vydání. Například u měsíční platnosti přijde jen připomínka 7 dní předem.
- Připomínky vyžadují, aby aplikace měla nastavené odesílání e-mailů. Pokud ho nemá, upozorní vás na to stránka **Nastavení organizace**.

E-mailové připomínky zaměstnancům jsou zpracování osobních údajů vaší organizace jako správce. U zaměstnanců se obvykle opírají o povinnost zaměstnavatele zajistit opakované školení. Výchozí informace o zpracování osobních údajů pro zkoušené uvádějí připomínky, osvědčení i delší uchování pokusů s platným osvědčením. Pokud máte v **Nastavení organizace** vlastní text informací, doplňte je do něj.

Souhrn připomínek obsahuje jména zkoušených. Posílejte ho jen těm, kdo opakování školení organizují.

## Doba uchování a platnost osvědčení

Doba uchování výsledků (**Nastavení organizace → Data a texty**) může být kratší než platnost osvědčení. Aby osvědčení nepřišlo o jméno dřív, než vyprší, anonymizuje aplikace pokus s platným osvědčením až 30 dní po konci jeho platnosti. Osvědčení bez omezení platnosti anonymizaci nebrzdí. **Nastavení organizace** vás na takový rozdíl upozorní a uvede, kolik pokusů se takto drží.

Ruční anonymizace osoby na její žádost se neomezuje. Osvědčení pak už nejde stáhnout.

*Pro role: Lektor, Administrátor pobočky, Administrátor organizace*
