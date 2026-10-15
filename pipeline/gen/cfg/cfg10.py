#--KEY
KEY = {"mellon", "bank", "aluminum", "alcoa", "oil", "tax", "treasury", "gallery", "painting", "paintings", "million", "richest", "scandal", "divorce", "crash", "free", "rembrandt", "debt"}
#--CH
CH = [("CHAPTER 1", "THE JUDGE'S", "QUIET SON"), ("CHAPTER 2", "THE SILENT", "PARTNER"), ("CHAPTER 3", "A COLD", "MARRIAGE"),
      ("CHAPTER 4", "THREE PRESIDENTS,", "ONE MINISTER"), ("CHAPTER 5", "BLAMED FOR", "THE CRASH"), ("CHAPTER 6", "THE SECRET", "PAINTINGS"), ("THE LESSON", "FUND THE", "OTHERS")]
CARDS = [("andrew william mellon was born on march", "1855", "MELLON IS BORN", "Pittsburgh, Pennsylvania", None),
         ("in nineteen-oh-one a gusher in texas", "1901", "SPINDLETOP", "the birth of Gulf Oil", None),
         ("in nineteen twelve she asked", "1912", "THE DIVORCE", "a public scandal", None),
         ("in nineteen twenty-one newly elected", "1921", "SECRETARY OF THE TREASURY", "appointed by Harding", None),
         ("in october nineteen twenty-nine", "1929", "THE GREAT CRASH", "the Depression begins", None),
         ("in nineteen thirty-four the justice", "1934", "TAX EVASION TRIAL", "a political case", None),
         ("in nineteen forty-one the national gallery", "1941", "NATIONAL GALLERY OPENS", "free for everyone", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("pittsburgh was a smoky", FFg("pitt"), 5.5), ("created steel and coal", FFg("steel"), 5.0), ("gusher in texas", FFg("oil"), 5.5),
       ("the top income tax rate fell", g_tax, 5.5), ("reducing it by about a third", g_debt, 5.0), ("in october nineteen twenty-nine the stock market", FFg("wall"), 5.5),
       ("liquidate labor", FFg("depress"), 5.5), ("the price was about seven million", g_hermitage, 5.5), ("sending him to london", FFg("ship"), 5.5),
       ("men who had met kings", FFg("bank"), 5.0), ("a national gallery in washington", FFg("capitol"), 5.5), ("walk in and see a rembrandt", FFg("art"), 5.5)] + MAPBRT
#--PHOTOS
PHOTOS = [
 ('his name is andrew mellon', 'people/mellon.jpg', '1855 – 1937', 'ANDREW W. MELLON', 'the banker who owned Pittsburgh', True, 0),
 ('his father thomas mellon', 'people/thomas.jpg', '1813 – 1908', 'THOMAS MELLON', 'judge and banker', True, 0),
 ('charles martin hall', 'people/hall.jpg', '1863 – 1914', 'CHARLES M. HALL', 'inventor of cheap aluminum', True, 0),
 ('henry clay frick', 'people/frick.jpg', '1849 – 1919', 'HENRY CLAY FRICK', 'steel baron and friend', True, 0),
 ('nora mcmullen', 'fotos/nora_0.jpg', '1869 – 1973', 'NORA McMULLEN', 'his wife until 1912', True, 0),
 ('president warren harding', 'people/harding.jpg', '1921', 'WARREN G. HARDING', 'named Mellon to the Treasury', True, 0),
 ('harding coolidge and hoover', 'people/coolidge.jpg', '1920s', 'CALVIN COOLIDGE', 'one of three presidents he served', True, 0),
 ('herbert hoover later claimed', 'people/hoover.jpg', '1929', 'HERBERT HOOVER', 'sent Mellon to London', True, 0),
 ('then roosevelts government struck', 'people/fdr.jpg', '1934', 'FRANKLIN D. ROOSEVELT', 'his government charged Mellon', True, 0),
 ('paul', 'people/paul.jpg', '1907 – 1999', 'PAUL MELLON', 'his son and art patron', True, 0),
 ('a gusher in texas called spindletop', 'fotos/spindle_0.jpg', '1901', 'SPINDLETOP', 'the Texas gusher behind Gulf Oil', True, 0),
 ('from the hermitage museum', 'fotos/hermitage_0.jpg', '1930', 'THE HERMITAGE', 'Leningrad · source of the paintings', True, 0),
 ('rembrandt', 'fotos/rembrandt_0.jpg', '1655', 'REMBRANDT · POLISH RIDER', 'once owned by the Soviet state', True, 0),
 ('the national gallery of art opened', 'fotos/ng2_0.jpg', '1941', 'NATIONAL GALLERY OF ART', 'a gift to the American people', True, 0)]
#--EMPH
EMPH = [("three presidents served under him", "THREE PRESIDENTS", "SERVED HIM"), ("the best government was the one that stayed out of sight", "STAY OUT", "OF SIGHT"),
        ("liquidate labor", "LIQUIDATE", "EVERYTHING"), ("for seven million dollars", "$7 MILLION", "IN SECRET"), ("admission was free", "ADMISSION", "IS FREE"), ("see a rembrandt for free", "A REMBRANDT", "FOR FREE")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "dark", 4: "triumph", 5: "dark", 6: "wonder", 7: "reflect"}
TRG = [("nineteen thirty-five a frail", "tense"), ("andrew william mellon was born", "sad"), ("pittsburgh was a smoky", "drive"), ("his first big bet", "wonder"),
       ("but mellons private life", "sad"), ("in nineteen twenty-one newly", "triumph"), ("the economy boomed", "triumph"), ("then the crash came", "dark"),
       ("in london he found", "wonder"), ("then roosevelts government", "dark"), ("he died on august", "sad"), ("four years later in nineteen forty-one", "wonder"),
       ("the second is that a fortune", "reflect")]
TWISTS = ["his name is andrew mellon", "then the crash came", "then roosevelts government struck back", "he died on august twenty-sixth", "four years later in nineteen forty-one"]
#--NSC
75
#--MAP
MAPBRT = [("andrew william mellon was born on march", lambda u: g_map(u, -79.99, 40.44, "PITTSBURGH, PENNSYLVANIA", "UNITED STATES  ·  1855"), 7.0)]
#--KW
{"A federal courtroom with tall": "crash_1", "A marble Treasury building": "treasury_0", "A Pittsburgh steel city skyline": "pitt1_0", "A small family bank interior": "bank_0",
 "An aluminum smelter hall": "hall_1", "A Texas oil gusher": "spindle_1", "A coke oven battery": "koppers_0", "A Wall Street": "crash_0", "Wall Street stock exchange floor": "crash_2",
 "An empty bread line": "depression_0", "A transatlantic ocean liner": "london_0", "A Soviet museum hall": "hermitage_1", "A marble museum under construction": "ng_0",
 "The grand opening of a marble museum": "ng2_0", "The White House exterior": "harding_1", "A tax office": "treasury_1"}
