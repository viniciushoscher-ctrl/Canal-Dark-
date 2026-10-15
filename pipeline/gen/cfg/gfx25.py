def g_miles(u):
    g = G(); g.head("PACIFIC RAILWAY ACT · 1862", "$16,000 TO $48,000 PER MILE", "flat track vs. mountain track")
    t = ease(cl((u - 0.1) / 0.6)); v = 16 + 32 * t
    g.text(640, 440, "$%dK / MILE" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_univ(u):
    g = G(); g.head("1891 · PALO ALTO", "$20 MILLION FOR A SON", "Leland Stanford Junior University")
    t = ease(cl((u - 0.1) / 0.6)); v = 20 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_big4(u):
    g = G(); g.head("SACRAMENTO · 1861", "THE BIG FOUR", "four merchants, one railroad")
    t = ease(cl((u - 0.1) / 0.7)); n = int(t * 4 + 0.99)
    for i in range(4):
        x = 230 + i * 220
        g.rect(x, 340, x + 160, 460, GOLDc if i < n else GREY)
    g.text(640, 540, "STANFORD · HUNTINGTON · HOPKINS · CROCKER", 28, W_, anchor="ma")
    return g.out()
