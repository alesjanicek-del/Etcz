// node tools/shot.js web/index.html out.png [šířka]
const { chromium } = require('playwright');const path=require('path');
(async()=>{const [f,o,w]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:+(w||1280),height:900}});
await p.goto('file://'+path.resolve(f),{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);await p.screenshot({path:o,fullPage:true});await b.close()})();
