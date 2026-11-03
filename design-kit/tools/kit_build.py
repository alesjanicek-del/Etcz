"""Sestaví rozcestník (index.html) a audit (audit.html) z sitemap.json, reports/*.json a specifikací stránek.
Spuštění: python3 tools/kit_build.py   (nejdřív node tools/check.js a node tools/nahledy.js)"""
import json, os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
S = dict(re.findall(r'<symbol id="i-([a-z-]+)" viewBox="0 0 24 24">(.*?)</symbol>', open('assets/icons.svg').read()))
I = lambda n: f'<svg class="i" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{S[n]}</svg>'
E = lambda s: html.escape(str(s))
SM = json.load(open('sitemap.json'))
REVIZE = json.load(open('tools/revize.json')) if os.path.exists('tools/revize.json') else {}
def rep(f):
    p = os.path.join('reports', f.replace('.html', '.json'))
    return json.load(open(p)) if os.path.exists(p) else None
SKUP = [('W', 'Veřejný web'), ('A1', 'Aplikace · přihlášení, přehledy, otázky'), ('A2', 'Aplikace · testy, zadání, tisk, kalendář'), ('A3', 'Aplikace · výsledky, statistiky, správa, účet, nápověda'), ('Z', 'Zkoušený, e-mail a tiskové dokumenty'), ('EN', 'Angličtina – první vzory'), ('EN-W', 'EN · veřejný web'), ('EN-A1', 'EN · přihlášení, přehledy, otázky'), ('EN-A2', 'EN · testy, zadání, tisk, kalendář'), ('EN-A3', 'EN · výsledky, statistiky, správa, účet, nápověda'), ('EN-Z', 'EN · zkoušený, e-mail a tisk')]
HEAD = lambda t, cur: f'''<!doctype html>
<html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="kit-stranka" content="1"><title>{t} · exam-test design kit</title><link rel="icon" href="assets/logo/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/brand.css">
<style>.kit-nav{{display:flex;flex-wrap:wrap;gap:var(--s-1);margin-left:auto}}.kit-nav a{{display:inline-flex;align-items:center;min-height:var(--cil-min);padding:0 12px;color:var(--c-grafit);text-decoration:none;font-weight:var(--w-tucne);font-size:var(--t-maly)}}.kit-nav a[aria-current]{{background:var(--c-grafit);color:var(--c-papir)}}.site-header__in{{flex-wrap:wrap;padding-block:var(--s-2)}}@media (max-width:767px){{.kit-nav{{margin-left:0}}}}
.pg{{background:var(--c-bila);border:var(--b-silna) solid var(--c-grafit);display:flex;flex-direction:column}}.pg img{{width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top;border-bottom:var(--b-silna) solid var(--c-grafit);background:var(--c-papir)}}.pg__t{{padding:var(--s-3);display:flex;flex-direction:column;gap:6px;flex:1}}
.au summary{{cursor:pointer;list-style:none;display:flex;flex-wrap:wrap;gap:var(--s-3);align-items:center;min-height:56px;padding:var(--s-2) 0}}.au summary::-webkit-details-marker{{display:none}}.au{{border-top:var(--b-silna) solid var(--c-grafit)}}.au>div{{padding:0 0 var(--s-5)}}</style></head>
<body><a class="skip" href="#obsah">Přeskočit na obsah</a>
<header class="site-header"><div class="container site-header__in"><a class="logo" href="index.html"><img src="assets/logo/exam-test-logo.svg" alt="exam-test – rozcestník design kitu" width="170" height="28"></a><nav class="kit-nav" aria-label="Design kit">''' + ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{n}</a>' for h, n in [('logo.html', 'Logo manuál'), ('brand.html', 'Brand manuál'), ('komponenty.html', 'Komponenty'), ('index.html#stranky', 'Stránky'), ('audit.html', 'Audit')]) + '</nav></div></header>'
FOOT = '<footer class="site-footer"><div class="container"><p>exam-test · design kit 1.0 · směr B „Odpovědní list“</p></div></footer></body></html>\n'

def stav(r):
    if not r: return '<span class="stav stav--neutral">Nezkontrolováno</span>'
    s = r['souhrn']; bad = s['axe_chyby'] + s['vlastni_chyby']
    return f'<span class="stav stav--ok">{I("check")}Bez chyb</span>' if not bad else f'<span class="stav stav--ne">{I("minus-kruh")}{bad} chyb</span>'

