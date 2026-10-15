def g_deal(u):
    g = G(); g.head("1961 · THE BUYOUT", "$2.7 MILLION", "the price of the McDonald brothers' company")
    t = ease(cl((u - 0.1) / 0.6)); v = 2.7 * t
    g.text(640, 440, "$%.1f MILLION" % v, 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_opening(u):
    g = G(); g.head("APRIL 15, 1955 · DES PLAINES", "$366 ON OPENING DAY", "the first Kroc restaurant")
    t = ease(cl((u - 0.1) / 0.6)); v = 366 * t
    g.text(640, 440, "$%d" % round(v), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_growth(u):
    g = G(); g.head("1955 – TODAY", "FROM 1 TO ~40,000", "restaurants in more than 100 countries")
    t = ease(cl((u - 0.1) / 0.6)); v = 1 + 39999 * t
    g.text(640, 440, "%s" % format(int(v), ","), 120, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
