import sys, json, os, re, time, urllib.parse, urllib.request
UA = {"User-Agent": "CanalDarkBot/1.0 (educational documentary; contact viniciushoscher@gmail.com)"}
def get(u):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
        except Exception as e: time.sleep(4); err = e
    raise err
out = sys.argv[2]; os.makedirs(out, exist_ok=True); cred = []
for line in open(sys.argv[1]):
    if "|" not in line: continue
    tag, q = line.strip().split("|", 1)
    d = json.loads(get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(dict(action="query", format="json", generator="search", gsrsearch=q, gsrnamespace=6, gsrlimit=8, prop="imageinfo", iiprop="url|mime|extmetadata", iiurlwidth=1000))))
    n = 0
    for p in sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99)):
        ii = p.get("imageinfo", [{}])[0]
        if not ii.get("thumburl"): continue
        fn = "%s/%s_%d.png" % (out, tag, n)
        try: open(fn, "wb").write(get(ii["thumburl"]))
        except Exception as e: print("falha", e); continue
        ex = ii.get("extmetadata", {})
        cred.append(dict(file=fn, title=p["title"], license=ex.get("LicenseShortName", {}).get("value", ""))); print(fn, p["title"], cred[-1]["license"]); n += 1
        if n >= 4: break
json.dump(cred, open(out + "/credits.json", "w"), indent=1)
