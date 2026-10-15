import re
s = open("build_v4.py", encoding="utf-8").read()
s = s.replace("video_build4", "video_build5").replace("video4-", "video5-").replace("Morgan_Video4", "Ford_Video5")
s = s.replace('NAMES = ["00_hook","01_cap1","02_cap2","03_cap3","04_cap4","05_cap5","06_cap6","07_cap7","08_cap8","09_lesson"]',
              'NAMES = ["00_hook","01_cap1","02_cap2","03_cap3","04_cap4","05_cap5","06_cap6","07_lesson"]')
s = s.replace("NSC = 119", "NSC = 86")
s = s.replace('part3_morgan.py', 'part3_ford.py')
def blk(a, b, new):
    global s
    i = s.index(a); j = s.index(b, i); s = s[:i] + new + s[j:]
blk("KEY = {", "def is_key", 'KEY = {"ford", "million", "billion", "dollar", "dollars", "wages", "wage", "factory", "assembly", "line", "model", "engine", "machine", "cars", "car", "richest", "failure", "collapsed", "fortune", "died", "lost", "power", "control", "bomber", "five-dollar", "price", "mother", "edison", "dodge", "rouge"}\n')
blk("CH = [", "import importlib", '''CH = [("CHAPTER 1", "THE FARM BOY WHO", "HATED FARMING"), ("CHAPTER 2", "THE FAILURES BEFORE", "THE FORTUNE"), ("CHAPTER 3", "THE CAR FOR", "EVERYONE"),
      ("CHAPTER 4", "THE FIVE-", "DOLLAR DAY"), ("CHAPTER 5", "THE PRICE", "OF CONTROL"), ("CHAPTER 6", "THE ARSENAL", "OF DEMOCRACY"), ("THE LESSON", "THE MARKET", "HE BUILT")]
CARDS = [("henry ford was born on july", "1863", "HENRY FORD IS BORN", "Greenfield Township, Michigan", None),
         ("in eighteen ninety-one he joined", "1891", "EDISON ILLUMINATING CO.", "chief engineer by 1893", None),
         ("in june eighteen ninety-six", "1896", "THE QUADRICYCLE", "Ford's first car", None),
         ("in october nineteen hundred and one he beat", "1901", "FORD BEATS WINTON", "the race that opened the door", None),
         ("in june nineteen oh-three", "1903", "FORD MOTOR COMPANY", "12 investors · about $28,000", None),
         ("in october nineteen oh-eight", "1908", "THE MODEL T", "$850", None),
         ("in nineteen thirteen at the highland park", "1913", "HIGHLAND PARK", "the moving assembly line", None),
         ("so on january fifth nineteen fourteen he announced", "1914", "THE FIVE-DOLLAR DAY", "double the going wage", None),
         ("in nineteen nineteen he bought out", "1919", "THE BUYOUT", "about $106 million", None),
         ("by nineteen twenty-seven sales had collapsed", "1927", "THE MODEL A", "after 19 years of the Model T", None),
         ("edsel died in nineteen forty-three", "1943", "EDSEL FORD DIES", "aged 49", None),
         ("henry ford died on april seventh", "1947", "HENRY FORD DIES", "aged 83", None)]
QUOTES = []
chap_t = []
for ci_, (k, l1, l2) in enumerate(CH):
    a = chap_start[ci_] + 0.15
    if TLIM and a > TLIM: continue
    chap_t.append(a); e = a + 3.4
    events.append((a, e, "Dim", 0, "{\\\\fad(250,500)\\\\an7\\\\pos(0,0)\\\\1c&H000000&\\\\1a&H50&\\\\p1}m 0 0 l 1280 0 1280 720 0 720{\\\\p0}"))
    events.append((a, e, "Kick", 3, "{\\\\an7\\\\fad(250,400)\\\\move(70,236,90,236,0,600)}%s" % k))
    events.append((a, e, "Bar", 2, "{\\\\an7\\\\fad(250,400)\\\\pos(90,284)\\\\p1\\\\fscx0\\\\t(0,700,\\\\fscx100)}m 0 0 l 90 0 90 5 0 5{\\\\p0}"))
    events.append((a, e, "Big", 3, "{\\\\an7\\\\fad(250,400)\\\\move(60,300,90,300,0,600)}%s" % l1))
    events.append((a, e, "Big", 3, "{\\\\an7\\\\fad(250,400)\\\\move(60,388,90,388,100,700)}%s" % l2))

''')
blk("FF = lambda n:", "BR = []", '''def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video5-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("ten thousand men are standing", FFg("crowd"), 6.0), ("it is january fifth", FFg("detroit"), 5.0),
       ("steam engine moving down a country road", FFg("road"), 5.5), ("took a job in a machine shop", FFg("factory"), 5.5),
       ("a rattling four-wheeled machine", FFg("car"), 5.5), ("he went racing", FFg("car", 1), 5.5),
       ("the model t arrived", FFg("modelt"), 6.0), ("farmers stopped feeling isolated", FFg("farm"), 5.5),
       ("a moving line with each worker", FFg("assembly"), 6.0), ("about ninety-three minutes", g_time, 5.0),
       ("prices began to fall", g_price, 5.5), ("double the going wage", g_wage5, 4.8),
       ("half of all the cars in the world", g_share, 4.6), ("he built the giant river rouge complex", FFg("rouge"), 5.5),
       ("turned his factories into the arsenal", FFg("war"), 5.5), ("a bomber rolled off that line", g_bomber, 5.5),
       ("the stress had broken him", FFg("crowd", 1), 5.0), ("workers were bleeding", FFg("factory", 1), 5.0)] + MAPBRT
''')
s = s.replace("if st is None or (TLIM and st > TLIM - 5): continue\n    st += 0.25", "if st is None or fn is None or (TLIM and st > TLIM - 5): continue\n    st += 0.25")
blk("PHOTOS = [", "PH = []", '''PHOTOS = [
 ('his name is henry ford', 'people/ford.jpg', '1863 – 1947', 'HENRY FORD', 'the man who put the world on wheels', True, 0),
 ('a year later his mother died', 'fotos/mary_0.jpg', 'HIS MOTHER', 'MARY FORD', 'her death in 1876 marked him forever', True, 0),
 ('joined the edison illuminating company', 'people/edison.jpg', '1891', 'THOMAS EDISON', 'Ford worked for his company', True, 0),
 ('a rattling four-wheeled machine', 'fotos/quad_0.jpg', '1896', 'THE QUADRICYCLE', "Ford's first car", True, 0),
 ('alexander winton', 'people/winton.jpg', '1901', 'ALEXANDER WINTON', 'the most famous driver in America', True, 0),
 ('ford motor company was born', 'fotos/motor1903_0.jpg', '1903', 'THE FIRST FORD CAR', 'Ford Model A of 1903', True, 0),
 ('the model t arrived', 'fotos/modelt_0.jpg', '1908', 'THE MODEL T', 'a car for the great multitude', True, 0),
 ('a moving line with each worker', 'fotos/line1_0.jpg', '1913', 'THE ASSEMBLY LINE', 'Highland Park, Michigan', True, 0),
 ('it was neither', 'fotos/fivedollar_0.jpg', 'JANUARY 1914', 'THE FIVE-DOLLAR DAY', 'crowds outside the Ford employment office', True, 0),
 ('including the dodge brothers', 'people/dodge1.jpg', '1919', 'JOHN DODGE', 'early investor, later a rival', True, 0),
 ('the giant river rouge complex', 'fotos/rouge1_0.jpg', '1920s', 'RIVER ROUGE', 'ore in one end, cars out the other', True, 0),
 ('the dearborn independent', 'fotos/dearborn_0.jpg', '1920s', 'THE DEARBORN INDEPENDENT', "a newspaper that spread hate", True, 0),
 ('general motors offered color', 'people/sloan.jpg', '1920s', 'ALFRED SLOAN', 'built General Motors into a rival', True, 0),
 ('his own son edsel', 'people/edsel.jpg', '1943', 'EDSEL FORD', 'died at only forty-nine', True, 0),
 ('at willow run near detroit', 'fotos/willow1_0.jpg', '1942', 'WILLOW RUN', 'a bomber plant almost a mile long', True, 0),
 ('his security chief harry bennett', 'people/bennett.jpg', '1937', 'HARRY BENNETT', 'Ford security chief', True, 0),
 ('the battle of the overpass', 'fotos/overpass_0.jpg', '1937', 'THE OVERPASS', 'River Rouge, May 1937', True, 0),
 ('only a family intervention', 'fotos/family_0.jpg', '1945', 'THE FORD FAMILY', 'Henry, Clara and Edsel', True, 0),
 ('his wife clara', 'people/clara.jpg', '1945', 'CLARA FORD', 'forced the handover of power', True, 0),
 ('his grandson henry the second', 'people/henry2.jpg', '1945', 'HENRY FORD II', 'saved the company', True, 0),
 ('henry ford died on april seventh', 'people/ford.jpg', '1863 – 1947', 'HENRY FORD', 'the empire that put the world on wheels', True, 0)]
''')
# DEF / TRG / TWISTS
i = s.index("DEF = {"); j = s.index("segs = [(chap_start")
s = s[:i] + '''DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "upbeat", 5: "dark", 6: "drive", 7: "reflect"}
TRG = [("inside one man has just made", "tense"), ("his name is henry ford", "dark"), ("henry ford was born", "wonder"), ("a year later his mother died", "sad"),
       ("then came the failures", "dark"), ("he went racing", "drive"), ("in june nineteen oh-three", "triumph"), ("the model t arrived", "triumph"),
       ("but ford noticed something", "tense"), ("a moving line", "drive"), ("but the line had a hidden cost", "dark"), ("the press called it", "wonder"),
       ("it was neither", "triumph"), ("by the early nineteen twenties", "triumph"), ("but the same man who understood", "dark"),
       ("edsel died in nineteen forty-three", "sad"), ("then the world changed again", "tense"), ("at willow run", "drive"),
       ("only a family intervention", "tense"), ("the young grandson saved", "triumph"), ("henry ford died on april seventh", "sad"),
       ("his story gives two lessons", "reflect"), ("every great builder needs", "triumph")]
TWISTS = ["and the secret behind that decision", "it was neither", "but the same man who understood", "edsel died in nineteen forty-three", "every great builder needs one thing"]
''' + s[j:]
# EMPH center captions
emph = '''EMPH = [("it made him the richest industrialist", "THE RICHEST", "INDUSTRIALIST"), ("why does a human being have to do", "WHY NOT", "A MACHINE?"),
        ("his first company collapsed", "FAILURE", "NUMBER ONE"), ("he beat the most famous driver", "HE BEAT", "THE BEST"),
        ("a motor car for the great multitude", "A CAR FOR", "THE MULTITUDE"), ("it cost eight hundred and fifty dollars", "$850", "THE MODEL T"),
        ("two hundred and sixty dollars", "$260", "AND FALLING"), ("the company belonged to henry ford alone", "HIS", "ALONE"),
        ("every single hour", "EVERY HOUR", "ONE BOMBER"), ("someone brave enough to tell him", "TELL HIM", "HE IS WRONG"),
        ("the best customer the company can ever have", "THE BEST", "CUSTOMER")]
emph_t = []
for ph_, l1, l2 in EMPH:
    a = find(ph_)
    if a is None or (TLIM and a > TLIM - 4): continue
    a -= 0.05
    if any(abs(a - c) < 4.2 for c in chap_t + card_t) or any(b0_ - 0.5 < a < b0_ + b[2] + 0.5 for b0_, b in zip(BR_T, BR)) or any(p0 - 4.5 < a < p1 + 0.3 for p0, p1 in PHT): continue
    if any(abs(a - x) < 8 for x in emph_t): continue
    emph_t.append(a); e = a + 2.6
    events.append((a - 0.05, e, "Dim", 0, "{\\\\fad(120,350)\\\\an7\\\\pos(0,0)\\\\1c&H000000&\\\\1a&H30&\\\\p1}m 0 0 l 1280 0 1280 720 0 720{\\\\p0}"))
    events.append((a - 0.03, a + 0.18, "Dim", 4, "{\\\\an7\\\\pos(0,0)\\\\1c&HFFFFFF&\\\\1a&H60&\\\\fad(0,170)\\\\p1}m 0 0 l 1280 0 1280 720 0 720{\\\\p0}"))
    events.append((a, e, "Emph", 4, "{\\\\an5\\\\fad(80,350)\\\\blur12\\\\fscx150\\\\fscy150\\\\pos(640,300)\\\\t(0,260,\\\\blur0\\\\fscx100\\\\fscy100)\\\\t(260,2600,\\\\fscx106\\\\fscy106)}%s" % l1))
    events.append((a + 0.12, e, "EmphG", 4, "{\\\\an5\\\\fad(80,350)\\\\blur12\\\\fscx150\\\\fscy150\\\\pos(640,430)\\\\t(0,260,\\\\blur0\\\\fscx100\\\\fscy100)\\\\t(260,2600,\\\\fscx106\\\\fscy106)}%s" % l2))
    events.append((a + 0.2, e, "Bar", 2, "{\\\\an7\\\\fad(120,350)\\\\pos(590,505)\\\\p1\\\\fscx0\\\\t(0,500,\\\\fscx100)}m 0 0 l 100 0 100 5 0 5{\\\\p0}"))
'''
s = s.replace("for ph_, big, src_ in QUOTES:", emph + "\nfor ph_, big, src_ in QUOTES:", 1)
s = s.replace("Style: Quote,", "Style: Emph,Poppins,118,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,5,4,5,0,0,0,1\nStyle: EmphG,Poppins,118,%s,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,5,4,5,0,0,0,1\nStyle: Quote,", 1)
s = s.replace('""" % (GOLD, GOLD)', '""" % (GOLD, GOLD, GOLD)')
s = s.replace("Style: Bar,Poppins,20,%s", "Style: Bar,Poppins,20,%s")
open("build_v5.py", "w", encoding="utf-8").write(s)