def index():
    tot = len(SM); hotovo = sum(1 for p in SM if os.path.exists(p['soubor'])); ok = 0
    groups = ''
    for g, gn in SKUP:
        cards = ''
        for p in [x for x in SM if x['skupina'] == g]:
            r = rep(p['soubor']); ex = os.path.exists(p['soubor'])
            if r and not (r['souhrn']['axe_chyby'] + r['souhrn']['vlastni_chyby']): ok += 1
            th = 'assets/nahledy/' + p['soubor'].replace('/en-', '/').replace('/', '_').replace('.html', '.png')
            img = f'<img src="{th}" alt="" width="400" height="250" loading="lazy">' if os.path.exists(th) else '<div style="aspect-ratio:16/10;background:var(--c-papir);border-bottom:var(--b-silna) solid var(--c-grafit)"></div>'
            link = f'<a href="{p["soubor"]}"><b>{E(p["nazev"])}</b></a>' if ex else f'<b>{E(p["nazev"])}</b> <span class="t-maly">(chybí)</span>'
            cards += f'<li class="pg">{img}<div class="pg__t">{link}<span class="t-stitek" style="text-transform:none;letter-spacing:0">{E(p["route"])}</span><span class="t-maly">{E(p.get("role", "veřejnost"))}</span><span class="row" style="margin-top:auto">{stav(r)}<a class="btn btn--tiche btn--male" href="audit.html#{p["soubor"].replace("/", "-").replace(".html", "")}">Specifikace<span class="sr-only">: {E(p["nazev"])} ({E(p["soubor"])})</span></a></span></div></li>'
        groups += f'<section class="stack-3" aria-labelledby="g-{g}" style="margin-top:var(--s-6)"><h3 id="g-{g}" class="t-titulek">{gn}</h3><ul class="grid-4" style="list-style:none;padding:0">{cards}</ul></section>'
    page = HEAD('Rozcestník', 'index.html') + f'''<main id="obsah">
<section class="hero grid-bg"><div class="container stack-4"><p class="t-stitek">Design kit · směr B „Odpovědní list“ · verze 1.0</p><h1 class="t-display">exam-test v&nbsp;novém designu</h1>
<p class="t-perex measure">Logo, brand manuál, knihovna komponent a {tot} navržených stránek webu i aplikace – jako hotové HTML a CSS pro kodéra. Každá stránka má specifikaci a je zkontrolovaná na WCAG 2.2 AA, pravidla značky a srozumitelnost textů.</p>
<div class="kpi" style="max-width:760px"><div><span class="t-cislo">{hotovo}/{tot}</span><span class="t-maly">navržených stránek</span></div><div><span class="t-cislo">{ok}</span><span class="t-maly">bez chyb v kontrole</span></div><div><span class="t-cislo">47</span><span class="t-maly">ikon</span></div><div><span class="t-cislo">19</span><span class="t-maly">variant loga</span></div></div>
<div class="row"><a class="btn btn--hlavni" href="logo.html">Logo manuál</a><a class="btn" href="brand.html">Brand manuál</a><a class="btn" href="komponenty.html">Komponenty</a><a class="btn" href="audit.html">Audit stránek</a></div></div></section>
<section class="section section--bila"><div class="container grid-3">
<div class="feature"><h2 class="t-nadpis">Pro kodéra</h2><p>Každá stránka = <code>web/…</code>, <code>app/…</code>, <code>tisk/…</code>. Styly jen z <code>assets/brand.css</code> a tokenů. Zdroje stránek v <code>src/</code>, kostra v <code>tools/build.py</code>.</p></div>
<div class="feature"><h2 class="t-nadpis">Specifikace</h2><p>U každé stránky: účel, hlavní akce, stavy, změny UX, přepisy textů (dnes → nově → proč) a řešení přístupnosti. V auditu nebo v <code>&lt;script id="spec"&gt;</code> stránky.</p></div>
<div class="feature"><h2 class="t-nadpis">Kontrola</h2><p>Příkaz <code>npm run check -- app/testy.html</code> spustí axe-core (WCAG 2.2 AA). Hlídá i reflow na 320 px, velikost cílů, typografii, barvy, délku vět a zakázané formulace.</p></div>
</div></section>
<section class="section" id="stranky" aria-labelledby="st-h"><div class="container"><h2 id="st-h" class="t-sekce">Všechny stránky</h2>{groups}</div></section>
</main>''' + FOOT
    open('index.html', 'w').write(page)

def lst(items):
    return '<ul class="list-check">' + ''.join(f'<li><span>{E(x)}</span></li>' for x in items) + '</ul>' if items else '<p class="t-maly">—</p>'

