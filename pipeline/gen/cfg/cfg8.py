#--KEY
KEY = {"getty", "oil", "million", "billion", "ransom", "ear", "kidnapped", "richest", "desert", "fortune", "died", "grandson", "refused", "dollars", "telephone", "pay", "miser", "museum", "paul"}
#--CH
CH = [("CHAPTER 1", "THE OIL BOY", "FROM MINNEAPOLIS"), ("CHAPTER 2", "THE PLAYBOY", "WHO CAME BACK"), ("CHAPTER 3", "THE BET ON", "THE DESERT"),
      ("CHAPTER 4", "THE PAY PHONE", "BILLIONAIRE"), ("CHAPTER 5", "THE RULES OF", "A MISER"), ("CHAPTER 6", "THE PRICE OF", "THE RANSOM"), ("THE LESSON", "THE COST OF", "COUNTING COINS")]
CARDS = [("jean paul getty was born on december", "1892", "J. PAUL GETTY IS BORN", "Minneapolis, Minnesota", None),
         ("a well he had a stake in came in", "1916", "FIRST MILLION", "at age 24", None),
         ("in nineteen forty-nine getty took", "1949", "THE NEUTRAL ZONE", "Saudi Arabia and Kuwait", None),
         ("in nineteen fifty-three the well finally", "1953", "OIL!", "after four years of dry holes", None),
         ("in nineteen fifty-seven fortune magazine", "1957", "RICHEST AMERICAN", "about $1 billion", None),
         ("then in july nineteen seventy-three", "1973", "THE KIDNAPPING", "Rome · $17 million ransom", None),
         ("on june sixth nineteen seventy-six", "1976", "GETTY DIES", "aged 83 · about $2 billion", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("a sixteen-year-old boy is dragged", FFg("car"), 5.5), ("a package arrives at a newspaper", FFg("newspaper"), 5.5), ("in a single year he made his first million", g_million, 5.0),
       ("a payment of nine and a half million dollars", g_neutral, 5.0), ("he went to the middle east", FFg("plane"), 5.5), ("about one billion dollars", g_fortune, 5.0),
       ("moved to england and bought a tudor mansion", FFg("mansion"), 5.5), ("the kidnappers demanded seventeen million", g_ransom, 5.0),
       ("oil fever was sweeping", FFg("train"), 5.5), ("pacific western oil", FFg("ship"), 5.5), ("newspapers called him the miser", FFg("newspaper", 1), 5.0),
       ("a collector with a passion", FFg("mansion", 1), 5.0)] + MAPBRT
#--PHOTOS
PHOTOS = [
 ('his name is jean paul getty', 'people/getty.jpg', '1892 – 1976', 'J. PAUL GETTY', 'the richest private citizen in America', True, 0),
 ('his father george', 'people/georgef.jpg', 'HIS FATHER', 'GEORGE GETTY', 'lawyer and oilman', True, 0),
 ('the saudi king', 'people/abdulaziz.jpg', '1949', 'KING IBN SAUD', 'wanted money for his kingdom', True, 0),
 ('the neutral zone', 'fotos/neutral_0.jpg', '1949', 'THE NEUTRAL ZONE', 'between Saudi Arabia and Kuwait', False, 0),
 ('a tudor mansion called sutton place', 'fotos/sutton2_0.jpg', '1959', 'SUTTON PLACE', 'a Tudor mansion near London', False, 0),
 ('his grandson paul the third', 'people/gettyiii.jpg', '1973', 'JOHN PAUL GETTY III', 'kidnapped at sixteen', True, 0),
 ('a replica of an ancient roman villa', 'fotos/gettyvilla2_0.jpg', '1974', 'THE GETTY VILLA', 'Malibu, California', False, 0),
 ('he died on june sixth', 'people/getty.jpg', '1892 – 1976', 'J. PAUL GETTY', 'the richest man who counted every coin', True, 0)]
#--EMPH
EMPH = [("fourteen other grandchildren", "14 OTHER", "GRANDCHILDREN"), ("a human ear", "A HUMAN", "EAR"), ("nine and a half million dollars", "$9.5 MILLION", "UP FRONT"),
        ("his company drilled and found nothing", "4 YEARS", "NOTHING"), ("a pay telephone for guests", "A PAY PHONE", "FOR GUESTS"), ("at four percent interest", "4%", "INTEREST"),
        ("patience beats panic", "PATIENCE", "BEATS PANIC")]
#--MUSIC
DEF = {0: "tense", 1: "wonder", 2: "drive", 3: "triumph", 4: "upbeat", 5: "dark", 6: "dark", 7: "reflect"}
TRG = [("a sixteen-year-old boy", "tense"), ("his name is jean paul getty", "dark"), ("jean paul getty was born", "wonder"), ("in nineteen fifteen paul went", "drive"),
       ("at twenty-four with a million dollars", "upbeat"), ("in the nineteen thirties", "tense"), ("the next move changed everything", "tense"),
       ("for four years", "dark"), ("the well finally came in", "triumph"), ("in nineteen fifty-seven", "upbeat"), ("getty lived by strict rules", "dark"),
       ("then in july nineteen seventy-three", "tense"), ("only then did getty relent", "dark"), ("three years later", "sad"), ("getty left most of his wealth", "reflect"),
       ("the second is the cost", "dark")]
TWISTS = ["instead he says he has fourteen other", "the well finally came in", "then in july nineteen seventy-three", "only then did getty relent", "the second is the cost"]
#--NSC
81
#--MAP
MAPBRT = [("jean paul getty was born on december", lambda u: g_map(u, -93.27, 44.98, "MINNEAPOLIS, MINNESOTA", "UNITED STATES  ·  1892"), 7.0)]
#--KW
{"A Minneapolis street": "minneapolis_0", "An English Tudor mansion": "sutton2_0", "A Roman villa replica": "gettyvilla2_0", "Marble statues in a sunlit": "gettyvilla2_1",
 "A narrow Roman street": "rome_0", "Rain on a dark Roman": "rome_1", "An oil refinery": "gettyoil2_2", "A grand villa courtyard": "gettyvilla2_3", "A museum entrance": "gettyvilla_0",
 "Snow on the grounds": "sutton_0", "A boy's empty school desk": "paulIII_0", "A sealed envelope on a newspaper": "rome_2"}
