#!/usr/bin/env python3
"""Video 1 (Rockefeller): preto e branco nas cenas normais, cor nas reviravoltas."""
import os, time, urllib.parse, urllib.request, pathlib

BW = ("Cinematic historical documentary still, black and white archival photograph, high contrast, "
      "dramatic chiaroscuro lighting, fine film grain, deep shadows, wide 16:9, "
      "no text, no letters, no signs, no logos, no watermark. Scene: ")
COLOR = ("Cinematic documentary still, rich color grading with deep teal shadows and golden amber highlights, "
         "dramatic volumetric light, ultra detailed, epic scale, wide 16:9, "
         "no text, no letters, no signs, no logos, no watermark. Scene: ")
SEED = 7
KEY = os.environ.get("POLLINATIONS_KEY", "")
out = pathlib.Path("imagens"); out.mkdir(exist_ok=True)
rows = [l.strip().split("|", 1) for l in open("scenes.txt", encoding="utf-8") if "|" in l]
rows = rows[:int(os.environ.get("MAX_IMAGENS", "9999"))]

for i, (mode, scene) in enumerate(rows, 1):
    f = out / f"{i:03d}_{mode.lower()}.jpg"
    if f.exists() and f.stat().st_size > 10000:
        continue
    prompt = (COLOR if mode.strip() == "COLOR" else BW) + scene
    url = ("https://image.pollinations.ai/prompt/" + urllib.parse.quote(prompt) +
           f"?width=1280&height=720&model=flux&nologo=true&seed={SEED}")
    if KEY: url += "&key=" + KEY
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            f.write_bytes(urllib.request.urlopen(req, timeout=120).read()); print("ok", f.name); break
        except Exception as e:
            print("erro", f.name, e, "- tentando de novo"); time.sleep(15)
    time.sleep(8)
print("Pronto:", len(list(out.glob('*.jpg'))), "imagens")
