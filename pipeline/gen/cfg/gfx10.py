def g_tax(u):
    g = G(); g.head("1921 – 1929", "THE TOP TAX RATE", "Mellon's cuts under Harding and Coolidge")
    t = ease(cl((u - 0.1) / 0.6)); v = 73 - 48 * t
    g.text(640, 440, "%d%%" % round(v), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * (v / 73), 550, GOLDc)
    return g.out()
def g_debt(u):
    g = G(); g.head("THE TREASURY · 1920s", "DEBT CUT BY A THIRD", "a budget surplus paid it down")
    t = ease(cl((u - 0.1) / 0.6)); v = 33 * t
    g.text(640, 440, "-%d%%" % round(v), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_hermitage(u):
    g = G(); g.head("1930 – 1931", "$7 MILLION IN MASTERPIECES", "bought secretly from the Soviet Union")
    t = ease(cl((u - 0.1) / 0.6)); v = 7 * t
    g.text(640, 440, "$%.1f MILLION" % v, 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