def audit():
    rows = ''; det = ''; T = dict(axe=0, vl=0, var=0, n=0, styly=[])
    for p in SM:
        r = rep(p['soubor'])
        if not r: continue
        s = r['souhrn']; T['axe'] += s['axe_chyby']; T['vl'] += s['vlastni_chyby']; T['var'] += s['varovani']; T['n'] += 1; T['styly'].append(r['stats']['stylu_textu'])
        aid = p['soubor'].replace('/', '-').replace('.html', '')
        rows += f'<tr><td data-label="Stránka"><a href="#{aid}">{E(p["nazev"])}</a><span class="t-maly">{E(p["soubor"])}</span></td><td class="num" data-label="WCAG chyby">{s["axe_chyby"]}</td><td class="num" data-label="WCAG drobné">{s["axe_ostatni"]}</td><td class="num" data-label="Značka a text – chyby">{s["vlastni_chyby"]}</td><td class="num" data-label="Varování">{s["varovani"]}</td><td class="num" data-label="Stylů textu">{r["stats"]["stylu_textu"]}</td><td data-label="Stav">{stav(r)}</td></tr>'
        sp = r.get('spec') or {}
        tx = sp.get('texty') or []
        ttab = ('<div class="table-wrap"><table class="table table--stack"><caption class="sr-only">Změny textů</caption><thead><tr><th scope="col">Dnes</th><th scope="col">Nově</th><th scope="col">Proč</th></tr></thead><tbody>' + ''.join(f'<tr><td class="no-check" data-label="Dnes">{E(t.get("dnes", ""))}</td><td data-label="Nově"><b>{E(t.get("nove", ""))}</b></td><td data-label="Proč">{E(t.get("proc", ""))}</td></tr>' for t in tx) + '</tbody></table></div>') if tx else '<p class="t-maly">Bez změn textu.</p>'
        nal = [f'axe ({v["impact"]}): {v["help"]}' for v in {v['id']: v for v in r['axe']['desktop'] + r['axe']['mobil']}.values()] + [f'{x["level"]}: {x["msg"]}' for x in r['custom'] + r['text']]
        rv = REVIZE.get(p['soubor'])
        rvh = f'<div class="card stack-2"><p class="t-stitek">Ruční revize (UX · UI · text)</p>{lst(rv)}</div>' if rv else ''
        det += f'''<details class="au" id="{aid}"><summary><span class="t-nadpis">{E(p["nazev"])}</span><span class="t-stitek" style="text-transform:none;letter-spacing:0">{E(sp.get("route", p["route"]))}</span>{stav(r)}</summary><div class="stack-4">
<p><a href="{p["soubor"]}">Otevřít návrh: {E(p["nazev"])}</a> · role: {E(sp.get("role", p.get("role", "")))} · šablona: {E(sp.get("sablona", ""))}</p>
<div class="grid-2" style="align-items:start"><div class="stack-2"><h3 class="t-nadpis">Účel</h3><p>{E(sp.get("ucel", ""))}</p><h3 class="t-nadpis">Hlavní akce</h3><p>{E(sp.get("hlavni_akce", ""))}</p><h3 class="t-nadpis">Stavy</h3>{lst(sp.get("stavy", []))}</div>
<div class="stack-2"><h3 class="t-nadpis">UX a UI změny</h3>{lst(sp.get("zmeny_ux", []))}<h3 class="t-nadpis">Přístupnost (WCAG)</h3>{lst(sp.get("pristupnost", []))}</div></div>
<h3 class="t-nadpis">Srozumitelnost textů – přepisy</h3>{ttab}
{('<h3 class="t-nadpis">Poznámky pro kodéra</h3>' + lst(sp.get("poznamky_pro_kodera", []))) if sp.get("poznamky_pro_kodera") else ""}
{rvh}
<div class="card card--tenka stack-2"><p class="t-stitek">Automatická kontrola · {r["stats"]["stylu_textu"]} stylů textu · {r["stats"]["slov"]} slov</p>{lst(nal) if nal else "<p>Bez nálezů: WCAG 2.2 AA (axe, desktop i mobil), reflow 320 px, cíle ≥ 24 px, typografie a barvy z tokenů, věty ≤ 25 slov, slovník pojmů.</p>"}</div>
</div></details>'''
    avg = round(sum(T['styly']) / len(T['styly']), 1) if T['styly'] else 0
    en = json.load(open('reports/en-delka.json')) if os.path.exists('reports/en-delka.json') else {}
    en_bad = {k2: v['nalezy'] for k2, v in en.items() if v['nalezy']}
    en_html = f'<p>Test délky textu pro angličtinu (pseudo-lokalizace +35&nbsp;%, 320 a 1280&nbsp;px): <b>{len(en) - len(en_bad)} z {len(en)}</b> stránek bez nálezu.</p>' + (lst([f"{k2}: {'; '.join(v)}" for k2, v in en_bad.items()]) if en_bad else '')
    dec = [(p, x.replace('Rozhodnout: ', '')) for p, xs in REVIZE.items() for x in xs if x.startswith('Rozhodnout')] + [(p, x) for p, xs in REVIZE.items() for x in xs if x.startswith('Známá chyba')]
    dec_html = '<div class="table-wrap"><table class="table table--stack"><caption class="sr-only">Body k rozhodnutí</caption><thead><tr><th scope="col">Stránka</th><th scope="col">Co rozhodnout</th></tr></thead><tbody>' + ''.join(f'<tr><td data-label="Stránka"><a href="{p}">{E(p)}</a></td><td data-label="Rozhodnout">{E(x)}</td></tr>' for p, x in dec) + '</tbody></table></div>'
    page = HEAD('Audit', 'audit.html') + f'''<main id="obsah"><div class="container">
<section class="hero" style="padding-bottom:var(--s-5)"><div class="stack-4"><p class="t-stitek">Audit návrhů · WCAG 2.2 AA · UX · UI · srozumitelnost</p><h1 class="t-display">Audit stránek</h1>
<p class="t-perex measure">Každá stránka prošla automatickou kontrolou na desktopu (1280 px) a mobilu (375 px) a revizí podle čtyř hledisek. Klikněte na stránku pro specifikaci, přepisy textů a nálezy.</p>
<div class="kpi"><div><span class="t-cislo">{T["n"]}</span><span class="t-maly">zkontrolovaných stránek</span></div><div><span class="t-cislo">{T["axe"]}</span><span class="t-maly">závažných chyb WCAG</span></div><div><span class="t-cislo">{T["vl"]}</span><span class="t-maly">chyb značky a textu</span></div><div><span class="t-cislo">{avg}</span><span class="t-maly">stylů textu na stránku (dnes 20)</span></div></div></div></section>
<section class="stack-4" aria-labelledby="met-h"><h2 id="met-h" class="t-sekce">Jak se kontrolovalo</h2><div class="grid-4">
<div class="feature"><h3 class="t-nadpis">WCAG 2.2 AA</h3><p>axe-core 4.10 na 1280 a 375 px. Navíc reflow na 320 px (1.4.10), cíle ≥ 24 px (2.5.8), účel odkazů (2.4.4), jedno H1 a pořadí nadpisů.</p></div>
<div class="feature"><h3 class="t-nadpis">UI</h3><p>Velikosti písma jen ze škály 13–56 px. Barvy textu jen z palety. Počet stylů textu na stránku. Vizuální kontrola screenshotů.</p></div>
<div class="feature"><h3 class="t-nadpis">UX</h3><p>Účel a hlavní akce stránky, všechny stavy (prázdný, chyba, načítání, oprávnění), jedna hlavní akce na obrazovku, mobil – obsah v první polovině obrazovky.</p></div>
<div class="feature"><h3 class="t-nadpis">Srozumitelnost</h3><p>Věty nad 25 slov, odstavce nad 90 slov, zakázané a zastaralé formulace ze slovníku, každá změna textu zdůvodněná (dnes → nově → proč).</p></div></div>
<p class="t-maly">Automatické nástroje odhalí asi třetinu problémů přístupnosti. Před spuštěním je nutný ruční test s čtečkou obrazovky (NVDA, VoiceOver) a klávesnicí – viz poznámky u jednotlivých stránek.</p></section>
<section class="stack-4" aria-labelledby="roz-h" style="padding-top:var(--s-5)"><h2 id="roz-h" class="t-sekce">K rozhodnutí</h2>{dec_html}</section>
<section class="stack-3" aria-labelledby="en-h" style="padding-top:var(--s-5)"><h2 id="en-h" class="t-sekce">Angličtina – délka textu</h2>{en_html}</section>
<section class="section" aria-labelledby="sum-h" style="padding-top:var(--s-5)"><h2 id="sum-h" class="t-sekce">Souhrn</h2>
<div class="table-wrap" style="margin-top:var(--s-4)"><table class="table table--stack"><caption class="sr-only">Výsledky kontrol podle stránek</caption><thead><tr><th scope="col">Stránka</th><th scope="col" class="num">WCAG chyby</th><th scope="col" class="num">WCAG drobné</th><th scope="col" class="num">Značka a text</th><th scope="col" class="num">Varování</th><th scope="col" class="num">Stylů</th><th scope="col">Stav</th></tr></thead><tbody>{rows}</tbody></table></div></section>
<section aria-labelledby="det-h" style="padding-bottom:var(--s-6)"><h2 id="det-h" class="t-sekce">Stránky podrobně</h2><div style="margin-top:var(--s-4)">{det}</div></section>
</div></main>''' + FOOT
    open('audit.html', 'w').write(page)

if __name__ == '__main__':
    index(); audit(); print('index + audit ok')
