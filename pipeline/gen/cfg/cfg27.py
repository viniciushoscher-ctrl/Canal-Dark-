#--KEY
KEY = ['albany', 'america', 'bear', 'bible', 'bull', 'carmel', 'central', 'city', 'company', 'cornelius', 'daniel', 'drew', 'eighteen', 'erie', 'fisk', 'gould', 'great', 'head', 'hudson', 'jersey', 'july', 'madison', 'manhattan', 'methodist', 'railroad', 'ring', 'river', 'robinson', 'seminary', 'september', 'speculator', 'street', 'theological', 'twelve', 'university', 'vanderbilt', 'wall', 'york']
#--CH
CH = [('CHAPTER 1', 'THE COW DROVER', 'OF NEW YORK'), ('CHAPTER 2', 'STEAMBOATS', 'AND WALL STREET'), ('CHAPTER 3', 'THE SPECULATIVE', 'DIRECTOR'), ('CHAPTER 4', 'THE ERIE WAR', ''), ('CHAPTER 5', 'THE PANIC', 'OF 1873'), ('CHAPTER 6', 'THE FALL', "OF UNCLE DAN'L"), ('THE LESSON', 'WATERED', 'STOCK')]
CARDS = [('daniel drew was born on july twenty-ninth', '1797', 'DREW', 'Daniel Drew was born on July twent', None),
 ('he opened a brokerage firm on wall', '1846', 'WALL STREET', 'He opened a brokerage firm on Wall', None),
 ('he funded a methodist church in lower', '1867', 'METHODIST', 'He funded a Methodist church in lo', None),
 ('the erie war began in eighteen sixty-eight', '1868', 'ERIE WAR', 'The Erie War began in eighteen six', None),
 ('in eighteen sixty-nine gould and fisk turned', '1869', 'GOULD', 'In eighteen sixty-nine, Gould and', None)]
#--BRT
MAPBRT = []
BRT = []
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = []
#--EMPH
EMPH = []
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'reflect', 7: 'reflect'}
TRG = [('eighteen sixty-eight', 'tense'), ('daniel drew was born on july', 'sad'), ('drew developed a trick', 'drive'), ('the steamboat war was fierce', 'wonder'), ('at the same time drew was', 'triumph'), ('the erie war began in eighteen', 'dark'), ('drew had made one fatal mistake', 'reflect'), ("daniel drew's story holds two lessons", 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
