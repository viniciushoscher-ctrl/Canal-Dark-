# graficos animados do Video 5 (Henry Ford)
def g_time(u):
    g = G(); g.head("HIGHLAND PARK · 1913", "THE MOVING LINE", "time to build one chassis")
    t = ease(cl((u - 0.1) / 0.65))
    for x, v, lab, col, val in [(330, 1.0, "BEFORE", GREY, "12.5 HOURS"), (730, 93 / 750, "AFTER", GOLDc, "93 MINUTES")]:
        hh = 250 * (1 - (1 - v) * t) if x > 500 else 250
        g.rect(x, 530 - hh, x + 240, 530, col); g.text(x + 120, 546, lab, 24, W_, anchor="ma"); g.text(x + 120, 530 - hh - 54, val, 36, W_, anchor="ma")
    return g.out()
def g_price(u):
    g = G(); g.head("THE MODEL T", "THE PRICE KEPT FALLING", "price of a new Model T")
    pts = [(1908, 850), (1910, 780), (1912, 600), (1914, 490), (1916, 360), (1920, 440), (1923, 295), (1925, 260)]
    p = ease(cl((u - 0.1) / 0.7)); n = p * (len(pts) - 1)
    def xy(i): return (170 + 940 * (pts[i][0] - 1908) / 17, 520 - 290 * (pts[i][1] - 200) / 700)
    for i in range(len(pts) - 1):
        if i + 1 <= n + 1e-6:
            g.line([xy(i), xy(i + 1)], GOLDc, 6)
        elif i < n:
            a = xy(i); b = xy(i + 1); f = n - i; g.line([a, (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f)], GOLDc, 6)
    k = min(len(pts) - 1, int(n + 0.001)); x, y = xy(k)
    g.circ(x, y, 12, REDc); g.text(x, y - 40, "$%d" % pts[k][1], 44, W_, anchor="ms"); g.text(x, 560, str(pts[k][0]), 24, (190, 190, 190), anchor="ma")
    return g.out()
def g_wage5(u):
    g = G(); g.head("JANUARY 5, 1914", "THE FIVE-DOLLAR DAY", "daily wage, before and after")
    t = ease(cl((u - 0.1) / 0.6))
    for x, v, lab, col, val in [(330, 2.34, "BEFORE", GREY, "$2.34"), (730, 2.34 + 2.66 * t, "AFTER", GOLDc, "$5.00")]:
        hh = 240 * v / 5.0; g.rect(x, 530 - hh, x + 220, 530, col); g.text(x + 110, 546, lab, 24, W_, anchor="ma")
        g.text(x + 110, 530 - hh - 56, ("$%.2f" % v) if x > 500 else val, 44, W_, anchor="ma")
    return g.out()
def g_share(u):
    g = G(); g.head("THE EARLY 1920s", "HALF THE CARS ON EARTH", "were Fords")
    t = ease(cl((u - 0.1) / 0.6)); import math
    cx, cy, r = 640, 440, 150
    g.circ(cx, cy, r, GREY)
    pts = [(cx, cy)]; a0 = -math.pi / 2
    for i in range(61):
        a = a0 + math.pi * t * i / 60 * 1.0; pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    g.d.polygon([(x * SS, y * SS) for x, y in pts], fill=GOLDc)
    g.text(cx, cy + r + 20, "~50%", 60, W_, anchor="ma")
    return g.out()
def g_bomber(u):
    g = G(); g.head("WILLOW RUN · 1944", "ONE BOMBER EVERY HOUR", "B-24 Liberator production at its peak")
    n = int(ease(cl((u - 0.1) / 0.7)) * 24)
    for i in range(24):
        x = 120 + (i % 12) * 88; y = 330 + (i // 12) * 120
        g.rect(x, y, x + 60, y + 12, GOLDc if i < n else GREY); g.rect(x + 24, y - 24, x + 36, y + 36, GOLDc if i < n else GREY)
    g.text(640, 590, "%d BOMBERS" % n, 60, W_, anchor="ma")
    return g.out()
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
    src = Image.open("/home/claude/canal-dark-/video5-commons/mapa/worldmap_0.jpg").convert("RGB").resize((3840, 1808), Image.LANCZOS)
    a = np.asarray(src).astype(np.int16)
    water = (a[..., 2] > 190) & (a[..., 0] < 140)
    border = (a[..., 0] < 110) & (a[..., 2] < 140) & ~water
    out = np.zeros_like(a, dtype=np.uint8); out[:] = (11, 11, 15)
    out[~water] = (58, 58, 68); out[border] = (22, 22, 28)
    cv = Image.new("RGB", (3840, 2160), (11, 11, 15)); cv.paste(Image.fromarray(out), (0, 176))
    return cv
_MAP = None
def g_map(u, lon=-83.25, lat=42.35, place1="GREENFIELD TOWNSHIP, MICHIGAN", place2="UNITED STATES  ·  1863"):
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
MAPBRT = [("henry ford was born on july", g_map, 7.0)]
