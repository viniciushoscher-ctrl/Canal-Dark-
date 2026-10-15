def g_dos(u):
    g = G(); g.head("1980 · THE DEAL", "$50,000 FOR MS-DOS", "bought from Seattle Computer Products")
    t = ease(cl((u - 0.1) / 0.6)); v = 50 * t
    g.text(640, 440, "$%dK" % round(v), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_ipo(u):
    g = G(); g.head("MARCH 1986 · MICROSOFT IPO", "A $300 MILLION STAKE", "Gates, age 30, owned about 45%")
    t = ease(cl((u - 0.1) / 0.6)); v = 300 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_peak(u):
    g = G(); g.head("LATE 1990s", "OVER $100 BILLION", "the richest man in the world")
    t = ease(cl((u - 0.1) / 0.6)); v = 100 * t
    g.text(640, 440, "$%d BILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
