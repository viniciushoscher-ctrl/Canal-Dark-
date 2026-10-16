import sys, glob, os
from PIL import Image, ImageDraw
n = sys.argv[1]; fs = sorted(glob.glob(f"/home/claude/canal-dark-/video{n}-commons/people/*.jpg") + glob.glob(f"/home/claude/canal-dark-/video{n}-commons/fotos/*.jpg") + glob.glob(f"/home/claude/canal-dark-/video{n}-commons/f/*.jpg"))
W, H, C = 240, 135, 8; rows = (len(fs) + C - 1) // C; im = Image.new("RGB", (W * C, (H + 14) * rows), "black"); d = ImageDraw.Draw(im)
for i, f in enumerate(fs):
    x, y = (i % C) * W, (i // C) * (H + 14)
    try:
        t = Image.open(f).convert("RGB"); t.thumbnail((W, H)); im.paste(t, (x, y + 14))
    except Exception: pass
    d.text((x + 2, y + 1), os.path.basename(f)[:-4][:30], fill="yellow")
im.save(sys.argv[2]); print(len(fs))
