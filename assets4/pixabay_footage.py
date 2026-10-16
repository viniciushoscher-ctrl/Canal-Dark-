import sys, json, os, time, subprocess, urllib.parse, urllib.request
KEY = os.environ.get("PIXABAY_API_KEY", "")
if not KEY: sys.exit("sem PIXABAY_API_KEY")
def get(url, tmo=60, raw=False):
    err = None
    for i in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "CanalDarkBot/1.0"}), timeout=tmo).read()
            return r if raw else json.loads(r)
        except Exception as e: err = e; time.sleep(3 + 3 * i)
    raise Exception(str(err).replace(KEY, "***"))
out = sys.argv[2]; os.makedirs(out + "/clips", exist_ok=True); os.makedirs(out + "/thumbs", exist_ok=True); log = []
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.strip()
    if "|" not in line or line.startswith("#"): continue
    tag, q = line.split("|", 1)
    try: d = get("https://pixabay.com/api/videos/?" + urllib.parse.urlencode(dict(key=KEY, q=q, per_page=6, safesearch="true")))
    except Exception as e: print("erro busca", tag, e); continue
    n = 0
    for h in d.get("hits", []):
        v = h["videos"].get("small") or h["videos"].get("tiny")
        if not v or not v.get("url") or h.get("duration", 0) < 5: continue
        fn = "%s/clips/%s_%d_0.mp4" % (out, tag, n); raw = "/tmp/px_%s_%d.mp4" % (tag, n)
        try:
            open(raw, "wb").write(get(v["url"], 120, True))
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "0.5", "-i", raw, "-t", "6.5", "-an", "-vf", "scale=960:540:force_original_aspect_ratio=decrease,pad=960:540:(ow-iw)/2:(oh-ih)/2,fps=25,format=yuv420p", "-c:v", "libx264", "-crf", "27", "-preset", "veryfast", fn], timeout=120)
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "2", "-i", fn, "-frames:v", "1", "-vf", "scale=320:180", "%s/thumbs/%s_%d_0.jpg" % (out, tag, n)])
        except Exception as e: print("falha", tag, str(e).replace(KEY, "***")); continue
        os.remove(raw)
        log.append(dict(tag=tag, id=h["id"], tags=h.get("tags"), url=h.get("pageURL"), lic="Pixabay Content License")); n += 1
        if n >= 3: break
    print(tag, n)
    time.sleep(1.5)
json.dump(log, open(out + "/log.json", "w"), indent=1)
