"""Sestaví stránky z fragmentů v src/ do web/, app/, tisk/.
Fragment: src/<oddil>/<nazev>.html
  <!--meta {"titulek":"…","popis":"…","sablona":"web|app|exam|cisty|a4","aktivni":"funkce.html","role":"lektor|autor|admin|zkouseny","demo":false} -->
  <!--spec { …JSON specifikace… } -->
  …HTML obsahu (to, co patří do <main>)…
Spuštění: python3 tools/build.py [src/web/index.html …]"""
import json, os, re, sys, glob, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SYM = dict(re.findall(r'<symbol id="i-([a-z-]+)" viewBox="0 0 24 24">(.*?)</symbol>', open(os.path.join(ROOT, 'assets', 'icons.svg'), encoding='utf-8').read()))
def I(n, c='i'):
    if n not in _SYM: raise KeyError('Neznámá ikona: ' + n)
    return f'<svg class="{c}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{_SYM[n]}</svg>'

WEB_NAV = [('funkce.html', 'Funkce'), ('pro-urady.html', 'Pro úřady'), ('pro-firmy.html', 'Pro firmy'), ('pro-vzdelavani.html', 'Pro vzdělávání'), ('bezpecnost.html', 'Bezpečnost'), ('cenik.html', 'Ceník')]
APP_NAV = {
 'lektor': [(None, [('lektor-prehled.html', 'Přehled', 'domu')]),
            ('Otázky', [('soubory.html', 'Soubory otázek', 'slozka'), ('otazky-hledat.html', 'Hledat otázky', 'hledat'), ('stitky.html', 'Štítky', 'stitek')]),
            ('Zkoušení', [('testy.html', 'Testy', 'soubor'), ('pouziti.html', 'Použití testů', 'prehrat'), ('tisk.html', 'Tisk', 'tisk'), ('kalendar.html', 'Kalendář', 'kalendar')]),
            ('Vyhodnocení', [('vysledky.html', 'Výsledky', 'check-kruh'), ('platnost-skoleni.html', 'Platnost školení', 'hodiny'), ('statistiky.html', 'Statistiky', 'graf')])],
 'autor': [(None, [('autor-prehled.html', 'Přehled', 'domu')]),
           ('Otázky', [('soubory.html', 'Soubory otázek', 'slozka'), ('otazky-hledat.html', 'Hledat otázky', 'hledat'), ('stitky.html', 'Štítky', 'stitek')]),
           ('Vyhodnocení', [('statistiky.html', 'Statistiky', 'graf')])],
 'zkouseny': [(None, [('moje-testy.html', 'Moje testy', 'soubor'), ('moje-vysledky.html', 'Moje výsledky', 'check-kruh')])],
}
APP_NAV['admin'] = [(None, [('admin-prehled.html', 'Přehled', 'domu')]),
  ('Otázky', [('soubory.html', 'Soubory otázek', 'slozka'), ('otazky-hledat.html', 'Hledat otázky', 'hledat'), ('stitky.html', 'Štítky', 'stitek'), ('ke-schvaleni.html', 'Ke schválení', 'check')]),
  APP_NAV['lektor'][2], APP_NAV['lektor'][3],
  ('Správa pobočky', [('uzivatele.html', 'Uživatelé', 'uzivatel'), ('skupiny.html', 'Skupiny studujících', 'uzivatele'), ('audit.html', 'Záznam změn', 'obnovit')])]
USER = {'lektor': 'Lucie Lektorová', 'autor': 'Adam Autor', 'admin': 'Barbora Veselá', 'zkouseny': 'Zdeněk Zkoušený'}
HOME = {'lektor': 'lektor-prehled.html', 'autor': 'autor-prehled.html', 'admin': 'admin-prehled.html', 'zkouseny': 'moje-testy.html'}

