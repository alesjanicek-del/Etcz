// Loop 2 a 3: node tools/logo_test2.js <dir> <out.png> <2|3>
const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
const [dir,out,loop]=process.argv.slice(2);const r=f=>fs.readFileSync(path.join(dir,f),'utf8');
const img=(f,style)=>`<img src="data:image/svg+xml;base64,${Buffer.from(r(f)).toString('base64')}" style="${style}">`;
const photo="background:radial-gradient(circle at 30% 40%,#e9e2cf,#7d826f 45%,#2f3a40 80%)";
const L2=`<h2>A · Fotografie a rušné pozadí</h2><div class=row>
<div class=bg style="${photo}">${img('exam-test-logo.svg','width:240px')}</div>
<div class=bg style="${photo}">${img('exam-test-logo-na-podkladu.svg','width:270px')}</div>
<div class=bg style="${photo}">${img('exam-test-logo-negativ.svg','width:240px;mix-blend-mode:normal')}</div></div>
<h2>B · Mřížka značky B a tónované papíry</h2><div class=row>
<div class=bg style="background:#F6F4EC;background-image:linear-gradient(#C9D3DD 1px,transparent 1px),linear-gradient(90deg,#C9D3DD 1px,transparent 1px);background-size:24px 24px">${img('exam-test-logo.svg','width:240px')}</div>
<div class=bg style="background:#E9E4D4">${img('exam-test-logo.svg','width:240px')}</div>
<div class=bg style="background:#C9D3DD">${img('exam-test-logo.svg','width:240px')}</div></div>
<h2>C · Jednobarevná verze v malých velikostech</h2><div class=row>${[320,200,140,100].map(w=>`<div class=c>${img('exam-test-logo-cerne.svg',`width:${w}px`)}<span>${w}px</span></div>`).join('')}</div>
<h2>D · Simulace tisku: laser 1 barva (práh), inkoust na nenatíraném papíře (rozpití), fax</h2><div class=row>
<div class=bg style="background:#fff;filter:grayscale(1) contrast(30)">${img('exam-test-logo-cerne.svg','width:200px')}</div>
<div class=bg style="background:#F3EFE2;filter:blur(0.9px) saturate(.8)">${img('exam-test-logo.svg','width:200px')}</div>
<div class=bg style="background:#fff;filter:grayscale(1) contrast(30) blur(.6px)">${img('exam-test-logo.svg','width:120px')}</div></div>`;
const L3=`<h2>A · UI: značka vs. ikona zavřít, zaškrtávací pole, stav nesplněno (nové ikony)</h2><div class=row style="align-items:center">
${img('exam-test-znacka.svg','width:28px')}<span>značka</span>
<span style="display:inline-flex;gap:6px;align-items:center;border:2px solid #22262A;padding:6px 10px;font:600 14px sans-serif">Zavřít <svg width=14 height=14 viewBox="0 0 14 14"><path d="M3 3l8 8M11 3l-8 8" stroke="#22262A" stroke-width="1.6"/></svg></span>
<span style="display:inline-flex;width:24px;height:24px;background:#22262A;align-items:center;justify-content:center"><svg width=16 height=16 viewBox="0 0 16 16"><path d="M3 8.5l3.2 3L13 4.5" stroke="#fff" stroke-width="2.2" fill="none"/></svg></span><span>checkbox zaškrtnuto</span>
<span style="display:inline-flex;gap:6px;align-items:center;border:1.5px solid #B3261E;color:#B3261E;background:#FBE7E4;padding:5px 9px;font:600 13px monospace">
<svg width=14 height=14 viewBox="0 0 14 14"><circle cx=7 cy=7 r=6 fill="none" stroke="#B3261E" stroke-width="1.6"/><path d="M4 7h6" stroke="#B3261E" stroke-width="1.8"/></svg>NESPLNĚNO</span>
<span style="display:inline-flex;gap:6px;align-items:center;border:1.5px solid #1E6B45;color:#1E6B45;background:#E3F0E6;padding:5px 9px;font:600 13px monospace"><svg width=14 height=14 viewBox="0 0 14 14"><path d="M2.5 7.5l3 3L11.5 4" stroke="#1E6B45" stroke-width="2" fill="none"/></svg>SPLNĚNO</span></div>
<h2>B · Hlavička protokolu PDF, e-mailový podpis, záhlaví odpovědního listu</h2><div class=row>
<div style="width:420px;border:1px solid #ccc;padding:20px;background:#fff">${img('exam-test-logo.svg','width:150px')}<div style="font:600 18px sans-serif;margin-top:14px">Protokol o výsledku zkoušky</div></div>
<div style="width:360px;border:1px solid #ccc;padding:14px;background:#fff;font:14px sans-serif"><b>Lucie Lektorová</b><br>Krajská vzdělávací agentura<br><div style="margin-top:10px">${img('exam-test-logo.svg','width:120px')}</div></div>
<div style="width:300px;border:1px solid #ccc;padding:14px;background:#fff">${img('exam-test-znacka-mala.svg','width:20px')} <span style="font:600 13px monospace;vertical-align:5px">exam-test</span></div></div>
<h2>C · Sociální sítě: profil (kruh), náhled odkazu 1200×630 (zmenšeno)</h2><div class=row>
<div style="width:120px;height:120px;border-radius:50%;background:#F6F4EC;display:flex;align-items:center;justify-content:center;outline:1px solid #ccc">${img('exam-test-znacka.svg','width:72px')}</div>
<div style="width:480px;height:252px;background:#F6F4EC;background-image:linear-gradient(#C9D3DD 1px,transparent 1px),linear-gradient(90deg,#C9D3DD 1px,transparent 1px);background-size:20px 20px;position:relative;outline:1px solid #ccc">
<div style="position:absolute;left:28px;top:28px">${img('exam-test-logo.svg','width:170px')}</div><div style="position:absolute;left:28px;bottom:30px;font:800 30px/1.05 sans-serif;color:#22262A;width:400px">Jeden test. Online<br>i na papíře.</div></div></div>
<h2>D · Razítko (1 barva modrá) a raznice (slepotisk – simulace)</h2><div class=row>
<div class=bg style="background:#fff">${img('exam-test-logo-cerne.svg','width:180px;filter:invert(19%) sepia(80%) saturate(2500%) hue-rotate(220deg) opacity(.8)')}</div>
<div class=bg style="background:#EEEAE0">${img('exam-test-logo-cerne.svg','width:180px;opacity:.18;filter:drop-shadow(1px 1px 0 #fff) drop-shadow(-1px -1px 0 #9a9585)')}</div></div>`;
const html=`<!doctype html><html><head><meta charset=utf-8><style>body{margin:0;padding:24px;font:13px/1.3 monospace;background:#fff;color:#222;width:1560px}
h2{font-size:15px;margin:18px 0 8px;text-transform:uppercase;letter-spacing:.08em}.row{display:flex;gap:28px;align-items:flex-end;flex-wrap:wrap}.c{display:flex;flex-direction:column;gap:6px}.bg{padding:18px}</style></head>
<body><h1 style="font-size:20px">Logo · testovací arch · loop ${loop}</h1>${loop=='2'?L2:L3}</body></html>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1608,height:900}});await p.setContent(html);await p.screenshot({path:out,fullPage:true});await b.close();console.log('ok')})();
