#--KEY
KEY = {"hilton", "hotel", "hotels", "conrad", "waldorf", "astoria", "crash", "depression", "bankrupt", "bankruptcy", "million", "dollars", "lobby", "prayer", "borrowed", "bellboy", "mobley", "statler", "creditors", "word"}
#--CH
CH = [("CHAPTER 1", "THE BOARDINGHOUSE", "BOY"), ("CHAPTER 2", "THE HOTEL", "BY ACCIDENT"), ("CHAPTER 3", "A HILTON IN", "EVERY TEXAS TOWN"),
      ("CHAPTER 4", "BROKE IN", "THE LOBBY"), ("CHAPTER 5", "THE PICTURE ON", "THE WALL"), ("CHAPTER 6", "A LITTLE", "AMERICA"), ("THE LESSON", "KEEP THE", "DREAM IN SIGHT")]
CARDS = [("conrad nicholson hilton was born on december", "1887", "HILTON IS BORN", "San Antonio, New Mexico", None),
         ("he found a hotel called the mobley", "1919", "THE MOBLEY HOTEL", "Cisco, Texas", None),
         ("in nineteen twenty-five he built", "1925", "THE DALLAS HILTON", "the first hotel with his name", None),
         ("in october nineteen twenty-nine", "1929", "THE GREAT CRASH", "his hotels go under", None),
         ("in nineteen forty-nine he finally reached", "1949", "THE WALDORF ASTORIA", "bought for $3 million", None),
         ("in nineteen fifty-four he bought the statler", "1954", "THE STATLER DEAL", "$111 million", None),
         ("conrad hilton died on january third", "1979", "HILTON DIES", "age 91", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("the clerk rent the same room", g_shifts, 5.5), ("oilmen", FFg("train"), 5.0), ("in october nineteen twenty-nine the stock market", FFg("nyc"), 5.5),
       ("he owed more than half a million", g_debt, 5.5), ("soldiers and officials", FFg("war"), 5.5), ("a hundred and eleven million", g_statler, 5.5),
       ("istanbul hilton", FFg("nyc", 1), 5.0), ("hotels across texas", FFg("train", 1), 5.0)] + MAPBRT
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is conrad hilton', 'people/conrad.jpg', '1887 – 1979', 'CONRAD HILTON', 'from a desert boardinghouse to a global empire', True, 0),
 ('san antonio new mexico', 'fotos/sanantonio_0.jpg', '1887', 'SAN ANTONIO, NEW MEXICO', 'where Hilton was born', True, 0),
 ('he found a hotel called the mobley', 'fotos/mobley_0.jpg', '1919', 'THE MOBLEY HOTEL', 'Cisco, Texas', True, 0),
 ('the dallas hilton', 'fotos/dallas_0.jpg', '1925', 'THE DALLAS HILTON', 'the first hotel with his name', True, 0),
 ('el paso', 'fotos/elpaso_0.jpg', '1930', 'EL PASO', 'part of his Texas chain', True, 0),
 ('stock market collapsed', 'fotos/crash_0.jpg', '1929', 'THE CRASH OF 1929', 'his hotels were mortgaged', True, 0),
 ('albuquerque', 'fotos/albuquerque_0.jpg', '1939', 'THE ALBUQUERQUE HILTON', 'close to his boyhood home', True, 0),
 ('the palmer house in chicago', 'fotos/palmer_0.jpg', '1945', 'THE PALMER HOUSE', 'one of the largest hotels on Earth', True, 0),
 ('the waldorf astoria in new york', 'fotos/waldorf_0.jpg', '1949', 'THE WALDORF ASTORIA', 'the dream on his office wall', True, 0),
 ('the statler hotels', 'fotos/statler_0.jpg', '1954', 'THE STATLER HOTELS', 'bought for $111 million', True, 0),
 ('istanbul hilton', 'fotos/istanbul_0.jpg', '1955', 'THE ISTANBUL HILTON', 'the first overseas flagship', True, 0),
 ('zsa zsa gabor', 'people/zsa.jpg', '1946', 'ZSA ZSA GABOR', 'his second wife, briefly', True, 0),
 ('his son barron', 'people/barron.jpg', '1927 – 2007', 'BARRON HILTON', 'took over the business', True, 0),
 ('paris would one day', 'people/paris.jpg', '', 'PARIS HILTON', 'his great-granddaughter', True, 0)]
#--EMPH
EMPH = [("by accident", "A HOTELIER", "BY ACCIDENT"), ("the same room in three shifts", "THREE SHIFTS", "ONE ROOM"), ("he borrowed five dollars from a bellboy", "$5 FROM", "A BELLBOY"),
        ("a man's word was his most valuable asset", "HIS WORD", "WAS HIS ASSET"), ("hung on his wall for twenty years", "TWENTY YEARS", "ON HIS WALL"), ("little america", "A LITTLE", "AMERICA")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "dark", 5: "triumph", 6: "upbeat", 7: "reflect"}
TRG = [("nineteen twenty-nine a young texas", "tense"), ("conrad nicholson hilton was born", "sad"), ("at twenty-five hilton served", "drive"), ("he asked the owner what he wanted", "wonder"),
       ("by the mid nineteen twenties", "triumph"), ("then came the crash", "dark"), ("he owed more than half a million", "dark"), ("slowly a recovery began", "wonder"),
       ("in nineteen forty-nine he finally reached", "triumph"), ("hilton had a second dream", "upbeat"), ("conrad hilton died on january", "sad"), ("the second is to keep a picture", "reflect")]
TWISTS = ["then came the crash", "he borrowed five dollars from a bellboy", "he bought the waldorf astoria in new york", "conrad hilton died on january third", "the second is to keep a picture"]
#--NSC
75
#--MAP
MAPBRT = [("conrad nicholson hilton was born on december", lambda u: g_map(u, -106.87, 33.92, "SAN ANTONIO, NEW MEXICO", "UNITED STATES  ·  1887"), 7.0)]
#--KW
{"A tiny desert general store": "sanantonio_0", "A frontier boardinghouse": "sanantonio_1", "A state legislature chamber": "newmexico_0", "A Texas oil boomtown": "oil_0",
 "A crowded Texas hotel lobby": "mobley_0", "A hotel room rented": "mobley_1", "A tall Texas hotel under construction": "dallas_0", "Dallas skyline": "dallas_1",
 "The stock market crash": "crash_1", "A Depression-era bank": "depression_0", "A hotel in Albuquerque": "albuquerque_0", "A busy Chicago hotel lobby": "palmer_1",
 "The Waldorf Astoria in New York": "waldorf_0", "Hotel staff lined up": "waldorf_1", "A modern hotel in Istanbul": "istanbul_0", "A hotel in Havana": "havana_0",
 "American soldiers marching": "ww2_0"}
