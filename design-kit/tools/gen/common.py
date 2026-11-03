import json
ROOT='/home/user/Etcz/design-kit/src/tisk/'
TEST='Kybernetická bezpečnost — roční ověření'
CROP=''.join(f'<span aria-hidden="true" style="position:absolute;{v}:var(--s-4);{h}:var(--s-4);width:var(--s-4);height:var(--s-4);border-{v}:var(--b-silna) solid var(--c-grafit);border-{h}:var(--b-silna) solid var(--c-grafit)"></span>' for v in ('top','bottom') for h in ('left','right'))
def page(inner, crop=False, label=''):
    return f'''<div class="a4" style="display:flex;flex-direction:column;gap:var(--s-3);margin-bottom:var(--s-5);font-size:var(--t-maly);line-height:1.4">{CROP if crop else ''}
{inner}
</div>'''
def foot(left,right):
    return f'<footer class="row-between" style="margin-top:auto;padding-top:var(--s-2);border-top:var(--b-tenka) solid var(--c-grafit)"><p class="t-stitek" style="text-transform:none;letter-spacing:0">{left}</p><p class="t-stitek" style="text-transform:none;letter-spacing:0">{right}</p></footer>'
def write(name, meta, spec, pages, label):
    body=f'''<main id="obsah"><div role="region" aria-label="Náhled tisku A4: {label}" tabindex="0" style="overflow-x:auto">
{pages}
</div></main>'''
    open(ROOT+name,'w').write('<!--meta '+json.dumps(meta,ensure_ascii=False)+' -->\n<!--spec '+json.dumps(spec,ensure_ascii=False,indent=1)+' -->\n'+body+'\n')
BOX='<span aria-hidden="true" style="display:block;width:var(--s-4);height:var(--s-4);border:var(--b-silna) solid var(--c-grafit);margin:0 auto;background:var(--c-bila)"></span>'
