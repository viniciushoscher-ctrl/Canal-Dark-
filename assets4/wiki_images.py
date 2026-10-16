#!/usr/bin/env python3
"""uso: wiki_images.py lista.txt saida_dir  (linhas 'tag|Titulo_do_artigo_da_Wikipedia')
Baixa as imagens do proprio artigo (retratos, gravuras, fotos de epoca) com legenda e licenca. So midia publica."""
import sys, os, json, re, time, urllib.request, urllib.parse
UA = {"User-Agent": "CanalDarkBot/1.0 (educational documentary; contact: viniciushoscher@gmail.com)"}
API = "https://en.wikipedia.org/w/api.php"
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
        except Exception as e:
            time.sleep(2 + i * 3)
    return None
def api(**p):
    p["format"] = "json"; r = get(API + "?" + urllib.parse.urlencode(p))
    return json.loads(r) if r else {}
BAD = re.compile(r"(flag|logo|icon|symbol|map of|commons-|wiki|edit-|question|stub|signature|coat of arms|seal of|\.svg|\.ogg|\.webm|\.pdf|\.tif|lock-|ambox|folder|padlock|red pog|increase|decrease|steady)", re.I)
lst, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True); cred = []
for ln in open(lst, encoding="utf-8"):
    if "|" not in ln: continue
    tag, title = ln.strip().split("|", 1)
    d = api(action="query", titles=title, prop="images", imlimit=60, redirects=1)
    files = []
    for pg in d.get("query", {}).get("pages", {}).values():
        files += [x["title"] for x in pg.get("images", [])]
    n = 0
    for f in files:
        if BAD.search(f) or not re.search(r"\.(jpe?g|png)$", f, re.I): continue
        info = api(action="query", titles=f, prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=1600)
        for pg in info.get("query", {}).get("pages", {}).values():
            ii = (pg.get("imageinfo") or [{}])[0]
            if not ii or ii.get("width", 0) < 500 or ii.get("height", 0) < 350: continue
            em = ii.get("extmetadata", {}); desc = re.sub(r"<[^>]+>", "", em.get("ImageDescription", {}).get("value", ""))[:220]
            lic = em.get("LicenseShortName", {}).get("value", "")
            if lic and not re.search(r"(public domain|pd|cc|gfdl|free)", lic, re.I): continue
            data = get(ii.get("thumburl") or ii["url"])
            if not data or len(data) < 15000: continue
            fn = f"{tag}_{n}.jpg"; open(os.path.join(out, fn), "wb").write(data); n += 1
            cred.append({"file": os.path.join(out, fn), "tag": tag, "article": title, "title": f[5:], "desc": desc, "license": lic, "w": ii["width"], "h": ii["height"]})
        if n >= 10: break
    print(tag, title, n, flush=True)
json.dump(cred, open(os.path.join(out, "credits.json"), "w"), ensure_ascii=False, indent=1)
