#--KEY
KEY = {"huntington", "collis", "railroad", "central", "pacific", "southern", "hopkins", "crocker", "stanford", "judah", "washington", "congress", "lobbying", "octopus", "million", "frugal", "peddler", "hardware", "panama", "shipyard"}
#--CH
CH = [("CHAPTER 1", "THE CLOCK", "PEDDLER"), ("CHAPTER 2", "THE HARDWARE MAN", "OF SACRAMENTO"), ("CHAPTER 3", "THE MAN WHO WENT", "TO WASHINGTON"),
      ("CHAPTER 4", "COUNTING EVERY", "NICKEL"), ("CHAPTER 5", "THE RAILROAD", "EMPIRE"), ("CHAPTER 6", "THE HATED", "MILLIONAIRE"), ("THE LESSON", "PERSISTENCE", "BEATS PEDIGREE")]
CARDS = [("collis potter huntington was born on october", "1821", "HUNTINGTON IS BORN", "Harwinton, Connecticut", None),
         ("in eighteen forty-nine huntington set out", "1849", "THE GOLD RUSH", "across Panama", None),
         ("in eighteen sixty a young engineer", "1860", "JUDAH'S PLAN", "a railroad over the Sierra", None),
         ("he won the pacific railway act", "1862", "THE RAILWAY ACT", "money from Washington", None),
         ("after the transcontinental line", "1869", "THE EMPIRE GROWS", "Southern Pacific", None),
         ("in eighteen eighty-three", "1883", "A NEW WIFE", "Arabella Huntington", None),
         ("he died on august thirteenth", "1900", "HUNTINGTON DIES", "age 78", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("seven dollars a month", g_peddler, 5.5), ("a fortune of about fifty million", g_estate, 5.5), ("from san francisco to virginia", g_lines, 5.5),
       ("sailed across panama", FFg("ship"), 5.5), ("the pacific railway act", FFg("capitol"), 5.5), ("through the sierra", FFg("mountain"), 5.5),
       ("shipyard in newport news", FFg("shipyard"), 5.5), ("coal fields", FFg("coal"), 5.0), ("steam locomotive", FFg("train"), 5.0)] + MAPBRT
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is collis huntington', 'people/huntington.jpg', '1821 – 1900', 'COLLIS HUNTINGTON', 'the most feared railroad man in America', True, 0),
 ('harwinton connecticut', 'fotos/harwinton_0.jpg', '1821', 'HARWINTON, CT', 'where Huntington was born', True, 0),
 ('panama', 'fotos/panama_0.jpg', '1849', 'THE PANAMA CROSSING', 'on the way to the gold rush', True, 0),
 ('san francisco', 'fotos/sf_0.jpg', '1850', 'SAN FRANCISCO', 'where he arrived', True, 0),
 ('mark hopkins', 'people/hopkins.jpg', '1813 – 1878', 'MARK HOPKINS', 'his partner in Sacramento', True, 0),
 ('theodore judah', 'people/judah.jpg', '1826 – 1863', 'THEODORE JUDAH', 'the engineer with the plan', True, 0),
 ('charles crocker', 'people/crocker.jpg', '1822 – 1888', 'CHARLES CROCKER', 'the builder', True, 0),
 ('leland stanford', 'people/stanford.jpg', '1824 – 1893', 'LELAND STANFORD', 'the public face', True, 0),
 ('abraham lincoln', 'people/lincoln.jpg', '1862', 'ABRAHAM LINCOLN', 'signed the railway act', True, 0),
 ('the big four', 'fotos/bigfour_0.jpg', '1861', 'THE BIG FOUR', 'four merchants, one railroad', True, 0),
 ('promontory', 'fotos/promontory_0.jpg', '1869', 'PROMONTORY SUMMIT', 'the transcontinental is done', True, 0),
 ('southern pacific', 'fotos/sp_0.jpg', '1870s', 'SOUTHERN PACIFIC', 'the second railroad', True, 0),
 ('chesapeake and ohio', 'fotos/co_0.jpg', '1880s', 'CHESAPEAKE AND OHIO', 'the east coast link', True, 0),
 ('newport news', 'fotos/newport_0.jpg', '1886', 'NEWPORT NEWS SHIPYARD', 'one of the greatest', True, 0),
 ('the octopus', 'fotos/octopus_0.jpg', '1882', 'THE OCTOPUS', 'the railroad as a villain', True, 0),
 ('frank norris', 'fotos/norris_0.jpg', '1901', 'FRANK NORRIS', 'wrote The Octopus', True, 0),
 ('arabella', 'people/arabella.jpg', '1851 – 1924', 'ARABELLA HUNTINGTON', 'his second wife', True, 0),
 ('henry huntington', 'people/henry.jpg', '1850 – 1927', 'HENRY HUNTINGTON', 'the nephew who inherited', True, 0),
 ('huntington library', 'fotos/library_0.jpg', '1919', 'HUNTINGTON LIBRARY', 'in San Marino, California', True, 0)]
#--EMPH
EMPH = [("they are insane", "THEY CALLED", "HIM INSANE"), ("persistence beats pedigree", "PERSISTENCE", "BEATS PEDIGREE"), ("bribes", "THE PRICE OF", "FAVORS"),
        ("a man had to love his job", "LOVE THE JOB", ""), ("hated by half of california", "HATED BY", "HALF OF CALIFORNIA"), ("the octopus", "THE", "OCTOPUS")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "dark", 5: "triumph", 6: "reflect", 7: "reflect"}
TRG = [("eighteen sixty-three a forty-one-year-old", "tense"), ("collis potter huntington was born", "sad"), ("at sixteen he became", "drive"), ("in eighteen forty-nine huntington set out", "wonder"),
       ("in eighteen sixty a young engineer", "wonder"), ("it was the most important job", "drive"), ("during the years of construction", "dark"), ("after the transcontinental line", "triumph"),
       ("his private life was complicated", "dark"), ("he died on august thirteenth", "sad"), ("the second is that persistence", "reflect")]
TWISTS = ["nearly every banker in the city has told him that his plan is insane", "he won the pacific railway act", "after the transcontinental line huntington looked south", "he died on august thirteenth", "the second is that persistence"]
#--NSC
74
#--MAP
MAPBRT = [("collis potter huntington was born on october", lambda u: g_map(u, -73.06, 41.76, "HARWINTON, CONNECTICUT", "UNITED STATES  ·  1821"), 7.0)]
#--KW
{"A hardware merchant with surveying": "sierra_0", "Bankers shaking their heads": "sf_0", "A tinsmith's workshop": "harwinton_0", "A teenage peddler": "harwinton_1", "A tiny store on a village": "harwinton_2",
 "A ship leaving New York harbor": "panama_0", "The Panama jungle": "panama_1", "San Francisco harbor full": "sf_1", "Four men shaking hands": "bigfour_0", "A man walking into the US Capitol": "lincoln_0",
 "Lincoln signing the Pacific": "lincoln_1", "Two rail lines meeting": "promontory_0", "A railroad line crossing the Arizona": "sp_0", "A coal train crossing West Virginia": "co_0",
 "A huge shipyard": "newport_0", "A cartoon of a giant octopus": "octopus_0", "A mansion drawing room filled with art": "arabella_0", "A nephew taking over": "henry_0"}
