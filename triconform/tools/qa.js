// QA rebrandu B „Týden“ – spouští se na PC proti testu (Basic auth z proměnných prostředí, heslo se nikam nevypisuje).
//   set TC_USER=… & set TC_PASS=…   (PowerShell: $env:TC_USER='…'; $env:TC_PASS='…')
//   (axe-core: npm i axe-core v adresáři, odkud se spouští)
//   node triconform/tools/qa.js https://test.triconform.com /prihlaseni /zapomenute-heslo [další cesty]
//   volitelně TC_STATE=cesta/k/storageState.json pro stránky po přihlášení (ukázková organizace na testu)
// Výstup: řádek na stránku × šířku × motiv (písma, pozadí, H1, logo, tlačítko, přetečení, axe) + snímky do ./qa-out/
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const [base, ...paths] = process.argv.slice(2);
if (!base || !paths.length) { console.error('použití: node qa.js <base-url> <cesta> [cesta…]'); process.exit(2); }
const axePath = require.resolve('axe-core/axe.min.js', { paths: [process.cwd(), __dirname] });
const AX = fs.readFileSync(axePath, 'utf8');
const OUT = path.resolve('qa-out'); fs.mkdirSync(OUT, { recursive: true });
const cred = process.env.TC_USER ? { username: process.env.TC_USER, password: process.env.TC_PASS || '' } : undefined;
(async () => {
  const b = await chromium.launch(); let fail = 0;
  for (const [W, cs] of [[1280, 'light'], [375, 'light'], [1280, 'dark'], [375, 'dark']]) {
    const c = await b.newContext({ viewport: { width: W, height: 900 }, colorScheme: cs, httpCredentials: cred,
      ...(process.env.TC_STATE ? { storageState: process.env.TC_STATE } : {}) });
    const p = await c.newPage(); const bad = new Set();
    p.on('response', r => { if (r.status() >= 400) bad.add(r.status() + ' ' + new URL(r.url()).pathname); });
    p.on('console', m => { if (m.type() === 'error') bad.add('console: ' + m.text().slice(0, 120)); });
    for (const pth of paths) {
      const r = await p.goto(base + pth, { waitUntil: 'networkidle' }); await p.waitForTimeout(600);
      const i = await p.evaluate(async () => {
        await document.fonts.ready; const cs = s => getComputedStyle(s);
        const h = document.querySelector('h1'); const br = document.querySelector('.app-brand, .brand'); const bt = document.querySelector('.btn-primary');
        return { fonts: [...new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family))].join('+'),
          bg: cs(document.body).backgroundColor, h1: h ? cs(h).fontFamily.split(',')[0] + ' ' + cs(h).fontSize : '-',
          logo: br ? (cs(br, '::before').backgroundImage.includes('znacka') ? 'B' : 'staré') : '-',
          btn: bt ? cs(bt).backgroundColor : '-', overflow: document.documentElement.scrollWidth > innerWidth };
      });
      await p.evaluate(AX);
      const v = await p.evaluate(async () => (await axe.run({ runOnly: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] })).violations.map(v => v.id + '×' + v.nodes.length));
      if (v.length || i.overflow || r.status() >= 400) fail++;
      console.log([W, cs, r.status(), pth, 'písma:' + i.fonts, 'pozadí:' + i.bg, 'H1:' + i.h1, 'logo:' + i.logo, 'tlačítko:' + i.btn, 'přetečení:' + i.overflow, 'axe:' + (v.join(',') || 0)].join(' | '));
      await p.screenshot({ path: path.join(OUT, `${pth.replace(/\W+/g, '_') || 'root'}_${W}_${cs}.png`), fullPage: true });
    }
    if (bad.size) console.log('  chyby sítě/konzole:', [...bad].join(' ; '));
    await c.close();
  }
  await b.close(); console.log(fail ? `NÁLEZY: ${fail}` : 'OK: 0 nálezů'); process.exit(fail ? 1 : 0);
})();
