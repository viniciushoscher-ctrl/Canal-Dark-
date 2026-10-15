#!/usr/bin/env python3
"""uso: sheet_auto.py N -> /tmp/claude-0/s/aN_k.jpg: fotos usadas (cena + arquivo) para vetar"""
import sys, glob, re, os
from PIL import Image, ImageDraw
N = sys.argv[1]; B = f"/home/claude/video_build{N}"; log = open(B + "/auto_log.txt").read().split("\n")
fs = sorted(glob.glob(B + "/bright/*.jpg")); W, H, cols = 213, 120, 8
for k in range(0, len(fs), 48):
    part = fs[k:k + 48]; rows = (len(part) + cols - 1) // cols
    s = Image.new("RGB", (cols * W, rows * (H + 12)), (15, 15, 15)); d = ImageDraw.Draw(s)
    for i, f in enumerate(part):
        im = Image.open(f).convert("RGB").resize((W, H)); x = (i % cols) * W; y = (i // cols) * (H + 12); s.paste(im, (x, y))
        p = log[k + i].split(" "); d.text((x + 2, y + H), p[0] + " " + (p[2][:14] if p[1] == "foto" else "CART"), fill=(255, 255, 0))
    s.save(f"/tmp/claude-0/s/a{N}_{k // 48}.jpg", quality=78)
print(len(fs))
