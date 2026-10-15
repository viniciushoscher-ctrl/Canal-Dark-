#--KEY
KEY = {"walt", "disney", "mickey", "mouse", "oswald", "snow", "white", "disneyland", "bankrupt", "million", "dollars", "folly", "impossible", "sound", "cartoon", "studio", "roy", "brother", "borrowed", "mortgaged", "park"}
#--CH
CH = [("CHAPTER 1", "THE BOY WHO", "DREW ANIMALS"), ("CHAPTER 2", "BROKE, WITH", "A MOUSE"), ("CHAPTER 3", "THE STOLEN", "RABBIT"),
      ("CHAPTER 4", "A MOUSE", "WITH A VOICE"), ("CHAPTER 5", "DISNEY'S", "FOLLY"), ("CHAPTER 6", "THE MAGIC", "KINGDOM"), ("THE LESSON", "OWN WHAT", "YOU CREATE")]
CARDS = [("walter elias disney was born on december", "1901", "WALT IS BORN", "Chicago, Illinois", None),
         ("in nineteen twenty-three with forty dollars", "1923", "HOLLYWOOD", "the Disney Brothers Studio", None),
         ("in nineteen twenty-eight walt traveled", "1928", "OSWALD IS LOST", "Mintz takes the rabbit", None),
         ("on november eighteenth nineteen twenty-eight", "1928", "STEAMBOAT WILLIE", "Mickey Mouse is born", None),
         ("at the premiere in december", "1937", "SNOW WHITE", "the first animated feature", None),
         ("on july seventeenth nineteen fifty-five", "1955", "DISNEYLAND OPENS", "Anaheim, California", None),
         ("he died of lung cancer on december", "1966", "WALT DISNEY DIES", "age 65", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("with forty dollars in his pocket", g_pocket, 5.5), ("boarded a train to hollywood", FFg("train"), 5.5), ("he made a cartoon with sound", FFg("cartoon"), 5.5),
       ("almost one and a half million", g_budget, 5.5), ("earned more than eight million", g_box, 5.5), ("hollywoods biggest stars", FFg("hollywood"), 5.5),
       ("turned to television", FFg("tv"), 5.5), ("a second park in florida", FFg("florida"), 5.5), ("analyst", None, 0), ("a strike by his animators", FFg("war"), 5.0),
       ("walked inside a film", FFg("street"), 5.0)] + MAPBRT
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is walt disney', 'people/walt.jpg', '1901 – 1966', 'WALT DISNEY', 'from bankruptcy to a kingdom', True, 0),
 ('his father elias', 'people/elias.jpg', '1859 – 1941', 'ELIAS DISNEY', 'a strict and restless father', True, 0),
 ('a friend named ub iwerks', 'people/ub.jpg', '1901 – 1971', 'UB IWERKS', 'the animator behind Mickey', True, 0),
 ('his brother roy', 'people/roy.jpg', '1893 – 1971', 'ROY O. DISNEY', 'the brother who ran the business', True, 0),
 ('charles mintz', 'fotos/mintz_0.jpg', '1928', 'CHARLES MINTZ', 'the distributor who took Oswald', True, 0),
 ('oswald the lucky rabbit', 'fotos/oswald_0.jpg', '1927', 'OSWALD THE LUCKY RABBIT', 'the character Walt lost', True, 0),
 ('lillian', 'people/lillian.jpg', '1925', 'LILLIAN DISNEY', 'she named Mickey Mouse', True, 0),
 ('steamboat willie premiered', 'fotos/steam_0.jpg', '1928', 'STEAMBOAT WILLIE', 'the first cartoon with synchronized sound', True, 0),
 ('snow white and the seven dwarfs', 'fotos/snow_0.jpg', '1937', 'SNOW WHITE', 'the first full-length animated feature', True, 0),
 ('pinocchio fantasia dumbo', 'fotos/fantasia_0.jpg', '1940', 'FANTASIA', 'the next great gamble', True, 0),
 ('disneyland opened in anaheim', 'fotos/disneyland_0.jpg', '1955', 'DISNEYLAND', 'Anaheim, California', True, 0),
 ('a second park in florida', 'fotos/wdw_0.jpg', '1971', 'WALT DISNEY WORLD', 'opened five years after his death', True, 0)]
#--EMPH
EMPH = [("disneys folly", "DISNEY'S", "FOLLY"), ("owned the character not walt", "HE OWNED", "THE CHARACTER"), ("the mice kept him company", "THE MICE", "KEPT HIM COMPANY"),
        ("black sunday", "BLACK", "SUNDAY"), ("own what you create", "OWN WHAT", "YOU CREATE"), ("kind of fun to do the impossible", "FUN TO DO", "THE IMPOSSIBLE")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "dark", 4: "triumph", 5: "tense", 6: "wonder", 7: "reflect"}
TRG = [("nineteen thirty-seven a packed", "tense"), ("walter elias disney was born", "sad"), ("laugh-o-gram made short", "drive"), ("he was bankrupt", "dark"),
       ("in nineteen twenty-eight walt traveled", "dark"), ("on the long train ride", "wonder"), ("the first two mickey", "drive"), ("on november eighteenth", "triumph"),
       ("the film was snow white", "tense"), ("at the premiere in december", "triumph"), ("then the war came", "dark"), ("on july seventeenth", "wonder"),
       ("he died of lung cancer", "sad"), ("the second is that people", "reflect")]
TWISTS = ["the distributor a man named charles mintz told him something shocking", "on november eighteenth nineteen twenty-eight", "at the premiere in december nineteen thirty-seven", "he died of lung cancer on december", "the second is that people will call"]
#--NSC
82
#--MAP
MAPBRT = [("walter elias disney was born on december", lambda u: g_map(u, -87.63, 41.88, "CHICAGO, ILLINOIS", "UNITED STATES  ·  1901"), 7.0)]
#--KW
{"A Chicago street": "chicago_0", "A Missouri farm": "marceline_0", "An advertising studio desk": "kansas_0", "An animation desk": "laugh_0", "A tiny studio office": "laugh_1",
 "A film distributor's office": "mintz_0", "A steamboat on a river": "steam_1", "A Hollywood studio lot": "burbank_0", "An Academy Awards banquet": "oscar_0",
 "A new studio campus": "burbank_1", "Animators on strike": "strike_0", "A 1950s family watching": "tv_0", "The opening day crowd": "disneyland_1", "Families with children": "disneyland_0"}
