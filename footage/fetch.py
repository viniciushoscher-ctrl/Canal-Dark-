import json, os, subprocess, urllib.parse, urllib.request, sys, time
Q = {"steel": "steel mill OR blast furnace OR foundry OR molten", "rail": "railroad OR locomotive OR train", "telegraph": "telegraph OR telegram",
     "city": "Pittsburgh OR New York street 1900", "ship": "steamship OR ocean liner OR harbor", "factory": "factory workers OR machinery OR assembly line",
     "library": "library books reading", "bank": "bank OR Wall Street OR stock exchange", "oil": "oil well OR derrick OR refinery",
     "construction": "skyscraper OR bridge construction", "strike": "strike OR labor union OR picket", "scotland": "Scotland castle OR Scottish village",
     "textile": "textile mill OR cotton OR loom", "money": "money OR coins OR gold"}
def get(u, t=60):
    return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=t).read()
os.makedirs("footage/clips", exist_ok=True); os.makedirs("footage/thumbs", exist_ok=True)
log = []
for key, terms in Q.items():
    q = f"({terms}) AND mediatype:movies AND (collection:prelinger OR collection:opensource_movies OR collection:library_of_congress)"
    u = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode({"q": q, "fl[]": "identifier", "rows": 14, "sort[]": "downloads desc", "output": "json"})
    try: ids = [d["identifier"] for d in json.loads(get(u))["response"]["docs"]]
    except Exception as e: print("busca falhou", key, e); continue
    n = 0
    for ident in ids:
        if n >= 6: break
        try:
            md = json.loads(get(f"https://archive.org/metadata/{ident}"))
            fs = [f for f in md.get("files", []) if f["name"].lower().endswith(".mp4") and 3e6 < int(f.get("size", 0) or 0) < 90e6]
            if not fs: continue
            f = sorted(fs, key=lambda x: int(x["size"]))[0]
            url = f"https://archive.org/download/{ident}/" + urllib.parse.quote(f["name"])
            src = "/tmp/src.mp4"
            subprocess.run(["curl", "-sSL", "--max-time", "240", "-o", src, url], check=True)
            d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src], capture_output=True, text=True).stdout or 0)
            if d < 20: continue
            for j, frac in enumerate((0.2, 0.5, 0.8)):
                out = f"footage/clips/{key}_{ident[:24]}_{j}.mp4"
                subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{d*frac:.1f}", "-t", "7", "-i", src, "-an", "-vf",
                                "scale=960:540:force_original_aspect_ratio=increase,crop=960:540,fps=25", "-c:v", "libx264", "-preset", "veryfast", "-crf", "29", out])
                subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "2", "-i", out, "-frames:v", "1", "-vf", "scale=320:-1", out.replace("clips", "thumbs").replace(".mp4", ".jpg")])
                n += 1; log.append((key, ident, md.get("metadata", {}).get("title", "")))
            print("ok", key, ident, flush=True)
        except Exception as e: print("erro", key, ident, e, flush=True)
json.dump(log, open("footage/log.json", "w"), ensure_ascii=False)
# rerun
