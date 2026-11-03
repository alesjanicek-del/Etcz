const { chromium } = require('playwright'); const fs=require('fs'),path=require('path');
const D='assets/logo';const jobs=[
 ['exam-test-logo.svg',[240,480,960,1920]],['exam-test-logo-negativ.svg',[480,960]],['exam-test-logo-negativ-pruhledne.svg',[480,960]],['exam-test-logo-cerne.svg',[480,960]],
 ['exam-test-logo-na-podkladu.svg',[480,960]],['exam-test-logo-male.svg',[240,480]],['exam-test-logo-svisle.svg',[320,640]],['exam-test-znacka.svg',[64,128,256,512]],
 ['exam-test-znacka-negativ.svg',[256,512]],['exam-test-znacka-cerna.svg',[256,512]],['app-icon.svg',[180,192,512]],['favicon-16.svg',[16]],['favicon-32.svg',[32,48]]];
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const [f,ws] of jobs){const s=fs.readFileSync(path.join(D,f),'utf8');const m=s.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);const ar=m[2]/m[1];
 for(const w of ws){const h=Math.round(w*ar);await p.setViewportSize({width:w,height:h});
  await p.setContent(`<html><body style="margin:0;background:transparent">${s.replace(/width="[\d.]+" height="[\d.]+" role/,`width="${w}" height="${h}" role`)}</body></html>`);
  await p.screenshot({path:`${D}/png/${f.replace('.svg','')}-${w}.png`,omitBackground:true,clip:{x:0,y:0,width:w,height:h}});}}
// OG image
const logo=fs.readFileSync(D+'/exam-test-logo.svg','utf8');await p.setViewportSize({width:1200,height:630});
const og=`<html><head><meta charset=utf-8><style>@font-face{font-family:S;font-weight:700;src:url(../assets/fonts/SchibstedGrotesk-700-latin.woff2)}@font-face{font-family:S;font-weight:700;src:url(../assets/fonts/SchibstedGrotesk-700-latin-ext.woff2);unicode-range:U+0100-02BA}</style></head><body style="margin:0;width:1200px;height:630px;background:#F6F4EC;background-image:linear-gradient(#C9D3DD 1px,transparent 1px),linear-gradient(90deg,#C9D3DD 1px,transparent 1px);background-size:30px 30px;position:relative;font-family:S">
<div style="position:absolute;left:72px;top:64px;width:420px">${logo.replace(/width="[\d.]+" height="[\d.]+" role/,'width="420" height="69" role')}</div>
<div style="position:absolute;left:72px;bottom:72px;font-weight:700;font-size:84px;line-height:1.02;letter-spacing:-3px;color:#22262A">Jeden test.<br>Online i <span style="background:linear-gradient(transparent 55%,#F2CB2E 55%,#F2CB2E 92%,transparent 92%)">na papíře.</span></div></body></html>`;fs.writeFileSync('tools/_og.html',og);await p.goto('file://'+process.cwd()+'/tools/_og.html');await p.evaluate(()=>document.fonts.ready);
await p.waitForTimeout(400);await p.screenshot({path:D+'/png/og-image-1200x630.png'});await b.close();console.log('ok')})();
