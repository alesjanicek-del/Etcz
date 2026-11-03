import json, sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Etcz/55de0f84-554c-5f5c-ac5b-96e089e53363/scratchpad/gen')
from legal import conv
D={
'podminky':dict(route='/podminky',nazev='Obchodní podmínky',titulek='Obchodní podmínky',
 popis='Obchodní podmínky služby exam-test (ABUCO ICT s.r.o.) – návrh čekající na právní revizi.',
 kostka=['Služba je jen pro firmy, úřady a další organizace, ne pro spotřebitele (čl. 1.2).',
  'Máte-li s námi individuální smlouvu (typicky úřad po výběrovém řízení), platí přednostně ona (čl. 1.3).',
  'Tarif platíte předem na 12&nbsp;měsíců; předplatné se samo neprodlužuje (čl. 2.2 a 4.6).',
  'Limit pokusů lze překročit až do 110&nbsp;% a běžící zkoušku nikdy nepřerušíme. Ve zkušebním provozu je limit pevný (čl. 2.4).',
  'Obsah i výsledky patří vám. Smlouvu můžete kdykoli vypovědět a data si do jejího skončení vyexportovat (čl. 5.2, 10.1 a 10.3).']),
'ochrana-osobnich-udaju':dict(route='/ochrana-osobnich-udaju',nazev='Ochrana osobních údajů a cookies',titulek='Ochrana osobních údajů',
 popis='Jak provozovatel exam-test zpracovává osobní údaje návštěvníků webu, zájemců a kontaktních osob zákazníků. Cookies jen technicky nezbytné.',
 kostka=['Údaje zkoušených a uživatelů zpracováváme jen na pokyn organizace, která službu používá – ta je správcem a vyřizuje vaše žádosti.',
  'Jako správce zpracováváme hlavně poptávky z&nbsp;webu, registrace, fakturaci a komunikaci s&nbsp;podporou. Poptávky uchováváme 12&nbsp;měsíců.',
  'Data jsou na serverech v&nbsp;Německu (EU). Mimo Evropský hospodářský prostor je nepředáváme.',
  'Používáme jen technicky nezbytné cookies, proto nepotřebujeme souhlas. Analytické ani reklamní cookies nemáme.',
  'Své žádosti posílejte na podpora@exam-test.cz. Stížnost můžete podat u&nbsp;Úřadu pro ochranu osobních údajů.']),
'zpracovatelska-smlouva':dict(route='/zpracovatelska-smlouva',nazev='Zpracovatelská smlouva',titulek='Zpracovatelská smlouva',
 popis='Vzor smlouvy o zpracování osobních údajů podle čl. 28 GDPR mezi zákazníkem exam-test (správce) a ABUCO ICT s.r.o. (zpracovatel).',
 kostka=['Vy (organizace) jste správce, my zpracovatel. Údaje zpracováváme jen na vaše doložené pokyny (čl. 4).',
  'Údaje ukládáme a zpracováváme v&nbsp;EU nebo EHP; seznam dalších zpracovatelů je v&nbsp;příloze 2 (čl. 8).',
  'Dobu uchování výsledků určujete vy; po ní aplikace osobní údaje zkoušených nevratně anonymizuje (čl. 9.1).',
  'Po skončení smlouvy vám předáme export a údaje nejpozději do 60&nbsp;dnů vymažeme (čl. 9.4).',
  'Technik podpory vstoupí do vaší organizace jen s&nbsp;vaším souhlasem (čl. 7).']),
'prohlaseni-o-pristupnosti':dict(route='/prohlaseni-o-pristupnosti',nazev='Prohlášení o přístupnosti',titulek='Prohlášení o přístupnosti',
 popis='Prohlášení o přístupnosti aplikace exam-test a veřejných stránek: stav souladu se zákonem č. 99/2019 Sb., známé nedostatky a kontakt.',
 kostka=['Aplikace je zatím částečně v&nbsp;souladu se zákonem č.&nbsp;99/2019&nbsp;Sb. (WCAG 2.1 AA).',
  'Známé nedostatky: obsah vložený autory (popisy obrázků, zápisy s&nbsp;indexy), velké tiskové dávky PDF a dosud chybějící ruční test se čtečkou obrazovky.',
  'Potřebujete delší čas na test? Požádejte o&nbsp;prodloužení před zkouškou pořadatele.',
  'Nedostatky hlaste na podpora@exam-test.cz – odpovíme nejpozději do 30&nbsp;dnů.',
  'Povinným subjektem je organizace, která aplikaci používá; provozovatel prohlášení vydává dobrovolně.'],
 vypracovano=True),
}
SPEC_EXTRA={
 'ochrana-osobnich-udaju':{'pozn':'Text obsahuje odkaz na formulář „Domluvit ukázku“ (dnešní název). Převzato doslova; kontrola to hlásí jako zastaralou formulaci (1 chyba). Doporučení pro právníka: při revizi nahradit názvem „Ukázka s průvodcem“ (jde jen o název formuláře). Kotva #cookies je cílem odkazu z patičky.'},
}
for name,d in D.items():
    title,alert,toc,body=conv(name)
    numstyle=' style="list-style:none;padding-left:0"' if toc and toc[0][1][0].isdigit() else ''
    toc_html=''.join(f'<li><a href="#{i}">{t}</a></li>' for i,t in toc)
    kost=''.join(f'<li><span>{k}</span></li>' for k in d['kostka'])
    al=f'<div class="alert" role="note">{{{{I:pozor}}}}<div><p class="alert__nadpis">Návrh</p><p>{alert}</p></div></div>' if alert else ''
    extra=SPEC_EXTRA.get(name,{}).get('pozn')
    spec={"route":d['route'],"nazev":d['nazev'],"role":"veřejnost – zákazníci, zájemci, zkoušení, právníci a pověřenci","sablona":"web",
     "ucel":"Zveřejnit závazné znění dokumentu v přehledné, čitelné podobě s obsahem a ukotvenými nadpisy; krátké shrnutí pomůže laikovi se zorientovat.",
     "hlavni_akce":"Najít a přečíst konkrétní článek (obsah → kotva); sdílet odkaz na článek",
     "komponenty":["t-display","alert (Návrh)","card card--papir („V kostce“)","list-check","toc","prose prose-pravni","table table--stack (jen přílohy/tabulky)"],
     "stavy":["Statická stránka – bez stavů.","Bez označení „Návrh“, až text projde právní revizí (alert se odstraní)."],
     "zmeny_ux":["Text je převzat beze změny (doslova z dnešního webu); upraveno jen strukturování: nadpisy H2/H3 s kotvami, seznamy, tabulka, odkazy mailto, tučná čísla článků.",
      "Nový blok „V kostce“ (3–5 bodů v běžné řeči), jasně označený jako shrnutí, které nenahrazuje text.",
      "Obsah (.toc) s odkazy na kotvy nadpisů; články číslované „1.1“ mají kotvu #cl-1-1 pro přímé odkazy (např. z ceníku).",
      "Upozornění „Návrh – čeká na právní revizi“ je .alert v běžné velikosti nahoře (pravidlo 3)."],
     "texty":[{"dnes":"(celý text dokumentu)","nove":"beze změny – převzato doslova","proc":"Právní text se nepřepisuje; mění se jen struktura."},
              {"dnes":"(nové)","nove":"V kostce – shrnutí, které nenahrazuje text","proc":"Orientace pro laiky; každý bod odkazuje na článek, ze kterého vychází."}],
     "pristupnost":["Jediné H1; oddíly H2 s id (kotvy), pododdíly H3.","Obsah je <nav aria-label=\"Obsah dokumentu\"> s uspořádaným seznamem.","Shrnutí je <aside> s nadpisem a viditelnou poznámkou, že nenahrazuje text.","Tabulky mají caption (sr-only „Další zpracovatelé“ – jediný doplněný text, nadpis je hned nad tabulkou), th scope=col a data-label pro mobil.","Text v .prose má max. šířku 720 px (čitelnost)."],
     "poznamky_pro_kodera":["Text generovat ze zdroje dokumentu (CMS/markdown), ne ručně – zachová se doslovné znění.","Kontrola délky vět vynechává .prose-pravni (právní text)."]+([extra] if extra else []),
     "chybi_komponenta":["Rozvržení právní stránky s obsahem vedle textu (sticky .toc na desktopu) – nyní obsah nad textem v jednom sloupci"]}
    frag=f'''<!--meta {json.dumps({"titulek":d['titulek'],"popis":d['popis'],"sablona":"web","aktivni":""},ensure_ascii=False)} -->
<!--spec {json.dumps(spec,ensure_ascii=False,indent=1)} -->
<section class="section grid-bg">
 <div class="container stack-5" style="max-width:calc(var(--max-text) + 2 * var(--s-5))">
  <div class="stack-4"><p class="t-stitek">Právní informace</p><h1 class="t-display">{title}</h1></div>
  {al}
  <aside class="card card--papir stack" aria-labelledby="kostka">
   <p class="t-stitek">Shrnutí</p>
   <h2 id="kostka" class="t-nadpis">V kostce</h2>
   <ul class="list-check">{kost}</ul>
   <p class="t-maly">Shrnutí slouží jen pro orientaci a nenahrazuje text dokumentu. Závazné je plné znění níže.</p>
  </aside>
  <nav class="toc stack-2" aria-label="Obsah dokumentu"><p class="t-stitek">Obsah</p><ol{numstyle}>{toc_html}</ol></nav>
 </div>
</section>
<section class="section section--bila" aria-label="Plné znění">
 <div class="container" style="max-width:calc(var(--max-text) + 2 * var(--s-5))">
  <div class="prose prose-pravni">
{body}
  </div>
 </div>
</section>
'''
    open(f'/home/user/Etcz/design-kit/src/web/{name}.html','w',encoding='utf-8').write(frag)
    print(name, len(toc))