def head(t, popis='', lang='cs'):
    d = f'<meta name="description" content="{html.escape(popis)}">\n' if popis else ''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t)} · exam-test</title>
{d}<link rel="icon" href="../assets/logo/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/brand.css">
</head>'''

WEB_NAV_EN = [('#', 'Features'), ('#', 'Public sector'), ('#', 'Companies'), ('#', 'Education'), ('#', 'Security'), ('#', 'Pricing')]
def web(meta, body):
    if meta.get('lang') == 'en': return web_en(meta, body)
    a = meta.get('aktivni', '')
    nav = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == a else ""}>{t}</a></li>' for h, t in WEB_NAV)
    mnav = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == a else ""}>{t}</a>' for h, t in WEB_NAV)
    return f'''{head(meta['titulek'], meta.get('popis', ''))}
<body>
<a class="skip" href="#obsah">Přeskočit na obsah</a>
<header class="site-header">
 <div class="container site-header__in">
  <a class="logo" href="index.html"><img src="../assets/logo/exam-test-logo.svg" alt="exam-test – úvodní stránka" width="170" height="28"></a>
  <nav class="site-nav" aria-label="Hlavní"><ul>{nav}</ul></nav>
  <div class="site-header__cta">
   <a class="btn btn--tiche btn--male" href="../app/prihlaseni.html">Přihlásit</a>
   <a class="btn btn--hlavni btn--male" href="vyzkouset.html">Vyzkoušet demo</a>
   <nav class="lang" aria-label="Jazyk / Language"><a href="index.html" lang="cs" aria-current="true">CS</a><a href="en-index.html" lang="en" hreflang="en">EN</a></nav>
  </div>
  <details class="menu">
   <summary class="btn btn--male">{I('menu')}Menu</summary>
   <nav class="menu__panel" aria-label="Hlavní (mobil)">{mnav}<a href="../app/prihlaseni.html">Přihlásit</a><a href="en-index.html" lang="en" hreflang="en">English</a>
    <div class="row" style="margin-top:var(--s-3)"><a class="btn" href="vyzkouset.html">Vyzkoušet demo</a><a class="btn btn--hlavni" href="ukazka.html">Ukázka s průvodcem</a></div>
   </nav>
  </details>
 </div>
</header>
<main id="obsah">
{body}
</main>
<footer class="site-footer">
 <div class="container">
  <div class="site-footer__grid">
   <div class="stack-2"><img src="../assets/logo/exam-test-logo-negativ-pruhledne.svg" alt="exam-test" width="150" height="25"><p>Testy a zkoušky online i na papíře. Pro úřady, firmy a vzdělávání.</p><p><a href="overeni.html">Ověřit pravost protokolu</a></p></div>
   <nav class="stack-2" aria-label="Produkt"><p class="t-stitek">Produkt</p><ul><li><a href="funkce.html">Funkce</a></li><li><a href="cenik.html">Ceník</a></li><li><a href="sablony-testu.html">Šablony testů a služby</a></li><li><a href="bezpecnost.html">Bezpečnost a data</a></li><li><a href="napoveda.html">Nápověda</a></li></ul></nav>
   <nav class="stack-2" aria-label="Pro koho"><p class="t-stitek">Pro koho</p><ul><li><a href="pro-urady.html">Úřady a veřejná správa</a></li><li><a href="pro-firmy.html">Firmy a BOZP</a></li><li><a href="pro-vzdelavani.html">Školy a kurzy</a></li><li><a href="pro-vzdelavani.html#strediska">Školicí střediska</a></li></ul></nav>
   <div class="stack-2"><p class="t-stitek">Kontakt</p><ul><li><a href="mailto:podpora@exam-test.cz">podpora@exam-test.cz</a></li><li><a href="tel:+420725311531">+420 725 311 531</a></li><li><a href="kontakt.html">Kontakt a fakturační údaje</a></li><li><a href="najit-organizaci.html">Přihlášení do organizace</a></li></ul></div>
  </div>
  <div class="site-footer__legal row-between"><p>ABUCO ICT s.r.o. · IČO 29153905 · Třebohostická 987/5, 100 00 Praha 10</p>
   <ul class="row"><li><a href="podminky.html">Obchodní podmínky</a></li><li><a href="ochrana-osobnich-udaju.html">Ochrana osobních údajů</a></li><li><a href="zpracovatelska-smlouva.html">Zpracovatelská smlouva</a></li><li><a href="prohlaseni-o-pristupnosti.html">Prohlášení o přístupnosti</a></li></ul></div>
  <p class="row" style="margin-top:var(--s-3)"><span class="t-maly">Jazyk / Language:</span><a href="index.html" lang="cs" aria-current="true">Česky</a><a href="en-index.html" lang="en" hreflang="en">English</a></p>
  <p class="t-maly" style="margin-top:var(--s-2)">Web nepoužívá analytické ani reklamní cookies, jen <a href="ochrana-osobnich-udaju.html#cookies">technicky nezbytné</a>.</p>
 </div>
