import sys, json, os, re, time, urllib.parse, urllib.request
# uso: commons2.py queries.txt outdir  (linhas "tag|termos"); filtra por relevancia do titulo
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "CanalDarkBot/1.0 (educational documentary; github.com/viniciushoscher-ctrl/Canal-Dark-)"}
def get(url):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
        except Exception as e: time.sleep(2 + 2 * i); err = e
    raise err
def free(meta):
    lic = (meta.get("LicenseShortName", {}).get("value", "") + " " + meta.get("UsageTerms", {}).get("value", "")).lower()
    return any(k in lic for k in ("public domain", "pd", "cc0", "cc by", "cc-by"))
BAD = re.compile(r"\b(coin|stamp|logo|svg|map of|diagram|poster|cartoon|drawing|painting|screenshot)\b", re.I)
q, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True); credits = []
for line in open(q, encoding="utf-8"):
    line = line.strip()
    if "|" not in line: continue
    tag, terms = line.split("|", 1)
    words = [w for w in re.findall(r"[a-z]{4,}", terms.lower())]
    pars = dict(action="query", format="json", generator="search", gsrsearch=terms + " filetype:bitmap", gsrnamespace=6, gsrlimit=20,
                prop="imageinfo", iiprop="url|size|mime|extmetadata", iiurlwidth=1600)
    try: d = json.loads(get(API + "?" + urllib.parse.urlencode(pars)))
    except Exception as e: print("erro", tag, e); continue
    pages = sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99)); n = 0
    for p in pages:
        ii = p.get("imageinfo", [{}])[0]; meta = ii.get("extmetadata", {}); title = p["title"]
        if not ii.get("thumburl") or ii.get("width", 0) < 900 or not free(meta) or ii.get("mime") not in ("image/jpeg", "image/png") or BAD.search(title): continue
        if words and not any(w in title.lower() for w in words): continue
        fn = os.path.join(out, "%s_%d.jpg" % (tag, n))
        try: open(fn, "wb").write(get(ii["thumburl"]))
        except Exception as e: print("falha", fn); continue
        credits.append({"file": fn, "query": terms, "title": title, "license": meta.get("LicenseShortName", {}).get("value", ""), "url": ii.get("descriptionurl")}); n += 1
        if n >= 3: break
    print(tag, terms, n, flush=True); time.sleep(0.4)
json.dump(credits, open(os.path.join(out, "credits.json"), "w"), indent=1, ensure_ascii=False)
