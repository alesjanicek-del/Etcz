// Test délky textu pro angličtinu (pseudo-lokalizace, obdoba en_XA).
// Každý viditelný text se prodlouží o ~35 % (angličtina bývá delší v tlačítkách a štítcích,
// němčina až o 50 %) a stránka se zkontroluje na 320 a 1280 px:
//  - vodorovné posouvání stránky (WCAG 1.4.10),
//  - text, který přetéká svůj prvek nebo je oříznutý (nowrap, overflow:hidden, pevná šířka).
// Použití: node tools/check_en.js [stránky…]  → reports/en/*.json + výpis
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const SM = JSON.parse(fs.readFileSync(path.join(ROOT, 'sitemap.json')));
const files = process.argv.slice(2).length ? process.argv.slice(2) : SM.map(p => p.soubor).filter(f => fs.existsSync(path.join(ROOT, f)));
const PSEUDO = () => {
  const map = { a: 'á', e: 'é', i: 'í', o: 'ö', u: 'ü', c: 'ç', n: 'ñ', s: 'š', A: 'Å', E: 'É', O: 'Ö' };
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); const nodes = []; let n;
  while (n = w.nextNode()) { if (!n.textContent.trim()) continue; const p = n.parentElement; if (p.closest('script,style,.t-kod,.kod,.t-cislo,.num,code,.no-check,svg,.lang')) continue; nodes.push(n); }
  nodes.forEach(n => { const t = n.textContent; const extra = Math.max(2, Math.round(t.trim().length * 0.35)); const words = []; let k = extra; while (k > 0) { const l = Math.min(k, 6); words.push('x'.repeat(l)); k -= l + 1; } n.textContent = t.replace(/[aeioucnsAEO]/g, c => map[c] || c).replace(/(\S)(\s*)$/, '$1 ' + words.join(' ') + '$2'); });
  document.querySelectorAll('[aria-label]').forEach(e => e.setAttribute('aria-label', e.getAttribute('aria-label') + '··'));
};
const FIND = () => {
  const W = document.documentElement.clientWidth; const out = { sw: document.documentElement.scrollWidth, W, clip: [] };
  document.querySelectorAll('body *').forEach(e => {
    const s = getComputedStyle(e); if (s.display === 'none' || s.visibility === 'hidden') return; const r = e.getBoundingClientRect(); if (!r.width) return;
    if (e.closest('.table-wrap,.a4,[role=region][tabindex],.sr-only,details:not([open])>:not(summary)')) return;
    const own = [...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim());
    if (!own) return;
    if (e.scrollWidth > e.clientWidth + 2 && (s.overflowX === 'hidden' || s.textOverflow === 'ellipsis' || s.whiteSpace === 'nowrap')) out.clip.push((e.tagName + '.' + [...e.classList].join('.')).slice(0, 50) + ' „' + e.textContent.trim().slice(0, 24) + '“');
    else if (r.right > W + 1) out.clip.push((e.tagName + '.' + [...e.classList].join('.')).slice(0, 50) + ' mimo obrazovku „' + e.textContent.trim().slice(0, 24) + '“');
  });
  out.clip = [...new Set(out.clip)].slice(0, 8); return out;
};
(async () => { const b = await chromium.launch(); const all = {};
  for (const f of files) { const p = await b.newPage(); const res = { page: f, nalezy: [] };
    for (const w of [320, 1280]) { await p.setViewportSize({ width: w, height: 800 }); await p.goto('file://' + path.join(ROOT, f), { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready); await p.evaluate(PSEUDO);
      const o = await p.evaluate(FIND);
      if (o.sw > o.W + 1) res.nalezy.push(`${w}px: stránka se posouvá vodorovně (${o.sw} px)`);
      o.clip.forEach(c => res.nalezy.push(`${w}px: ${c}`)); }
    all[f] = res; console.log(`${res.nalezy.length ? '✗' : '✓'} ${f}${res.nalezy.length ? '  ' + res.nalezy.length + ' nálezů' : ''}`); res.nalezy.forEach(x => console.log('   ' + x)); await p.close(); }
  fs.mkdirSync(path.join(ROOT, 'reports'), { recursive: true }); fs.writeFileSync(path.join(ROOT, 'reports', 'en-delka.json'), JSON.stringify(all, null, 1)); await b.close(); })();
