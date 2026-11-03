"""Logo Triconform, směr B „Týden“. Spuštění: python3 triconform/tools/logo_build.py
Značka: tři pruhy = Hned · Tento týden · Později (zároveň tři roviny) + odškrtnutí.
Nápis: Source Serif 4 Bold (OFL) převedený na křivky."""
import os,io
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JEDLE,SIGNAL,LISTI,MATA,PAPIR,BILA='#163D33','#E2622B','#8DB8A6','#DCEBE3','#F7F5EF','#FFFFFF'
f=TTFont(os.path.join(R,'fonts','SourceSerif4-latin.woff2'))
f=instantiateVariableFont(f,{'wght':700,'opsz':48})
gs=f.getGlyphSet();cmap=f.getBestCmap();upm=f['head'].unitsPerEm;xh=f['OS/2'].sxHeight;asc=f['OS/2'].sCapHeight
def word(text,track=-8):
    pen=SVGPathPen(gs);x=0;bp=BoundsPen(gs)
    for ch in text:
        g=cmap[ord(ch)];gs[g].draw(TransformPen(pen,(1,0,0,-1,x,0)));gs[g].draw(TransformPen(bp,(1,0,0,1,x,0)));x+=gs[g].width+track
    return pen.getCommands(),bp.bounds
WP,WB=word('triconform')   # WB: xmin,ymin,xmax,ymax (y nahoru)
# značka na mřížce 160×160
def mark(c1,c2,c3,ck,check=True):
    s=f'<rect x="8" y="24" width="144" height="28" fill="{c1}"/><rect x="8" y="66" width="104" height="28" fill="{c2}"/><rect x="8" y="108" width="62" height="28" fill="{c3}"/>'
    if check: s+=f'<path d="M86 118 L102 134 L140 92" fill="none" stroke="{ck}" stroke-width="13" stroke-linecap="square" stroke-linejoin="miter"/>'
    return s
def svg(w,h,body,bg=None,t='Triconform'):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{t}"><title>{t}</title>{b}{body}</svg>\n'
def lockup(c,ink,bg=None):
    # výška značky = 1,9× výška malých písmen x-height; nápis sedí na účaří spodního pruhu
    mh=xh*1.9*160/112; sc=mh/160; gap=xh*0.55
    wx0,wy0,wx1,wy1=WB; ww=wx1-wx0
    base=136*sc  # účaří = spodní hrana spodního pruhu
    top=min(0,base-wy1); H=max(mh,base-wy0)-top
    body=f'<g transform="translate(0,{-top:.1f}) scale({sc:.5f})">{mark(*c)}</g><path transform="translate({mh+gap-wx0:.1f},{base-top:.1f})" d="{WP}" fill="{ink}"/>'
    return svg(mh+gap+ww,H,body,bg)
def stacked(c,ink,bg=None):
    wx0,wy0,wx1,wy1=WB;ww=wx1-wx0;mh=ww*0.42;sc=mh/160;g=xh*0.5
    H=mh+g+(wy1-wy0)
    body=f'<g transform="translate({(ww-mh)/2:.1f},0) scale({sc:.5f})">{mark(*c)}</g><path transform="translate({-wx0:.1f},{mh+g+wy1:.1f})" d="{WP}" fill="{ink}"/>'
    return svg(ww,H,body,bg)
POS=(SIGNAL,JEDLE,LISTI,JEDLE); NEG=(SIGNAL,PAPIR,LISTI,PAPIR)
MONO_D=(JEDLE,JEDLE,JEDLE,JEDLE); MONO_L=(PAPIR,PAPIR,PAPIR,PAPIR)
out=os.path.join(R,'logo');os.makedirs(out,exist_ok=True)
files={
 'triconform-logo.svg':lockup(POS,JEDLE),
 'triconform-logo-negativ.svg':lockup(NEG,PAPIR,JEDLE),
 'triconform-logo-negativ-pruhledne.svg':lockup(NEG,PAPIR),
 'triconform-logo-mono-tmave.svg':lockup(MONO_D,JEDLE),
 'triconform-logo-mono-svetle.svg':lockup(MONO_L,PAPIR),
 'triconform-logo-na-vysku.svg':stacked(POS,JEDLE),
 'triconform-znacka.svg':svg(160,160,mark(*POS)),
 'triconform-znacka-negativ.svg':svg(160,160,mark(*NEG),JEDLE),
 'triconform-znacka-svetla.svg':svg(160,160,mark(*NEG)),
 # favicona: bez odškrtnutí, pruhy zesílené pro 16–32 px
 'favicon.svg':svg(32,32,f'<rect width="32" height="32" fill="{PAPIR}"/><rect x="3" y="5" width="26" height="6" fill="{SIGNAL}"/><rect x="3" y="13" width="19" height="6" fill="{JEDLE}"/><rect x="3" y="21" width="11" height="6" fill="{LISTI}"/>'),
 'app-icon.svg':svg(512,512,f'<g transform="translate(96,96) scale(2)">{mark(*NEG)}</g>',JEDLE),
}
for n,s in files.items(): open(os.path.join(out,n),'w').write(s)
print('\n'.join(files))
