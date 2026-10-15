#!/usr/bin/env python3
"""uso: python3 prep_curated.py N map.txt -> bright/NNN_real.jpg. map.txt: 'cena|arquivo' (relativo a videoN-commons ou videoN-footage/thumbs) ou 'cena|PLATE|ano|titulo|linha2'. So midia publica."""
import sys, os, glob
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter
import numpy as np
N = sys.argv[1]; R = "/home/claude/canal-dark-"; dst = f"/home/claude/video_build{N}/bright"; os.makedirs(dst, exist_ok=True)
for f in glob.glob(dst + "/*.jpg"): os.remove(f)
src = open(R + "/pipeline/gen/prepgen.py", encoding="utf-8").read(); ns = {}
exec("import numpy as np\nfrom PIL import Image, ImageOps, ImageFilter, ImageStat\n" + src[src.index("def fit"):src.index("for f in sorted(glob.glob(src")], ns)
fit, bright = ns["fit"], ns["bright"]
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"; FI = "/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf"
def plate(year, t1, t2):
    rng = np.random.default_rng(abs(hash(t1)) % 9999); a = np.linspace(28, 12, 720)[:, None] * np.ones((720, 1280)) + rng.normal(0, 3, (720, 1280))
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGB"); d = ImageDraw.Draw(im)
    d.text((640, 300), year, font=ImageFont.truetype(FB, 36), fill=(245, 197, 66), anchor="mm")
    d.line((590, 330, 690, 330), fill=(245, 197, 66), width=3)
    d.text((640, 385), t1, font=ImageFont.truetype(FB, 46), fill=(240, 240, 240), anchor="mm")
    d.text((640, 450), t2, font=ImageFont.truetype(FI, 30), fill=(190, 190, 190), anchor="mm")
    return im
n = 0
for l in open(sys.argv[2], encoding="utf-8"):
    p = l.rstrip("\n").split("|")
    if len(p) < 2 or not p[0].strip().isdigit(): continue
    i = int(p[0])
    if p[1] == "PLATE": im = plate(p[2], p[3], p[4] if len(p) > 4 else "")
    else:
        f = R + f"/video{N}-commons/{p[1]}"
        if not os.path.exists(f): f = R + f"/video{N}-footage/thumbs/{p[1]}"
        im = fit(ImageOps.autocontrast(Image.open(f).convert("RGB"), cutoff=0.3))
    bright(im).save(dst + f"/{i:03d}_real.jpg", quality=93); n += 1
print("cenas", n)
