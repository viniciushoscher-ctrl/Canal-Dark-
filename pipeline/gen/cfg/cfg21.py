#--KEY
KEY = {"musk", "elon", "spacex", "tesla", "rocket", "falcon", "orbit", "nasa", "paypal", "zip2", "starlink", "mars", "million", "billion", "bankruptcy", "payroll", "electric", "twitter", "richest", "dragon"}
#--CH
CH = [("CHAPTER 1", "THE BULLIED BOY", "FROM PRETORIA"), ("CHAPTER 2", "THE INTERNET", "MILLIONAIRE"), ("CHAPTER 3", "TWO IMPOSSIBLE", "COMPANIES"),
      ("CHAPTER 4", "THE DARKEST", "MONTH"), ("CHAPTER 5", "RUSHING TO", "ORBIT"), ("CHAPTER 6", "THE RICHEST", "PERSON ON EARTH"), ("THE LESSON", "THE LINE BETWEEN", "FOOL AND VISIONARY")]
CARDS = [("elon reeve musk was born on june", "1971", "MUSK IS BORN", "Pretoria, South Africa", None),
         ("in nineteen ninety-nine compaq bought", "1999", "ZIP2 IS SOLD", "$307 million", None),
         ("in two thousand two musk founded spacex", "2002", "SPACEX IS FOUNDED", "to make rockets cheap", None),
         ("on september twenty-eighth the fourth", "2008", "ORBIT", "Falcon 1 succeeds", None),
         ("in two thousand fifteen one of its rockets", "2015", "THE LANDING", "a rocket lands upright", None),
         ("by the end of two thousand twenty-one musk", "2021", "RICHEST PERSON", "over $300 billion", None),
         ("musk now speaks about colonizing mars", "TODAY", "THE MARS PLAN", "Starship and beyond", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("compaq bought zip2 for three hundred", g_zip2, 5.5), ("one point six billion dollars", g_nasa, 5.5), ("the first rocket the falcon one failed", g_fail, 6.0),
       ("a rocket sits on a tiny island", FFg("rocket"), 5.5), ("dragon capsule", FFg("space"), 5.5), ("an electric car startup", FFg("car"), 5.5),
       ("slept on the factory floor", FFg("factory"), 5.5), ("satellite network", FFg("satellite"), 5.5), ("colonizing mars", FFg("mars"), 5.5), ("mission control", FFg("mission"), 5.0)] + MAPBRT
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is elon musk', 'fotos/m1_0.jpg', '1971 –', 'ELON MUSK', 'the man who bet everything on two dreams', True, 0),
 ('pretoria', 'fotos/pretoria_0.jpg', '1971', 'PRETORIA', 'where Musk grew up', True, 0),
 ('his father errol', 'fotos/errol_0.jpg', '1970s', 'ERROL MUSK', 'an engineer from South Africa', True, 0),
 ('maye', 'fotos/maye_0.jpg', '1971', 'MAYE MUSK', 'his mother', True, 0),
 ('university of pennsylvania', 'fotos/penn_0.jpg', '1992', 'UNIVERSITY OF PENNSYLVANIA', 'physics and economics', True, 0),
 ('his brother kimbal', 'fotos/kimbal_0.jpg', '1995', 'KIMBAL MUSK', 'co-founder of Zip2', True, 0),
 ('x dot com', 'fotos/paypal_0.jpg', '1999', 'PAYPAL', 'the bank that became PayPal', True, 0),
 ('peter thiel', 'fotos/thiel_0.jpg', '2000', 'PETER THIEL', 'a PayPal co-founder', True, 0),
 ('omelek', 'fotos/omelek_0.jpg', '2008', 'OMELEK ISLAND', 'the launch site', True, 0),
 ('the falcon one', 'fotos/falcon1_0.jpg', '2008', 'FALCON 1', 'the first to reach orbit', True, 0),
 ('the roadster', 'fotos/roadster_0.jpg', '2008', 'TESLA ROADSTER', 'the first Tesla', True, 0),
 ('nasa announced a contract', 'fotos/nasa_0.jpg', '2008', 'NASA', 'the contract that saved SpaceX', True, 0),
 ('dragon capsule', 'fotos/dragon_0.jpg', '2012', 'DRAGON', 'first private craft to the station', True, 0),
 ('landed upright', 'fotos/falcon9_0.jpg', '2015', 'FALCON 9', 'the first upright landing', True, 0),
 ('the model three', 'fotos/model3_0.jpg', '2017', 'MODEL 3', 'production hell', True, 0),
 ('neuralink', 'fotos/neuralink_0.jpg', '2016', 'NEURALINK', 'brains to computers', True, 0),
 ('starlink', 'fotos/starlink_0.jpg', '2020', 'STARLINK', 'satellite internet', True, 0)]
#--EMPH
EMPH = [("if this launch fails the company is finished", "ONE LAST", "LAUNCH"), ("it reaches orbit", "IT REACHES", "ORBIT"), ("tesla could not make payroll", "NO MONEY", "FOR PAYROLL"),
        ("a hundred million dollars of his own money", "$100 MILLION", "OF HIS OWN"), ("production hell", "PRODUCTION", "HELL"), ("the line between a visionary and a fool", "VISIONARY", "OR FOOL?")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "dark", 4: "triumph", 5: "upbeat", 6: "wonder", 7: "reflect"}
TRG = [("two thousand eight a rocket sits", "tense"), ("elon reeve musk was born", "sad"), ("in nineteen ninety-five musk", "drive"), ("in two thousand two musk founded", "wonder"),
       ("december two thousand eight was the darkest", "dark"), ("then on september twenty-eighth", "triumph"), ("the next ten years", "drive"), ("musk's rockets were now reusable", "upbeat"),
       ("by the end of two thousand twenty-one", "triumph"), ("he kept making bold bets", "wonder"), ("the second is that extreme", "reflect")]
TWISTS = ["it is the fourth attempt", "december two thousand eight was the darkest month", "then on september twenty-eighth the fourth falcon one reached orbit", "by the end of two thousand twenty-one", "the second is that extreme"]
#--NSC
80
#--MAP
MAPBRT = [("elon reeve musk was born on june", lambda u: g_map(u, 28.19, -25.75, "PRETORIA, SOUTH AFRICA", "SOUTH AFRICA  ·  1971"), 7.0)]
#--KW
{"A rocket on a launch pad": "omelek_0", "Engineers watching a launch": "falcon1_0", "A South African suburb": "pretoria_0", "A teenager with a backpack": "penn_0",
 "The University of Pennsylvania": "penn_1", "Silicon Valley startup office": "zip2_0", "An internet bank startup": "paypal_0", "An aerospace workshop": "falcon1_1",
 "An electric sports car": "roadster_0", "A rocket reaching orbit": "falcon1_2", "A capsule docking": "dragon_0", "A rocket landing upright": "falcon9_0", "A factory with robots": "factory_0",
 "A fleet of electric cars": "model3_0", "A brain scan": "neuralink_0", "A social network logo": "twitter_0", "Satellites launching": "starlink_0", "A red planet": "starship_0"}
