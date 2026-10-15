#!/usr/bin/env python3
"""uso: python3 prep_public.py N cfg.py -> /home/claude/video_buildN/bright so com fotos publicas (Commons), sem imagens de IA"""
import sys, glob, os, re, json
from PIL import Image, ImageOps, ImageFilter, ImageStat
import numpy as np
N = sys.argv[1]; R = "/home/claude/canal-dark-"; dst = f"/home/claude/video_build{N}/bright"; os.makedirs(dst, exist_ok=True)
for f in glob.glob(dst + "/*.jpg"): os.remove(f)
src_py = open(R + "/pipeline/gen/prepgen.py", encoding="utf-8").read()
ns = {}; exec("import numpy as np\nfrom PIL import Image, ImageOps, ImageFilter, ImageStat\n" + src_py[src_py.index("def fit"):src_py.index("for f in sorted(glob.glob(src")], ns)
fit, bright = ns["fit"], ns["bright"]
sc = [l.split("|", 1)[1].strip() for l in open(R + f"/video{N}-imagens/scenes.txt", encoding="utf-8") if "|" in l]
cred = json.load(open(R + f"/video{N}-commons/fotos/credits.json"))
pool = [(c["file"].replace("video%s-commons/fotos/" % N, ""), set(re.findall(r"[a-z]{4,}", c["title"].lower()))) for c in cred]
ppl = sorted(glob.glob(R + f"/video{N}-commons/people/*.jpg")) + sorted(glob.glob(R + f"/video{N}-commons/people/*.png"))
files = {n: R + f"/video{N}-commons/fotos/{n}" for n, _ in pool if os.path.exists(R + f"/video{N}-commons/fotos/{n}")}
pool = [(n, w) for n, w in pool if n in files]
used = set(); out = {}
for i, t in enumerate(sc, 1):
    words = set(re.findall(r"[a-z]{4,}", t.lower())); best = None; bs = -1
    for n, w in pool:
        if n in used: continue
        s = len(words & w)
        if s > bs: bs = s; best = n
    if best is None: used.clear(); best = pool[(i * 7) % len(pool)][0]
    used.add(best); out[i] = files[best]
for i, p in out.items(): bright(fit(ImageOps.autocontrast(Image.open(p).convert("RGB"), cutoff=0.3))).save(dst + f"/{i:03d}_real.jpg", quality=93)
print("publicas", len(out), "de", len(sc), "pool", len(pool))
