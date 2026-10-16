import sys, glob, os
from PIL import Image, ImageDraw
n = sys.argv[1]; fs = sorted(glob.glob(f"/home/claude/canal-dark-/video{n}-footage-ia/thumbs/*.jpg")); W, H, C = 240, 135, 8
rows = (len(fs) + C - 1) // C; im = Image.new("RGB", (W * C, (H + 14) * rows), "black"); d = ImageDraw.Draw(im)
for i, f in enumerate(fs):
    x, y = (i % C) * W, (i // C) * (H + 14); im.paste(Image.open(f).resize((W, H)), (x, y + 14)); d.text((x + 2, y + 1), os.path.basename(f)[:-4], fill="yellow")
im.save(sys.argv[2])
