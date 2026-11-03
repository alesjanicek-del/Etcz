import re,json,os
S=dict(re.findall(r'<symbol id="i-([a-z-]+)" viewBox="0 0 24 24">(.*?)</symbol>',open('assets/icons.svg').read()))
I=lambda n,c='i':f'<svg class="{c}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{S[n]}</svg>'
def L(h):
    h=h.lstrip('#');r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)];f=lambda c:c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def cr(a,b):x,y=sorted([L(a),L(b)],reverse=True);return (x+0.05)/(y+0.05)
COL=[('Grafit','--c-grafit','#22262A','Text, linky, rámečky, tmavé plochy, hlavní tlačítko'),('Šedá','--c-seda','#5A6068','Sekundární text: metadata, nápovědy, štítky; okraj polí'),('Propiska','--c-propiska','#2747A0','Odkazy, fokus z klávesnice, informační stav'),('Papír','--c-papir','#F6F4EC','Pozadí stránek'),('Bílá','--c-bila','#FFFFFF','Karty, formulářová pole, tabulky, tisk'),('Zvýrazňovač','--c-zvyraznovac','#F2CB2E','Akcent: stín hlavního tlačítka, aktuální otázka, zvýraznění – nikdy text'),('Zvýrazňovač světlý','--c-zvyraznovac-svetly','#FFF7D1','Vybraná odpověď, upozornění, najetí myší'),('Mřížka','--c-mrizka','#C9D3DD','Rastr pozadí, neaktivní prvky, prázdná část pruhu'),('Linka','--c-linka','#D9DCD3','Jemné oddělovače řádků'),('Splněno','--c-splneno','#1E6B45','Stav splněno – vždy s ikonou ✓ a slovem'),('Nesplněno','--c-nesplneno','#B3261E','Stav nesplněno, chyby formuláře – vždy s ikonou ⊖'),('Pozor (text)','--c-pozor','#6B5A00','Text varování na světle žluté')]
sw=''.join(f'<div class="tile"><div class="swatch" style="background:{h}"></div><div class="tile__txt"><h3 class="t-nadpis">{n}</h3><p class="t-kod">{h}</p><p class="t-maly"><code>{v}</code></p><p class="t-maly">{u}</p></div></div>' for n,v,h,u in COL)
PAIRS=[('Grafit','#22262A','Papír','#F6F4EC','text'),('Grafit','#22262A','Bílá','#FFFFFF','text'),('Grafit','#22262A','Zvýrazňovač','#F2CB2E','text'),('Grafit','#22262A','Zvýrazňovač světlý','#FFF7D1','text'),('Šedá','#5A6068','Papír','#F6F4EC','text'),('Šedá','#5A6068','Bílá','#FFFFFF','text'),('Šedá','#5A6068','Zvýrazňovač','#F2CB2E','text'),('Propiska','#2747A0','Papír','#F6F4EC','text'),('Propiska','#2747A0','Bílá','#FFFFFF','text'),('Papír','#F6F4EC','Grafit','#22262A','text'),('Šedá na tmavé','#C7CBCF','Grafit','#22262A','text'),('Zvýrazňovač','#F2CB2E','Grafit','#22262A','text'),('Splněno','#1E6B45','Splněno pozadí','#E3F0E6','text'),('Nesplněno','#B3261E','Nesplněno pozadí','#FBE7E4','text'),('Pozor','#6B5A00','Zvýrazňovač světlý','#FFF7D1','text'),('Propiska','#2747A0','Info pozadí','#E7ECF8','text'),('Okraj pole (šedá)','#5A6068','Bílá','#FFFFFF','prvek'),('Zvýrazňovač','#F2CB2E','Papír','#F6F4EC','dekorace'),('Mřížka','#C9D3DD','Papír','#F6F4EC','dekorace')]
rows=''
for a,ah,b,bh,typ in PAIRS:
    c=cr(ah,bh);need=4.5 if typ=='text' else (3 if typ=='prvek' else 0)
    ok=c>=need
    st=f'<span class="stav stav--ok">{I("check")}Vyhovuje</span>' if ok and need else (f'<span class="stav stav--neutral">Jen dekorace</span>' if not need else f'<span class="stav stav--ne">{I("minus-kruh")}Nepoužívat</span>')
    rows+=f'<tr{" class=\"no-check\"" if (need and not ok) else ""}><td data-label="Popředí">{a}</td><td data-label="Pozadí">{b}</td><td data-label="Ukázka"><span style="background:{bh};color:{ah};padding:4px 10px;border:1px solid var(--c-linka);font-weight:700" class="no-check">Aa 123</span></td><td class="num" data-label="Kontrast">{str(round(c,1)).replace(".",",")} : 1</td><td data-label="Použití">{ {"text":"text (min. 4,5)","prvek":"okraj prvku (min. 3)","dekorace":"bez informace"}[typ]}</td><td data-label="Výsledek">{st}</td></tr>'
icons=''.join(f'<li style="display:flex;flex-direction:column;align-items:center;gap:8px;padding:var(--s-3) var(--s-2);background:var(--c-bila);border:var(--b-tenka) solid var(--c-linka)">{I(n,"i i-l")}<span class="t-stitek" style="text-transform:none;letter-spacing:0">{n}</span></li>' for n in S)
open('_brand_parts.json','w').write(json.dumps({'SWATCHES':sw,'CONTRAST':rows,'ICONS':icons}))
s=open('tools/src/brand.src.html').read()
for k,v in {'SWATCHES':sw,'CONTRAST':rows,'ICONS':icons}.items(): s=s.replace('{{'+k+'}}',v)
s=re.sub(r'\{\{I:([a-z-]+)\}\}',lambda m:I(m.group(1)),s)
open('brand.html','w').write(s);os.remove('_brand_parts.json');print('brand ok')