</footer>'''

def web_en(meta, body):
    a = meta.get('aktivni', '')
    nav = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == a else ""}>{t}</a></li>' for h, t in WEB_NAV_EN)
    return f'''{head(meta['titulek'], meta.get('popis', ''), 'en')}
<body>
<a class="skip" href="#obsah">Skip to content</a>
<header class="site-header">
 <div class="container site-header__in">
  <a class="logo" href="en-index.html"><img src="../assets/logo/exam-test-logo.svg" alt="exam-test – home" width="170" height="28"></a>
  <nav class="site-nav" aria-label="Main"><ul>{nav}</ul></nav>
  <div class="site-header__cta">
   <a class="btn btn--tiche btn--male" href="../app/prihlaseni.html">Sign in</a>
   <a class="btn btn--hlavni btn--male" href="#">Try the demo</a>
   <nav class="lang" aria-label="Language / Jazyk"><a href="index.html" lang="cs" hreflang="cs">CS</a><a href="en-index.html" lang="en" aria-current="true">EN</a></nav>
  </div>
  <details class="menu"><summary class="btn btn--male">{I('menu')}Menu</summary><nav class="menu__panel" aria-label="Main (mobile)">{''.join(f'<a href="{h}">{t}</a>' for h, t in WEB_NAV_EN)}<a href="../app/prihlaseni.html">Sign in</a><a href="index.html" lang="cs" hreflang="cs">Česky</a></nav></details>
 </div>
</header>
<main id="obsah">
{body}
</main>
<footer class="site-footer"><div class="container">
 <div class="site-footer__grid"><div class="stack-2"><img src="../assets/logo/exam-test-logo-negativ-pruhledne.svg" alt="exam-test" width="150" height="25"><p>Tests and exams online and on paper. For the public sector, companies and education.</p><p><a href="#">Verify a protocol</a></p></div>
 <div class="stack-2"><p class="t-stitek">Contact</p><ul><li><a href="mailto:podpora@exam-test.cz">podpora@exam-test.cz</a></li><li><a href="tel:+420725311531">+420 725 311 531</a></li></ul></div></div>
 <div class="site-footer__legal"><p>ABUCO ICT s.r.o. · Company ID 29153905 · Prague, Czech Republic. The Czech version of legal documents is legally binding; English translation in preparation.</p></div>
</div></footer>'''

def appnav(role, a, mobile=False):
    out = []
    for sec, items in APP_NAV[role]:
        if sec: out.append(f'<p class="t-stitek">{sec}</p>')
        for it in items:
            h, t, ic = it
            cur = ' aria-current="page"' if h == a else ''
            extra = '<span class="pocet" aria-label="3 čekají">3</span><!-- počet z dat -->' if h == 'ke-schvaleni.html' else ''
            out.append(f'<a href="{h}"{cur}>{I(ic)}{t}{extra}</a>')
    return ''.join(out)

def app(meta, body):
    role = meta.get('role', 'lektor'); a = meta.get('aktivni', ''); home = HOME[role]
    demo = '''<div class="demo-bar" role="region" aria-label="Upozornění dema"><b>Demo</b><span>Data se mažou každou noc ve 3:00.</span><a href="#">Přepnout roli</a><a href="schranka-dema.html">Schránka dema</a><a href="../web/ukazka.html">Chci aplikaci pro organizaci</a></div>''' if meta.get('demo') else ''
    pob = '' if role == 'zkouseny' else '<span class="stav stav--neutral">Pobočka Praha</span>'
    return f'''{head(meta['titulek'])}
