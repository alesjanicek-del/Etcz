// Vektorové PDF loga pro tiskárny (CMYK převod si dělá tiskárna; barvy viz manuál)
const { chromium } = require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const f of ['exam-test-logo','exam-test-logo-cerne','exam-test-logo-negativ','exam-test-znacka','exam-test-logo-svisle']){
 const s=fs.readFileSync(`assets/logo/${f}.svg`,'utf8');const m=s.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);const wmm=80,hmm=wmm*m[2]/m[1];
 await p.setContent(`<html><body style="margin:0">${s.replace(/width="[\d.]+" height="[\d.]+" role/,`width="${wmm}mm" height="${hmm}mm" role`)}</body></html>`);
 await p.pdf({path:`assets/logo/${f}.pdf`,width:wmm+'mm',height:(hmm+0.1)+'mm',printBackground:true,pageRanges:'1'});}
await b.close();console.log('pdf ok')})();
