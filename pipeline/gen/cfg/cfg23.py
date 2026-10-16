#--KEY
KEY = {"westinghouse", "george", "air", "brake", "alternating", "current", "direct", "edison", "tesla", "niagara", "railroad", "railroads", "patents", "electric", "chair", "chicago", "fair", "lamps", "panic", "forced"}
#--CH
CH = [("CHAPTER 1", "THE FARM BOY", "WITH A WRENCH"), ("CHAPTER 2", "THE BRAKE THAT", "STOPPED TRAINS"), ("CHAPTER 3", "THE GENTLEMAN", "INVENTOR"),
      ("CHAPTER 4", "THE WAR OF", "THE CURRENTS"), ("CHAPTER 5", "LIGHTING THE", "WORLD"), ("CHAPTER 6", "FORCED OUT", "OF HIS OWN FIRM"), ("THE LESSON", "THE BETTER IDEA", "WINS")]
CARDS = [("george westinghouse junior was born on october", "1846", "WESTINGHOUSE IS BORN", "Central Bridge, New York", None),
         ("he patented the air brake", "1869", "THE AIR BRAKE", "Westinghouse Air Brake Co.", None),
         ("then he bought the patents", "1888", "TESLA'S PATENTS", "alternating current", None),
         ("in eighteen ninety-three westinghouse won", "1893", "THE WORLD'S FAIR", "100,000 lamps", None),
         ("in eighteen ninety-five westinghouse built", "1895", "NIAGARA FALLS", "power to Buffalo", None),
         ("in the panic of nineteen-oh-seven", "1907", "FORCED OUT", "bankers take control", None),
         ("he died on march twelfth", "1914", "WESTINGHOUSE DIES", "age 67", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("a hundred thousand lamps", g_lamps, 5.5), ("twenty-six miles", g_niagara, 5.5), ("held more than three hundred patents", g_patents, 5.5),
       ("two locomotives had collided", FFg("train"), 5.5), ("niagara falls", FFg("niagara"), 5.5), ("power plant at niagara", FFg("power"), 5.0),
       ("electric trains", FFg("street"), 5.0), ("the world's columbian exposition", FFg("fair"), 5.5), ("the civil war", FFg("war"), 5.0)] + MAPBRT
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is george westinghouse', 'fotos/w1_0.jpg', '1846 – 1914', 'GEORGE WESTINGHOUSE', 'the man who won the war of the currents', True, 0),
 ('central bridge new york', 'fotos/central_0.jpg', '1846', 'CENTRAL BRIDGE, NY', 'where Westinghouse was born', True, 0),
 ('two locomotives had collided', 'fotos/wreck_0.jpg', '1869', 'THE TRAIN WRECK', 'that inspired the air brake', True, 0),
 ('cornelius vanderbilt', 'people/vanderbilt.jpg', '1794 – 1877', 'CORNELIUS VANDERBILT', 'the tycoon who laughed', True, 0),
 ('the air brake', 'fotos/airbrake_0.jpg', '1869', 'THE AIR BRAKE', 'compressed air stops trains', True, 0),
 ('railroad signals', 'fotos/signal_0.jpg', '1880s', 'RAILWAY SIGNALS', 'preventing crashes', True, 0),
 ('a model town for his employees', 'fotos/town_0.jpg', '1890', 'WILMERDING', 'the Westinghouse company town', True, 0),
 ('william stanley', 'people/stanley.jpg', '1858 – 1916', 'WILLIAM STANLEY', 'built the working transformer', True, 0),
 ('nikola tesla', 'people/tesla.jpg', '1856 – 1943', 'NIKOLA TESLA', 'inventor of the AC motor', True, 0),
 ('thomas edison', 'people/edison.jpg', '1847 – 1931', 'THOMAS EDISON', 'the rival who preached direct current', True, 0),
 ('the first electric chair', 'fotos/chair_0.jpg', '1890', 'THE ELECTRIC CHAIR', 'the ugliest weapon of the war', True, 0),
 ('the world\'s columbian exposition', 'fotos/fair_0.jpg', '1893', 'THE WHITE CITY', 'lit by Westinghouse', True, 0),
 ('niagara falls', 'fotos/niagara_0.jpg', '1895', 'NIAGARA FALLS', 'the first great hydro plant', True, 0),
 ('buffalo new york', 'fotos/buffalo_0.jpg', '1896', 'BUFFALO, NEW YORK', 'powered from the falls', True, 0),
 ('steam turbines', 'fotos/turbine_0.jpg', '1900s', 'STEAM TURBINES', 'his late-career focus', True, 0),
 ('the panic of nineteen-oh-seven', 'fotos/panic_0.jpg', '1907', 'THE PANIC OF 1907', 'the crash that cost him his firm', True, 0),
 ('arlington national cemetery', 'fotos/arlington_0.jpg', '1914', 'ARLINGTON', 'buried as a Civil War veteran', True, 0)]
#--EMPH
EMPH = [("stop trains with wind", "STOP A TRAIN", "WITH WIND?"), ("the war of the currents", "THE WAR OF", "THE CURRENTS"), ("tore up the contract", "TESLA TORE UP", "THE CONTRACT"),
        ("a hundred thousand lamps", "100,000", "LAMPS"), ("forced him out of the firm he had founded", "FORCED OUT", "OF HIS FIRM"), ("the better idea wins", "THE BETTER", "IDEA WINS")]
#--MUSIC
DEF = {0: "tense", 1: "drive", 2: "wonder", 3: "dark", 4: "triumph", 5: "dark", 6: "sad", 7: "reflect"}
TRG = [("october eighteen ninety-three on the shore", "tense"), ("george westinghouse junior was born", "sad"), ("the idea that made him famous", "wonder"), ("westinghouse persisted", "drive"),
       ("he hired a young engineer", "wonder"), ("edison was furious", "dark"), ("in eighteen ninety-three westinghouse won", "triumph"), ("the war of the currents was over", "triumph"),
       ("but the end of his career", "dark"), ("he died on march twelfth", "sad"), ("the second is that how you treat", "reflect")]
TWISTS = ["nearly everyone assumes it is the work of the famous inventor", "edison was furious", "the war of the currents was over", "bankers forced him out of the firm", "he died on march twelfth"]
#--NSC
72
#--MAP
MAPBRT = [("george westinghouse junior was born on october", lambda u: g_map(u, -74.37, 42.75, "CENTRAL BRIDGE, NEW YORK", "UNITED STATES  ·  1846"), 7.0)]
#--KW
{"A dazzling White City fair": "fair_0", "A crowd gazing at a grand electric fountain": "fair_1", "A farm machine shop": "central_0", "A railroad wreck": "wreck_0", "Brakemen running": "airbrake_0",
 "A railroad tycoon in a velvet": "vanderbilt_0", "An engineer testing a new air brake": "airbrake_1", "A railroad signal tower": "signal_0", "A model company town": "town_0",
 "A transformer coil": "stanley_0", "A public electrocution": "chair_0", "A state prison with an electric chair": "chair_1", "Niagara Falls with a hydroelectric plant": "niagara_0",
 "Transmission lines running": "adams_0", "A turbine hall with huge machines": "turbine_0", "Wall Street in the panic": "panic_0", "A military cemetery": "arlington_0", "A hospital bedroom": "marguerite_0"}
