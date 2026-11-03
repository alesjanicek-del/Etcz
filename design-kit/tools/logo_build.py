"""Generátor loga exam-test (směr B). Spuštění: python3 tools/logo_build.py
Wordmark je IBM Plex Mono SemiBold převedený na křivky (OFL licence)."""
import json,os,sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=json.load(open(os.path.join(ROOT,'tools','logo_params.json')))
GRAFIT,ZLUTA,PAPIR,BILA='#22262A','#F2CB2E','#F6F4EC','#FFFFFF'
font=TTFont(os.path.join(ROOT,'assets','fonts','IBMPlexMono-600-latin.woff2'))
gs=font.getGlyphSet();cmap=font.getBestCmap();upm=font['head'].unitsPerEm
cap=font['OS/2'].sCapHeight; xh=font['OS/2'].sxHeight
def word_path(text,tracking=0):
    pen=SVGPathPen(gs);x=0;t=P['word'].get('hyphen_tighten',0)
    for i,ch in enumerate(text):
        g=cmap[ord(ch)]
        if ch=='-': x-=t/2
        tp=TransformPen(pen,(1,0,0,-1,x,0));gs[g].draw(tp);x+=gs[g].width+tracking
        if ch=='-': x-=t
    return pen.getCommands(),x-tracking
def mark(c_ink,c_hi,c_bg,mode='full'):
    m=P['mark'];s=[]
    if mode in('full',) and c_hi:
        s.append(f'<path d="{m["hi"]}" fill="{c_hi}"/>')
    if mode=='mono-hatch':
        s.append(f'<path d="{m["hi"]}" fill="url(#h)"/>')
    s.append(f'<rect x="{m["box"][0]}" y="{m["box"][1]}" width="{m["box"][2]}" height="{m["box"][3]}" rx="{m["rx"]}" fill="none" stroke="{c_ink}" stroke-width="{m["sw"]}"/>')
    for d in m['x']:
        s.append(f'<path d="{d}" fill="none" stroke="{c_ink}" stroke-width="{m["xw"]}" stroke-linecap="round"/>')
    return ''.join(s)
