#!/usr/bin/env python3
"""uso: prep_plan.py N  -> video_buildN/bright/NNN_real.jpg + 9NN_hook.jpg + plan_counts.txt a partir de videoN-imagens/plan.txt
plan.txt: secoes '# hookmontage' (ate ~14 imagens, pode repetir), '# hook', '# cap1'..., uma imagem por linha:
  chave[@x,y,z]   chave = nome do arquivo sem extensao (qualquer pasta de videoN-commons) ; @x,y,z = recorte (centro em fracoes, z = zoom) para detalhes de mapas/pinturas"""
import sys, os, re, glob
from PIL import Image, ImageOps, ImageFilter, ImageStat
import numpy as np
N = sys.argv[1]; R = "/home/claude/canal-dark-"; B = f"/home/claude/video_build{N}"; dst = B + "/bright"
os.makedirs(dst, exist_ok=True)
for f in glob.glob(dst + "/*.jpg"): os.remove(f)
src2 = open(R + "/pipeline/gen/prepgen.py", encoding="utf-8").read(); ns = {}
exec("import numpy as np\nfrom PIL import Image, ImageOps, ImageFilter, ImageStat\n" + src2[src2.index("def fit"):src2.index("for f in sorted(glob.glob(src")], ns)
fit, bright = ns["fit"], ns["bright"]
names = re.findall(r"^### (\S+)", open(R + f"/video{N}-narracao/roteiro.txt", encoding="utf-8").read(), re.M)
sec = {}; cur = None
for l in open(R + f"/video{N}-imagens/plan.txt", encoding="utf-8"):
    l = l.split("//")[0].strip()
    if not l: continue
    if l.startswith("#"): cur = l[1:].strip(); sec[cur] = []; continue
    sec[cur].append(l.split()[0])
idx = {}
for d in ("wiki", "people", "f", "fotos", "mapa", "logos"):
    for p in sorted(glob.glob(R + f"/video{N}-commons/{d}/*")):
        if p.lower().endswith((".jpg", ".jpeg", ".png")): idx.setdefault(os.path.splitext(os.path.basename(p))[0], p); idx.setdefault(d + "/" + os.path.splitext(os.path.basename(p))[0], p)
def load(key):
    m = re.match(r"([^@]+)(?:@([\d.]+),([\d.]+),([\d.]+))?$", key); k = m.group(1)
    if k not in idx: print("!! falta", k); return None
    im = Image.open(idx[k]).convert("RGB")
    if m.group(2):
        cx, cy, z = float(m.group(2)), float(m.group(3)), float(m.group(4)); w, h = im.width / z, im.height / z
        x0 = min(max(cx * im.width - w / 2, 0), im.width - w); y0 = min(max(cy * im.height - h / 2, 0), im.height - h)
        im = im.crop((int(x0), int(y0), int(x0 + w), int(y0 + h)))
    im.thumbnail((2600, 2600)); return bright(fit(ImageOps.autocontrast(im, cutoff=0.3)))
counts = []; n = 0
for j, nm in enumerate(names):
    key = "hook" if j == 0 else nm.split("_", 1)[1] if nm.split("_", 1)[1] in sec else nm
    items = sec.get(key) or sec.get(nm) or []
    c = 0
    for it in items:
        im = load(it)
        if im is None: continue
        n += 1; c += 1; im.save(dst + f"/{n:03d}_real.jpg", quality=93)
    counts.append(max(c, 1)); print(nm, c)
for i, it in enumerate(sec.get("hookmontage", [])):
    im = load(it)
    if im is not None: im.save(dst + f"/9{i:02d}_hook.jpg", quality=93)
open(B + "/plan_counts.txt", "w").write(" ".join(map(str, counts)))
print("total", n, "hook", len(sec.get("hookmontage", [])))
