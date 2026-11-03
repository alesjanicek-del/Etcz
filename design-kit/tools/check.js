// Kontrola návrhů stránek: WCAG 2.2 AA (axe-core) + pravidla značky + srozumitelnost textu.
// Použití:  node tools/check.js web/index.html app/testy.html …   (nebo bez argumentů = všechny)
// Výstup:   reports/<cesta>.json + reports/summary.json + stručný výpis
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const AXE = fs.readFileSync(require.resolve('axe-core/axe.min.js', { paths: [ROOT, path.join(ROOT, '..'), '/tmp/claude-0/-home-user-Etcz/55de0f84-554c-5f5c-ac5b-96e089e53363/scratchpad/kit'] }), 'utf8');
const SIZES = [13, 15, 17, 22, 30, 36, 40, 56];
const COLORS = ['rgb(34, 38, 42)','rgb(90, 96, 104)','rgb(39, 71, 160)','rgb(27, 52, 120)','rgb(246, 244, 236)','rgb(255, 255, 255)','rgb(30, 107, 69)','rgb(179, 38, 30)','rgb(107, 90, 0)','rgb(199, 203, 207)','rgb(242, 203, 46)'];
// zakázané/zastaralé formulace (rozhodnutí z revize textů)
const BANNED = [/Uložit a další/i, /Prohlédnout demo/i, /Domluvit ukázku/i, /Přístupové kódy pro osoby/i, /Odkaz \(anonymní\)/i, /Uvolnit (vybrané )?výsledky/i, /Uvolněno/i, /Přidělení studujícím \/ skupině/i, /Označit k pozdějšímu návratu/i, /Přejít k odevzdání testu/i, /👁/, /\bdashboard\b/i, /\bproctoring\b/i, /\blogin\b/i, /klikněte zde/i];
const files = process.argv.slice(2).length ? process.argv.slice(2) : [...walk('web'), ...walk('app'), ...walk('tisk')];
function walk(d) { const p = path.join(ROOT, d); if (!fs.existsSync(p)) return []; return fs.readdirSync(p).filter(f => f.endsWith('.html')).map(f => path.join(d, f)); }

