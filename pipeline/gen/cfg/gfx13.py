def g_shifts(u):
    g = G(); g.head("CISCO, TEXAS · 1919", "ONE ROOM, THREE RENTALS", "the same bed rented every eight hours")
    t = ease(cl((u - 0.1) / 0.7)); n = int(t * 3 + 0.99)
    for i in range(3):
        x = 220 + i * 290
        g.rect(x, 340, x + 240, 520, GOLDc if i < n else GREY)
    g.text(640, 600, "SHIFT %d OF 3" % max(1, n), 44, W_, anchor="ma")
    return g.out()
def g_debt(u):
    g = G(); g.head("1931", "OWED $500,000", "and still he refused bankruptcy")
    t = ease(cl((u - 0.1) / 0.6)); v = 500 * t
    g.text(640, 440, "-$%dK" % round(v), 120, REDc, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, REDc)
    return g.out()
def g_statler(u):
    g = G(); g.head("1954 · STATLER DEAL", "$111 MILLION", "the biggest real estate deal in history")
    t = ease(cl((u - 0.1) / 0.6)); v = 111 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
