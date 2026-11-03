// Náhledy stránek pro rozcestník: node tools/nahledy.js [soubory…]
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const SM = JSON.parse(fs.readFileSync(path.join(ROOT, 'sitemap.json')));
const files = process.argv.slice(2).length ? process.argv.slice(2) : SM.map(p => p.soubor).filter(f => fs.existsSync(path.join(ROOT, f)));
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 800 } }); fs.mkdirSync(path.join(ROOT, 'assets/nahledy'), { recursive: true });
  for (const f of files) { await p.goto('file://' + path.join(ROOT, f), { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready);
    const out = path.join(ROOT, 'assets/nahledy', f.replace('/', '_').replace('.html', '.png'));
    const buf = await p.screenshot({ clip: { x: 0, y: 0, width: 1280, height: 800 } });
    const q = await b.newPage({ viewport: { width: 400, height: 250 } }); await q.setContent(`<body style="margin:0"><img src="data:image/png;base64,${buf.toString('base64')}" style="width:400px;height:250px;display:block">`); await q.screenshot({ path: out }); await q.close(); }
  await b.close(); console.log('náhledy', files.length); })();
