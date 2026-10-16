#--KEY
KEY = {"jobs", "steve", "apple", "pixar", "next", "macintosh", "iphone", "ipod", "ipad", "wozniak", "fired", "garage", "cancer", "million", "billion", "bankruptcy", "think", "different", "design", "simple"}
#--CH
CH = [("CHAPTER 1", "THE ADOPTED BOY", "AND THE GARAGE"), ("CHAPTER 2", "TWO STEVES,", "ONE COMPUTER"), ("CHAPTER 3", "FIRED FROM", "HIS OWN COMPANY"),
      ("CHAPTER 4", "THE WILDERNESS", "YEARS"), ("CHAPTER 5", "THE RETURN", "OF THE KING"), ("CHAPTER 6", "A THOUSAND SONGS", "IN YOUR POCKET"), ("THE LESSON", "TASTE IS", "A STRATEGY")]
CARDS = [("steven paul jobs was born on february", "1955", "JOBS IS BORN", "San Francisco, California", None),
         ("in nineteen seventy-six wozniak designed", "1976", "APPLE IS BORN", "Los Altos garage", None),
         ("in nineteen eighty-four jobs introduced", "1984", "THE MACINTOSH", "the 1984 Super Bowl ad", None),
         ("in nineteen eighty-five the board", "1985", "JOBS IS FIRED", "removed from Apple", None),
         ("in nineteen ninety-five pixar released", "1995", "TOY STORY", "Pixar goes public", None),
         ("on january ninth two thousand seven", "2007", "THE IPHONE", "San Francisco keynote", None),
         ("steve jobs died on october fifth", "2011", "JOBS DIES", "age 56", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("his stake was worth more than two hundred million", g_ipo, 5.5), ("ninety days from running out of cash", g_cash, 5.5), ("earned over three hundred and sixty million", g_toy, 5.5),
       ("traveled to india", FFg("india"), 5.5), ("the first apple computers", FFg("silicon"), 5.5), ("computer animation", FFg("animation"), 5.5),
       ("the iphone changed the world", FFg("phone"), 5.5), ("music would never be the same", FFg("music"), 5.0), ("keynote", FFg("stage"), 5.0)] + MAPBRT
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is steve jobs', 'people/jobs.jpg', '1955 – 2011', 'STEVE JOBS', 'the man who was fired from Apple', True, 0),
 ('paul and clara jobs', 'fotos/paul_0.jpg', '1960s', 'PAUL JOBS', 'the adoptive father who taught him craft', True, 0),
 ('reed college in oregon', 'fotos/reed_0.jpg', '1972', 'REED COLLEGE', 'six months, then calligraphy', True, 0),
 ('atari', 'fotos/atari_0.jpg', '1974', 'ATARI', 'his first job', True, 0),
 ('steve wozniak', 'people/woz.jpg', '1950 –', 'STEVE WOZNIAK', 'the engineer behind Apple', True, 0),
 ('the apple two', 'fotos/apple2_0.jpg', '1977', 'THE APPLE II', 'a mass-market hit', True, 0),
 ('mike markkula', 'fotos/markkula_0.jpg', '1977', 'MIKE MARKKULA', 'the first investor', True, 0),
 ('the macintosh', 'fotos/mac_0.jpg', '1984', 'THE MACINTOSH', 'graphical, expensive, slow', True, 0),
 ('john sculley', 'people/sculley.jpg', '1983', 'JOHN SCULLEY', 'the CEO who fired Jobs', True, 0),
 ('next', 'fotos/next_0.jpg', '1988', 'NeXT COMPUTER', 'the black cube', True, 0),
 ('george lucas', 'people/lucas.jpg', '1986', 'GEORGE LUCAS', 'sold Pixar to Jobs', True, 0),
 ('toy story', 'fotos/toy_0.jpg', '1995', 'TOY STORY', 'the first computer-animated feature', True, 0),
 ('the imac', 'fotos/imac_0.jpg', '1998', 'THE iMAC', 'the colorful comeback', True, 0),
 ('the ipod', 'fotos/ipod_0.jpg', '2001', 'THE iPOD', '1,000 songs in your pocket', True, 0),
 ('the iphone', 'fotos/iphone_0.jpg', '2007', 'THE iPHONE', 'three products in one', True, 0),
 ('the ipad', 'fotos/ipad_0.jpg', '2010', 'THE iPAD', 'another new category', True, 0)]
#--EMPH
EMPH = [("a man whom everyone has given up on", "FIRED FROM", "HIS OWN COMPANY"), ("ninety days", "90 DAYS", "TO LIVE"), ("one device", "ONE", "DEVICE"),
        ("a thousand songs in your pocket", "1,000 SONGS", "IN YOUR POCKET"), ("taste is a strategy", "TASTE IS", "A STRATEGY"), ("oh wow oh wow oh wow", "OH WOW.", "OH WOW. OH WOW.")]
#--MUSIC
DEF = {0: "tense", 1: "drive", 2: "wonder", 3: "dark", 4: "upbeat", 5: "triumph", 6: "sad", 7: "reflect"}
TRG = [("nineteen eighty-five a thirty-year-old", "tense"), ("steven paul jobs was born", "sad"), ("in nineteen seventy-six wozniak", "drive"), ("in nineteen eighty-four jobs introduced", "triumph"),
       ("the company's chief executive", "dark"), ("in nineteen eighty-five the board sided", "dark"), ("jobs started again", "wonder"), ("by nineteen ninety-seven apple was ninety", "tense"),
       ("on january ninth two thousand seven", "triumph"), ("but jobs was ill", "sad"), ("steve jobs died on october", "sad"), ("the second is that taste", "reflect")]
TWISTS = ["in nineteen eighty-five the board sided with sculley", "by nineteen ninety-seven apple was ninety days", "then he repeated the three words", "but jobs was ill", "steve jobs died on october fifth"]
#--NSC
76
#--MAP
MAPBRT = [("steven paul jobs was born on february", lambda u: g_map(u, -122.42, 37.77, "SAN FRANCISCO, CALIFORNIA", "UNITED STATES  ·  1955"), 7.0)]
#--KW
{"A man alone in a bare corporate office": "cupertino_0", "A suburban garage": "paul_0", "A mechanic building": "paul_1", "A college campus in Oregon": "reed_0",
 "A video game arcade": "atari_0", "A homebrew computer club": "apple1_0", "Two young men assembling": "apple1_1", "A computer expo": "apple2_0", "A venture capitalist": "markkula_0",
 "A Super Bowl stadium": "ad1984_0", "A small beige computer": "mac_0", "A boardroom vote": "sculley_0", "A workstation lab": "next_0", "A graphics studio": "pixar_0",
 "A movie theater audience": "toy_0", "A bright translucent computer": "imac_0", "A person with a portable music player": "ipod_0", "A keynote stage": "iphone_0",
 "A crowd waiting outside a store": "store_0", "A man waving from a stage": "j3_0", "Mourners leaving flowers": "store_1"}
