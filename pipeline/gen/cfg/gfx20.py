def g_growth(u):
    g = G(); g.head("1994", "WEB USAGE UP 2,300%", "the number that changed his life")
    t = ease(cl((u - 0.1) / 0.6)); v = 2300 * t
    g.text(640, 440, "+%s%%" % format(int(v), ","), 120, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_stock(u):
    g = G(); g.head("2000 · THE DOT-COM CRASH", "$100 TO $6", "Amazon's stock collapsed")
    t = ease(cl((u - 0.1) / 0.6)); v = 100 - 94 * t
    g.text(640, 440, "$%d" % round(v), 140, REDc, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * (v / 100), 550, REDc)
    return g.out()
def g_fortune(u):
    g = G(); g.head("2018", "OVER $150 BILLION", "the richest man in modern history")
    t = ease(cl((u - 0.1) / 0.6)); v = 150 * t
    g.text(640, 440, "$%d BILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