<body>
<a class="skip" href="#obsah">Přeskočit na obsah</a>
{demo}<div class="app">
 <aside class="app-side">
  <a class="logo" href="{home}"><img src="../assets/logo/exam-test-logo-male.svg" alt="exam-test – přehled" width="146" height="24"></a>
  <nav class="app-nav" aria-label="Hlavní">{appnav(role, a)}</nav>
 </aside>
 <div>
  <header class="app-top">
   <a class="logo" href="{home}"><img src="../assets/logo/exam-test-logo-male.svg" alt="exam-test – přehled" width="122" height="20"></a>
   {pob}<span class="sp"></span>
   <a href="napoveda.html">Nápověda k této stránce</a>
   <a href="ucet.html" aria-label="Můj účet: {USER[role]}">{USER[role]}</a>
   <details class="menu"><summary class="btn btn--male">{I('menu')}Menu</summary><nav class="menu__panel app-nav" aria-label="Hlavní (mobil)">{appnav(role, a)}<a href="ucet.html">Můj účet</a><a href="#">Odhlásit</a></nav></details>
  </header>
  <main id="obsah" class="app-main">
{body}
  </main>
  <footer class="app-foot"><span>exam-test 0.2.0</span><a href="prohlaseni-o-pristupnosti.html">Prohlášení o přístupnosti</a><a href="co-je-noveho.html">Co je nového</a></footer>
 </div>
</div>'''

def exam(meta, body):
    return f'''{head(meta['titulek'], '', meta.get('lang', 'cs'))}
<body class="grid-bg">
<a class="skip" href="#obsah">{meta.get('skip', 'Přeskočit na obsah')}</a>
{body}'''

def cisty(meta, body):
    return f'''{head(meta['titulek'], meta.get('popis', ''), meta.get('lang', 'cs'))}
<body class="{meta.get('body_class', 'grid-bg')}">
<a class="skip" href="#obsah">Přeskočit na obsah</a>
{body}'''

def a4(meta, body):
    return f'''{head(meta['titulek'])}
<body style="background:var(--c-mrizka);padding:var(--s-5) 0">
{body}'''

T = {'web': web, 'app': app, 'exam': exam, 'cisty': cisty, 'a4': a4}

def build(src):
    s = open(src, encoding='utf-8').read()
    m = re.search(r'<!--meta\s*(\{.*?\})\s*-->', s, re.S); sp = re.search(r'<!--spec\s*(\{.*\})\s*-->', s, re.S)
    meta = json.loads(m.group(1)); spec = json.loads(sp.group(1)) if sp else {}
    body = s[sp.end() if sp else m.end():].strip()
    body = re.sub(r'\{\{I:([a-z-]+)\}\}', lambda m: I(m.group(1)), body)
    out = T[meta.get('sablona', 'web')](meta, body)
    out += f'\n<script type="application/json" id="spec">{json.dumps(spec, ensure_ascii=False)}</script>\n</body>\n</html>\n'
    oddil = os.path.basename(os.path.dirname(src)); dst = os.path.join(ROOT, oddil, os.path.basename(src))
    os.makedirs(os.path.dirname(dst), exist_ok=True); open(dst, 'w', encoding='utf-8').write(out)
    return dst

if __name__ == '__main__':
    srcs = sys.argv[1:] or glob.glob(os.path.join(ROOT, 'src', '*', '*.html'))
    for f in srcs: print('→', os.path.relpath(build(os.path.abspath(f)), ROOT))
