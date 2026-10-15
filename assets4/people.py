import sys, json, os, re, time, urllib.parse, urllib.request
UA = {"User-Agent": "CanalDarkBot/1.0 (educational documentary; contact github.com/viniciushoscher-ctrl/Canal-Dark-)"}
def get(url):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e: time.sleep(3 + 3 * i); err = e
    raise err
J = lambda u: json.loads(get(u))
out = sys.argv[2]; os.makedirs(out, exist_ok=True); cred = []
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.strip()
    if "|" not in line: continue
    tag, title = line.split("|", 1)
    try:
        d = J("https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(dict(action="query", format="json", titles=title, prop="pageimages", piprop="thumbnail|name", pithumbsize=1600, redirects=1)))
        pg = list(d["query"]["pages"].values())[0]
        th = pg.get("thumbnail", {}).get("source"); nm = pg.get("pageimage")
        if not th: print("sem imagem", tag); continue
        lic = ""; au = ""
        try:
            m = J("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(dict(action="query", format="json", titles="File:" + nm, prop="imageinfo", iiprop="extmetadata")))
            ex = list(m["query"]["pages"].values())[0]["imageinfo"][0]["extmetadata"]
            lic = ex.get("LicenseShortName", {}).get("value", ""); au = re.sub("<[^>]+>", "", ex.get("Artist", {}).get("value", ""))
        except Exception as e: print("licenca?", tag, e)
        fn = os.path.join(out, tag + ".jpg")
        open(fn, "wb").write(get(th))
        cred.append(dict(file=fn, wiki=title, image=nm, license=lic, author=au)); print(tag, "ok", lic)
    except Exception as e: print("erro", tag, e)
    time.sleep(0.5)
json.dump(cred, open(os.path.join(out, "credits.json"), "w"), indent=1, ensure_ascii=False)
