def g_profit(u):
    g = G(); g.head("CARNEGIE STEEL · 1890s", "PROFITS UP 13X", "from $3 million to $40 million a year")
    t = ease(cl((u - 0.1) / 0.6)); v = 3 + 37 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_homestead(u):
    g = G(); g.head("JULY 6, 1892 · HOMESTEAD", "THE DEATH TOLL", "seven workers and three guards")
    t = ease(cl((u - 0.1) / 0.6)); n = int(round(10 * t))
    g.text(640, 440, "%d DEAD" % n, 120, REDc, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, REDc)
    return g.out()
def g_deal(u):
    g = G(); g.head("1901 · UNITED STATES STEEL", "A $400 MILLION SALE", "Carnegie Steel becomes the first billion-dollar company")
    t = ease(cl((u - 0.1) / 0.6)); v = 400 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
