#--KEY
KEY = {"walton", "wal", "mart", "walmart", "stores", "store", "sam", "arkansas", "rogers", "bentonville", "discount", "prices", "customer", "pickup", "associates", "billion", "richest", "ben", "franklin", "towns"}
#--CH
CH = [("CHAPTER 1", "THE PAPER-ROUTE", "BOY"), ("CHAPTER 2", "THE STORE HE", "LOST"), ("CHAPTER 3", "THE SMALL-TOWN", "BET"),
      ("CHAPTER 4", "ALWAYS LOW", "PRICES"), ("CHAPTER 5", "THE RICHEST MAN", "IN A PICKUP"), ("CHAPTER 6", "THE LEGACY", "OF WALMART"), ("THE LESSON", "GO WHERE", "NOBODY LOOKS")]
CARDS = [("samuel moore walton was born on march", "1918", "WALTON IS BORN", "Kingfisher, Oklahoma", None),
         ("in nineteen forty-five at twenty-seven", "1945", "THE BEN FRANKLIN STORE", "Newport, Arkansas", None),
         ("in nineteen fifty his landlord", "1950", "THE STORE IS LOST", "the lease is not renewed", None),
         ("on july second nineteen sixty-two", "1962", "THE FIRST WAL-MART", "Rogers, Arkansas", None),
         ("in nineteen eighty-three he started", "1983", "SAM'S CLUB", "the warehouse club", None),
         ("in nineteen eighty-five forbes", "1985", "RICHEST MAN IN AMERICA", "$2.8 billion", None),
         ("sam walton died on april", "1992", "WALTON DIES", "age 74", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("walton marked them up by twenty", g_margin, 5.5), ("cut out the middlemen", FFg("truck"), 5.5), ("built distribution centers", FFg("truck", 1), 5.5),
       ("thirty-eight stores", FFg("store"), 5.5), ("used computers and satellites", FFg("computer"), 5.5), ("richest man in america", g_rich, 5.5),
       ("nearly two thousand stores", g_stores, 5.5), ("flew a small airplane", FFg("plane"), 5.5), ("small town", FFg("town"), 5.0), ("shoppers", FFg("crowd"), 5.0)] + MAPBRT
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is sam walton', 'people/sam.jpg', '1918 – 1992', 'SAM WALTON', 'the richest man in a pickup truck', True, 0),
 ('shelbina missouri', 'fotos/shelbina_0.jpg', '1930s', 'SHELBINA, MISSOURI', 'where Sam grew up', True, 0),
 ('university of missouri', 'fotos/mizzou_0.jpg', '1940', 'UNIVERSITY OF MISSOURI', 'economics degree', True, 0),
 ('a ben franklin franchise', 'fotos/benfranklin_0.jpg', '1945', 'BEN FRANKLIN', 'his first variety store', True, 0),
 ('newport arkansas', 'fotos/newport_0.jpg', '1945', 'NEWPORT, ARKANSAS', 'the store he lost in 1950', True, 0),
 ('walton wal-mart discount city', 'fotos/walmart_0.jpg', '1962', 'WAL-MART DISCOUNT CITY', 'always low prices', True, 0),
 ('distribution centers', 'fotos/dc_0.jpg', '1970s', 'DISTRIBUTION CENTER', 'the secret weapon', True, 0),
 ('his fleet of trucks', 'fotos/truck_0.jpg', '1980s', 'THE WAL-MART TRUCKS', 'his own fleet', True, 0),
 ('his old ford pickup truck', 'fotos/cap_0.jpg', '1980s', 'THE CAP AND THE PICKUP', 'the richest man in America', True, 0),
 ('sams club', 'fotos/sams_0.jpg', '1983', "SAM'S CLUB", 'the warehouse club', True, 0),
 ('the first supercenter', 'fotos/super_0.jpg', '1988', 'THE SUPERCENTER', 'groceries and goods under one roof', True, 0),
 ('hairy cell leukemia', 'fotos/leuk_0.jpg', '1990', 'HAIRY CELL LEUKEMIA', 'diagnosed in 1990', True, 0),
 ('president george h w bush', 'people/bush.jpg', '1992', 'GEORGE H. W. BUSH', 'awarded the Medal of Freedom', True, 0),
 ('the medal of freedom', 'fotos/medal_0.jpg', '1992', 'MEDAL OF FREEDOM', 'highest civilian honor', True, 0),
 ('his family inherited', 'people/rob.jpg', '', 'ROB WALTON', 'the Walton heirs', True, 0)]
#--EMPH
EMPH = [("always low prices", "ALWAYS LOW", "PRICES"), ("who is number one", "WHO IS", "NUMBER ONE?"), ("management by walking around", "MANAGEMENT BY", "WALKING AROUND"),
        ("the customer", "THE CUSTOMER", "IS THE BOSS"), ("a good idea works best in the place that everyone else ignores", "GO WHERE", "NOBODY LOOKS")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "triumph", 5: "upbeat", 6: "reflect", 7: "reflect"}
TRG = [("nineteen sixty-two in a small town", "tense"), ("samuel moore walton was born", "sad"), ("when the second world war", "drive"), ("in nineteen fifty his landlord", "dark"),
       ("walton moved his family", "wonder"), ("on july second nineteen sixty-two", "triumph"), ("walton's secret was", "drive"), ("in the seventies and eighties", "upbeat"),
       ("in nineteen eighty-five forbes", "triumph"), ("in nineteen ninety walton learned", "dark"), ("sam walton died on april", "sad"), ("the second is to stay close", "reflect")]
TWISTS = ["in nineteen fifty his landlord", "on july second nineteen sixty-two", "in nineteen eighty-five forbes", "in nineteen ninety walton learned", "sam walton died on april"]
#--NSC
71
#--MAP
MAPBRT = [("samuel moore walton was born on march", lambda u: g_map(u, -97.93, 35.86, "KINGFISHER, OKLAHOMA", "UNITED STATES  ·  1918"), 7.0)]
#--KW
{"A plain discount store": "walmart_0", "A dusty Oklahoma farm town": "shelbina_0", "A high school football team": "shelbina_1", "A college dormitory": "mizzou_0",
 "A five-and-dime store interior": "benfranklin_0", "A landlord handing": "newport_0", "A courthouse square": "newport_1", "A warehouse distribution center": "dc_0",
 "An old pickup truck": "truck_0", "A huge warehouse club": "sams_0", "A gigantic modern supercenter": "super_0", "A president hanging a medal": "medal_0",
 "A hospital corridor": "leuk_0", "An old man in a baseball cap": "cap_0"}