(async () => {
  const b = await chromium.launch(); const summary = [];
  for (const rel of files) {
    const abs = path.resolve(ROOT, rel); const url = 'file://' + abs; const rep = { page: rel, axe: {}, custom: [], text: [], stats: {} };
    const ctx = await b.newContext(); const p = await ctx.newPage();
    for (const [name, w, h] of [['desktop', 1280, 900], ['mobil', 375, 812]]) {
      await p.setViewportSize({ width: w, height: h }); await p.goto(url, { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready);
      await p.addScriptTag({ content: AXE });
      const r = await p.evaluate(async () => { const r = await axe.run({ exclude: [['.no-check']] }, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'] }, rules: { 'region': { enabled: false } } }); return r.violations.map(v => ({ id: v.id, impact: v.impact, help: v.help, n: v.nodes.length, sample: v.nodes.slice(0, 3).map(x => x.target.join(' ') + ' :: ' + (x.failureSummary || '').split('\n')[1]) })); });
      rep.axe[name] = r;
    }
    // reflow 320 px (WCAG 1.4.10)
    await p.setViewportSize({ width: 320, height: 640 }); await p.goto(url, { waitUntil: 'load' });
    const ov = await p.evaluate(() => { const W = document.documentElement.clientWidth; const bad = []; document.querySelectorAll('body *').forEach(e => { const r = e.getBoundingClientRect(); if (r.width && r.right > W + 1) { let a = e.parentElement, ok = false; while (a) { const s = getComputedStyle(a); if (/(auto|scroll)/.test(s.overflowX)) { ok = true; break } a = a.parentElement } if (!ok) bad.push((e.tagName + '.' + [...e.classList].join('.')).slice(0, 60)) } }); return { sw: document.documentElement.scrollWidth, W, bad: [...new Set(bad)].slice(0, 6) } });
    if (ov.sw > ov.W + 1) rep.custom.push({ id: 'reflow-320', level: 'chyba', msg: `Vodorovné posouvání při 320 px (šířka obsahu ${ov.sw}px): ${ov.bad.join(', ')}` });
    // desktop – vlastní kontroly
    await p.setViewportSize({ width: 1280, height: 900 }); await p.goto(url, { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready);
    const c = await p.evaluate(([SIZES, COLORS]) => {
      const out = { issues: [], styles: {}, words: 0, sentences: [], paras: [] };
      const vis = e => { const s = getComputedStyle(e); const r = e.getBoundingClientRect(); return s.visibility !== 'hidden' && s.display !== 'none' && r.width > 0 && r.height > 0 && !e.closest('[hidden],.sr-only,script,style,template,details:not([open])>*:not(summary)') };
      const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; const fsBad = new Set(), colBad = new Set();
      while (n = w.nextNode()) { const t = n.textContent.trim(); if (!t) continue; const el = n.parentElement; if (!vis(el)) continue; const s = getComputedStyle(el);
        const fs = Math.round(parseFloat(s.fontSize)); const key = `${fs}/${s.fontWeight}/${s.color}/${s.fontFamily.split(',')[0].replace(/"/g, '')}`; out.styles[key] = (out.styles[key] || 0) + 1;
        if (!SIZES.includes(fs) && !el.closest('.a4,.no-check')) fsBad.add(fs + 'px „' + t.slice(0, 24) + '“');
        if (!COLORS.includes(s.color) && !el.closest('.no-check')) colBad.add(s.color + ' „' + t.slice(0, 20) + '“'); }
      if (fsBad.size) out.issues.push({ id: 'typo-velikost', level: 'chyba', msg: 'Velikost mimo škálu: ' + [...fsBad].slice(0, 5).join('; ') });
      if (colBad.size) out.issues.push({ id: 'barva-textu', level: 'chyba', msg: 'Barva textu mimo paletu: ' + [...colBad].slice(0, 5).join('; ') });
      const h1 = document.querySelectorAll('h1'); if (h1.length !== 1) out.issues.push({ id: 'h1', level: 'chyba', msg: `Počet H1: ${h1.length}` });
      let last = 0; document.querySelectorAll('h1,h2,h3,h4').forEach(h => { const l = +h.tagName[1]; if (last && l > last + 1) out.issues.push({ id: 'nadpisy', level: 'varovani', msg: `Přeskočená úroveň nadpisu: H${last} → H${l} („${h.textContent.trim().slice(0, 30)}“)` }); last = l; });
      const links = {}; document.querySelectorAll('a[href]').forEach(a => { if (!vis(a)) return; const t = (a.getAttribute('aria-label') || a.textContent).trim().replace(/\s+/g, ' ').toLowerCase(); if (!t) return; (links[t] = links[t] || new Set()).add(a.getAttribute('href')); });
      Object.entries(links).forEach(([t, h]) => { if (h.size > 1) out.issues.push({ id: 'ucel-odkazu', level: 'varovani', msg: `Stejný text odkazu vede na ${h.size} různá místa: „${t.slice(0, 40)}“ (WCAG 2.4.4)` }) });
      const small = []; document.querySelectorAll('a,button,input:not([type=hidden]),select,textarea,summary,[role=button]').forEach(e => { if (!vis(e)) return; const r = e.getBoundingClientRect(); const inline = e.tagName === 'A' && e.closest('p,li,td,dd,.t-maly') && getComputedStyle(e).display === 'inline'; if (inline) return; const lab = e.matches('input') && e.closest('label'); if (lab) { const lr = lab.getBoundingClientRect(); if (lr.width >= 24 && lr.height >= 24) return; } if (r.width < 24 || r.height < 24) small.push(((e.textContent || e.getAttribute('aria-label') || e.tagName).trim().slice(0, 20)) + ` ${Math.round(r.width)}×${Math.round(r.height)}`) });
      if (small.length) out.issues.push({ id: 'velikost-cile', level: 'chyba', msg: 'Ovládací prvek menší než 24×24 px (WCAG 2.5.8): ' + small.slice(0, 5).join('; ') });
      document.querySelectorAll('p,li,dd,td,.alert,summary,h1,h2,h3,label,.hint').forEach(e => { if (!vis(e) || e.closest('.no-check,.prose-pravni')) return; if (e.querySelector('p,li,dd')) return; const t = e.innerText.replace(/\s+/g, ' ').trim(); if (!t) return; const wc = t.split(' ').length; out.words += wc; if (e.tagName === 'P' && wc > 90) out.paras.push(wc + ' slov: „' + t.slice(0, 50) + '…“');
        t.split(/(?<=[.!?])\s+(?=[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ0-9„])/).forEach(sn => { const k = sn.split(' ').filter(Boolean).length; if (k > 25) out.sentences.push(k + ' slov: „' + sn.slice(0, 60) + '…“') }) });
      const cl = document.body.cloneNode(true); cl.querySelectorAll('.no-check,script,style').forEach(e => e.remove()); out.text = cl.textContent; return out;
    }, [SIZES, COLORS]);
    rep.custom.push(...c.issues);
    c.sentences.forEach(s => rep.text.push({ id: 'dlouha-veta', level: 'varovani', msg: s }));
    c.paras.forEach(s => rep.text.push({ id: 'dlouhy-odstavec', level: 'varovani', msg: s }));
    const kit = await p.evaluate(() => !!document.querySelector('meta[name=kit-stranka]'));
    if (!kit) BANNED.forEach(re => { const m = c.text.match(re); if (m) rep.text.push({ id: 'zakazana-formulace', level: 'chyba', msg: `Zastaralá formulace „${m[0]}“` }) });
    const lang = await p.evaluate(() => document.documentElement.lang);
    if (lang === 'en') { const cz = await p.evaluate(() => { const out = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; while (n = w.nextNode()) { const t = n.textContent.trim(); if (!t || !/[ěščřžůňťďĚŠČŘŽŮŇŤĎ]/.test(t)) continue; const el = n.parentElement; if (el.closest('[lang=cs],.no-check,script,style')) continue; out.push(t.slice(0, 40)); } return out; });
      if (cz.length) rep.text.push({ id: 'cestina-v-en', level: 'chyba', msg: `Čeština v anglické stránce (${cz.length}×, mimo lang="cs"): „${cz.slice(0, 4).join('“, „')}“` }); }
    rep.stats = { stylu_textu: Object.keys(c.styles).length, slov: c.words };
    // specifikace
    const spec = await p.evaluate(() => { const s = document.getElementById('spec'); if (!s) return null; try { return JSON.parse(s.textContent) } catch (e) { return { _chyba: e.message } } });
    if (kit) {} else if (!spec) rep.custom.push({ id: 'spec', level: 'chyba', msg: 'Chybí <script id="spec">' }); else if (spec._chyba) rep.custom.push({ id: 'spec', level: 'chyba', msg: 'Neplatný JSON specifikace: ' + spec._chyba });
    else { for (const k of ['route', 'nazev', 'role', 'sablona', 'ucel', 'hlavni_akce', 'stavy', 'zmeny_ux', 'texty', 'pristupnost']) if (!(k in spec)) rep.custom.push({ id: 'spec', level: 'chyba', msg: 'Specifikace nemá pole ' + k }); }
    rep.spec = spec;
    const axeAll = [...rep.axe.desktop, ...rep.axe.mobil]; const uniq = {}; axeAll.forEach(v => uniq[v.id] = v);
    rep.souhrn = { axe_chyby: Object.values(uniq).filter(v => ['critical', 'serious'].includes(v.impact)).length, axe_ostatni: Object.values(uniq).filter(v => !['critical', 'serious'].includes(v.impact)).length, vlastni_chyby: rep.custom.filter(x => x.level === 'chyba').length + rep.text.filter(x => x.level === 'chyba').length, varovani: rep.custom.filter(x => x.level === 'varovani').length + rep.text.filter(x => x.level === 'varovani').length };
    const out = path.join(ROOT, 'reports', rel.replace(/\.html$/, '.json')); fs.mkdirSync(path.dirname(out), { recursive: true }); fs.writeFileSync(out, JSON.stringify(rep, null, 1));
    summary.push({ page: rel, ...rep.souhrn, stylu: rep.stats.stylu_textu });
    const flag = rep.souhrn.axe_chyby + rep.souhrn.vlastni_chyby ? '✗' : '✓';
    console.log(`${flag} ${rel}  axe:${rep.souhrn.axe_chyby}/${rep.souhrn.axe_ostatni}  vlastní:${rep.souhrn.vlastni_chyby}  var:${rep.souhrn.varovani}  stylů:${rep.stats.stylu_textu}`);
    for (const v of Object.values(uniq)) console.log(`   axe ${v.impact} ${v.id}: ${v.help} → ${v.sample[0] || ''}`);
    for (const x of [...rep.custom, ...rep.text]) console.log(`   ${x.level} ${x.id}: ${x.msg}`);
    await ctx.close();
  }
  const sp = path.join(ROOT, 'reports', 'summary.json'); let all = {}; if (fs.existsSync(sp)) all = JSON.parse(fs.readFileSync(sp)); summary.forEach(s => all[s.page] = s); fs.writeFileSync(sp, JSON.stringify(all, null, 1));
  await b.close();
})();
