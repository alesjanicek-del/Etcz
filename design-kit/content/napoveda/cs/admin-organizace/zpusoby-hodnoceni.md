---
title: Způsoby hodnocení
source: https://demo.exam-test.cz/napoveda/admin-organizace/zpusoby-hodnoceni
translation: unofficial-draft
---

Přednastavená pravidla, podle kterých se určí, zda zkoušený test splnil. Procento, body, známky podle pásem nebo povinné otázky.

Způsob hodnocení určuje, zda zkoušený test splnil. Administrátor organizace připraví způsoby hodnocení a lektoři si je vybírají v parametrech testu. Lektor může u testu nastavit i vlastní hodnocení.

## Nový způsob hodnocení

Otevřete **Správa** → **Způsoby hodnocení** → **Nový způsob hodnocení**.

- **Název**, například „ZOZ – 80 %“.
- **Typ hodnocení**:
  - **Procento správných s prahem**: test splní, kdo dosáhne alespoň zadaného procenta bodů,
  - **Body s prahem**: test splní, kdo získá alespoň zadaný počet bodů,
  - **Známky podle pásem**: podle dosaženého procenta dostane zkoušený známku; test splní se zadanou nejhorší známkou nebo lepší,
  - **Všechny povinné otázky správně a zároveň práh %**: kromě procenta musí být správně každá povinná otázka.
- **Práh úspěšnosti (%)** nebo **Práh úspěšnosti (body)**.
- **Pásma známek**: na každý řádek minimální procento, mezeru a známku, například `90 1`, `75 2`, `50 3`, `0 4`. Pásma musí začínat od 0 %. Dále **Nejhorší známka, se kterou zkoušený test splnil**.
- **Částečné body u otázek s více správnými odpověďmi**. Bez zaškrtnutí je taková otázka správně jen při přesné shodě.
- **Výchozí způsob hodnocení organizace**: předvyplní se u nových testů. Výchozí může být jen jeden.

Bez výběru způsobu hodnocení platí úspěšnost 80 %.

## Smazání a archivace

V přehledu **Způsoby hodnocení** ukazuje sloupec **Použito**, kolik testů způsob hodnocení používá.

- **Smazat** jde jen způsob hodnocení, který nepoužívá žádný test.
- Použitý způsob hodnocení archivujte tlačítkem **Archivovat**. U nových testů ani jako výchozí se pak nenabízí. Testy, které ho používají, hodnotí dál beze změny. Archivovaný způsob najdete ve sbalené části **Archivované způsoby hodnocení** a tlačítkem **Obnovit** ho vrátíte mezi nabízené.

Smazání, archivace i obnovení se zapíšou do auditu.

## Jak se výsledek počítá

Úspěšnost je podíl získaných bodů z maximálního počtu bodů testu v procentech (váhy sekcí se započítají). Zobrazuje se na desetiny procenta. Příklad: test má 10 otázek po 1 bodu a práh 80 %. Zkoušený odpoví správně na 7 otázek, získá 7 z 10 bodů, úspěšnost je 70 % a test nesplnil. Ke splnění potřeboval alespoň 8 bodů.

Výsledek zkoušeného, detail výsledku pro lektora i protokol PDF uvádějí totéž: **Pravidlo hodnocení** (i s přepočtem prahu na body), **Jak vznikl výsledek** (body, úspěšnost, splněno nebo nesplněno) a u nesplněného testu **Důvod nesplnění**. Pravidlo se bere ze záznamu pokusu, pozdější změna způsobu hodnocení na již odevzdané pokusy nepůsobí.

*Pro role: Administrátor organizace*
