#--KEY
KEY = {"astor", "fur", "furs", "million", "dollars", "land", "manhattan", "richest", "died", "fortune", "beaver", "astoria", "lease", "rent", "immigrant", "sold", "sell", "bet", "panic"}
#--CH
CH = [("CHAPTER 1", "THE BUTCHER'S SON", "WITH A FEW FLUTES"), ("CHAPTER 2", "THE MAN WHO", "BEAT FURS"), ("CHAPTER 3", "THE BET ON", "THE PACIFIC"),
      ("CHAPTER 4", "THE FUR", "MONOPOLY"), ("CHAPTER 5", "THE BET", "ON DIRT"), ("CHAPTER 6", "THE RICHEST MAN", "IN AMERICA"), ("THE LESSON", "KNOW WHEN", "TO LEAVE")]
CARDS = [("john jacob astor was born on july", "1763", "ASTOR IS BORN", "Walldorf, Germany", None),
         ("in seventeen eighty-three as the american", "1783", "ASTOR ARRIVES", "Baltimore · a few flutes", None),
         ("in eighteen-oh-eight astor founded", "1808", "AMERICAN FUR COMPANY", "trapper to China", None),
         ("and then in eighteen twelve", "1812", "THE WAR OF 1812", "Astoria is lost", None),
         ("so in eighteen thirty-four he sold", "1834", "THE GREAT EXIT", "sold at the peak", None),
         ("the astor house a grand hotel", "1836", "THE ASTOR HOUSE", "Broadway, New York", None),
         ("he died on march twenty-ninth", "1848", "ASTOR DIES", "richest man in America", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("a sixty-nine-year-old german immigrant", FFg("nyc"), 5.5), ("boarded a ship to baltimore", FFg("ship"), 5.5), ("astor lost about four hundred thousand", g_loss, 5.0),
       ("his ships would carry goods around cape horn", FFg("ship", 1), 5.5), ("twenty-one years", g_lease, 5.0), ("about twenty million dollars", g_estate20, 5.0),
       ("an immigrant who arrived with a few flutes", FFg("harbor"), 5.5), ("he began buying land farms", FFg("wall"), 5.5), ("when a panic crushed", FFg("crowd"), 5.5),
       ("the astor library", FFg("library"), 5.5), ("a public library in new york", FFg("library", 1), 5.0), ("took a job beating furs", FFg("nyc", 1), 5.0)] + MAPBRT
#--PHOTOS
PHOTOS = [
 ('but john jacob astor is not retiring', 'people/astor.jpg', '1763 – 1848', 'JOHN JACOB ASTOR', 'from fur trader to landlord of New York', True, 0),
 ('he married sarah todd', 'fotos/sarah_0.jpg', '1785', 'SARAH TODD ASTOR', 'his partner in business', True, 0),
 ('and call it astoria', 'fotos/astoria_0.jpg', '1811', 'ASTORIA', 'on the Columbia River', True, 0),
 ('one ship the tonquin', 'fotos/tonquin_0.jpg', '1811', 'THE TONQUIN', 'destroyed near Vancouver Island', True, 0),
 ('opened in eighteen thirty-six', 'fotos/astorhouse_2.jpg', '1836', 'THE ASTOR HOUSE', 'one of the first luxury hotels', True, 0),
 ('the writer washington irving', 'people/irving.jpg', '1840s', 'WASHINGTON IRVING', "Astor's friend", True, 0),
 ('his son william backhouse astor', 'people/william.jpg', '1848', 'WILLIAM B. ASTOR', 'doubled the family fortune', True, 0),
 ('the waldorf astoria', 'fotos/waldorf_0.jpg', '1897', 'THE WALDORF-ASTORIA', 'the family hotel empire', True, 0),
 ('john jacob astor the fourth', 'people/jjiv.jpg', '1912', 'JOHN JACOB ASTOR IV', 'died on the Titanic', True, 0),
 ('he died on march twenty-ninth', 'people/astor.jpg', '1763 – 1848', 'JOHN JACOB ASTOR', 'the richest man in America', True, 0)]
#--EMPH
EMPH = [("a bet on dirt", "A BET", "ON DIRT"), ("a few flutes and little else", "A FEW", "FLUTES"), ("he sold the american fur company", "HE SOLD", "AT THE PEAK"),
        ("it was the perfect machine", "THE PERFECT", "MACHINE"), ("every immigrant who arrived in new york", "EVERY IMMIGRANT", "PAID RENT"), ("the second is to know when to leave", "KNOW WHEN", "TO LEAVE")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "dark", 5: "upbeat", 6: "reflect", 7: "reflect"}
TRG = [("he is making the smartest bet", "tense"), ("john jacob astor was born", "sad"), ("at sixteen he left home", "drive"), ("in seventeen eighty-three", "wonder"),
       ("in eighteen-oh-eight astor founded", "triumph"), ("but the plan was risky", "tense"), ("a british warship", "dark"), ("after the war astor", "dark"),
       ("so in eighteen thirty-four", "triumph"), ("with his money astor", "wonder"), ("it was the perfect machine", "triumph"), ("astor lived modestly", "sad"),
       ("he died on march twenty-ninth", "sad"), ("john jacob astor made a fortune twice", "reflect")]
TWISTS = ["but john jacob astor is not retiring", "so in eighteen thirty-four he sold", "it was the perfect machine", "he died on march twenty-ninth", "the second is to know when to leave"]
#--NSC
80
#--MAP
MAPBRT = [("john jacob astor was born on july", lambda u: g_map(u, 8.65, 49.30, "WALLDORF, GERMANY", "KINGDOM OF GERMANY  ·  1763"), 7.0)]
#--KW
{"A busy nineteenth century New York harbor": "nyc3_0", "An empty frontier trading post": "amfur2_2", "A New York street with muddy road": "nyc1_0", "A tall sailing ship rounding Cape Horn": "tonquin_0",
 "The mouth of a great river meeting": "columbia_0", "A frontier fort at a river border": "amfur2_1", "A fur company headquarters": "amfur2_0", "A Great Lakes fur trading post": "mackinac_0",
 "A canoe on a misty": "canoe_0", "A map of Manhattan island": "nyc2_3", "A grand hotel on Broadway": "astorhouse_2", "A panic day in New York": "bank_0", "A public library reading room": "library_1",
 "A grand library hall": "library2_1", "A Fifth Avenue mansion": "fifth_0", "A luxury hotel exterior": "waldorf_0", "A great ocean liner": "titanic_0", "A forest trail in upstate": "trapper_3",
 "A starving expedition": "trapper_1"}
