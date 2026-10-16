import sys, json, os, time, subprocess, urllib.parse, urllib.request
UA = {"User-Agent": "CanalDarkBot/1.0 (educational documentary; github.com/viniciushoscher-ctrl/Canal-Dark-)"}
def get(url, tmo=60):
    err = None
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=tmo).read()
        except Exception as e: err = e; time.sleep(3 + 3 * i)
    raise err
out = sys.argv[2]; os.makedirs(out + "/clips", exist_ok=True); os.makedirs(out + "/thumbs", exist_ok=True); log = []
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.strip()
    if "|" not in line or line.startswith("#"): continue
    tag, q = line.split("|", 1)
    try:
        d = json.loads(get("https://archive.org/advancedsearch.php?" + urllib.parse.urlencode({"q": "(%s) AND mediatype:movies AND collection:prelinger" % q, "fl[]": ["identifier", "title", "year"], "rows": 4, "sort[]": "downloads desc", "output": "json"}, doseq=True)))["response"]["docs"]
    except Exception as e: print("erro busca", tag, e); continue
    n = 0
    for doc in d:
        try:
            md = json.loads(get("https://archive.org/metadata/" + doc["identifier"]))
            fs = [f for f in md.get("files", []) if f["name"].lower().endswith(".mp4") and int(f.get("size", 0) or 0) > 0]
            if not fs: continue
            f = min(fs, key=lambda f: int(f["size"]))
            url = "https://archive.org/download/%s/%s" % (doc["identifier"], urllib.parse.quote(f["name"]))
            dur = float(f.get("length") or md.get("metadata", {}).get("runtime", 0) or 0)
            if dur < 20: dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", url], capture_output=True, text=True, timeout=90).stdout.strip() or 0)
        except Exception as e: print("falha meta", doc.get("identifier"), e); continue
        if dur < 30: continue
        ok = 0
        for j, fr in enumerate((0.2, 0.5, 0.78)):
            fn = "%s/clips/%s_%d_%d.mp4" % (out, tag, n, j)
            try:
                subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "%.1f" % (dur * fr), "-i", url, "-t", "6.5", "-an", "-vf", "scale=960:540:force_original_aspect_ratio=decrease,pad=960:540:(ow-iw)/2:(oh-ih)/2,fps=25,format=yuv420p", "-c:v", "libx264", "-crf", "27", "-preset", "veryfast", fn], timeout=180)
                subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "2", "-i", fn, "-frames:v", "1", "-vf", "scale=320:180", "%s/thumbs/%s_%d_%d.jpg" % (out, tag, n, j)])
                ok += 1
            except Exception as e: print("falha corte", fn, e)
        log.append(dict(tag=tag, id=doc["identifier"], title=doc.get("title"), year=doc.get("year"), dur=dur, lic="Prelinger Archives (public domain)", url="https://archive.org/details/" + doc["identifier"]))
        print(tag, doc.get("title"), round(dur), "s", ok); n += 1
        if n >= 3: break
json.dump(log, open(out + "/log.json", "w"), indent=1)
