def g_ipo(u):
    g = G(); g.head("DECEMBER 1980 · APPLE IPO", "A $200 MILLION STAKE", "Jobs was 25 years old")
    t = ease(cl((u - 0.1) / 0.6)); v = 200 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_cash(u):
    g = G(); g.head("1997 · APPLE", "90 DAYS FROM BANKRUPTCY", "the return of Steve Jobs")
    t = ease(cl((u - 0.1) / 0.6)); v = 90 - 90 * t
    g.text(640, 440, "%d DAYS LEFT" % round(v), 110, REDc, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * (v / 90), 550, REDc)
    return g.out()
def g_toy(u):
    g = G(); g.head("1995 · TOY STORY", "$360 MILLION", "the first fully computer-animated film")
    t = ease(cl((u - 0.1) / 0.6)); v = 360 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
