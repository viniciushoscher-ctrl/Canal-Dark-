def g_million(u):
    g = G(); g.head("OKLAHOMA · 1916", "FIRST MILLION AT 24", "from oil leases")
    t = ease(cl((u - 0.1) / 0.6)); v = 1.0 * t
    g.text(640, 440, "$%.2f MILLION" % v, 100, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_neutral(u):
    g = G(); g.head("1949 · THE NEUTRAL ZONE", "A BET ON THE DESERT", "paid whether or not any oil was found")
    t = ease(cl((u - 0.1) / 0.6))
    for x, v, lab, col, val in [(330, 9.5, "UP FRONT", GOLDc, "$9.5M"), (730, 1.0, "PER YEAR", GREY, "$1M")]:
        hh = 240 * v / 9.5 * t; g.rect(x, 530 - hh, x + 220, 530, col); g.text(x + 110, 546, lab, 24, W_, anchor="ma")
        if hh > 12: g.text(x + 110, 530 - hh - 52, val, 44, W_, anchor="ma")
    return g.out()
def g_ransom(u):
    g = G(); g.head("ROME · 1973", "THE RANSOM", "demanded vs. paid")
    t = ease(cl((u - 0.1) / 0.6))
    for x, v, lab, col, val in [(330, 17.0, "DEMANDED", REDc, "$17M"), (730, 2.2, "PAID", GOLDc, "$2.2M")]:
        hh = 240 * v / 17.0 * t; g.rect(x, 530 - hh, x + 220, 530, col); g.text(x + 110, 546, lab, 24, W_, anchor="ma")
        if hh > 12: g.text(x + 110, 530 - hh - 52, val, 44, W_, anchor="ma")
    return g.out()
def g_fortune(u):
    g = G(); g.head("1957 · FORTUNE MAGAZINE", "THE RICHEST AMERICAN", "estimated fortune")
    t = ease(cl((u - 0.1) / 0.6)); v = 1.0 * t
    g.text(640, 440, "$%.2f BILLION" % v, 100, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
