#--KEY
KEY = {"stanford", "leland", "railroad", "central", "pacific", "sierra", "chinese", "workers", "spike", "huntington", "crocker", "hopkins", "judah", "governor", "university", "palo", "alto", "octopus", "million", "typhoid"}
#--CH
CH = [("CHAPTER 1", "THE LAWYER WHO", "WENT WEST"), ("CHAPTER 2", "THE GROCER", "GOVERNOR"), ("CHAPTER 3", "THE BIG FOUR", "OF SACRAMENTO"), ("CHAPTER 4", "THROUGH THE", "SIERRA SNOW"),
      ("CHAPTER 5", "THE OCTOPUS", "AND THE HORSE"), ("CHAPTER 6", "A SON'S", "MEMORIAL"), ("THE LESSON", "GRIEF CAN", "BUILD A LEGACY")]
CARDS = [("amasa leland stanford was born on march", "1824", "STANFORD IS BORN", "near Albany, New York", None),
         ("in eighteen fifty-two leland left jane", "1852", "THE GOLD RUSH", "Stanford sails to California", None),
         ("in eighteen sixty-one they formed", "1861", "CENTRAL PACIFIC", "the Big Four", None),
         ("in eighteen sixty-two president abraham lincoln", "1862", "PACIFIC RAILWAY ACT", "land and loans", None),
         ("on may tenth eighteen sixty-nine", "1869", "THE GOLDEN SPIKE", "Promontory Summit, Utah", None),
         ("in eighteen eighty-four the family traveled", "1884", "THE LOSS OF A SON", "Florence, Italy", None),
         ("stanford died on june twenty-first", "1893", "STANFORD DIES", "age 69", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("they became known as the big four", g_big4, 6.0), ("sixteen thousand dollars for every mile", g_miles, 5.5), ("about twenty million dollars", g_univ, 5.5),
       ("through granite and snow", FFg("snow"), 5.5), ("cross the sierra nevada", FFg("train"), 5.5), ("gold rush", FFg("gold"), 5.0),
       ("a galloping horse", FFg("horse"), 5.5), ("california", FFg("city"), 5.0), ("a university", FFg("campus"), 5.0)] + MAPBRT
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is leland stanford', 'people/stanford.jpg', '1824 – 1893', 'LELAND STANFORD', 'the grocer who built a railroad', True, 0),
 ('near albany new york', 'fotos/albany_0.jpg', '1824', 'ALBANY, NEW YORK', 'where Stanford was born', True, 0),
 ('jane lathrop', 'people/jane.jpg', '1828 – 1905', 'JANE LATHROP STANFORD', 'his wife and partner', True, 0),
 ('sacramento', 'fotos/sac_0.jpg', '1856', 'SACRAMENTO', 'the grocery and the railroad', True, 0),
 ('theodore judah', 'people/judah.jpg', '1826 – 1863', 'THEODORE JUDAH', 'the engineer who found the route', True, 0),
 ('collis huntington', 'people/huntington.jpg', '1821 – 1900', 'COLLIS HUNTINGTON', 'the hardware dealer', True, 0),
 ('mark hopkins', 'people/hopkins.jpg', '1813 – 1878', 'MARK HOPKINS', 'the bookkeeper', True, 0),
 ('charles crocker', 'people/crocker.jpg', '1822 – 1888', 'CHARLES CROCKER', 'the builder', True, 0),
 ('abraham lincoln', 'people/lincoln.jpg', '1862', 'ABRAHAM LINCOLN', 'signed the Pacific Railway Act', True, 0),
 ('chinese laborers', 'fotos/chinese_0.jpg', '1866', 'CHINESE RAILROAD WORKERS', 'thousands built the line', True, 0),
 ('snow sheds', 'fotos/sierra_0.jpg', '1867', 'THE SIERRA SNOW SHEDS', 'avalanches buried camps', True, 0),
 ('promontory summit', 'fotos/promontory_0.jpg', '1869', 'PROMONTORY SUMMIT', 'the last spike', True, 0),
 ('the octopus', 'fotos/octopus_0.jpg', '1882', 'THE OCTOPUS', 'a cartoon of the railroad', True, 0),
 ('eadweard muybridge', 'people/muybridge.jpg', '1878', 'EADWEARD MUYBRIDGE', 'photographed the galloping horse', True, 0),
 ('the palo alto farm', 'fotos/palo_0.jpg', '1880s', 'THE PALO ALTO FARM', 'now Stanford University', True, 0),
 ('leland junior', 'fotos/junior_0.jpg', '1868 – 1884', 'LELAND STANFORD JR.', 'the son who died at 15', True, 0),
 ('stanford junior university', 'fotos/univ_0.jpg', '1891', 'STANFORD UNIVERSITY', 'opened in 1891', True, 0)]
#--EMPH
EMPH = [("he swings and he misses", "HE SWUNG", "AND MISSED"), ("hundreds died perhaps more", "HUNDREDS", "DIED"), ("they paid themselves with the government's money", "PAID WITH", "PUBLIC MONEY"),
        ("they called it the octopus", "THE", "OCTOPUS"), ("the children of california would be his children", "HIS CHILDREN", "NOW"), ("a university in memory of their son", "A MEMORIAL", "TO A SON")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "dark", 5: "upbeat", 6: "sad", 7: "reflect"}
TRG = [("may tenth eighteen sixty-nine", "tense"), ("amasa leland stanford was born", "sad"), ("stanford sold shovels", "drive"), ("they became known as the big four", "wonder"),
       ("building the central pacific", "dark"), ("on may tenth eighteen sixty-nine the central pacific met", "triumph"), ("after the transcontinental", "upbeat"), ("in eighteen eighty-four the family traveled", "dark"),
       ("stanford died on june", "sad"), ("the second is that grief", "reflect")]
TWISTS = ["he swings and he misses", "in eighteen eighty-four the family traveled to europe", "leland junior caught typhoid fever", "stanford died on june twenty-first", "the second is that grief"]
#--NSC
76
#--MAP
MAPBRT = [("amasa leland stanford was born on march", lambda u: g_map(u, -73.76, 42.65, "ALBANY, NEW YORK", "UNITED STATES  ·  1824"), 7.0)]
#--KW
{"A desert railroad summit": "spike_0", "A telegraph operator": "promontory_1", "An inn and a farm": "albany_0", "A mining camp general store": "sac_0", "A Sacramento riverfront": "sac_1",
 "Four merchants around a table": "bigfour_0", "A surveyor with a theodolite": "judah_0", "President Lincoln signing": "lincoln_0", "Chinese laborers swinging": "chinese_0",
 "A snow shed over railroad": "sierra_0", "The Central Pacific meets": "promontory_0", "A Southern Pacific train": "cp_0", "An octopus drawn": "octopus_0", "A mansion on Nob Hill": "palo_0",
 "A racehorse farm": "palo_1", "A line of cameras": "muy_0", "A ranch with farmland": "univ_0", "The opening day of a new university": "univ_1", "A university campus in the 1920s": "quad_0"}
