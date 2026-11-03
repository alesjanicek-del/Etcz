// Testovací arch loga: node tools/logo_test.js <dir_s_logy> <out.png> <loop>
const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
const [dir,out,loop]=process.argv.slice(2);const r=f=>fs.readFileSync(path.join(dir,f),'utf8');
const img=(f,style)=>`<img src="data:image/svg+xml;base64,${Buffer.from(r(f)).toString('base64')}" style="${style}">`;
const html=`<!doctype html><html><head><meta charset=utf-8><style>
body{margin:0;padding:24px;font:13px/1.3 'IBM Plex Mono',monospace;background:#fff;color:#222;width:1560px}
h2{font-size:15px;margin:18px 0 8px;text-transform:uppercase;letter-spacing:.08em}
.row{display:flex;gap:28px;align-items:flex-end;flex-wrap:wrap}.c{display:flex;flex-direction:column;gap:6px;align-items:flex-start}
.bg{padding:18px;display:flex;gap:24px;align-items:center}
.px{image-rendering:pixelated}
</style></head><body><h1 style="font-size:20px">Logo · testovací arch · ${loop}</h1>
<h2>1 · Velikosti – logo (šířka v px)</h2><div class="row">${[480,240,160,120,96,72].map(w=>`<div class=c>${img('exam-test-logo.svg',`width:${w}px`)}<span>${w}px</span></div>`).join('')}</div>
<h2>2 · Velikosti – značka (px) a malá značka</h2><div class="row">${[96,48,32,24,16].map(w=>`<div class=c>${img('exam-test-znacka.svg',`width:${w}px`)}<span>${w}</span></div>`).join('')}<span style="width:30px"></span>${[32,24,16].map(w=>`<div class=c>${img('exam-test-znacka-mala.svg',`width:${w}px`)}<span>malá ${w}</span></div>`).join('')}</div>
<h2>3 · Favicon 16 a 32 px – zvětšeno ×6 (pixely)</h2><div class="row" id="fav"></div>
<h2>4 · Pozadí a barevné varianty</h2><div class="row">
<div class="bg" style="background:#F6F4EC">${img('exam-test-logo.svg','width:240px')}</div>
<div class="bg" style="background:#FFFFFF;outline:1px solid #ddd">${img('exam-test-logo.svg','width:240px')}</div>
<div class="bg" style="background:#22262A">${img('exam-test-logo-negativ.svg','width:240px')}</div>
<div class="bg" style="background:#F2CB2E">${img('exam-test-logo-na-zlute.svg','width:240px')}</div>
<div class="bg" style="background:linear-gradient(120deg,#8a8f7a,#c7c2b0 40%,#5d6470)">${img('exam-test-logo.svg','width:240px')}</div></div>
<h2>5 · Reprodukce: odstíny šedi, 1 barva, fotokopie (práh 50 %)</h2><div class="row">
<div class="bg" style="background:#fff;filter:grayscale(1)">${img('exam-test-logo.svg','width:240px')}</div>
<div class="bg" style="background:#fff">${img('exam-test-logo-cerne.svg','width:240px')}</div>
<div class="bg" style="background:#fff">${img('exam-test-logo-cerne-srafa.svg','width:240px')}</div>
<div class="bg" style="background:#fff;filter:grayscale(1) contrast(40)">${img('exam-test-logo.svg','width:240px')}</div></div>
<h2>6 · Svislá verze, wordmark, aplikační ikona v maskách</h2><div class="row">
${img('exam-test-logo-svisle.svg','width:160px')}${img('exam-test-wordmark.svg','width:200px')}
${img('app-icon.svg','width:96px;border-radius:22px')}${img('app-icon.svg','width:96px;border-radius:50%')}${img('app-icon.svg','width:48px;border-radius:11px')}</div>
<h2>7 · Kontext UI: vedle ikon „zavřít“ a stavu „nesplněno“</h2><div class="row" style="align-items:center">
${img('exam-test-znacka.svg','width:32px')}<svg width="32" height="32" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" stroke="#22262A" stroke-width="2"/></svg>
<span style="border:1.5px solid #B3261E;color:#B3261E;padding:4px 8px">✕ NESPLNĚNO</span><span>← riziko záměny</span></div>
</body></html>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1608,height:900},deviceScaleFactor:1});
await p.setContent(html);
// favicon real pixels: render 16/32 at dsf1 into canvas then upscale
const fav=r('favicon-16.svg'),fav32=r('favicon-32.svg'),mk=r('exam-test-znacka.svg');
await p.evaluate(async([fav,fav32,mk])=>{const host=document.getElementById('fav');
 for(const [s,svg,lab] of [[16,fav,'favicon 16'],[32,fav32,'favicon 32'],[16,mk,'plná značka 16']]){const im=new Image();im.src='data:image/svg+xml;base64,'+btoa(unescape(encodeURIComponent(svg)));await im.decode();
 const c=document.createElement('canvas');c.width=s;c.height=s;c.getContext('2d').drawImage(im,0,0,s,s);
 const z=document.createElement('canvas');z.width=s*6;z.height=s*6;const zc=z.getContext('2d');zc.imageSmoothingEnabled=false;zc.drawImage(c,0,0,s*6,s*6);
 const d=document.createElement('div');d.className='c';d.append(z);const l=document.createElement('span');l.textContent=lab;d.append(l);host.append(d);}},[fav,fav32,mk]);
await p.screenshot({path:out,fullPage:true});await b.close();console.log('ok',out)})();
