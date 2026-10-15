def g_sixty(u):
    g = G(); g.head("BUENOS AIRES · 1923", "$60 IN HIS POCKET", "a seventeen-year-old refugee")
    t = ease(cl((u - 0.1) / 0.6)); v = 60 * t
    g.text(640, 440, "$%d" % round(v), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_freighters(u):
    g = G(); g.head("1933", "SIX FREIGHTERS AT SCRAP PRICE", "$20,000 each, built for $1 million")
    t = ease(cl((u - 0.1) / 0.7)); n = int(t * 6 + 0.99)
    for i in range(6):
        x = 150 + i * 170
        g.rect(x, 340, x + 140, 440, GOLDc if i < n else GREY)
    g.text(640, 540, "$20,000 EACH", 56, W_, anchor="ma")
    return g.out()
def g_fleet(u):
    g = G(); g.head("EARLY 1950s", "OVER 100 SHIPS", "the largest private fleet on Earth")
    t = ease(cl((u - 0.1) / 0.6)); v = 100 * t
    g.text(640, 440, "%d SHIPS" % round(v), 120, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
