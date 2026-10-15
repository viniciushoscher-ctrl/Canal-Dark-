import sys, json, os, re, time, urllib.parse, urllib.request
# uso: commons.py queries.txt outdir  (linhas "tag|termos de busca")
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "CanalDarkBot/1.0 (educational documentary; contact github.com/viniciushoscher-ctrl/Canal-Dark-)"}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e:
            time.sleep(3 + 3 * i); err = e
    raise err
def free(meta):
    lic = (meta.get("LicenseShortName", {}).get("value", "") + " " + meta.get("UsageTerms", {}).get("value", "")).lower()
    return any(k in lic for k in ("public domain", "pd", "cc0", "cc by", "cc-by"))
q, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
credits = []
for line in open(q):
    line = line.strip()
    if not line or "|" not in line: continue
    tag, terms = line.split("|", 1)
    pars = dict(action="query", format="json", generator="search", gsrsearch=terms + " filetype:bitmap",
                gsrnamespace=6, gsrlimit=12, prop="imageinfo", iiprop="url|size|mime|extmetadata", iiurlwidth=1920)
    try:
        d = json.loads(get(API + "?" + urllib.parse.urlencode(pars)))
    except Exception as e:
        print("erro", tag, e); continue
    pages = sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
    n = 0
    for p in pages:
        ii = p.get("imageinfo", [{}])[0]
        meta = ii.get("extmetadata", {})
        if not ii.get("thumburl") or ii.get("width", 0) < 900 or not free(meta): continue
        if ii.get("mime") not in ("image/jpeg", "image/png"): continue
        fn = os.path.join(out, "%s_%d.jpg" % (tag, n))
        try:
            open(fn, "wb").write(get(ii["thumburl"]))
        except Exception as e:
            print("falha", fn, e); continue
        credits.append({"file": fn, "title": p["title"], "license": meta.get("LicenseShortName", {}).get("value", ""),
                        "author": re.sub("<[^>]+>", "", meta.get("Artist", {}).get("value", "")), "url": ii.get("descriptionurl")})
        n += 1
        if n >= 4: break
    print(tag, n, "imagens")
    time.sleep(1)
json.dump(credits, open(os.path.join(out, "credits.json"), "w"), indent=1, ensure_ascii=False)
