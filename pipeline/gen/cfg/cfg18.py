#--KEY
KEY = {"gates", "bill", "microsoft", "ibm", "dos", "windows", "software", "allen", "paul", "harvard", "billion", "billions", "monopoly", "antitrust", "foundation", "lakeside", "computer", "operating", "system", "license"}
#--CH
CH = [("CHAPTER 1", "THE KID IN", "THE COMPUTER ROOM"), ("CHAPTER 2", "THE BLUFF", "THAT BECAME BASIC"), ("CHAPTER 3", "THE DEAL OF", "THE CENTURY"),
      ("CHAPTER 4", "A WINDOW ON", "EVERY DESK"), ("CHAPTER 5", "THE MONOPOLY", "TRIAL"), ("CHAPTER 6", "THE GIVING", "MACHINE"), ("THE LESSON", "SAY YES,", "THEN DELIVER")]
CARDS = [("william henry gates the third was born", "1955", "GATES IS BORN", "Seattle, Washington", None),
         ("in january nineteen seventy-five allen", "1975", "THE ALTAIR BLUFF", "Microsoft is born", None),
         ("gates called seattle computer", "1980", "MS-DOS", "bought for $50,000", None),
         ("in nineteen eighty-six microsoft went public", "1986", "MICROSOFT IPO", "Gates owns 45%", None),
         ("in nineteen ninety-eight the united states", "1998", "THE ANTITRUST CASE", "U.S. vs. Microsoft", None),
         ("in two thousand they merged", "2000", "THE GATES FOUNDATION", "the largest in the world", None),
         ("today microsoft is one of the most valuable", "TODAY", "MICROSOFT", "over $3 trillion", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("for about fifty thousand dollars", g_dos, 5.5), ("worth about three hundred million", g_ipo, 5.5), ("over a hundred billion dollars", g_peak, 5.5),
       ("waited in line at midnight", FFg("crowd"), 5.5), ("sued microsoft", FFg("court"), 5.5), ("rolling stones", FFg("tv"), 5.0), ("microsoft was growing fast", FFg("office"), 5.0)] + MAPBRT
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is bill gates', 'people/gates.jpg', '1955 –', 'BILL GATES', 'co-founder of Microsoft', True, 0),
 ('lakeside school', 'fotos/lakeside_0.jpg', '1968', 'LAKESIDE SCHOOL', 'where he met Paul Allen', True, 0),
 ('a teletype terminal', 'fotos/terminal_0.jpg', '1968', 'THE TELETYPE', 'his first computer terminal', True, 0),
 ('a boy two years older named paul allen', 'people/allen.jpg', '1953 – 2018', 'PAUL ALLEN', 'co-founder of Microsoft', True, 0),
 ('harvard in nineteen seventy-three', 'fotos/harvard_0.jpg', '1973', 'HARVARD', 'the dropout', True, 0),
 ('the altair', 'fotos/altair_0.jpg', '1975', 'THE ALTAIR 8800', 'the first personal computer', True, 0),
 ('gary kildall', 'people/kildall.jpg', '1942 – 1994', 'GARY KILDALL', 'creator of CP/M', True, 0),
 ('tim paterson', 'people/paterson.jpg', '1980', 'TIM PATERSON', 'creator of QDOS', True, 0),
 ('the ibm pc', 'fotos/ibmpc_0.jpg', '1981', 'THE IBM PC', 'the machine that ran MS-DOS', True, 0),
 ('steve jobs', 'people/jobs.jpg', '1985', 'STEVE JOBS', 'angry about Windows', True, 0),
 ('xerox', 'fotos/xerox_0.jpg', '1973', 'XEROX ALTO', 'the original graphical interface', True, 0),
 ('windows ninety-five', 'fotos/win95_0.jpg', '1995', 'WINDOWS 95', 'a cultural phenomenon', True, 0),
 ('netscape', 'fotos/netscape_0.jpg', '1995', 'NETSCAPE', 'the browser Microsoft crushed', True, 0),
 ('justice department sued', 'fotos/doj_0.jpg', '1998', 'U.S. vs. MICROSOFT', 'the antitrust trial', True, 0),
 ('melinda french', 'people/melinda.jpg', '1994', 'MELINDA FRENCH GATES', 'co-founder of the foundation', True, 0),
 ('warren buffett', 'people/buffett.jpg', '2010', 'WARREN BUFFETT', 'the Giving Pledge partner', True, 0),
 ('a vaccine', 'fotos/vaccine_0.jpg', '2000s', 'GLOBAL HEALTH', 'vaccines and malaria', True, 0)]
#--EMPH
EMPH = [("but he says yes", "BUT HE", "SAYS YES"), ("keeps the right to sell the same software to everyone", "HE KEPT THE", "RIGHT TO SELL"), ("illegal monopoly", "AN ILLEGAL", "MONOPOLY"),
        ("not a reward but a responsibility", "NOT A REWARD.", "A RESPONSIBILITY."), ("say yes", "SAY YES.", "THEN DELIVER.")]
#--MUSIC
DEF = {0: "tense", 1: "drive", 2: "wonder", 3: "triumph", 4: "upbeat", 5: "dark", 6: "wonder", 7: "reflect"}
TRG = [("nineteen eighty a twenty-four-year-old", "tense"), ("william henry gates the third was born", "sad"), ("gates entered harvard", "drive"), ("in january nineteen seventy-five", "wonder"),
       ("then came the great opportunity", "tense"), ("then he made the deal of the century", "triumph"), ("in nineteen eighty-six microsoft", "upbeat"), ("but success brought enemies", "dark"),
       ("in nineteen ninety-eight the united states", "dark"), ("gates then made a dramatic change", "wonder"), ("the second is that power", "reflect")]
TWISTS = ["he does not but he says yes", "then he made the deal of the century", "in nineteen ninety-eight the united states justice department", "gates then made a dramatic change", "the second is that power"]
#--NSC
76
#--MAP
MAPBRT = [("william henry gates the third was born", lambda u: g_map(u, -122.33, 47.61, "SEATTLE, WASHINGTON", "UNITED STATES  ·  1955"), 7.0)]
#--KW
{"A young man in an ill-fitting suit": "msft_0", "A Seattle skyline": "lakeside_0", "A school computer room": "terminal_0", "Two teenagers hunched": "terminal_1",
 "Harvard University gates": "harvard_0", "A Harvard Square newsstand": "altair_0", "A computer lab with a mainframe": "harvard_1", "A corporate headquarters of a computer giant": "ibmpc_0",
 "A personal computer on a desk": "ibmpc_1", "A graphical computer interface": "win_0", "A crowd waiting in line": "win95_0", "A browser war": "netscape_0",
 "A Justice Department building": "doj_0", "A global health clinic": "vaccine_0", "A foundation headquarters": "foundation_0"}
