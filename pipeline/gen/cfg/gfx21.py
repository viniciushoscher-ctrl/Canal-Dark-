def g_zip2(u):
    g = G(); g.head("1999 · ZIP2", "SOLD FOR $307 MILLION", "Musk's share: about $22 million")
    t = ease(cl((u - 0.1) / 0.6)); v = 307 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_nasa(u):
    g = G(); g.head("DECEMBER 2008 · NASA", "A $1.6 BILLION CONTRACT", "the deal that saved SpaceX")
    t = ease(cl((u - 0.1) / 0.6)); v = 1.6 * t
    g.text(640, 440, "$%.1f BILLION" % v, 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_fail(u):
    g = G(); g.head("2006 – 2008 · FALCON 1", "THREE FAILURES", "the fourth launch decided everything")
    t = ease(cl((u - 0.1) / 0.7)); n = int(t * 3 + 0.99)
    for i in range(4):
        x = 230 + i * 220
        g.rect(x, 340, x + 160, 440, REDc if i < min(n, 3) else GREY)
    g.text(640, 520, "FAILED %d OF 3" % max(1, min(n, 3)), 44, W_, anchor="ma")
    return g.out()
