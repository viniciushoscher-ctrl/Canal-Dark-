#!/usr/bin/env python3
"""uso: thumb.py N "WHITE L1|WHITE L2" "RED L1|RED L2" portrait.jpg logo.png [size_white=130] [size_red=120]"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"; R = "/home/claude/canal-dark-"
N, wl, rl, por, logo = sys.argv[1:6]; sw = int(sys.argv[6]) if len(sys.argv) > 6 else 130; sr = int(sys.argv[7]) if len(sys.argv) > 7 else 120
im = Image.open(R + "/video4-thumb/Thumbnail_Video4.png").convert("RGB"); d = ImageDraw.Draw(im); bgc = (10, 10, 10)
d.rectangle([84, 30, 668, 612], fill=bgc); d.rectangle([668, 0, 1280, 720], fill=bgc)
def txt(lines, y, col, size, step):
    f = ImageFont.truetype(FB, size)
    for ln in lines:
        w = int(d.textlength(ln, font=f)); t = Image.new("RGBA", (w + 20, size + 40), (0, 0, 0, 0)); ImageDraw.Draw(t).text((10, 0), ln, font=f, fill=col)
        sx = min(0.60, 560 / (w + 20)); t = t.resize((int((w + 20) * sx), size + 40), Image.LANCZOS); im.paste(t, (92, y), t); y += step
txt(wl.split("|"), 55, (245, 245, 245), sw, int(sw * 1.02)); txt(rl.split("|"), 55 + len(wl.split("|")) * int(sw * 1.02) + 18, (232, 35, 14), sr, int(sr * 0.98))
p = Image.open(R + "/" + por).convert("L"); w, h = p.size; ch = int(w * 608 / 626)
if ch > h: cw = int(h * 626 / 608); p = p.crop(((w - cw) // 2, 0, (w - cw) // 2 + cw, h))
else: p = p.crop((0, 0, w, ch))
p = ImageOps.autocontrast(p.resize((626, 608), Image.LANCZOS), cutoff=0.5).convert("RGB")
m = Image.new("L", (626, 608), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, 625, 607], 40, fill=255); im.paste(p, (672, 112), m)
lg = Image.open(R + "/" + logo).convert("RGBA"); lg = lg.crop(lg.getbbox()); lg.thumbnail((420, 110))
pl = Image.new("RGB", (lg.width + 36, lg.height + 20), (245, 245, 245)); pl.paste(lg, (18, 10), lg); im.paste(pl, (820 + (420 - pl.width) // 2, 10))
import os; os.makedirs(R + f"/video{N}-thumb", exist_ok=True); im.save(R + f"/video{N}-thumb/Thumbnail_Video{N}.png")
