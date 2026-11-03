---
title: Sestavení testu krok za krokem
source: https://demo.exam-test.cz/napoveda/lektor/sestaveni-testu
lang: cs
---

Průvodce Základ → Sekce → Parametry → Kontrola. Povinné a náhodně vybírané otázky, štítky, čas, heslo, hodnocení a úřední režim.

Otevřete **Testy a zkoušení → Testy → Nový test**. Průvodce má čtyři kroky: **Základ**, **Sekce**, **Parametry** a **Kontrola**.

## Krok 1: Základ

- **Název testu**,
- **Popis**: jen pro vás a kolegy, zkoušený ho neuvidí,
- **Úvodní stránka**: pokyny, které zkoušený uvidí před zahájením.

Test se založí v aktivní pobočce. Pokračujte tlačítkem **Založit test a pokračovat**.

## Krok 2: Sekce

Každá sekce vybírá otázky z jednoho souboru otázek. Test může mít víc sekcí, například „Radiační ochrana“ a „BOZP“.

1. V části **Přidat sekci** zvolte **Soubor otázek**, případně **Nadpis sekce**, a klikněte na **Přidat sekci**. Nabízejí se jen soubory, které smíte použít v testu.
2. U sekce klikněte na **Upravit sekci** a nastavte:
   - **Váha sekce v hodnocení**,
   - **Náhodně vybrat nejméně** a **Náhodně vybrat nejvíce**: kolik otázek se losuje kromě povinných. Stejné číslo v obou polích znamená pevný počet,
   - **Povinné a vyloučené otázky**: zaškrtněte **Povinná** (dostane ji každý zkoušený) nebo **Vyloučit** (nikdy se nevybere). Pole **Filtrovat otázky** jen zužuje zobrazení,
   - **Povolené štítky**: losuje se jen z otázek s nimi. Volba **Otázka musí mít** určí, zda stačí jeden z povolených štítků, nebo musí mít všechny,
   - **Zakázané štítky**: takové otázky se nevylosují.
3. **Souhrn sekce** nahoře se při každé změně přepočítá: **Povinné**, **Kandidátů**, **Vybírá se náhodně** a **Možných výběrů**. Když otázky nestačí, uvidíte vysvětlení chyby.
4. Uložte tlačítkem **Uložit sekci**, nebo **Uložit a zůstat**.

Pořadí sekcí měníte šipkami ↑ ↓, sekci odstraníte tlačítkem **Odebrat**. Dokud test obsahuje chyby, krok **Kontrola** je zamčený.

## Krok 3: Parametry

Parametry se předvyplní z nastavení organizace.

Když už test zkoušení ostře vyplnili, nelze měnit časový limit, počet pokusů, zobrazení výsledků, zpětnou vazbu, způsob hodnocení ani úřední režim. Změnit jde jen heslo, zobrazení otázek, osvědčení a záznam o školení a dohled nad zkouškou. Jiné parametry nastavíte v kopii testu (**Vytvořit kopii testu**).

### Průběh testu

- **Časový limit (minuty)**: prázdné pole znamená bez limitu,
- **Míchat pořadí otázek**,
- **Zobrazení otázek**: jedna otázka na stránku, nebo všechny na jedné stránce.

### Přístup a opakování

- **Heslo pro přístup k testu**: nepovinné,
- **Maximální počet pokusů**: prázdné pole znamená neomezeně,
- **Další pokus jen při nesplnění**.

### Výsledky a zpětná vazba

- **Zobrazení výsledků zkoušenému**: nic (jen potvrzení odevzdání), výsledek, výsledek a chybně zodpovězené otázky, nebo plné vyhodnocení se správnými odpověďmi,
- **Výsledek zobrazit až po uvolnění lektorem**,
- **Zpětná vazba k odpovědím**: nezobrazovat, po vyhodnocení testu, nebo ihned po potvrzení odpovědi (cvičné testy).

### Způsob hodnocení

Vyberte přednastavený způsob hodnocení organizace, nebo **Vlastní hodnocení tohoto testu** (typ, práh, pásma známek a částečné body). Pole vlastního hodnocení se zobrazí po výběru **Vlastní hodnocení tohoto testu**. Bez výběru platí úspěšnost 80 %. Viz kapitola [Způsoby hodnocení](../admin-organizace/zpusoby-hodnoceni.md).

### Úřední režim

**Úřední test**: zkoušený nedostane zpětnou vazbu ani správné odpovědi, maximální počet pokusů je povinný a test nelze použít přes odkaz. Pro zkoušky zvláštní odborné způsobilosti ho zapínejte vždy. Úřední test nevydává osvědčení.

### Osvědčení a záznam o školení

**Vydávat osvědčení při splnění** s platností v měsících, **Název školení**, **Školitel**, **Vyžadovat potvrzení proškoleného** a **Osnova školení**. Podrobnosti popisuje kapitola [Osvědčení a záznam o školení](osvedceni-a-zaznam-o-skoleni.md).

Uložte tlačítkem **Uložit a přejít na kontrolu**.

## Krok 4: Kontrola

Kontrola shrne sekce a parametry, celkový počet otázek a **Možných unikátních variací**.

Unikátní variace se liší výběrem otázek, pořadím otázek (je-li zapnuté míchání otázek) nebo pořadím odpovědí (u otázek s mícháním odpovědí). Stejně počítá tisk i zkoušení online. Přednost má výběr otázek, který ještě nikdo nedostal; teprve potom nové pořadí otázek a nakonec nové pořadí odpovědí. Pokusy nanečisto se nezapočítávají. Když jsou všechny kombinace použité, online zkoušení pokračuje s nejméně použitou kombinací. Tisk se neodmítne: další variace zopakují nejméně použité kombinace a dávka i klíč to výrazně uvedou.

Do pole **Očekávaný počet pokusů** zadejte, kolik lidí čekáte, a klikněte na **Přepočítat**. Je-li variací málo, aplikace poradí, jak výběr rozšířit.

Na konci jsou tlačítka **Náhled variace**, **Zkusit nanečisto**, **Použít test** a **Hotovo**.

## Přehled testů

**Testy** mají záložky **Aktivní**, **Archivované** a **Koš** a filtr **Hledat podle názvu**, **Jen moje testy** a **Pobočka**. Sloupec **Kontrola** ukazuje „V pořádku“, nebo počet chyb.

U testu jsou tlačítka **Použít** a **Upravit** (s právem čtení **Náhled**). Další akce najdete v nabídce **Další**: **Náhled**, **Zkusit nanečisto**, **Vytvořit kopii**, **Práva**, **Archivovat** a **Do koše**. Archivovaný test vrátíte tlačítkem **Obnovit z archivu**, test z koše tlačítkem **Obnovit**. Použitý test nelze přesunout do koše, jen archivovat.

Tlačítko **Nový test** nevidíte? Organizace lektorům zakládání testů zakázala. Požádejte administrátora.

## Práva k testu

Práva přiděluje vlastník testu: u testu klikněte na **Práva**. Právo dáte uživateli, pobočce nebo celé organizaci:

- **Čtení**: náhled a použití testu,
- **Editace**: úpravy sekcí a parametrů,
- **Vlastník**: vše včetně práv a převodu vlastnictví.

*Pro role: Lektor, Administrátor pobočky, Administrátor organizace*
