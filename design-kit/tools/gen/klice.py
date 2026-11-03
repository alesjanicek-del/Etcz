from common import *
V1=[("A, C, D, E, G",2),("B",1),("B",2),("A, C, F",2),("A, B, E",2),("D",1),("C",1),("C",1),("A",1),("D",1),("B, D, F",2),("D",1)]
V2=[("B",2),("B",1),("C, D, E",2),("B",1),("A, B, C",2),("D",1),("B, C, E",2),("A",1),("D",1),("C",1),("D",1),("D",1)]
TD='style="padding:var(--s-2) var(--s-2);border-bottom:var(--b-tenka) solid var(--c-linka)"'
TH='class="t-stitek" style="font-weight:var(--w-mono);text-align:left;padding:var(--s-2);border-bottom:var(--b-silna) solid var(--c-grafit)"'
band='<div class="section--grafit row-between" style="padding:var(--s-2) var(--s-3)"><p class="t-stitek">Důvěrné · klíč · nerozdávat</p><p class="t-stitek">Každé stažení je v&nbsp;auditu</p></div>'
def ktab(n,kod,mx,data):
    rows=''.join(f'<tr><th scope="row" class="t-cislo" {TD.replace("style=\"","style=\"text-align:left;")}>{i:02d}</th><td class="t-kod" {TD}>{a}</td><td class="t-cislo" {TD.replace("style=\"","style=\"text-align:right;")}>{b}</td></tr>' for i,(a,b) in enumerate(data,1))
    return f'''<table style="width:100%;border-collapse:collapse">
 <caption style="text-align:left;padding-bottom:var(--s-2);border-bottom:var(--b-akcent) solid var(--c-grafit)"><span class="row-between"><span class="t-stitek">Variace {n}</span><b class="t-kod t-nadpis">{kod}</b><span class="t-maly">max. {mx}&nbsp;b.</span></span></caption>
 <thead><tr><th scope="col" {TH}>Ot.</th><th scope="col" {TH}>Správně</th><th scope="col" {TH.replace("text-align:left","text-align:right")}>Body</th></tr></thead>
 <tbody>{rows}</tbody>
</table>'''
srows=''.join(f'<tr><td class="t-cislo" {TD}>{n}</td><td class="t-kod" {TD}>{k}</td><td {TD.replace("style=\"","style=\"white-space:nowrap;")}>Návštěvník 6013</td><td class="t-cislo" {TD.replace("style=\"","style=\"text-align:right;")}>12</td><td class="t-cislo" {TD.replace("style=\"","style=\"text-align:right;")}>{m}</td><td {TD.replace("style=\"","style=\"min-width:160px;")}><span class="sr-only">vyplní lektor</span></td><td {TD.replace("style=\"","style=\"min-width:64px;")}><span class="sr-only">vyplní lektor</span></td></tr>' for n,k,m in [(1,"UG98N3X6",17),(2,"A6WR8XTV",16)])
th2=lambda t,r=False: f'<th scope="col" {TH.replace("text-align:left","text-align:right") if r else TH}>{t}</th>'
p1=f'''{band}
<header class="stack-2">
 <p class="t-stitek">Klíče a vyhodnocovací tabulka · dávka „Náhled pro návrh“</p>
 <h1 class="t-nadpis">{TEST}</h1>
 <p class="t-maly">Ukázková organizace (demo) · Návštěvník 6013 · počet variací: 2 · vytvořeno 3.&nbsp;11.&nbsp;2026 18:20</p>
</header>
<section class="stack" aria-labelledby="souhrn-h">
 <h2 id="souhrn-h" class="t-nadpis">Souhrnná tabulka dávky</h2>
 <p class="t-maly">Po opravě listů zapište jméno a body. Pak odpovědi zapište do aplikace: Tisk → dávka → Zápis papírových odpovědí.</p>
 <table style="width:100%;border-collapse:collapse">
  <caption class="sr-only">Variace dávky s kódy a maximem bodů; sloupce Jméno a Body vyplní lektor</caption>
  <thead><tr>{th2("Variace")}{th2("Kód")}{th2("Pobočka")}{th2("Otázek",1)}{th2("Max. bodů",1)}{th2("Jméno")}{th2("Body")}</tr></thead>
  <tbody>{srows}</tbody>
 </table>
</section>
{foot(TEST+' · Klíče · DŮVĚRNÉ','strana 1 / 2')}'''
p2=f'''{band}
<header class="stack-2">
 <p class="t-stitek">Klíče po variacích · dávka „Náhled pro návrh“</p>
 <p class="t-nadpis">{TEST}</p>
</header>
<section aria-labelledby="klice-h" class="stack">
 <h2 id="klice-h" class="sr-only">Klíče po variacích</h2>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:var(--s-5)">{ktab(1,"UG98N3X6",17,V1)}{ktab(2,"A6WR8XTV",16,V2)}</div>
 <p class="t-maly">Otázky s&nbsp;více odpověďmi se hodnotí podle způsobu hodnocení nastaveného u&nbsp;testu.</p>
</section>
{foot(TEST+' · Klíče · DŮVĚRNÉ','strana 2 / 2')}'''
spec={"route":"(PDF) Tisk → dávka → Klíče","nazev":"Klíče a vyhodnocovací tabulka (A4)","role":"lektor (důvěrné)","sablona":"a4",
"ucel":"Důvěrný dokument pro opravu papírových listů: souhrn variací dávky k ručnímu vyplnění a klíč správných odpovědí s body pro každou variaci.",
"hlavni_akce":"Opravit odpovědní listy podle klíče a zapsat body do souhrnné tabulky",
"komponenty":["a4","section--grafit (pruh Důvěrné)","t-stitek","t-kod","t-cislo","table (tisková)"],
"stavy":["strana 1: souhrnná tabulka dávky (nakresleno)","strana 2+: klíče po 2 variacích na stranu (nakresleno); při 20+ otázkách 1 variace na stranu","velká dávka (až 500 variací): souhrn pokračuje na dalších stranách, záhlaví tabulky se opakuje","prázdný/chyba/oprávnění: soubor stáhne jen lektor/administrátor; každé stažení se zapíše do auditu"],
"zmeny_ux":["Tmavý pruh „Důvěrné · klíč · nerozdávat“ nahoře na každé straně místo dnešního šikmého vodoznaku – čitelné i při ČB tisku a nepřekrývá text.","Pruh připomíná, že každé stažení je v auditu (odrazuje od rozdávání).","Souhrnná tabulka má prázdné sloupce Jméno a Body s minimální šířkou pro ruční vyplnění.","Klíč: každá variace má nad tabulkou velký kód (stejný jako na listu), správné odpovědi mono písmeny, body zarovnané vpravo.","Návod pod souhrnem: kam body a odpovědi zapsat v aplikaci."],
"texty":[{"dnes":"DŮVĚRNÉ · KLÍČ – NEROZDÁVAT (vodoznak a záhlaví)","nove":"Důvěrné · klíč · nerozdávat | Každé stažení je v auditu","proc":"Jednou, v pruhu; doplněn důsledek."},{"dnes":"Kybernetická bezpečnost — roční ověření – klíče a vyhodnocovací tabulka","nove":"Klíče a vyhodnocovací tabulka · dávka „Náhled pro návrh“ (štítek) + název testu","proc":"Typ dokumentu a dávka ve štítku."},{"dnes":"Variace 1 – UG98N3X6","nove":"Variace 1 · UG98N3X6 · max. 17 b.","proc":"Maximum bodů u variace – nemusí se sčítat."},{"dnes":"(nic)","nove":"Po opravě listů zapište jméno a body. Pak odpovědi zapište do aplikace: Tisk → dávka → Zápis papírových odpovědí.","proc":"Další krok je na dokumentu."}],
"pristupnost":["Tisk: tabulky s jasnými linkami, čísla mono s tabulkovými číslicemi, kontrast grafit/bílá; pruh světlý text na grafitu (10:1).","HTML náhled: tabulky s caption, th scope; prázdné buňky mají sr-only „vyplní lektor“.","Axe/kontrola: A4 má pevnou šířku 210 mm, náhled je v posuvné oblasti (role=region, tabindex=0); na mobilu 375 px se posouvá vodorovně – přijatelné u náhledu tisku."],
"poznamky_pro_kodera":["Data doslovně z PDF dema (klice-20261103-1820): 2 variace, UG98N3X6 (17 b.), A6WR8XTV (16 b.).","Pruh opakovat na každé straně (@page nebo vložit do každé strany).","Klíč se generuje jako samostatný soubor (oddělený od zadání a listů), aby se nevytiskl omylem s nimi."],
"chybi_komponenta":["pruh důvěrného dokumentu (.a4__duverne) – použit .section--grafit s inline paddingem","tisková tabulka klíče – inline styly s tokeny"]}
write('klice.html',{"titulek":"Klíče a vyhodnocovací tabulka – "+TEST,"sablona":"a4"},spec,page(p1)+page(p2),'Klíče a vyhodnocovací tabulka')
