def g_returns(u):
    g = G(); g.head("1956 – 1969 · THE PARTNERSHIP", "29% A YEAR", "vs. about 11% for the market")
    t = ease(cl((u - 0.1) / 0.6)); v = 29 * t
    g.text(640, 440, "%d%%" % round(v), 140, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_sees(u):
    g = G(); g.head("1972 · SEE'S CANDIES", "$25 MILLION", "it earned over $1 billion for Berkshire")
    t = ease(cl((u - 0.1) / 0.6)); v = 25 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_worth(u):
    g = G(); g.head("TODAY · BERKSHIRE HATHAWAY", "~$1 TRILLION", "from a failing textile mill")
    t = ease(cl((u - 0.1) / 0.6)); v = 1000 * t
    g.text(640, 440, "$%d BILLION" % round(v), 100, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
