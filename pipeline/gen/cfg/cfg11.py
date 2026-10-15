#--KEY
KEY = {"frick", "coke", "coal", "steel", "carnegie", "homestead", "union", "pinkerton", "pinkertons", "strike", "shot", "killed", "million", "dollars", "mansion", "paintings", "museum", "will", "morgan", "assassin", "workers"}
#--CH
CH = [("CHAPTER 1", "THE ROCK", "NOBODY WANTED"), ("CHAPTER 2", "THE COKE", "KING"), ("CHAPTER 3", "THE BATTLE", "OF HOMESTEAD"),
      ("CHAPTER 4", "SHOT TWICE,", "STILL AT HIS DESK"), ("CHAPTER 5", "SEE YOU", "IN HELL"), ("CHAPTER 6", "THE PALACE", "OF ART"), ("THE LESSON", "LOOK", "NEXT TO YOU")]
CARDS = [("henry clay frick was born on december", "1849", "FRICK IS BORN", "West Overton, Pennsylvania", None),
         ("at twenty-one he borrowed", "1870", "THE FIRST OVENS", "borrowed from the Mellons", None),
         ("on the morning of july sixth", "1892", "THE BATTLE OF HOMESTEAD", "Pinkertons vs. steelworkers", None),
         ("on july twenty-third a young", "1892", "THE ATTEMPT", "shot twice, stabbed", None),
         ("in eighteen ninety-nine the two", "1899", "THE FEUD", "Carnegie vs. Frick", None),
         ("in nineteen thirteen he built", "1913", "THE FRICK MANSION", "Fifth Avenue, New York", None),
         ("he died on december second", "1919", "FRICK DIES", "his art goes to the public", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("coal in the eighteen seventies", FFg("coal"), 5.5), ("controlled about eighty percent", FFg("train"), 5.5), ("profits rose from about three", g_profit, 5.5),
       ("twelve-hour shifts", FFg("steel"), 5.5), ("three hundred armed guards", FFg("river"), 5.5), ("seven workers and three guards", g_homestead, 5.0),
       ("eight thousand state militia", FFg("soldiers"), 5.5), ("a deal worth more than four hundred million", g_deal, 5.5),
       ("moved to new york city", FFg("nyc"), 5.5), ("collecting paintings", FFg("art"), 5.5), ("thousands of steelworkers", FFg("crowd"), 5.0)] + MAPBRT
#--PHOTOS
PHOTOS = [
 ('his name is henry clay frick', 'people/frick.jpg', '1849 – 1919', 'HENRY CLAY FRICK', 'the coke king of Pittsburgh', True, 0),
 ('west overton pennsylvania', 'fotos/overton_0.jpg', '1849', 'WEST OVERTON', 'where Frick was born', True, 0),
 ('judge thomas mellon', 'people/mellon.jpg', '1870s', 'ANDREW MELLON', 'banker and lifelong friend', True, 0),
 ('coke ovens', 'fotos/coke_0.jpg', '1880s', 'CONNELLSVILLE COKE OVENS', 'the fuel that made steel', True, 0),
 ('andrew carnegie', 'people/carnegie.jpg', '1835 – 1919', 'ANDREW CARNEGIE', 'steel king and Frick\'s partner', True, 0),
 ('amalgamated association', 'fotos/union_0.jpg', '1892', 'THE UNION', 'Iron and Steel Workers', True, 0),
 ('barges up the river', 'fotos/barge_0.jpg', '1892', 'THE PINKERTON BARGES', 'Homestead, Pennsylvania', True, 0),
 ('alexander berkman', 'people/berkman.jpg', '1892', 'ALEXANDER BERKMAN', 'the anarchist who shot Frick', True, 0),
 ('j p morgan', 'people/morgan.jpg', '1837 – 1913', 'J. P. MORGAN', 'built U.S. Steel in 1901', True, 0),
 ('his daughter helen', 'people/helen.jpg', '1888 – 1984', 'HELEN CLAY FRICK', 'his surviving daughter', True, 0),
 ('fifth avenue at seventieth', 'fotos/mansion_0.jpg', '1913', 'THE FRICK MANSION', 'a palace for art', True, 0),
 ('vermeer', 'fotos/vermeer_0.jpg', '1650s', 'VERMEER', 'part of the Frick Collection', True, 0)]
#--EMPH
EMPH = [("a rock that everybody else ignored", "A ROCK", "NOBODY WANTED"), ("he locked them out", "HE LOCKED", "THEM OUT"), ("at least nine people are dead", "NINE", "DEAD"),
        ("he signed the letters on his desk first", "HE SIGNED", "THE LETTERS FIRST"), ("meet carnegie in hell", "SEE YOU", "IN HELL"), ("chose to give it all away", "GIVE IT", "ALL AWAY")]
#--MUSIC
DEF = {0: "tense", 1: "drive", 2: "dark", 3: "tense", 4: "dark", 5: "wonder", 6: "reflect", 7: "reflect"}
TRG = [("july sixth eighteen ninety-two", "tense"), ("henry clay frick was born", "sad"), ("coal in the eighteen seventies", "drive"), ("by thirty he was a millionaire", "triumph"),
       ("the union was called", "dark"), ("on the morning of july sixth", "dark"), ("then came the strangest event", "tense"), ("when doctors arrived", "wonder"),
       ("in eighteen ninety-nine the two", "dark"), ("it was the largest company", "triumph"), ("in nineteen-oh-five frick moved", "wonder"), ("he died on december second", "sad"),
       ("the second is that wealth", "reflect")]
TWISTS = ["a shot rang out", "berkman shot frick twice", "he died on december second", "his will was a surprise", "the second is that wealth"]
#--NSC
72
#--MAP
MAPBRT = [("henry clay frick was born on december", lambda u: g_map(u, -79.60, 40.10, "WEST OVERTON, PENNSYLVANIA", "UNITED STATES  ·  1849"), 7.0)]
#--KW
{"Barges drifting": "barge_0", "A crowd of steelworkers": "home_0", "A stone farmhouse": "overton_0", "An old whiskey distillery": "overton_1", "A coal mine entrance": "coke2_0",
 "Rows of beehive coke ovens": "coke_1", "A steel mill interior": "mill_0", "A tall wooden fence": "home_1", "Armed guards": "home2_0", "A smoky riverbank": "home_2",
 "Soldiers with rifles": "militia_0", "A closed union hall": "union_0", "A giant steel plant": "ussteel_0", "A mansion on Fifth Avenue": "mansion_0", "An art gallery with paintings": "mansion2_0",
 "A Pittsburgh office": "frickbldg_0", "A lawyer reading": "frickbldg_1"}
