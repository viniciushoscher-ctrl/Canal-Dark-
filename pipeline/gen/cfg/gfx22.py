def g_patents(u):
    g = G(); g.head("EDISON'S LIFETIME", "1,093 U.S. PATENTS", "a record that stood for decades")
    t = ease(cl((u - 0.1) / 0.6)); v = 1093 * t
    g.text(640, 440, "%s" % format(int(v), ","), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_lamps(u):
    g = G(); g.head("SEPTEMBER 4, 1882 · PEARL STREET", "400 LAMPS LIT", "the first commercial power plant")
    t = ease(cl((u - 0.1) / 0.6)); v = 400 * t
    g.text(640, 440, "%d LAMPS" % round(v), 120, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_tries(u):
    g = G(); g.head("1879 · THE FILAMENT", "THOUSANDS OF MATERIALS TESTED", "from platinum to bamboo")
    t = ease(cl((u - 0.1) / 0.7)); v = 6000 * t
    g.text(640, 440, "%s TESTS" % format(int(v), ","), 110, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
