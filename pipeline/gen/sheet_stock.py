import sys, glob, os
from PIL import Image, ImageDraw
n = sys.argv[1]; tags = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
fs = []
for d in ("footage-ia", "footage-px"):
    for f in sorted(glob.glob(f"/home/claude/canal-dark-/video{n}-{d}/thumbs/*.jpg")):
        b = os.path.basename(f)[:-4]; t = b.split("_")[0]
        if b.endswith("_1") or b.endswith("_2"):
            if d == "footage-ia": continue
        if tags and t not in tags: continue
        fs.append((f, ("P:" if d.endswith("px") else "I:") + b))
W, H, C = 240, 135, 8; rows = (len(fs) + C - 1) // C; im = Image.new("RGB", (W * C, (H + 14) * rows), "black"); d = ImageDraw.Draw(im)
for i, (f, lab) in enumerate(fs):
    x, y = (i % C) * W, (i // C) * (H + 14); im.paste(Image.open(f).resize((W, H)), (x, y + 14)); d.text((x + 2, y + 1), lab, fill="yellow")
im.save(sys.argv[2]); print(len(fs))
