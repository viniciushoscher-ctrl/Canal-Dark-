import re,sys,glob,json
sys.path.insert(0,'/tmp/w'); import lib
M=lib.M
KW=re.compile(r"\b(dead|died|death|bankrupt\w*|million|billion|fired|lost|lose|crash\w*|never|first|secret|refused|nearly|broke|failed|fail\w*|shot|prison|war|worth|\$)\b|\d",re.I)
def pick(srt,n=2,skip=40):
    cs=lib.cues(M+srt); out=[]
    cands=[]
    for i,(s,e,t) in enumerate(cs):
        if s<skip: continue
        if i>0 and not cs[i-1][2].rstrip().endswith(('.','?','!')): continue
        j=i
        while j+1<len(cs) and cs[j][1]-s<30: j+=1
        while j+1<len(cs) and not cs[j][2].rstrip().endswith(('.','?','!')) and cs[j][1]-s<35: j+=1
        d=cs[j][1]-s
        if not(28<=d<=35.5) or not cs[j][2].rstrip().endswith(('.','?','!')): continue
        txt=" ".join(c[2] for c in cs[i:j+1])
        sc=len(KW.findall(txt))+ (3 if KW.search(t) else 0)
        cands.append((sc,s,cs[j][1],t,txt))
    cands.sort(reverse=True); sel=[]
    for c in cands:
        if all(c[2]<x[1]-5 or c[1]>x[2]+5 for x in sel): sel.append(c)
        if len(sel)==n: break
    return sorted(sel,key=lambda x:x[1])
if __name__=="__main__":
    vids=sys.argv[1:]
    n=6;meta=[]
    for v in vids:
        d=glob.glob(M+f"video{v}/*_Video{v}_Final.mp4")[0]; srt=d.replace("_Final.mp4","_English.srt")
        name=d.split("/")[-1].split("_")[0]
        for sc,a,b,first,txt in pick(srt.replace(M,"")):
            w=re.sub(r"[^\w'’$%,.? -]","",first).split(); hook=" ".join(w[:9]).upper().rstrip(",.")
            num=f"{n:03d}"; hook=json.load(open('/tmp/w/hooks.json')).get(num,hook); lib.make(f"{num}_v{v}",d.replace(M,""),srt.replace(M,""),a,b,hook)
            meta.append(dict(n=num,v=v,name=name,hook=hook,txt=txt,a=a,b=b)); n+=1
    json.dump(meta,open('/tmp/w/meta.json','w'),indent=1)