HATCH='<defs><pattern id="h" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="1.6" height="4" fill="#22262A"/></pattern></defs>'
def svg(w,h,body,title='exam-test',bg=None):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{b}{body}</svg>\n'
def build(outdir):
    os.makedirs(outdir,exist_ok=True)
    wp,ww=word_path(P['word']['text'],P['word']['tracking'])
    M=96 # mark grid
    # lockup: mark height = k * cap height (in font units)
    k=P['lockup']['mark_to_cap']; mh=cap*k; sc=mh/M
    gap=P['lockup']['gap_cap']*cap
    pad=P['lockup']['clear_cap']*cap*0  # clear space defined in manual, not baked
    W=mh+gap+ww; H=mh
    base=(mh+cap)/2 # vertically center cap height on mark
    def lock(ink,hi,bg=None,mode='full'):
        body=(HATCH if mode=='mono-hatch' else '')+f'<g transform="scale({sc:.5f})">{mark(ink,hi,bg,mode)}</g><path transform="translate({mh+gap:.1f},{base:.1f})" d="{wp}" fill="{ink}"/>'
        return svg(round(W),round(H),body,bg=bg)
    def stacked(ink,hi,bg=None):
        mh2=cap*P['stack']['mark_to_cap'];sc2=mh2/M;g2=P['stack']['gap_cap']*cap
        W2=max(ww,mh2);H2=mh2+g2+cap
        body=f'<g transform="translate({(W2-mh2)/2:.1f},0) scale({sc2:.5f})">{mark(ink,hi,bg)}</g><path transform="translate({(W2-ww)/2:.1f},{mh2+g2+cap:.1f})" d="{wp}" fill="{ink}"/>'
        return svg(round(W2),round(H2),body,bg=bg)
    def markonly(ink,hi,bg=None,mode='full',small=False):
        mk=mark(ink,hi,bg,mode) if not small else small_mark(ink,hi)
        return svg(M,M,(HATCH if mode=='mono-hatch' else '')+mk,bg=bg)
    def lock_small(ink,hi):
        sc2=mh/32;mk=P['px32']['svg'].replace('#22262A',ink)
        body=f'<g transform="scale({sc2:.5f})">{mk}</g><path transform="translate({mh+gap:.1f},{base:.1f})" d="{wp}" fill="{ink}"/>'
        return svg(round(W),round(H),body)
    def plate():
        pd=cap*P['lockup']['clear_cap'];Wp=W+2*pd;Hp=H+2*pd
        body=f'<rect width="{Wp:.0f}" height="{Hp:.0f}" fill="{PAPIR}"/><g transform="translate({pd:.1f},{pd:.1f})"><g transform="scale({sc:.5f})">{mark(GRAFIT,ZLUTA,None)}</g><path transform="translate({mh+gap:.1f},{base:.1f})" d="{wp}" fill="{GRAFIT}"/></g>'
        return svg(round(Wp),round(Hp),body)
    files={
     'exam-test-logo.svg':lock(GRAFIT,ZLUTA),
     'exam-test-logo-cerne.svg':lock('#000000',None,mode='mono'),
     'exam-test-logo-negativ.svg':lock(PAPIR,ZLUTA,bg=GRAFIT),
     'exam-test-logo-negativ-pruhledne.svg':lock(PAPIR,ZLUTA),
     'exam-test-logo-male.svg':lock_small(GRAFIT,ZLUTA),
     'exam-test-logo-male-negativ.svg':lock_small(PAPIR,ZLUTA),
     'exam-test-logo-na-zlute.svg':lock(GRAFIT,None,bg=ZLUTA,mode='mono'),
     'exam-test-logo-svisle.svg':stacked(GRAFIT,ZLUTA),
     'exam-test-logo-na-podkladu.svg':plate(),
     'exam-test-znacka.svg':markonly(GRAFIT,ZLUTA),
     'exam-test-znacka-cerna.svg':markonly('#000000',None,mode='mono'),
     'exam-test-znacka-negativ.svg':markonly(PAPIR,ZLUTA,bg=GRAFIT),
     'exam-test-znacka-mala.svg':svg(32,32,P['px32']['svg']),
     'exam-test-wordmark.svg':svg(round(ww),round(cap*1.0+ (upm*0.0)),f'<path transform="translate(0,{cap:.1f})" d="{wp}" fill="{GRAFIT}"/>'),
    }
    for n,c in files.items(): open(os.path.join(outdir,n),'w').write(c)
    # app icon (square, bg paper, mark centered with safe zone 70%)
    def icon(sz,bg,small=False):
        inner=sz*P['icon']['inner']; s=inner/M; o=(sz-inner)/2
        mk=small_mark(GRAFIT,ZLUTA) if small else mark(GRAFIT,ZLUTA,None)
        return svg(sz,sz,f'<rect width="{sz}" height="{sz}" fill="{bg}"/><g transform="translate({o:.2f},{o:.2f}) scale({s:.5f})">{mk}</g>')
    open(os.path.join(outdir,'app-icon.svg'),'w').write(icon(512,PAPIR))
    for n in (16,32):
        q=P['px%d'%n];open(os.path.join(outdir,'favicon-%d.svg'%n),'w').write(svg(n,n,f'<rect width="{n}" height="{n}" rx="{q["bg_rx"]}" fill="{PAPIR}"/>'+q['svg']))
    open(os.path.join(outdir,'favicon.svg'),'w').write(open(os.path.join(outdir,'favicon-32.svg')).read())
    json.dump({'mark_grid':M,'cap':cap,'wordmark_width':ww,'lockup':[W,H]},open(os.path.join(outdir,'_metrics.json'),'w'))
def small_mark(ink,hi):
    m=P['small'];s=[]
    if hi: s.append(f'<path d="{m["hi"]}" fill="{hi}"/>')
    s.append(f'<rect x="{m["box"][0]}" y="{m["box"][1]}" width="{m["box"][2]}" height="{m["box"][3]}" rx="{m["rx"]}" fill="none" stroke="{ink}" stroke-width="{m["sw"]}"/>')
    for d in m['x']: s.append(f'<path d="{d}" fill="none" stroke="{ink}" stroke-width="{m["xw"]}" stroke-linecap="round"/>')
    return ''.join(s)
if __name__=='__main__': build(sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,'assets','logo'))
