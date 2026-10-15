# graficos animados do Video 4 (J.P. Morgan); usa G, ease, cl, GOLDc, W_, GREY, REDc, money de part3_graphics
def g_rate(u):
    g = G(); g.head("OCTOBER 1907", "100% INTEREST", "emergency loans, in the middle of the panic")
    t = ease(cl((u - 0.08) / 0.7)); v = 6 + 94 * t
    g.text(640, 460, "%d%%" % round(v), 190, REDc if t > 0.85 else W_, anchor="mm")
    g.rect(190, 560, 1090, 570, (30, 30, 36)); g.rect(190, 560, 190 + 900 * t, 570, REDc)
    g.text(190, 582, "NORMAL RATES", 24, (180, 180, 180)); g.text(1090, 582, "PANIC", 24, (180, 180, 180), anchor="ra")
    return g.out()
def g_gold(u):
    g = G(); g.head("1895 · THE GOLD CRISIS", "THE TREASURY IS EMPTYING", "reserve against the safe level")
    for x, v, lab, col, val in [(330, 1.0, "SAFE LEVEL", GREY, "$100M"), (730, 0.09, "ACTUAL RESERVE", REDc, "~$9M")]:
        h = 250 * v * ease(cl((u - 0.1) / 0.65)); g.rect(x, 530 - h, x + 220, 530, col)
        g.text(x + 110, 546, lab, 22, W_, anchor="ma")
        if h > 14: g.text(x + 110, 530 - h - 56, val, 44, W_, anchor="ma")
    return g.out()
def g_deal(u):
    g = G(); g.head("1901 · A SLIP OF PAPER", "THE PRICE OF AN EMPIRE", "Carnegie's number. Morgan's answer: \"I accept.\"")
    t = ease(cl((u - 0.08) / 0.7)); v = 480 * t
    g.text(640, 470, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_usteel(u):
    g = G(); g.head("UNITED STATES STEEL", "THE FIRST $1 BILLION COMPANY", "capitalized at about $1.4 billion")
    for x, v, lab, col, val in [(330, 1.0, "U.S. STEEL", GOLDc, "$1.4B"), (730, 0.45, "ANNUAL U.S. BUDGET", GREY, "< $1.4B")]:
        h = 250 * v * ease(cl((u - 0.1) / 0.65)); g.rect(x, 530 - h, x + 220, 530, col)
        g.text(x + 110, 546, lab, 22, W_, anchor="ma")
        if h > 14: g.text(x + 110, 530 - h - 56, val, 40, W_, anchor="ma")
    return g.out()
def g_panic(u):
    g = G(); g.head("THE PANIC OF 1907", "THREE WEEKS THAT BROKE NEW YORK")
    ev = [("OCT 22", "KNICKERBOCKER\nTRUST FAILS"), ("OCT 24", "THE STOCK EXCHANGE\nNEARLY CLOSES"), ("NOV 2", "MORGAN LOCKS\nTHE LIBRARY DOOR")]
    p = ease(cl((u - 0.1) / 0.7)); g.rect(190, 400, 190 + 900 * p, 406, GOLDc)
    for i, (d_, t_) in enumerate(ev):
        x = 190 + 450 * i; on = p * 2.0 >= i - 0.02
        g.circ(x, 403, 14, GOLDc if on else GREY)
        if on:
            g.text(x, 340, d_, 34, W_, anchor="ms")
            for j, ln in enumerate(t_.split("\n")): g.text(x, 450 + 34 * j, ln, 26, (210, 210, 210), anchor="ma")
    return g.out()
def g_estate(u):
    g = G(); g.head("THE TWIST IN HIS WILL", "UNDER $100 MILLION", "much of it in art")
    t = ease(cl((u - 0.1) / 0.6))
    g.text(640, 470, "\"HE WASN'T EVEN A RICH MAN\"", 56, GOLDc, anchor="mm") if t > 0.5 else None
    g.rect(190, 540, 1090, 548, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t * 0.35, 548, GOLDc)
    return g.out()
def g_foot(path, grade=True):
    import subprocess, numpy as np
    from PIL import Image, ImageFilter
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", "scale=960:540,fps=25,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    n = len(raw) // (960 * 540); fr = np.frombuffer(raw[:n * 960 * 540], np.uint8).reshape(n, 540, 960)
    def fn(u):
        a = fr[min(n - 1, int(u * n))].astype(np.float32) / 255
        a = np.clip((a - 0.5) * 1.35 + 0.52, 0, 1)
        yy, xx = np.mgrid[0:540, 0:960]; v = 1 - 0.55 * (((xx - 480) / 560) ** 2 + ((yy - 270) / 330) ** 2)
        a = np.clip(a * v, 0, 1)
        im = Image.fromarray((a * 255).astype(np.uint8)).convert("RGB").resize((1920, 1080), Image.BICUBIC)
        return im
    return fn
def _mk_map():
    from PIL import Image
    import numpy as np
    src = Image.open("/home/claude/canal-dark-/video4-commons/mapa/worldmap_0.jpg").convert("RGB").resize((3840, 1808), Image.LANCZOS)
    a = np.asarray(src).astype(np.int16)
    water = (a[..., 2] > 190) & (a[..., 0] < 140)
    border = (a[..., 0] < 110) & (a[..., 2] < 140) & ~water
    out = np.zeros_like(a, dtype=np.uint8); out[:] = (11, 11, 15)
    out[~water] = (58, 58, 68); out[border] = (22, 22, 28)
    cv = Image.new("RGB", (3840, 2160), (11, 11, 15)); cv.paste(Image.fromarray(out), (0, 176))
    return cv
_MAP = None
def g_map(u, lon=-72.68, lat=41.76, place1="HARTFORD, CONNECTICUT", place2="UNITED STATES  ·  1837"):
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
MAPBRT = [("john pierpont morgan was born", g_map, 7.0)]
