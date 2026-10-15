#--KEY
KEY = {"onassis", "aristotle", "tanker", "tankers", "ships", "ship", "smyrna", "callas", "jackie", "yacht", "christina", "olympic", "skorpios", "million", "dollars", "oil", "saudi", "alexander", "fleet", "freighters", "refugee"}
#--CH
CH = [("CHAPTER 1", "THE BURNING", "OF SMYRNA"), ("CHAPTER 2", "SIXTY DOLLARS", "AND SIX SHIPS"), ("CHAPTER 3", "THE LORD OF", "THE TANKERS"),
      ("CHAPTER 4", "THE OIL", "GAMBLE"), ("CHAPTER 5", "YACHTS, STARS,", "AND CALLAS"), ("CHAPTER 6", "THE WIDOW", "AND THE SON"), ("THE LESSON", "BUY WHEN", "THEY PANIC")]
CARDS = [("aristotelis sokratis onassis was born", "1906", "ONASSIS IS BORN", "Smyrna, Ottoman Empire", None),
         ("in nineteen twenty-three at seventeen", "1923", "BUENOS AIRES", "$60 and no friends", None),
         ("in nineteen thirty-three the world", "1933", "SIX FREIGHTERS", "bought at scrap price", None),
         ("his boldest deal came", "1954", "THE JEDDAH AGREEMENT", "the Saudi oil gamble", None),
         ("in nineteen fifty-six onassis took control", "1956", "MONTE CARLO", "the casino and the yacht", None),
         ("in nineteen sixty-eight onassis married", "1968", "THE WEDDING", "Jackie Kennedy", None),
         ("he died in paris on march", "1975", "ONASSIS DIES", "age 69", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("with about sixty dollars", g_sixty, 5.5), ("six canadian freighters", g_freighters, 6.0), ("he owned over a hundred ships", g_fleet, 5.5),
       ("convoy", FFg("war"), 5.0), ("the largest tankers ever built", FFg("tanker"), 5.5), ("winston churchill sailed on it", FFg("yacht"), 5.5),
       ("bought the greek national airline", FFg("plane"), 5.5), ("married jacqueline kennedy", FFg("wedding"), 5.5), ("a hundred ships", FFg("ship"), 5.0)] + MAPBRT
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is aristotle onassis', 'people/onassis.jpg', '1906 – 1975', 'ARISTOTLE ONASSIS', 'the poor refugee who ruled the sea', True, 0),
 ('the city was burned', 'fotos/smyrna_0.jpg', '1922', 'THE FIRE OF SMYRNA', 'the city Onassis fled', True, 0),
 ('buenos aires argentina', 'fotos/buenos_0.jpg', '1923', 'BUENOS AIRES', 'where he started again', True, 0),
 ('turkish tobacco', 'fotos/tobacco_0.jpg', '1927', 'TOBACCO', 'his first fortune', True, 0),
 ('six canadian freighters', 'fotos/freighter_0.jpg', '1933', 'THE FREIGHTERS', 'bought for scrap price', True, 0),
 ('flags of convenience', 'fotos/oil_0.jpg', '1950s', 'THE TANKER FLEET', 'the largest private fleet', True, 0),
 ('the king of saudi arabia', 'fotos/saudi_0.jpg', '1954', 'KING SAUD', 'the Jeddah Agreement', True, 0),
 ('the casino of monte carlo', 'fotos/rainier_0.jpg', '1956', 'PRINCE RAINIER', 'the ruler of Monaco', True, 0),
 ('winston churchill', 'people/churchill.jpg', '1958', 'WINSTON CHURCHILL', 'a guest on the Christina', True, 0),
 ('maria callas', 'people/callas.jpg', '1923 – 1977', 'MARIA CALLAS', 'the opera singer he loved', True, 0),
 ('the greek national airline', 'fotos/olympic_0.jpg', '1957', 'OLYMPIC AIRWAYS', 'bought by Onassis', True, 0),
 ('skorpios', 'fotos/skorpios_0.jpg', '1963', 'SKORPIOS', 'his private island', True, 0),
 ('jacqueline kennedy', 'people/jackie.jpg', '1968', 'JACQUELINE KENNEDY', 'married Onassis in 1968', True, 0),
 ('his only son alexander', 'fotos/alexander_0.jpg', '1948 – 1973', 'ALEXANDER ONASSIS', 'died in a plane crash', True, 0),
 ('his daughter christina', 'fotos/christinaonassis_0.jpg', '1950 – 1988', 'CHRISTINA ONASSIS', 'the heiress', True, 0)]
#--EMPH
EMPH = [("sixty dollars", "SIXTY", "DOLLARS"), ("when each had cost a million to build", "$20,000", "EACH"), ("a boycott", "A BOYCOTT", "TO RUIN HIM"),
        ("the widow of the assassinated american president", "THE PRESIDENT'S", "WIDOW"), ("he died in paris", "HE DIED", "IN PARIS"), ("a crisis can be the best time to buy", "BUY IN", "A CRISIS")]
#--MUSIC
DEF = {0: "tense", 1: "dark", 2: "drive", 3: "upbeat", 4: "wonder", 5: "dark", 6: "sad", 7: "reflect"}
TRG = [("nineteen fifty-nine on a yacht", "tense"), ("aristotelis sokratis onassis was born", "sad"), ("that life ended in september", "dark"), ("in nineteen twenty-three at seventeen", "drive"),
       ("he was twenty-seven", "triumph"), ("his boldest deal came", "tense"), ("onassis fought back", "dark"), ("in nineteen fifty-six onassis took control", "wonder"),
       ("in nineteen sixty-eight onassis married", "dark"), ("in nineteen seventy-three his only son", "sad"), ("he died in paris", "sad"), ("the second is that a great fortune", "reflect")]
TWISTS = ["that life ended in september", "he was twenty-seven", "but the deal collapsed", "in nineteen seventy-three his only son", "he died in paris on march"]
#--NSC
72
#--MAP
MAPBRT = [("aristotelis sokratis onassis was born", lambda u: g_map(u, 27.14, 38.42, "SMYRNA (IZMIR)", "OTTOMAN EMPIRE  ·  1906"), 7.0)]
#--KW
{"A burning harbor city": "smyrna_0", "A crowd of refugees": "smyrna2_0", "A grand Ottoman merchant house": "izmir_0", "A tobacco merchant's warehouse": "tobacco_0",
 "Buenos Aires port": "buenos_0", "Rusty freighters": "freighter_0", "A huge tanker launched": "oil_1", "A Saudi desert oil field": "saudi_0", "Monte Carlo casino": "rainier_1",
 "A luxury yacht sailing": "sinatra_0", "An airline passenger plane": "olympic_0", "A private Greek island": "skorpios_0", "A lavish wedding": "jackie2_0", "A small plane wreck": "alexander_1",
 "A hospital room in Paris": "paris_0"}
