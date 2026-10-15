#--KEY
KEY = {"bezos", "jeff", "amazon", "books", "garage", "internet", "wall", "street", "regret", "prime", "aws", "cloud", "kindle", "blue", "origin", "rocket", "richest", "billion", "million", "customer", "mackenzie"}
#--CH
CH = [("CHAPTER 1", "THE UNICYCLIST'S", "SON"), ("CHAPTER 2", "THE SIX-FIGURE", "JOB HE QUIT"), ("CHAPTER 3", "A BOOKSTORE IN", "A GARAGE"),
      ("CHAPTER 4", "AMAZON", "DOT BOMB"), ("CHAPTER 5", "THE CLOUD", "BEHIND THE CART"), ("CHAPTER 6", "THE RICHEST MAN", "IN HISTORY"), ("THE LESSON", "THINK", "LONG TERM")]
CARDS = [("jeffrey preston jorgensen was born on january", "1964", "BEZOS IS BORN", "Albuquerque, New Mexico", None),
         ("in nineteen ninety-four while reading", "1994", "THE BIG IDEA", "web usage up 2,300%", None),
         ("amazon opened for business on july", "1995", "AMAZON OPENS", "Bellevue garage, Washington", None),
         ("the dot-com crash in two thousand nearly", "2000", "THE DOT-COM CRASH", "stock falls to $6", None),
         ("in two thousand six amazon launched", "2006", "AMAZON WEB SERVICES", "the cloud begins", None),
         ("in two thousand eighteen bezos became", "2018", "RICHEST IN HISTORY", "over $150 billion", None),
         ("in july two thousand twenty-one bezos", "2021", "BEZOS STEPS DOWN", "flies to space", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("web usage was growing at twenty-three hundred", g_growth, 5.5), ("the stock fell from over a hundred dollars", g_stock, 5.5), ("fortune of over a hundred and fifty billion", g_fortune, 5.5),
       ("a mental trick", FFg("nyc"), 5.0), ("packages to the post office", FFg("truck"), 5.5), ("rent computing power", FFg("data"), 5.5),
       ("blue origin", FFg("rocket"), 5.5), ("edge of space", FFg("space"), 5.5), ("moved to seattle", FFg("seattle"), 5.0)] + MAPBRT
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is jeff bezos', 'people/bezos.jpg', '1964 –', 'JEFF BEZOS', 'the man who quit Wall Street for books', True, 0),
 ('a cuban immigrant named miguel bezos', 'fotos/miguel_0.jpg', '1960s', 'MIGUEL BEZOS', 'his adoptive father', True, 0),
 ('a circus unicyclist', 'fotos/unicycle_0.jpg', '1964', 'THE UNICYCLIST', 'his biological father', True, 0),
 ('princeton', 'fotos/princeton_0.jpg', '1986', 'PRINCETON', 'electrical engineering', True, 0),
 ('d e shaw', 'fotos/deshaw_0.jpg', '1990', 'D. E. SHAW', 'the Wall Street job he left', True, 0),
 ('his wife mackenzie', 'people/mackenzie.jpg', '1993', 'MACKENZIE BEZOS', 'the co-founder who drove', True, 0),
 ('in the garage of a rented house', 'fotos/garage_0.jpg', '1994', 'THE GARAGE', 'Bellevue, Washington', True, 0),
 ('wooden doors', 'fotos/amazon2_0.jpg', '1995', 'EARLY AMAZON', 'the door-desk office', True, 0),
 ('amazon prime', 'fotos/prime_0.jpg', '2005', 'AMAZON PRIME', 'free two-day shipping', True, 0),
 ('amazon web services', 'fotos/aws_0.jpg', '2006', 'AMAZON WEB SERVICES', 'the cloud revolution', True, 0),
 ('the kindle', 'fotos/kindle_0.jpg', '2007', 'THE KINDLE', 'books become digital files', True, 0),
 ('the washington post', 'fotos/wapo_0.jpg', '2013', 'THE WASHINGTON POST', 'bought for $250 million', True, 0),
 ('whole foods', 'fotos/wholefoods_0.jpg', '2017', 'WHOLE FOODS', 'bought for $13.7 billion', True, 0),
 ('the spheres', 'fotos/spheres_0.jpg', '2018', 'THE SPHERES', 'Amazon headquarters, Seattle', True, 0),
 ('blue origin rocket', 'fotos/shepard_0.jpg', '2021', 'NEW SHEPARD', 'Blue Origin\'s rocket', True, 0)]
#--EMPH
EMPH = [("regret minimization framework", "REGRET", "MINIMIZATION"), ("he has not failed", "10,000 WAYS", "THAT FAIL"), ("a seventy percent chance they would lose it all", "70% CHANCE", "OF LOSING IT ALL"),
        ("day one", "IT IS STILL", "DAY ONE"), ("amazon dot bomb", "AMAZON", "DOT BOMB"), ("think long-term", "THINK", "LONG TERM")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "dark", 5: "triumph", 6: "upbeat", 7: "reflect"}
TRG = [("nineteen ninety-four a thirty-year-old", "tense"), ("jeffrey preston jorgensen was born", "sad"), ("bezos studied electrical", "drive"), ("in nineteen ninety-four while reading", "wonder"),
       ("bezos raised about a million", "drive"), ("amazon opened for business", "triumph"), ("the dot-com crash in two thousand", "dark"), ("in two thousand one amazon", "wonder"),
       ("bezos's next idea", "triumph"), ("in two thousand eighteen bezos", "upbeat"), ("in two thousand nineteen his divorce", "sad"), ("the second is to make decisions", "reflect")]
TWISTS = ["so he quits", "the dot-com crash in two thousand nearly killed amazon", "in two thousand one amazon finally reported a profit", "in two thousand nineteen his divorce", "the second is to make decisions"]
#--NSC
75
#--MAP
MAPBRT = [("jeffrey preston jorgensen was born on january", lambda u: g_map(u, -106.65, 35.08, "ALBUQUERQUE, NEW MEXICO", "UNITED STATES  ·  1964"), 7.0)]
#--KW
{"A young man in a suit leaving": "deshaw_0", "A walk through Central Park": "princeton_0", "A man typing a business plan": "garage_0", "A circus unicyclist": "unicycle_0",
 "A Cuban airlift": "cuba_0", "Princeton University campus": "princeton_1", "A hedge fund office": "deshaw_1", "A Seattle garage with desks": "garage_1", "Warehouse workers packing": "amazon2_0",
 "A warehouse the size of a stadium": "amazon2_1", "A stock market crash with a falling": "dotcom_0", "A package delivered": "prime_0", "A data center": "aws_0", "A startup founder": "kindle_0",
 "A newspaper newsroom": "wapo_0", "A grocery store aisle": "wholefoods_0", "A rocket launch pad": "shepard_0", "A small capsule landing": "shepard_1", "A glass tower campus": "hq_0"}
