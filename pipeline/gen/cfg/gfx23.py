def g_lamps(u):
    g = G(); g.head("1893 · CHICAGO WORLD'S FAIR", "100,000 LAMPS", "lit by Westinghouse's alternating current")
    t = ease(cl((u - 0.1) / 0.6)); v = 100000 * t
    g.text(640, 440, "%s" % format(int(v), ","), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_niagara(u):
    g = G(); g.head("1896 · NIAGARA FALLS", "26 MILES OF POWER", "from the falls to Buffalo, New York")
    t = ease(cl((u - 0.1) / 0.6)); v = 26 * t
    g.text(640, 440, "%d MILES" % round(v), 130, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
def g_patents(u):
    g = G(); g.head("A LIFETIME OF INVENTING", "300+ PATENTS", "the air brake and the AC grid")
    t = ease(cl((u - 0.1) / 0.6)); v = 300 * t
    g.text(640, 440, "%d+" % round(v), 140, GOLDc if t > 0.98 else W_, anchor="mm")
    g.rect(190, 540, 1090, 550, (30, 30, 36)); g.rect(190, 540, 190 + 900 * t, 550, GOLDc)
    return g.out()
