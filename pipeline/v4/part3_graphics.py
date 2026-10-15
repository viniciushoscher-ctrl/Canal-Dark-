from PIL import Image, ImageDraw, ImageFont
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"; FI = "/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf"
GOLDc = (245, 197, 66); W_ = (245, 245, 245); BG = (11, 11, 15); REDc = (232, 60, 40); GREY = (60, 60, 68)
SS = 2
_fc = {}
def fnt(sz, f=FB):
    k = (sz, f)
    if k not in _fc: _fc[k] = ImageFont.truetype(f, sz * SS)
    return _fc[k]
ease = lambda u: u * u * (3 - 2 * u)
cl = lambda u: min(1.0, max(0.0, u))
class G:
    def __init__(s):
        s.im = Image.new("RGB", (1280 * SS, 720 * SS), BG); s.d = ImageDraw.Draw(s.im)
        for gx in range(0, 1280, 80): s.line([(gx, 0), (gx, 720)], (20, 20, 26), 1)
        for gy in range(0, 720, 80): s.line([(0, gy), (1280, gy)], (20, 20, 26), 1)
    def line(s, pts, col, w=2): s.d.line([(x * SS, y * SS) for x, y in pts], fill=col, width=int(w * SS), joint="curve")
    def rect(s, x0, y0, x1, y1, col): s.d.rectangle([x0 * SS, y0 * SS, x1 * SS, y1 * SS], fill=col)
    def circ(s, cx, cy, r, col): s.d.ellipse([(cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS], fill=col)
    def text(s, x, y, t, sz, col, f=FB, anchor="la"): s.d.text((x * SS, y * SS), t, font=fnt(sz, f), fill=col, anchor=anchor)
    def head(s, kick, big=None, sub=None):
        s.text(90, 70, kick, 26, GOLDc); s.rect(90, 112, 180, 117, GOLDc)
        if big: s.text(90, 132, big, 60, W_)
        if sub: s.text(90, 214, sub, 30, (200, 200, 200), FI)
    def out(s): return s.im.resize((1920, 1080), Image.LANCZOS)
def money(v): return "${:,.2f}".format(v) if v < 100 else "${:,.0f}".format(v)
def g_counter(u):
    g = G(); g.head("53 YEARS LATER", "FROM A WEEKLY WAGE", "to the richest man in the world")
    t = ease(cl((u - 0.08) / 0.78)); v = 1.2 * (480e6 / 1.2) ** t
    g.text(640, 470, money(v), 118, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 530, 1090, 540, (30, 30, 36)); g.rect(190, 530, 190 + 900 * t, 540, GOLDc)
    g.text(190, 552, "$1.20 / WEEK", 24, (180, 180, 180)); g.text(1090, 552, "$480 MILLION", 24, (180, 180, 180), anchor="ra")
    return g.out()
def g_route(u):
    g = G(); g.head("1848 · THE CROSSING", "DUNFERMLINE TO PITTSBURGH")
    A, Bp, Cp = (230, 470), (1050, 340), (640, 250)
    pts = []
    for i in range(121):
        t = i / 120; x = (1 - t) ** 2 * A[0] + 2 * (1 - t) * t * Cp[0] + t * t * Bp[0]; y = (1 - t) ** 2 * A[1] + 2 * (1 - t) * t * Cp[1] + t * t * Bp[1]
        pts.append((x, y))
    p = ease(cl((u - 0.1) / 0.75)); n = max(2, int(120 * p))
    for i in range(0, 120, 6): g.line(pts[i:i + 3], (70, 70, 80), 3)
    g.line(pts[:n], GOLDc, 6)
    g.circ(*A, 14, W_); g.circ(*Bp, 14, W_ if p > 0.98 else GREY)
    g.text(A[0], A[1] + 30, "DUNFERMLINE", 28, W_, anchor="ma"); g.text(Bp[0], Bp[1] + 30, "PITTSBURGH", 28, W_, anchor="ma")
    sx, sy = pts[n - 1]; g.circ(sx, sy, 11, GOLDc); g.circ(sx, sy, 5, BG)
    return g.out()
def g_wage(u):
    g = G(); g.head("THE FIRST RAISE", "$1.20 TO $2.50 A WEEK", "a bobbin boy becomes a telegraph boy")
    for x, v, lab, col in [(330, 1.2, "COTTON MILL", GREY), (730, 2.5, "TELEGRAPH OFFICE", GOLDc)]:
        h = 200 * (v / 2.5) * ease(cl((u - 0.1) / 0.6)); g.rect(x, 520 - h, x + 220, 520, col)
        g.text(x + 110, 534, lab, 22, W_, anchor="ma")
        if h > 40: g.text(x + 110, 520 - h - 56, "$%.2f" % v, 44, W_, anchor="ma")
    return g.out()
def g_steel(u):
    g = G(); g.head("BY 1900", "MORE STEEL THAN BRITAIN", "one company against an entire nation")
    for x, v, lab, col in [(330, 1.0, "CARNEGIE STEEL", GOLDc), (730, 0.72, "ALL OF GREAT BRITAIN", GREY)]:
        h = 240 * v * ease(cl((u - 0.1) / 0.65)); g.rect(x, 530 - h, x + 220, 530, col)
        g.text(x + 110, 546, lab, 22, W_, anchor="ma")
    return g.out()
def g_wp(u):
    g = G(); g.head("THE PRICE OF EFFICIENCY", "PROFITS UP. PAY DOWN.", "illustrative")
    x0, x1 = 190, 1090; p = ease(cl((u - 0.1) / 0.75)); n = max(2, int(100 * p))
    pf = [(x0 + (x1 - x0) * i / 100, 520 - 250 * (0.05 + 0.95 * (i / 100) ** 1.6)) for i in range(101)]
    wg = [(x0 + (x1 - x0) * i / 100, 380 + 110 * (i / 100) ** 1.4) for i in range(101)]
    g.line([(x0, 560), (x1, 560)], (70, 70, 80), 3)
    g.line(pf[:n], GOLDc, 7); g.line(wg[:n], REDc, 7)
    g.circ(*pf[n - 1], 10, W_); g.circ(*wg[n - 1], 10, W_)
    g.text(x1 + 20, 270, "PROFITS", 26, GOLDc); g.text(x1 + 20, 500, "WAGES", 26, REDc)
    return g.out()
def g_pink(u):
    g = G(); g.head("JULY 6, 1892 · HOMESTEAD", "300 PINKERTON AGENTS", "sent up the river at night")
    n = int(300 * ease(cl((u - 0.1) / 0.7)))
    for i in range(300):
        r_, c_ = divmod(i, 30); x, y = 165 + c_ * 33, 290 + r_ * 34
        g.circ(x, y, 10, REDc if i < n else GREY)
    g.text(1090, 140, str(n), 56, GOLDc, anchor="ra")
    return g.out()
def g_deal(u):
    g = G(); g.head("1901 · THE SALE", "THE PRICE OF A STEEL EMPIRE", "written on a slip of paper")
    t = ease(cl((u - 0.08) / 0.7)); g.text(640, 460, "${:,.0f}".format(480e6 * t), 112, GOLDc if t > 0.98 else W_, anchor="mm")
    g.text(640, 550, "CARNEGIE STEEL COMPANY", 28, (190, 190, 190), anchor="mm")
    return g.out()
def g_billion(u):
    g = G(); g.head("UNITED STATES STEEL", "THE FIRST BILLION-DOLLAR COMPANY")
    t = ease(cl((u - 0.08) / 0.7)); g.text(640, 460, "${:,.0f}".format(1e9 * t), 112, GOLDc if t > 0.98 else W_, anchor="mm")
    g.text(640, 550, "JP MORGAN MERGES THE STEEL INDUSTRY", 28, (190, 190, 190), anchor="mm")
    return g.out()
def g_libs(u):
    g = G(); g.head("A GIFT TO THE WORLD", "2,500+ PUBLIC LIBRARIES")
    n = int(2500 * ease(cl((u - 0.1) / 0.7)))
    for i in range(2500):
        r_, c_ = divmod(i, 100); g.circ(150 + c_ * 10.8, 270 + r_ * 12, 3.2, GOLDc if i < n else (38, 38, 46))
    g.text(1090, 140, "{:,}".format(n), 56, GOLDc, anchor="ra")
    return g.out()
def g_donut(u):
    g = G(); g.head("THE GREAT GIVEAWAY", "ROUGHLY 90% GIVEN AWAY")
    cx, cy, r = 640, 400, 150; p = ease(cl((u - 0.1) / 0.7)) * 0.9
    g.d.ellipse([(cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS], outline=(38, 38, 46), width=44 * SS)
    if p > 0.002: g.d.arc([(cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS], -90, -90 + 360 * p, fill=GOLDc, width=44 * SS)
    g.text(cx, cy - 6, "%d%%" % round(p * 100), 76, W_, anchor="mm"); g.text(cx, cy + 50, "GIVEN AWAY", 22, (180, 180, 180), anchor="mm")
    return g.out()
