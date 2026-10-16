#--KEY
KEY = ['alice', 'america', 'april', 'beach', 'bridge', 'canal', 'civil', 'cleveland', 'comfort', 'daytona', 'edison', 'flagler', 'florida', 'folly', 'harkness', 'henry', 'highway', 'hopewell', 'hotel', 'jacksonville', 'january', 'john', 'julia', 'kenan', 'labor', 'leon', 'lily', 'louis', 'mary', 'miami', 'michigan', 'mile', 'morrison', 'north', 'northerners', 'ohio', 'overseas', 'palm', 'panama', 'poinciana', 'ponce', 'presbyterian', 'river', 'rockefeller', 'royal', 'seven', 'spanish', 'standard', 'states', 'thomas']
#--CH
CH = [('CHAPTER 1', "THE PREACHER'S SON", 'LEAVES SCHOOL'), ('CHAPTER 2', 'PARTNER OF', 'ROCKEFELLER'), ('CHAPTER 3', 'A HONEYMOON', 'IN FLORIDA'), ('CHAPTER 4', 'THE PALACE', 'AT ST. AUGUSTINE'), ('CHAPTER 5', 'THE ROAD TO', 'MIAMI'), ('CHAPTER 6', 'THE RAILROAD', 'OVER THE SEA'), ('THE LESSON', 'THE MAN WHO', 'BUILT FLORIDA')]
CARDS = [('henry morrison flagler was born on january', '1830', 'MORRISON FLAGLER', 'Henry Morrison Flagler was born on', None),
 ('in eighteen seventy rockefeller flagler and others', '1870', 'ROCKEFELLER', 'In eighteen seventy, Rockefeller', None),
 ('her doctor recommended a warm climate for', '1877', 'JACKSONVILLE', 'Her doctor recommended a warm clim', None),
 ('in eighteen eighty-five flagler began building the', '1885', 'FLAGLER', 'In eighteen eighty-five, Flagler b', None),
 ("in eighteen ninety-six flagler's railroad reached a", '1896', 'FLAGLER', "In eighteen ninety-six, Flagler's", None),
 ('on january twenty-second nineteen twelve the first', '1912', 'JANUARY', 'On January twenty-second, nineteen', None)]
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
TRG = [('nineteen twelve', 'tense'), ('henry morrison flagler was born on', 'sad'), ('flagler was thirty-five and nearly broke', 'drive'), ("but flagler's life was shaken by", 'wonder'), ('in eighteen eighty-five flagler began building', 'triumph'), ("in eighteen ninety-six flagler's railroad reached", 'dark'), ("flagler's greatest project began in nineteen-oh-five", 'reflect'), ("henry flagler's story holds two lessons", 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
