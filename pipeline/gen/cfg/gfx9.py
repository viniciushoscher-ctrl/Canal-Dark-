def g_loss(u):
    g = G(); g.head("1813 · ASTORIA SOLD", "A $400,000 LOSS", "the Pacific fur venture, lost in the war")
    t = ease(cl((u - 0.1) / 0.6)); v = 400 * t
    g.text(640, 440, "-$%dK" % round(v), 120, REDc, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, REDc)
    return g.out()
def g_lease(u):
    g = G(); g.head("MANHATTAN · 1830s", "THE 21-YEAR LEASE", "tenants build, Astor collects")
    t = ease(cl((u - 0.1) / 0.7)); n = int(t * 21)
    for i in range(21):
        x = 120 + (i % 7) * 150; y = 320 + (i // 7) * 90
        g.rect(x, y, x + 110, y + 60, GOLDc if i < n else GREY)
    g.text(640, 620, "YEAR %d OF 21" % max(1, n), 44, W_, anchor="ma")
    return g.out()
def g_estate20(u):
    g = G(); g.head("MARCH 29, 1848", "$20 MILLION", "richest man in the United States")
    t = ease(cl((u - 0.1) / 0.6)); v = 20 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
