import sys, json, os, re, time, subprocess, urllib.parse, urllib.request
UA = {"User-Agent": "CanalDarkBot/1.0 (educational documentary; contact github.com/viniciushoscher-ctrl/Canal-Dark-)"}
def get(url, tmo=120):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=tmo).read()
        except Exception as e: time.sleep(4 + 4 * i); err = e
    raise err
out = sys.argv[2]; os.makedirs(out + "/clips", exist_ok=True); os.makedirs(out + "/thumbs", exist_ok=True); log = []
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.strip()
    if "|" not in line: continue
    tag, q = line.split("|", 1)
    try:
        d = json.loads(get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(dict(action="query", format="json", generator="search", gsrsearch=q + " filetype:video", gsrnamespace=6, gsrlimit=10, prop="imageinfo", iiprop="url|size|mime|extmetadata"))))
    except Exception as e: print("erro busca", tag, e); continue
    n = 0
    for p in sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99)):
        ii = p.get("imageinfo", [{}])[0]; ex = ii.get("extmetadata", {})
        lic = (ex.get("LicenseShortName", {}).get("value", "") + " " + ex.get("UsageTerms", {}).get("value", "")).lower()
        if not any(k in lic for k in ("public domain", "pd", "cc0", "cc by")): continue
        if ii.get("size", 0) > 120e6 or not ii.get("url"): continue
        raw = "/tmp/raw_%s_%d" % (tag, n)
        try: open(raw, "wb").write(get(ii["url"], 300))
        except Exception as e: print("falha", p["title"], e); continue
        try:
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", raw], capture_output=True, text=True).stdout.strip() or 0)
        except Exception: dur = 0
        if dur < 4: os.remove(raw); continue
        k = 3 if dur > 24 else (2 if dur > 12 else 1)
        for j in range(k):
            ss = 1 + (dur - 8) * j / max(1, k - 1) if dur > 9 else 0
            fn = "%s/clips/%s_%d_%d.mp4" % (out, tag, n, j)
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "%.2f" % ss, "-i", raw, "-t", "6.5", "-an", "-vf", "scale=960:540:force_original_aspect_ratio=decrease,pad=960:540:(ow-iw)/2:(oh-ih)/2,fps=25,format=yuv420p", "-c:v", "libx264", "-crf", "27", "-preset", "veryfast", fn])
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "2", "-i", fn, "-frames:v", "1", "-vf", "scale=320:180", "%s/thumbs/%s_%d_%d.jpg" % (out, tag, n, j)])
        log.append(dict(tag=tag, title=p["title"], dur=dur, lic=ex.get("LicenseShortName", {}).get("value", ""))); os.remove(raw); n += 1
        print(tag, p["title"], round(dur), "s"); 
        if n >= 3: break
json.dump(log, open(out + "/log.json", "w"), indent=1)
