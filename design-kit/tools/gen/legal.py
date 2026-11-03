import re, html, sys, unicodedata, json
CR='/tmp/claude-0/-home-user-Etcz/55de0f84-554c-5f5c-ac5b-96e089e53363/scratchpad/crawl/web/'
H2X={'ochrana-osobnich-udaju':["Kdo je správce","Údaje zkoušených a uživatelů organizací","Jaké údaje zpracováváme jako správce, proč a jak dlouho","Kde jsou údaje uloženy a komu je předáváme","Cookies","Vaše práva"],
 'prohlaseni-o-pristupnosti':["Stav souladu","Nepřístupný obsah","Časový limit testu","Odhlášení po nečinnosti","Dohled nad zkouškou","Vypracování tohoto prohlášení o přístupnosti","Zpětná vazba a kontaktní údaje","Vynucovací postup"]}
def slug(t):
    t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower()
    t=re.sub(r'[^a-z0-9]+','-',t).strip('-'); return t[:48].strip('-')
def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'([\w.+-]+@[\w-]+\.[\w.]+[a-z])',r'<a href="mailto:\1">\1</a>',t)
    return t
def conv(name):
    L=open(CR+name+'.txt',encoding='utf-8').read().split('\n')
    title=L[0].strip(); out=[]; toc=[]; ids=set(); i=1; lst=[]; tbl=[]
    def flush():
        nonlocal lst,tbl
        if lst:
            items=[]
            for x in lst:
                m=re.match(r'^([^:]{3,90}?): (.*)$',x)
                items.append(f'<li><b>{inline(m.group(1))}:</b> {inline(m.group(2))}</li>' if m and not x[0].islower() else f'<li>{inline(x)}</li>')
            out.append('<ul>'+''.join(items)+'</ul>'); lst=[]
        if tbl:
            hd=tbl[0]; rows=tbl[1:]
            r=['<div class="table-wrap"><table class="table table--stack"><caption class="sr-only">Další zpracovatelé</caption><thead><tr>'+''.join(f'<th scope="col">{inline(c)}</th>' for c in hd)+'</tr></thead><tbody>']
            for row in rows: r.append('<tr>'+''.join(f'<td data-label="{html.escape(hd[k])}" style="text-align:left;white-space:normal">{inline(c)}</td>' for k,c in enumerate(row))+'</tr>')
            r.append('</tbody></table></div>'); out.append(''.join(r)); tbl=[]
    def heading(lvl,t):
        flush(); s=slug(t)
        if name=='ochrana-osobnich-udaju' and t=='Cookies': s='cookies'
        while s in ids: s+='-2'
        ids.add(s)
        out.append(f'<h{lvl} id="{s}">{inline(t)}</h{lvl}>')
        if lvl==2: toc.append((s,t))
    # gather blocks
    blocks=[]; cur=[]
    for ln in L[1:]:
        if ln.strip()=='' :
            if cur: blocks.append(cur); cur=[]
        else: cur.append(ln.strip())
    if cur: blocks.append(cur)
    intro_alert=None
    bi=0
    for b in blocks:
        if b[0]=='Návrh' and intro_alert is None:
            intro_alert=b[1] if len(b)>1 else ''; continue
        multi=len(b)>1
        for ln in b:
            if re.match(r'^\d+\. \S',ln) or re.match(r'^Příloha \d',ln) or ln in H2X.get(name,[]):
                heading(2,ln); continue
            if re.match(r'^[a-c]\) \S',ln) and len(ln)<80:
                heading(3,ln); continue
            if '\t' in ln:
                tbl.append(ln.split('\t')); continue
            if tbl: flush()
            # list item if the block (after headings) has multiple text lines
            textlines=[x for x in b if not (re.match(r'^\d+\. \S',x) or re.match(r'^Příloha \d',x) or x in H2X.get(name,[]) or (re.match(r'^[a-c]\) \S',x) and len(x)<80) or '\t' in x)]
            if len(textlines)>1:
                lst.append(ln); continue
            flush()
            m=re.match(r'^(\d+\.\d+) (.*)$',ln)
            if m: out.append(f'<p id="cl-{m.group(1).replace(".","-")}"><b>{m.group(1)}</b> {inline(m.group(2))}</p>')
            else: out.append(f'<p>{inline(ln)}</p>')
        flush()
    flush()
    return title,intro_alert,toc,'\n'.join(out)
if __name__=='__main__':
    t,a,toc,body=conv(sys.argv[1]); print(t,a,toc,sep='\n'); print(body[:3000])
