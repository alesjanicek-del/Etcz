import sys,re
OPTS=[('ukazka','Ukázka s průvodcem'),('organizace','Chci aplikaci pro svou organizaci (po vyzkoušení dema)'),('urad','Cenová nabídka pro úřad nebo veřejnou zakázku'),('dotaz','Dotaz k funkcím nebo k ceníku'),('sablona','Šablona z připravovaného katalogu (zatím zdarma)'),('zavedeni','Poptat službu: pomoc se zavedením do organizace'),('import','Poptat službu: import / převod otázek'),('jina','Jiná služba: otázky na míru, školení lektorů')]
def form(p, mode='prazdny', checked=None, heading='Poptávka', hid='h'):
    err = mode=='chyba'
    E={'duvod':'Vyberte, s čím vám můžeme pomoci.','org':'Vyplňte název organizace.','email':'Zadejte e-mail ve tvaru jmeno@organizace.cz.'}
    def errp(k): return f'<p class="error" id="{p}-{k}-e">{{{{I:minus-kruh}}}}{E[k]}</p>' if err and k in E else ''
    def inv(k): return ' aria-invalid="true"' if err and k in E else ''
    def desc(k, extra=''):
        ids=[x for x in [extra, f'{p}-{k}-e' if err and k in E else ''] if x]
        return f' aria-describedby="{" ".join(ids)}"' if ids else ''
    out=[f'<form class="card stack-4" action="ukazka-odeslano.html" method="get" novalidate aria-labelledby="{p}-{hid}">',
         f'<h2 id="{p}-{hid}" class="t-nadpis">{heading}</h2>']
    if err:
        out.append(f'<div class="error-summary stack-2" role="alert" tabindex="-1" aria-labelledby="{p}-es"><p id="{p}-es" class="alert__nadpis">Poptávku jsme neodeslali. Opravte prosím 3&nbsp;pole:</p><ul class="stack-2" style="padding-left:var(--s-4)"><li><a href="#{p}-duvod-1">{E["duvod"]}</a></li><li><a href="#{p}-org">{E["org"]}</a></li><li><a href="#{p}-email">{E["email"]}</a></li></ul></div>')
    rad=[]
    for i,(v,t) in enumerate(OPTS,1):
        c=' checked' if checked==v else ''
        rad.append(f'<label class="check"><input type="radio" name="duvod" value="{v}" id="{p}-duvod-{i}"{c}{inv("duvod") if False else ""}><span>{t}</span></label>')
    out.append(f'<fieldset class="stack-2"{desc("duvod")}><legend class="label">S čím vám můžeme pomoci?</legend>{errp("duvod")}<div class="stack-2" style="gap:0">{"".join(rad)}</div></fieldset>')
    val_org='' ; val_email=' value="jana.novakova@"' if err else ''
    val_name=' value="Jana Nováková"' if err else ''
    out.append(f'<div class="grid-2">')
    out.append(f'<div class="field"><label class="label" for="{p}-org">Organizace</label>{errp("org")}<input class="input" id="{p}-org" name="organizace" autocomplete="organization"{inv("org")}{desc("org")}></div>')
    out.append(f'<div class="field"><label class="label" for="{p}-jmeno">Jméno a příjmení</label><input class="input" id="{p}-jmeno" name="jmeno" autocomplete="name"{val_name}></div>')
    out.append(f'<div class="field"><label class="label" for="{p}-email">E-mail</label>{errp("email")}<input class="input" type="email" id="{p}-email" name="email" autocomplete="email"{val_email}{inv("email")}{desc("email")}></div>')
    out.append(f'<div class="field"><label class="label" for="{p}-tel">Telefon <span class="volitelne">(nepovinné)</span></label><input class="input" type="tel" id="{p}-tel" name="telefon" autocomplete="tel"></div>')
    out.append('</div>')
    out.append(f'<div class="field"><label class="label" for="{p}-zprava">Zpráva <span class="volitelne">(nepovinné)</span></label><span class="hint" id="{p}-zprava-h">Například co chcete ověřovat, kolik osob ročně zkoušíte a zda zkoušíte i&nbsp;na papíře.</span><textarea class="textarea" id="{p}-zprava" name="zprava" aria-describedby="{p}-zprava-h"></textarea></div>')
    out.append(f'<div class="alert alert--info" role="note">{{{{I:info}}}}<p>Do formuláře nepište osobní údaje zkoušených. Údaje použijeme jen k&nbsp;vyřízení poptávky a uchováme je 12&nbsp;měsíců od konce měsíce, kdy poptávka přišla. <a href="ochrana-osobnich-udaju.html">Zásady ochrany osobních údajů</a></p></div>')
    out.append(f'<div class="form-actions"><button class="btn btn--hlavni" type="submit">Odeslat poptávku</button><p class="t-maly">Odpovíme do 2&nbsp;pracovních dnů.</p></div>')
    out.append('</form>')
    return '\n'.join(out)
src=open(sys.argv[1]).read()
def rep(m):
    a=m.group(1).split('|'); return form(a[0], a[1], a[2] or None, a[3], a[4] if len(a)>4 else 'h')
open(sys.argv[2],'w').write(re.sub(r'\{\{FORM:([^}]*)\}\}',rep,src))
