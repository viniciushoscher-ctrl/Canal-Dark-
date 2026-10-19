#!/usr/bin/env python3
"""Agenda os proximos N Shorts (ordem.md + mp4 em MEDIA) no YouTube, via publishAt.
Env: YT_CLIENT_ID YT_CLIENT_SECRET YT_REFRESH_TOKEN. Estado em posted.json. Uso: postar_shorts.py MEDIA ORDEM.md [--n 2] [--horas 12:00,21:00] [--dry]"""
import sys,os,re,json,argparse,datetime as dt
p=argparse.ArgumentParser();p.add_argument("media");p.add_argument("ordem");p.add_argument("--n",type=int,default=2)
p.add_argument("--horas",default="12:00,21:00");p.add_argument("--fuso",default="-03:00");p.add_argument("--dry",action="store_true")
a=p.parse_args()
st=json.load(open("posted.json")) if os.path.exists("posted.json") else {}
ents=[]
for b in re.split(r"\n## ",open(a.ordem,encoding="utf-8").read())[1:]:
    h=b.split("\n")[0];f=re.search(r"([\w.-]+\.mp4)",h)
    t=re.search(r"\*\*Title:\*\*\s*(.+)",b);d=re.search(r"\*\*Description:\*\*\s*(.+)",b);g=re.search(r"\*\*Hashtags:\*\*\s*(.+)",b)
    if f and t and d: ents.append((f.group(1),t.group(1).strip()[:100],(d.group(1)+"\n\n"+(g.group(1) if g else "")).strip()))
todo=[e for e in ents if e[0] not in st and os.path.exists(os.path.join(a.media,e[0]))][:a.n]
if not todo: print("nada a postar");sys.exit()
horas=a.horas.split(",");now=dt.datetime.now(dt.timezone(dt.timedelta(hours=int(a.fuso[:3]))))
slots=[];day=now.date()
while len(slots)<len(todo):
    for h in horas:
        s=dt.datetime.fromisoformat(f"{day}T{h}:00{a.fuso}")
        if s>now+dt.timedelta(minutes=20): slots.append(s)
    day+=dt.timedelta(days=1)
if not a.dry:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    c=Credentials(None,refresh_token=os.environ["YT_REFRESH_TOKEN"],client_id=os.environ["YT_CLIENT_ID"],client_secret=os.environ["YT_CLIENT_SECRET"],token_uri="https://oauth2.googleapis.com/token")
    c.refresh(Request());yt=build("youtube","v3",credentials=c)
for (f,t,d),s in zip(todo,slots):
    pub=s.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ");print(f,t,pub)
    if a.dry: continue
    body={"snippet":{"title":t,"description":d,"categoryId":"27"},"status":{"privacyStatus":"private","publishAt":pub,"selfDeclaredMadeForKids":False}}
    r=yt.videos().insert(part="snippet,status",body=body,media_body=MediaFileUpload(os.path.join(a.media,f),mimetype="video/mp4",resumable=True)).execute()
    st[f]={"id":r["id"],"publishAt":pub};json.dump(st,open("posted.json","w"),indent=1)
