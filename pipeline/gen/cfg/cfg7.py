#--KEY
KEY = {"hughes", "howard", "million", "billion", "crash", "crashed", "fire", "flames", "record", "spruce", "goose", "germs", "hotel", "vegas", "died", "fortune", "plane", "airplane", "speed", "hollywood", "twa", "alone", "fear", "richest"}
#--CH
CH = [("CHAPTER 1", "THE ORPHAN WITH", "THE DRILL BIT"), ("CHAPTER 2", "THE HOLLYWOOD", "GAMBLER"), ("CHAPTER 3", "THE FASTEST MAN", "ON EARTH"),
      ("CHAPTER 4", "THE SPRUCE", "GOOSE"), ("CHAPTER 5", "THE EMPIRE", "AND THE FEAR"), ("CHAPTER 6", "THE LAST", "HOTEL ROOM"), ("THE LESSON", "THE PRICE OF", "NO LIMITS")]
CARDS = [("howard hughes was born on christmas eve", "1905", "HOWARD HUGHES IS BORN", "Houston, Texas", None),
         ("in nineteen thirty-two hughes started", "1932", "HUGHES AIRCRAFT", "the fastest plane in the world", None),
         ("in nineteen thirty-five he flew", "1935", "THE H-1 RACER", "352 mph world record", None),
         ("then in nineteen thirty-eight he did", "1938", "AROUND THE WORLD", "3 days, 19 hours, 17 minutes", None),
         ("in nineteen forty-six hughes was testing", "1946", "THE XF-11 CRASH", "Beverly Hills", None),
         ("on november second nineteen forty-seven", "1947", "THE SPRUCE GOOSE FLIES", "about a mile over Long Beach", None),
         ("in nineteen sixty-six he sold", "1966", "TWA SOLD", "about $550 million", None),
         ("he died on april fifth", "1976", "HOWARD HUGHES DIES", "on a flight to Houston", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("a burning airplane tears through", FFg("plane"), 5.5), ("he moved to hollywood", FFg("hollywood"), 5.5), ("he bought dozens of real planes", FFg("aviation"), 5.5),
       ("set a new world speed record", g_speed, 5.0), ("three days nineteen hours", g_world, 5.0), ("new york gave him a ticker tape parade", FFg("parade"), 5.5),
       ("the senate was investigating", FFg("senate"), 5.5), ("the spruce goose which everyone had mocked", FFg("flying"), 5.5),
       ("five hundred and fifty million dollars", g_twa, 5.0), ("he arrived in las vegas", FFg("vegas"), 5.5), ("he weighed about ninety pounds", g_weight, 5.0),
       ("hospital bed with controls", FFg("hospital"), 5.0), ("an oil", FFg("oil"), 5.0), ("he spent months in bed", FFg("hospital", 1), 5.0)] + MAPBRT
#--PHOTOS
PHOTOS = [
 ('his name is howard hughes', 'people/hughes.jpg', '1905 – 1976', 'HOWARD HUGHES', 'aviator, filmmaker, billionaire', True, 0),
 ('his father howard senior', 'fotos/sr_0.jpg', 'HIS FATHER', 'HOWARD HUGHES SR.', 'inventor of the drill bit', True, 0),
 ('hell\'s angels was a war epic', 'fotos/hellsangels_0.jpg', '1930', "HELL'S ANGELS", 'nearly $4 million', True, 0),
 ('jean harlow', 'people/harlow.jpg', '1930', 'JEAN HARLOW', 'launched by Hughes', True, 0),
 ('produced scarface', 'fotos/scarface_0.jpg', '1932', 'SCARFACE', 'banned in several states', True, 0),
 ('katharine hepburn', 'people/hepburn.jpg', '1930s', 'KATHARINE HEPBURN', 'one of his famous romances', True, 0),
 ('ava gardner', 'people/gardner.jpg', '1940s', 'AVA GARDNER', 'another Hollywood star', True, 0),
 ('the hughes h-1 racer', 'fotos/h1racer_0.jpg', '1935', 'THE H-1 RACER', 'flush rivets, record speed', True, 0),
 ('the press called it the spruce goose', 'fotos/spruce3_0.jpg', '1947', 'THE SPRUCE GOOSE', 'the largest wooden aircraft ever flown', True, 0),
 ('the airline twa', 'fotos/twa_3.jpg', 'TWA', 'CONSTELLATION', "Hughes's airline", True, 0),
 ('the glomar explorer', 'fotos/glomar_1.jpg', '1974', 'THE GLOMAR EXPLORER', 'built under Hughes\'s name', False, 0),
 ('he died on april fifth', 'people/hughes.jpg', '1905 – 1976', 'HOWARD HUGHES', 'the richest man who could not open a door', True, 0)]
#--EMPH
EMPH = [("he crashed his own experimental plane", "HE CRASHED", "HIS OWN PLANE"), ("three hundred and fifty-two miles per hour", "352 MPH", "WORLD RECORD"),
        ("three days nineteen hours", "3 DAYS", "19 HOURS"), ("which everyone had mocked had flown", "THE SPRUCE GOOSE", "FLEW"),
        ("five hundred and fifty million dollars", "$550 MILLION", "IN CASH"), ("he weighed about ninety pounds", "90", "POUNDS"),
        ("could not walk through a door", "COULD NOT WALK", "THROUGH A DOOR")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "triumph", 4: "wonder", 5: "dark", 6: "sad", 7: "reflect"}
TRG = [("a burning airplane", "tense"), ("his name is howard hughes", "dark"), ("howard hughes was born on", "sad"), ("hughes wanted to make movies", "drive"),
       ("in nineteen thirty-two hughes", "triumph"), ("he flew around the world", "triumph"), ("during the second world war", "tense"), ("the project was a disaster", "dark"),
       ("he did the impossible", "triumph"), ("after the crash in nineteen forty-six", "dark"), ("he became obsessed with germs", "dark"), ("in his last years", "sad"),
       ("he died on april fifth", "sad"), ("howard hughes lived a spectacular life", "reflect"), ("second a fortune is not freedom", "dark")]
TWISTS = ["instead they find a thin tall man", "he did the impossible", "he became obsessed with germs", "he died on april fifth", "second a fortune is not freedom"]
#--NSC
77
#--MAP
MAPBRT = [("howard hughes was born on christmas eve", lambda u: g_map(u, -95.37, 29.76, "HOUSTON, TEXAS", "UNITED STATES  ·  1905"), 7.0)]
#--KW
{"A burning small airplane": "xf11_0", "A Houston oil derrick": "oil_0", "A steel rotary drill bit": "tool1_1", "A cluttered garage workshop": "houston_0",
 "Rows of First World War biplanes": "hellsangels_3", "A film editing room": "harlow_1", "A crowded movie theater": "scarface_0", "A sleek single-engine racing": "h1racer_0",
 "An aircraft design office": "h1_0", "A wartime aircraft factory": "spruce_1", "A giant flying boat on calm water": "spruce3_0", "Las Vegas strip at night": "vegas2_0",
 "A penthouse floor": "lasvegas3_0", "An airline office": "twa_3", "A giant ship in a harbor": "glomar_0", "The deck of a huge ship": "glomar_1",
 "A flying boat in a museum hangar": "museum_1", "A small private jet": "twa_2", "A room full of film reels": "ha_3"}
