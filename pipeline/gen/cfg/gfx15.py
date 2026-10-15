def g_margin(u):
    g = G(); g.head("THE WAL-MART RULE", "20% vs 30% MARKUP", "lower margin, twice the sales")
    t = ease(cl((u - 0.1) / 0.6)); v = 30 - 10 * t
    g.text(640, 440, "%d%%" % round(v), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * (v / 30), 550, GOLDc)
    return g.out()
def g_stores(u):
    g = G(); g.head("1962 – 1992", "FROM 1 STORE TO ~2,000", "the biggest retailer in the world")
    t = ease(cl((u - 0.1) / 0.6)); v = 1 + 1999 * t
    g.text(640, 440, "%s STORES" % format(int(v), ","), 100, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_rich(u):
    g = G(); g.head("1985 · FORBES", "$2.8 BILLION", "the richest man in America")
    t = ease(cl((u - 0.1) / 0.6)); v = 2.8 * t
    g.text(640, 440, "$%.1f BILLION" % v, 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
