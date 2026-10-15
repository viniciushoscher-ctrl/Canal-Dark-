def g_budget(u):
    g = G(); g.head("1934 – 1937 · SNOW WHITE", "$1.5 MILLION BUDGET", "in the middle of the Great Depression")
    t = ease(cl((u - 0.1) / 0.6)); v = 1.5 * t
    g.text(640, 440, "$%.1f MILLION" % v, 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_box(u):
    g = G(); g.head("FIRST RUN · 1937–38", "$8 MILLION AT THE BOX OFFICE", "the biggest film in history, at the time")
    t = ease(cl((u - 0.1) / 0.6)); v = 8 * t
    g.text(640, 440, "$%.1f MILLION" % v, 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_pocket(u):
    g = G(); g.head("1923 · LOS ANGELES", "$40 IN HIS POCKET", "a one-way train ticket to Hollywood")
    t = ease(cl((u - 0.1) / 0.6)); v = 40 * t
    g.text(640, 440, "$%d" % round(v), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
