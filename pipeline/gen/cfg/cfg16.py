#--KEY
KEY = {"kroc", "ray", "mcdonald", "mcdonalds", "brothers", "burger", "burgers", "franchise", "milkshake", "multimixer", "restaurants", "land", "real", "estate", "million", "royalty", "handshake", "system", "persistence"}
#--CH
CH = [("CHAPTER 1", "THE LEMONADE", "BOY"), ("CHAPTER 2", "THE MILKSHAKE", "SALESMAN"), ("CHAPTER 3", "THE LINE IN", "SAN BERNARDINO"),
      ("CHAPTER 4", "THE SYSTEM", "IS THE STAR"), ("CHAPTER 5", "THE REAL ESTATE", "SECRET"), ("CHAPTER 6", "THE BROTHERS'", "BETRAYAL"), ("THE LESSON", "IT IS NEVER", "TOO LATE")]
CARDS = [("raymond albert kroc was born on october", "1902", "KROC IS BORN", "Oak Park, Illinois", None),
         ("then came the order from san bernardino", "1954", "SAN BERNARDINO", "the McDonald brothers' stand", None),
         ("on april fifteenth nineteen fifty-five", "1955", "DES PLAINES", "the first Kroc restaurant", None),
         ("in nineteen sixty-one kroc offered", "1961", "THE BUYOUT", "$2.7 million", None),
         ("in nineteen sixty-five mcdonald's went public", "1965", "THE IPO", "McDonald's goes public", None),
         ("in nineteen sixty-eight the big mac", "1968", "THE BIG MAC", "a new icon", None),
         ("ray kroc died on january", "1984", "KROC DIES", "age 81", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("on opening day sales were", g_opening, 5.5), ("two point seven million dollars", g_deal, 5.5), ("there are about forty thousand", g_growth, 5.5),
       ("drove into san bernardino", FFg("road"), 5.5), ("a line of customers", FFg("drive"), 5.5), ("food was served in paper wrappers", FFg("food"), 5.5),
       ("the stock market", FFg("stock"), 5.0), ("children", FFg("kids"), 5.0), ("lied about his age", FFg("ww1"), 5.0), ("suburb", FFg("suburb"), 5.0)] + MAPBRT
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is ray kroc', 'people/kroc.jpg', '1902 – 1984', 'RAY KROC', 'the milkshake salesman who built McDonald\'s', True, 0),
 ('oak park', 'fotos/oakpark_0.jpg', '1902', 'OAK PARK, ILLINOIS', 'where Kroc grew up', True, 0),
 ('walt disney', 'people/disney.jpg', '1918', 'WALT DISNEY', 'a fellow ambulance trainee', True, 0),
 ('lily-tulip cup', 'fotos/lily_0.jpg', '1920s', 'LILY-TULIP CUP', 'the paper cups he sold', True, 0),
 ('the multimixer', 'fotos/prince_0.jpg', '1939', 'EARL PRINCE', 'inventor of the Multimixer', True, 0),
 ('richard and maurice mcdonald', 'fotos/mcd_0.jpg', '1948', 'THE McDONALD BROTHERS', 'inventors of the Speedee system', True, 0),
 ('the speedee service system', 'fotos/speedee_0.jpg', '1948', 'SPEEDEE SERVICE SYSTEM', 'the assembly-line kitchen', True, 0),
 ('des plaines illinois', 'fotos/desplaines_0.jpg', '1955', 'DES PLAINES', 'the first Kroc restaurant', True, 0),
 ('hamburger university', 'fotos/franchise_0.jpg', '1961', 'HAMBURGER UNIVERSITY', 'training every franchisee', True, 0),
 ('harry sonneborn', 'fotos/sonneborn_0.jpg', '1956', 'HARRY SONNEBORN', 'the real estate idea', True, 0),
 ('the big mac', 'fotos/bigmac_0.jpg', '1968', 'THE BIG MAC', 'the icon of the menu', True, 0),
 ('ronald mcdonald', 'fotos/ronald_0.jpg', '1963', 'RONALD McDONALD', 'the clown symbol', True, 0),
 ('san diego padres', 'fotos/padres_0.jpg', '1974', 'SAN DIEGO PADRES', 'Kroc bought the team', True, 0),
 ('joan', 'people/joan.jpg', '1928 – 2003', 'JOAN KROC', 'his third wife and philanthropist', True, 0),
 ('the golden arches', 'fotos/arches_0.jpg', 'TODAY', 'THE GOLDEN ARCHES', 'about 40,000 restaurants', True, 0)]
#--EMPH
EMPH = [("eight of his machines at once", "EIGHT", "MACHINES"), ("the system", "THE SYSTEM", "IS THE STAR"), ("you are in the real estate business", "THE REAL ESTATE", "BUSINESS"),
        ("kroc never put it in writing", "NEVER PUT", "IN WRITING"), ("it is never too late", "NEVER", "TOO LATE"), ("persistence", "PERSISTENCE", "WINS")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "triumph", 5: "dark", 6: "upbeat", 7: "reflect"}
TRG = [("nineteen fifty-four a fifty-two", "tense"), ("raymond albert kroc was born", "sad"), ("for nearly twenty years", "drive"), ("then came the order from san bernardino", "wonder"),
       ("on april fifteenth", "triumph"), ("the turning point came", "drive"), ("in nineteen sixty-one kroc offered", "dark"), ("but there was a catch", "dark"),
       ("in nineteen sixty-five mcdonald's went public", "upbeat"), ("ray kroc died on january", "sad"), ("the warning is that success", "reflect")]
TWISTS = ["then came the order from san bernardino", "but there was a catch", "kroc never put it in writing", "ray kroc died on january", "the warning is that success"]
#--NSC
77
#--MAP
MAPBRT = [("raymond albert kroc was born on october", lambda u: g_map(u, -87.78, 41.89, "OAK PARK, ILLINOIS", "UNITED STATES  ·  1902"), 7.0)]
#--KW
{"A roadside hamburger stand": "speedee_0", "A kitchen assembly line": "speedee_1", "A suburb of Chicago": "oakpark_0", "A soda fountain counter": "shake_0", "A salesman with a case": "lily_0",
 "A milkshake mixing machine": "prince_1", "San Bernardino at noon": "mcd_1", "Two brothers at a counter": "mcd_2", "A contract being signed": "sonneborn_0", "A new drive-in restaurant": "desplaines_0",
 "A training class": "franchise_0", "A row of identical restaurants": "franchise_1", "A giant hamburger": "bigmac_0", "A baseball stadium": "padres_0", "A modern restaurant": "arches_0"}
