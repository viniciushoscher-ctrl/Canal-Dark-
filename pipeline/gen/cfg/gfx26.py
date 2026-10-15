def g_peddler(u):
    g = G(); g.head("1835 · CONNECTICUT", "$7 A MONTH", "a fourteen-year-old farm hand")
    t = ease(cl((u - 0.1) / 0.6)); v = 7 * t
    g.text(640, 440, "$%d / MONTH" % round(v), 120, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_estate(u):
    g = G(); g.head("1900 · HUNTINGTON'S ESTATE", "ABOUT $50 MILLION", "built on iron rails")
    t = ease(cl((u - 0.1) / 0.6)); v = 50 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_lines(u):
    g = G(); g.head("1860s – 1890s", "COAST TO COAST", "tracks he owned or controlled")
    t = ease(cl((u - 0.1) / 0.6)); v = 3000 * t
    g.text(640, 440, "%s MILES" % format(int(v), ","), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
