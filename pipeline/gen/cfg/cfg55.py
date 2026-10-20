#--KEY
KEY = ['america', 'american', 'americans', 'armour', 'barnstable', 'boston', 'brighton', 'canadian', 'cape', 'chicago', 'company', 'congress', 'cudahy', 'drug', 'east', 'eastern', 'england', 'esmark', 'five', 'food', 'franklin', 'grand', 'gustavus', 'inspection', 'june', 'jungle', 'march', 'massachusetts', 'meat', 'methodist', 'morris', 'premium', 'pure', 'railway', 'sandwich', 'sinclair', 'stock', 'swift', 'texas', 'trunk', 'union', 'upton', 'west', 'william', 'wilson', 'yards', 'york']
#--CH
CH = [('CHAPTER 1', 'THE BUTCHER', 'FROM CAPE COD'), ('CHAPTER 2', 'THE IMPOSSIBLE', 'IDEA'), ('CHAPTER 3', 'THE WAR', 'AGAINST THE BUTCHERS'), ('CHAPTER 4', 'EVERYTHING', 'BUT THE SQUEAL'), ('CHAPTER 5', 'THE JUNGLE', 'AND THE REFORMS'), ('CHAPTER 6', 'THE EMPIRE', 'AFTER SWIFT'), ('CHAPTER 7', 'THE COLD', 'CHAIN'), ('THE LESSON', 'THE LESSONS', 'OF GUSTAVUS SWIFT')]
CARDS = [('born on the twenty-fourth of june eighteen thirty-nine', '1839', 'GUSTAVUS SWIFT IS BORN', 'Cape Cod, Massachusetts', None),
 ('in eighteen seventy-five swift moved to chicago', '1875', 'SWIFT MOVES TO CHICAGO', 'the Union Stock Yards', None),
 ('in the late eighteen seventies they built an improved car', '1878', 'THE REFRIGERATED CAR', 'ice on top, air circulating', None),
 ('by the early eighteen eighties swift and company', '1880', 'ONE OF THE LARGEST', 'meatpackers in America', None),
 ('by eighteen eighty-five swift and company was slaughtering', '1885', '400,000 CATTLE A YEAR', 'Swift and Company', None),
 ('in nineteen oh six the writer upton sinclair', '1906', 'THE JUNGLE', 'Upton Sinclair', None),
 ('gustavus swift died suddenly on the twenty-ninth of march', '1903', 'GUSTAVUS SWIFT DIES', 'age 63', None),
 ('in nineteen twelve the government sued them', '1912', 'ANTITRUST LAWSUIT', 'the Big Five packers', None),
 ('in nineteen twenty the packers signed a consent decree', '1920', 'CONSENT DECREE', 'the packers\' power declines', None)]
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
EMPH = [('about sixty percent','60% WASTE','OF A STEER\'S WEIGHT'),('about twenty-five million dollars','$25 MILLION','HIS FORTUNE')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('chicago eighteen seventy-five', 'tense'), ('gustavus franklin swift was born on', 'sad'), ('in eighteen seventy-five swift moved to', 'drive'), ('but the technology was only the', 'wonder'), ('swift did not stop with beef', 'triumph'), ('swift was a stern but devout', 'dark'), ('gustavus swift died suddenly on the', 'sad'), ('the legacy of gustavus swift is', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
