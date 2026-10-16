#--KEY
KEY = {"edison", "thomas", "bulb", "light", "phonograph", "menlo", "park", "laboratory", "filament", "current", "alternating", "direct", "tesla", "westinghouse", "morgan", "patents", "electric", "invention", "invented", "genius"}
#--CH
CH = [("CHAPTER 1", "THE BOY IN", "THE BAGGAGE CAR"), ("CHAPTER 2", "THE TICKER", "AND THE LAB"), ("CHAPTER 3", "A THOUSAND", "FAILED FILAMENTS"), ("CHAPTER 4", "THE FIRST", "POWER PLANT"),
      ("CHAPTER 5", "THE WAR OF", "THE CURRENTS"), ("CHAPTER 6", "THE WIZARD", "AND HIS LEGACY"), ("THE LESSON", "BUILD THE", "WHOLE SYSTEM")]
CARDS = [("thomas alva edison was born on february", "1847", "EDISON IS BORN", "Milan, Ohio", None),
         ("in eighteen seventy-six he sold", "1876", "MENLO PARK", "the invention factory", None),
         ("in eighteen seventy-seven he invented", "1877", "THE PHONOGRAPH", "Mary had a little lamb", None),
         ("at last in october eighteen seventy-nine", "1879", "THE LIGHT BULB", "13 and a half hours", None),
         ("on september fourth eighteen eighty-two", "1882", "PEARL STREET STATION", "the first power plant", None),
         ("in eighteen ninety-two j p morgan", "1892", "GENERAL ELECTRIC", "Edison loses control", None),
         ("edison died on october eighteenth", "1931", "EDISON DIES", "age 84", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("tested thousands of materials", g_tries, 5.5), ("it lit up four hundred lamps", g_lamps, 5.5), ("one thousand and ninety-three", g_patents, 5.5),
       ("on the train between port huron", FFg("train"), 5.5), ("a telegraph operator", FFg("telegraph"), 5.0), ("the first commercial power plant", FFg("power"), 5.5),
       ("the movie camera", FFg("film"), 5.5), ("lower manhattan", FFg("newyork"), 5.0), ("electric light", FFg("electric"), 5.0)] + MAPBRT
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is thomas edison', 'people/edison.jpg', '1847 – 1931', 'THOMAS EDISON', 'the Wizard of Menlo Park', True, 0),
 ('milan ohio', 'fotos/milan_0.jpg', '1847', 'MILAN, OHIO', 'where Edison was born', True, 0),
 ('port huron michigan', 'fotos/porthuron_0.jpg', '1854', 'PORT HURON', 'where he grew up', True, 0),
 ('his mother', 'fotos/nancy_0.jpg', '1850s', 'NANCY EDISON', 'his first teacher', True, 0),
 ('a telegraph operator', 'fotos/telegraph_0.jpg', '1863', 'THE TELEGRAPH', 'his first career', True, 0),
 ('a stock ticker', 'fotos/ticker_0.jpg', '1869', 'THE STOCK TICKER', 'the machine he fixed', True, 0),
 ('newark new jersey', 'fotos/newark_0.jpg', '1871', 'NEWARK', 'his first factory', True, 0),
 ('menlo park', 'fotos/menlo_0.jpg', '1876', 'MENLO PARK', 'the invention factory', True, 0),
 ('the phonograph', 'fotos/phono_0.jpg', '1877', 'THE PHONOGRAPH', 'recorded sound', True, 0),
 ('bamboo filament', 'fotos/filament_0.jpg', '1880', 'THE FILAMENT', 'bamboo lasted over a thousand hours', True, 0),
 ('pearl street station', 'fotos/pearl_0.jpg', '1882', 'PEARL STREET STATION', 'the first power plant', True, 0),
 ('j p morgan', 'people/morgan.jpg', '1882', 'J. P. MORGAN', 'Edison\'s backer', True, 0),
 ('nikola tesla', 'people/tesla.jpg', '1856 – 1943', 'NIKOLA TESLA', 'inventor of the AC motor', True, 0),
 ('george westinghouse', 'people/westinghouse.jpg', '1846 – 1914', 'GEORGE WESTINGHOUSE', 'the rival who bet on AC', True, 0),
 ('the first electric chair', 'fotos/chair_0.jpg', '1890', 'THE ELECTRIC CHAIR', 'the ugly side of the war', True, 0),
 ('the kinetoscope', 'fotos/kinetoscope_0.jpg', '1893', 'THE KINETOSCOPE', 'the first movie viewer', True, 0),
 ('the black maria', 'fotos/blackmaria_0.jpg', '1893', 'THE BLACK MARIA', 'America\'s first film studio', True, 0),
 ('mina miller', 'people/mina.jpg', '1886', 'MINA MILLER', 'his second wife', True, 0),
 ('west orange', 'fotos/orange_0.jpg', '1887', 'WEST ORANGE', 'his huge new laboratory', True, 0)]
#--EMPH
EMPH = [("ten thousand ways that will not work", "10,000 WAYS", "THAT FAIL"), ("the war of the currents", "THE WAR OF", "THE CURRENTS"), ("the wizard of menlo park", "THE WIZARD OF", "MENLO PARK"),
        ("one percent inspiration", "1% INSPIRATION", "99% PERSPIRATION"), ("lost control of the company", "HE LOST HIS", "OWN COMPANY"), ("build the whole system", "BUILD THE", "WHOLE SYSTEM")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "triumph", 5: "dark", 6: "reflect", 7: "reflect"}
TRG = [("december eighteen seventy-nine in a small laboratory", "tense"), ("thomas alva edison was born", "sad"), ("at sixteen he became", "drive"), ("in eighteen seventy-six he made", "wonder"),
       ("in eighteen seventy-seven he invented", "triumph"), ("edison and his team tested", "drive"), ("on september fourth", "triumph"), ("the result was the war", "dark"),
       ("it was an ugly campaign", "dark"), ("in eighteen eighty-six after the death", "wonder"), ("edison died on october", "sad"), ("the second is that invention alone", "reflect")]
TWISTS = ["the power is switched on", "on september fourth eighteen eighty-two", "in eighteen ninety-two j p morgan merged", "edison lost control of the company", "edison died on october eighteenth"]
#--NSC
74
#--MAP
MAPBRT = [("thomas alva edison was born on february", lambda u: g_map(u, -82.60, 41.30, "MILAN, OHIO", "UNITED STATES  ·  1847"), 7.0)]
#--KW
{"A small New Jersey laboratory": "menlo_0", "A crowd of visitors arriving": "menlo2_0", "A boy reading a science book": "milan_0", "A Michigan town": "porthuron_0",
 "A young newsboy": "porthuron_1", "A telegraph operator at a night desk": "telegraph_0", "A brokerage office": "ticker_0", "A workshop in Newark": "newark_0", "A hand cranking": "phono_0",
 "A power plant in lower Manhattan": "pearl_0", "A banker in an elegant office": "morgan_0", "An inventor's notebook": "tesla_0", "A state prison with an electric chair": "chair_0",
 "A film studio shaped like a black barn": "blackmaria_0", "A vast laboratory complex": "orange_0", "A funeral procession": "funeral_0"}
