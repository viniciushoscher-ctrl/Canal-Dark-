#!/usr/bin/env python3
"""uso: python3 prepgen.py N cfg.py  (usa secao #--KW: dict palavra-da-cena -> arquivo commons)"""
import sys, glob, os, re
from PIL import Image, ImageOps, ImageFilter, ImageStat
import numpy as np
N = sys.argv[1]; cfg = open(sys.argv[2], encoding="utf-8").read()
KW = eval(re.search(r"#--KW\n(.*?)(?=#--\w+\n|\Z)", cfg, re.S).group(1))
R = "/home/claude/canal-dark-"; src = R + f"/video{N}-imagens/imagens"; dst = f"/home/claude/video_build{N}/bright"; os.makedirs(dst, exist_ok=True)
def fit(im):
    W, H = 1280, 720; r = im.width / im.height
    if abs(r - 16 / 9) < 0.25:
        s = max(W / im.width, H / im.height); im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
        x = (im.width - W) // 2; y = (im.height - H) // 2; return im.crop((x, y, x + W, y + H))
    s = max(W / im.width, H / im.height); bg = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.BICUBIC)
    x = (bg.width - W) // 2; y = (bg.height - H) // 2; bg = bg.crop((x, y, x + W, y + H)).filter(ImageFilter.GaussianBlur(40))
    bg = Image.eval(bg, lambda v: int(v * 0.35)); fs = min(H / im.height, W / im.width) * 0.96
    fg = im.resize((int(im.width * fs), int(im.height * fs)), Image.LANCZOS); bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2)); return bg
def bright(im):
    im = ImageOps.autocontrast(im, cutoff=0.4); l = ImageStat.Stat(im.convert("L")).mean[0] / 255
    if 0.02 < l < 0.40:
        g = np.log(0.40) / np.log(l); a = np.asarray(im).astype(np.float32) / 255; im = Image.fromarray((np.clip(a ** g, 0, 1) * 255).astype(np.uint8))
    return im
for f in sorted(glob.glob(src + "/*.jpg")): bright(Image.open(f).convert("RGB")).save(dst + "/" + os.path.basename(f), quality=93)
sc = [l.split("|", 1)[1] for l in open(R + f"/video{N}-imagens/scenes.txt", encoding="utf-8") if "|" in l]; used = set(); n = 0
for key, nm in KW.items():
    for i, t in enumerate(sc, 1):
        if t.startswith(key) and i not in used:
            p = glob.glob(R + f"/video{N}-commons/fotos/{nm}.*")
            if p: fit(ImageOps.autocontrast(Image.open(p[0]).convert("RGB"), cutoff=0.3)).save(dst + f"/{i:03d}_real.jpg", quality=93); used.add(i); n += 1
            break
print("reais", n)
