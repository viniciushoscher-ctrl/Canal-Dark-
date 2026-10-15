def g_foot(path, grade=True):
    import subprocess, numpy as np
    from PIL import Image
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", "scale=960:540,fps=25,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    n = len(raw) // (960 * 540); fr = np.frombuffer(raw[:n * 960 * 540], np.uint8).reshape(n, 540, 960)
    def fn(u):
        a = fr[min(n - 1, int(u * n))].astype(np.float32) / 255
        a = np.clip((a - 0.5) * 1.35 + 0.52, 0, 1)
        yy, xx = np.mgrid[0:540, 0:960]; v = 1 - 0.55 * (((xx - 480) / 560) ** 2 + ((yy - 270) / 330) ** 2)
        a = np.clip(a * v, 0, 1)
        return Image.fromarray((a * 255).astype(np.uint8)).convert("RGB").resize((1920, 1080), Image.BICUBIC)
    return fn
def _mk_map():
    from PIL import Image
    import numpy as np
    src = Image.open("/home/claude/canal-dark-/video%(N)s-commons/mapa/worldmap_0.jpg").convert("RGB").resize((3840, 1808), Image.LANCZOS)
    a = np.asarray(src).astype(np.int16)
    water = (a[..., 2] > 190) & (a[..., 0] < 140)
    border = (a[..., 0] < 110) & (a[..., 2] < 140) & ~water
    out = np.zeros_like(a, dtype=np.uint8); out[:] = (11, 11, 15)
    out[~water] = (58, 58, 68); out[border] = (22, 22, 28)
    cv = Image.new("RGB", (3840, 2160), (11, 11, 15)); cv.paste(Image.fromarray(out), (0, 176))
    return cv
_MAP = None
def g_map(u, lon=0, lat=0, place1="", place2=""):
    global _MAP
    from PIL import Image, ImageDraw
    if _MAP is None: _MAP = _mk_map()
    px = ((lon + 180) / 360 * 1920 - 8) * 2; py = (2 / 324 * 904 + (83 - lat) * 1.843 / 324 * 904) * 2 + 176
    t = ease(cl((u - 0.06) / 0.66)); s = 1 + 6.5 * t ** 1.15
    cx = 1920 + (px - 1920) * t; cy = 1080 + (py - 1080) * t
    cw, ch = 3840 / s, 2160 / s
    x0 = min(max(cx - cw / 2, 0), 3840 - cw); y0 = min(max(cy - ch / 2, 0), 2160 - ch)
    fr = _MAP.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((1920, 1080), Image.BICUBIC)
    d = ImageDraw.Draw(fr)
    ox = (px - x0) * 1920 / cw; oy = (py - y0) * 1920 / cw
    if u > 0.3:
        k = cl((u - 0.3) / 0.25); r = 10 + 8 * k
        pul = (u * 3) % 1.0
        d.ellipse([ox - r - 60 * pul, oy - r - 60 * pul, ox + r + 60 * pul, oy + r + 60 * pul], outline=(245, 197, 66), width=3)
        d.ellipse([ox - r, oy - r, ox + r, oy + r], fill=(232, 60, 40), outline=(255, 255, 255), width=3)
    from PIL import ImageFont
    f1 = ImageFont.truetype(FB, 40); f2 = ImageFont.truetype(FB, 64); f3 = ImageFont.truetype(FB, 34)
    d.text((110, 620), "BORN IN", font=f1, fill=(245, 197, 66))
    if u > 0.55:
        k = ease(cl((u - 0.55) / 0.2)); xo = int(-40 * (1 - k))
        d.rectangle([110 + xo, 672, 220 + xo, 678], fill=(245, 197, 66))
        d.text((110 + xo, 692), place1, font=f2, fill=(245, 245, 245))
        d.text((110 + xo, 772), place2, font=f3, fill=(200, 200, 200))
    return fr
