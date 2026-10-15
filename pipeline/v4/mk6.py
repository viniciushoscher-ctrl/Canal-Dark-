import re
s = open("/home/claude/video_build5/build_v5.py", encoding="utf-8").read()
s = s.replace("video_build5", "video_build6").replace("video5-", "video6-").replace("Ford_Video5", "Gould_Video6").replace("part3_ford.py", "part3_gould.py")
s = s.replace("NSC = 86", "NSC = 90")
def blk(a, b, new):
    global s
    i = s.index(a); j = s.index(b, i); s = s[:i] + new + s[j:]
blk("KEY = {", "def is_key", 'KEY = {"gould", "gold", "million", "millions", "billion", "railroad", "railroads", "erie", "vanderbilt", "fisk", "panic", "black", "friday", "hated", "fortune", "telegraph", "union", "pacific", "strike", "died", "fear", "power", "twist", "stock", "shares", "collapsed", "grant", "profit"}\n')
# chapters + cards
i = s.index("CH = ["); j = s.index("QUOTES = []")
s = s[:i] + '''CH = [("CHAPTER 1", "THE POOR BOY WITH", "THE MAPS"), ("CHAPTER 2", "THE ERIE", "WAR"), ("CHAPTER 3", "THE DAY GOLD", "BROKE AMERICA"),
      ("CHAPTER 4", "THE QUIET", "EMPIRE"), ("CHAPTER 5", "THE MOST HATED", "MAN IN AMERICA"), ("CHAPTER 6", "THE PRICE OF", "THE FORTUNE"), ("THE LESSON", "THE COST OF", "FEAR")]
CARDS = [("jason gould was born on december", "1836", "JAY GOULD IS BORN", "Roxbury, New York", None),
         ("in eighteen sixty-eight the richest", "1868", "THE ERIE WAR", "Gould and Fisk vs. Vanderbilt", None),
         ("in september eighteen sixty-nine they started", "1869", "THE GOLD CORNER", "gold: $130 to $162", None),
         ("on the morning of friday september twenty-fourth", "1869", "BLACK FRIDAY", "Grant sells $4 million in gold", None),
         ("in eighteen eighty-one they let", "1881", "WESTERN UNION", "bought almost for free", None),
         ("in eighteen seventy-two he was shot", "1872", "JIM FISK IS SHOT", "on a hotel staircase", None),
         ("in eighteen eighty-six the knights of labor", "1886", "THE GREAT STRIKE", "Gould breaks the union", None),
         ("he died on december second", "1892", "JAY GOULD DIES", "aged 56 · fortune ~$77 million", None)]
''' + s[j:]
blk("def FFg", "BR = []", '''def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video6-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("brokers are screaming in the street", FFg("wall"), 6.0), ("the price of gold is exploding", g_gold, 5.0),
       ("measuring land for farmers", FFg("farm"), 5.5), ("failing line", FFg("rail"), 5.5),
       ("the erie company had a printing press", g_erie, 5.0), ("grabbed about six million dollars", FFg("horse"), 5.0),
       ("hundreds of businesses went bankrupt", FFg("crowd"), 5.5), ("about a ninth of all the railroad", g_track, 5.0),
       ("almost every telegraph wire", FFg("telegraph"), 5.5), ("manhattan elevated railways", FFg("elevated"), 5.5),
       ("bought a weak railroad", FFg("train"), 5.5), ("seventy-seven million dollars", g_estate, 5.0),
       ("he kept working until the very end", FFg("newspaper"), 5.0), ("the monster in the newspapers", FFg("newspaper", 1), 5.0)] + MAPBRT
''')
i = s.index("PHOTOS = ["); j = s.index("PH = []")
s = s[:i] + '''PHOTOS = [
 ('his name is jay gould', 'people/gould.jpg', '1836 – 1892', 'JAY GOULD', 'the most hated man on Wall Street', True, 0),
 ('cornelius vanderbilt decided', 'people/vanderbilt.jpg', '1868', 'CORNELIUS VANDERBILT', 'the richest man in America', True, 0),
 ('daniel drew and a flamboyant', 'people/drew.jpg', '1868', 'DANIEL DREW', "Gould's partner in the Erie war", True, 0),
 ('abel corbin', 'fotos/corbin_0.jpg', '1869', 'ABEL CORBIN', "the president's brother-in-law", True, 0),
 ('the president ulysses grant', 'people/grant.jpg', '1869', 'ULYSSES S. GRANT', 'orders the Treasury to sell gold', True, 0),
 ('the knights of labor a powerful', 'fotos/knights_0.jpg', '1886', 'KNIGHTS OF LABOR', 'a powerful union', True, 0),
 ('the great southwest railroad strike', 'fotos/strike_0.jpg', '1886', 'THE GREAT STRIKE', 'workers against a railroad empire', True, 0),
 ('his son george', 'people/george.jpg', '1890s', 'GEORGE GOULD', 'tried to expand the empire', True, 0),
 ('his daughter helen', 'people/helen.jpg', '1890s', 'HELEN GOULD', 'gave away millions', True, 0),
 ('a man who grew orchids', 'fotos/lyndhurst_0.jpg', 'LYNDHURST', "GOULD'S MANSION", 'on the Hudson River', False, 0),
 ('the puck cartoon', 'fotos/gould3_1.jpg', '1880s', 'THE CARTOONS', 'Gould as the face of greed', False, 0),
 ('he died on december second', 'people/gould.jpg', '1836 – 1892', 'JAY GOULD', 'fortune: about $77 million', True, 0)]
''' + s[j:]
i = s.index("DEF = {"); j = s.index("segs = [(chap_start")
s = s[:i] + '''DEF = {0: "tense", 1: "sad", 2: "drive", 3: "dark", 4: "wonder", 5: "dark", 6: "sad", 7: "reflect"}
TRG = [("he has just cornered", "tense"), ("his name is jay gould", "dark"), ("jason gould was born", "sad"), ("at twenty-one", "drive"),
       ("then he found his real battlefield", "tense"), ("vanderbilt bought and bought", "upbeat"), ("in the end vanderbilt settled", "triumph"),
       ("but gould was not satisfied", "tense"), ("then on the morning of friday", "dark"), ("here is the twist", "dark"),
       ("after black friday", "wonder"), ("he took control of the union pacific", "triumph"), ("critics called him", "dark"),
       ("fisk had been gould's loud partner", "sad"), ("in eighteen eighty-six", "tense"), ("but he could not buy his health", "sad"),
       ("he died on december second", "sad"), ("jay gould did not build anything", "reflect"), ("the second is the price", "dark")]
TWISTS = ["here is the twist", "but gould was not satisfied", "after black friday any normal man", "but he could not buy his health", "the second is the price"]
''' + s[j:]
i = s.index("EMPH = ["); j = s.index("emph_t = []")
s = s[:i] + '''EMPH = [("he has just cornered the gold market", "CORNERED", "THE GOLD MARKET"), ("they simply printed more", "THEY PRINTED", "MORE STOCK"),
        ("about six million dollars", "$6 MILLION", "IN CASH"), ("the day became known as black friday", "BLACK", "FRIDAY"),
        ("he kept his profit", "HE KEPT", "THE PROFIT"), ("about a ninth", "ONE MILE", "IN NINE"), ("the mephistopheles of wall street", "THE DEVIL OF", "WALL STREET"),
        ("information is power", "INFORMATION", "IS POWER"), ("he built fortunes out of other people's fear", "BUILT ON", "FEAR")]
''' + s[j:]
open("build_v6.py", "w", encoding="utf-8").write(s)
