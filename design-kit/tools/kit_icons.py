"""Nahradí {{I:nazev}} (a starší {{IKONA}}/{{MINUS}}) inline ikonami ve stránkách kitu v kořeni."""
import re,sys,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S=dict(re.findall(r'<symbol id="i-([a-z-]+)" viewBox="0 0 24 24">(.*?)</symbol>',open(os.path.join(ROOT,'assets/icons.svg')).read()))
I=lambda n:f'<svg class="i" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{S[n]}</svg>'
for f in sys.argv[1:]:
    s=open(f).read().replace('{{IKONA}}','{{I:stahnout}}').replace('{{MINUS}}','{{I:minus-kruh}}')
    s=re.sub(r'\{\{I:([a-z-]+)\}\}',lambda m:I(m.group(1)),s);open(f,'w').write(s)
