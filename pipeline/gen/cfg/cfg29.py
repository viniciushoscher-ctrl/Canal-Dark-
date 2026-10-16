#--KEY
KEY = ['abraham', 'america', 'american', 'april', 'barrett', 'beman', 'black', 'british', 'brocton', 'brotherhood', 'buffalo', 'calumet', 'canal', 'chicago', 'cleveland', 'company', 'court', 'debs', 'erie', 'eugene', 'general', 'george', 'grover', 'hotel', 'illinois', 'lake', 'lincoln', 'march', 'mortimer', 'nathan', 'october', 'olney', 'palace', 'pioneer', 'porters', 'president', 'pullman', 'railway', 'richard', 'sleeping', 'solon', 'south', 'supreme', 'tremont', 'union', 'westfield', 'york']
#--CH
CH = [('CHAPTER 1', 'THE HOUSE', 'LIFTER'), ('CHAPTER 2', 'THE SLEEPING', 'CAR'), ('CHAPTER 3', 'THE PIONEER', ''), ('CHAPTER 4', 'THE MODEL', 'TOWN'), ('CHAPTER 5', 'WAGES AND', 'RENT'), ('CHAPTER 6', 'THE STRIKE', 'OF 1894'), ('THE LESSON', 'THE PEOPLE', 'BEHIND COMFORT')]
CARDS = [('george mortimer pullman was born on march', '1831', 'MORTIMER PULLMAN', 'George Mortimer Pullman was born o', None),
 ('in eighteen fifty-eight he persuaded a railroad', '1858', 'THE STORY', 'In eighteen fifty-eight, he persua', None),
 ('pullman created the pullman palace car company', '1867', 'PULLMAN PALACE CAR COMPA', 'Pullman created the Pullman Palace', None),
 ('in eighteen eighty pullman made his most', '1880', 'PULLMAN', 'In eighteen eighty, Pullman made h', None),
 ('in eighteen ninety-three a financial panic struck', '1893', 'THE STORY', 'In eighteen ninety-three, a financ', None),
 ('in eighteen ninety-eight the illinois supreme court', '1898', 'ILLINOIS SUPREME COURT', 'In eighteen ninety-eight, the Illi', None)]
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
TRG = [('eighteen ninety-four', 'tense'), ('george mortimer pullman was born on', 'sad'), ("but pullman's mind was on another", 'drive'), ('he was a master of detail', 'wonder'), ('in eighteen eighty pullman made his', 'triumph'), ('the town drew visitors from around', 'dark'), ('the strike was crushed but the', 'reflect'), ("george pullman's story holds two lessons", 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
