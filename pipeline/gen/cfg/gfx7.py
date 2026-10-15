# graficos Hughes
def g_speed(u):
    g = G(); g.head("1935", "352 MILES PER HOUR", "Hughes H-1 racer, world speed record")
    t = ease(cl((u - 0.1) / 0.65))
    for x, v, lab, col, val in [(330, 0.55, "FIGHTER OF THE ERA", GREY, "~200 MPH"), (730, 1.0, "HUGHES H-1", GOLDc, "352 MPH")]:
        hh = 250 * v * t; g.rect(x, 530 - hh, x + 220, 530, col); g.text(x + 110, 546, lab, 22, W_, anchor="ma")
        if hh > 14: g.text(x + 110, 530 - hh - 52, val, 40, W_, anchor="ma")
    return g.out()
def g_world(u):
    g = G(); g.head("JULY 1938", "AROUND THE WORLD", "record flight time")
    t = ease(cl((u - 0.1) / 0.6)); m = int(t * (3 * 1440 + 19 * 60 + 17)); d_, h_, mm = m // 1440, (m % 1440) // 60, m % 60
    g.text(640, 440, "%dd  %02dh  %02dm" % (d_, h_, mm), 96, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_twa(u):
    g = G(); g.head("1966", "TWA SOLD", "personal payout")
    t = ease(cl((u - 0.1) / 0.6)); v = 550 * t
    g.text(640, 440, "$%d MILLION" % round(v), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_weight(u):
    g = G(); g.head("APRIL 5, 1976", "90 POUNDS", "his weight at death, at 6 feet 4 inches")
    t = ease(cl((u - 0.1) / 0.6))
    g.rect(560, 530 - 300 * t, 720, 530, GREY); g.rect(560, 530 - 300 * t * 0.35, 720, 530, REDc)
    g.text(640, 570, "%d LB" % round(90 * t), 54, W_, anchor="ma")
    return g.out()
