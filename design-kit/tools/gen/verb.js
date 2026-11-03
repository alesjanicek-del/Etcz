const { chromium } = require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
const CR='/tmp/claude-0/-home-user-Etcz/55de0f84-554c-5f5c-ac5b-96e089e53363/scratchpad/crawl/web/';
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const n of ['podminky','ochrana-osobnich-udaju','zpracovatelska-smlouva','prohlaseni-o-pristupnosti']){
 await p.goto('file:///home/user/Etcz/design-kit/web/'+n+'.html');
 const got=await p.evaluate(()=>document.querySelector('.prose-pravni').textContent.replace(/\s+/g,''));
 const h1=await p.evaluate(()=>document.querySelector('h1').textContent.replace(/\s+/g,''));
 const al=await p.evaluate(()=>{const a=document.querySelector('.alert p:not(.alert__nadpis)');return a?a.textContent.replace(/\s+/g,''):''});
 let src=fs.readFileSync(CR+n+'.txt','utf8').replace(/\s+/g,'');
 src=src.replace(h1,'').replace('Návrh'+al,'');
 console.log(n, got===src?'VERBATIM OK':'DIFF', got.length, src.length);
 if(got!==src){let i=0;while(got[i]===src[i])i++;console.log(' at',i,'got:',got.slice(i-20,i+40),'\n src:',src.slice(i-20,i+40));}
}await b.close()})();
