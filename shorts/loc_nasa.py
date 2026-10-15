import sys, json, os, re, time, urllib.parse, urllib.request
# uso: loc_nasa.py queries.txt outdir -> fotos da Library of Congress (sem restricao conhecida) e NASA; sem chave
UA = {"User-Agent": "CanalDarkBot/1.0 (educational documentary; github.com/viniciushoscher-ctrl/Canal-Dark-)"}
def get(url):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
        except Exception as e: time.sleep(2 + 2 * i); err = e
    raise err
q, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True); credits = []
def save(tag, n, url, rec):
    fn = os.path.join(out, "%s_%d.jpg" % (tag, n)); open(fn, "wb").write(get(url)); rec["file"] = fn; credits.append(rec)
def loc(tag, terms):
    words = re.findall(r"[a-z]{4,}", terms.lower()); n = 0
    d = json.loads(get("https://www.loc.gov/photos/?" + urllib.parse.urlencode({"q": terms, "fo": "json", "c": 12})))
    for r in d.get("results", []):
        title = r.get("title", ""); rights = " ".join(r.get("item", {}).get("rights", []) if isinstance(r.get("item", {}).get("rights"), list) else [str(r.get("item", {}).get("rights", ""))]).lower() + " " + str(r.get("rights_information", "")).lower()
        imgs = [u for u in r.get("image_url", []) if u.lower().endswith((".jpg", ".jpeg"))]
        if not imgs or not any(w in title.lower() for w in words): continue
        if not re.search(r"no known restrictions|public domain|unrestricted|no restrictions", rights) and rights.strip(): continue
        url = imgs[-1] if imgs[-1].startswith("http") else "https:" + imgs[-1]
        try: save(tag, n, url, {"query": terms, "title": title, "license": "LoC: " + (rights.strip()[:80] or "no known restrictions listed"), "url": r.get("id", "")}); n += 1
        except Exception: continue
        if n >= 2: break
def nasa(tag, terms):
    words = re.findall(r"[a-z]{4,}", terms.lower()); n = 0
    d = json.loads(get("https://images-api.nasa.gov/search?" + urllib.parse.urlencode({"q": terms, "media_type": "image"})))
    for it in d.get("collection", {}).get("items", [])[:10]:
        data = it["data"][0]; title = data.get("title", "")
        if not any(w in title.lower() for w in words) or not it.get("links"): continue
        try: save(tag, n, it["links"][0]["href"], {"query": terms, "title": title, "license": "NASA (public domain)", "url": "https://images.nasa.gov/details/" + data.get("nasa_id", "")}); n += 1
        except Exception: continue
        if n >= 1: break
for line in open(q, encoding="utf-8"):
    line = line.strip()
    if "|" not in line: continue
    tag, terms = line.split("|", 1)
    for fn in (loc, nasa if re.search(r"nasa|rocket|space|moon|shepard|apollo", terms.lower()) else None):
        if not fn: continue
        try: fn(tag, terms)
        except Exception as e: print("ERRO", tag, repr(e)[:150], flush=True)
    json.dump(credits, open(os.path.join(out, "credits.json"), "w"), indent=1, ensure_ascii=False); time.sleep(0.5)
print("ok", len(credits))
