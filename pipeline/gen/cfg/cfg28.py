#--KEY
KEY = ['america', 'american', 'asia', 'builder', 'burlington', 'canada', 'canadian', 'cascades', 'catholic', 'chicago', 'company', 'court', 'dakota', 'empire', 'europe', 'george', 'germany', 'great', 'hill', 'irish', 'james', 'january', 'jerome', 'john', 'lakes', 'manitoba', 'minneapolis', 'minnesota', 'mississippi', 'montana', 'morgan', 'mountains', 'north', 'northern', 'northwest', 'ocean', 'ontario', 'pacific', 'panic', 'pass', 'quincy', 'railroad', 'railway', 'river', 'rockwood', 'rocky', 'roosevelt', 'santa', 'scandinavia', 'scottish']
#--CH
CH = [('CHAPTER 1', 'THE BOY WITH', 'ONE EYE'), ('CHAPTER 2', 'THE FAILED', 'RAILROAD'), ('CHAPTER 3', 'WITHOUT LAND', 'GRANTS'), ('CHAPTER 4', 'THE ROAD TO', 'THE PACIFIC'), ('CHAPTER 5', 'THE FIGHT', 'WITH HARRIMAN'), ('CHAPTER 6', 'THE EMPIRE', 'BUILDER'), ('THE LESSON', 'BUILD', 'CAREFULLY')]
CARDS = [('james jerome hill was born on september', '1838', 'JEROME HILL', 'James Jerome Hill was born on Sept', None),
 ('with three partners including a canadian banker', '1878', 'CANADIAN', 'With three partners, including a C', None),
 ('in eighteen ninety he renamed his company', '1890', 'GREAT NORTHERN RAILWAY', 'In eighteen ninety, he renamed his', None),
 ('the great northern reached seattle on january', '1893', 'GREAT NORTHERN', 'The Great Northern reached Seattle', None),
 ('he died on may twenty-ninth nineteen sixteen', '1916', 'THE STORY', 'He died on May twenty-ninth, ninet', None)]
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
TRG = [('january eighteen ninety-three', 'tense'), ('james jerome hill was born on', 'sad'), ('he was also fierce about work', 'drive'), ('hill brought thousands of immigrants from', 'wonder'), ('hill also surprised bankers with his', 'triumph'), ('the great northern reached seattle on', 'dark'), ('but the government objected', 'reflect'), ('james j', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
