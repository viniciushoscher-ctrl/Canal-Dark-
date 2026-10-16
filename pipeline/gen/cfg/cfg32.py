#--KEY
KEY = ['america', 'american', 'april', 'army', 'atlantic', 'avenue', 'caramel', 'catherine', 'centennial', 'chicago', 'chocolate', 'city', 'cocoa', 'colorado', 'columbian', 'company', 'denver', 'derry', 'dutch', 'east', 'england', 'english', 'europe', 'exposition', 'fanny', 'german', 'henry', 'hershey', 'hersheypark', 'industrial', 'joseph', 'kiss', 'kitty', 'lancaster', 'mennonite', 'milton', 'october', 'orleans', 'pennsylvania', 'philadelphia', 'ration', 'royer', 'school', 'september', 'snavely', 'states', 'sweeney', 'swiss', 'titanic', 'township']
#--CH
CH = [('CHAPTER 1', 'THE BOY FROM', 'DERRY TOWNSHIP'), ('CHAPTER 2', 'THE FIRST', 'FAILURE'), ('CHAPTER 3', 'THE WILDERNESS', 'YEARS'), ('CHAPTER 4', 'THE CARAMEL', 'COMEBACK'), ('CHAPTER 5', 'THE CHOCOLATE', 'BET'), ('CHAPTER 6', 'THE TOWN BUILT', 'ON COCOA'), ('CHAPTER 7', 'THE ORPHAN', "BOYS' HEIR"), ('CHAPTER 8', 'THE DEPRESSION', 'AND THE WAR'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('milton snavely hershey was born on', '1857', 'MILTON HERSHEY IS BORN', 'Derry Township, Pennsylvania', None),
 ('in eighteen seventy-six the united states', '1876', 'THE CENTENNIAL EXPOSITION', 'his first shop opens', None),
 ('after six years in eighteen eighty-two', '1882', 'THE FIRST BANKRUPTCY', 'the Philadelphia shop closes', None),
 ('in eighteen eighty-six at the age of', '1886', 'LANCASTER CARAMEL COMPANY', 'caramels made with fresh milk', None),
 ('in eighteen ninety-three chicago hosted the', '1893', "THE WORLD'S FAIR", 'German chocolate machinery', None),
 ('later that year the first hershey milk', '1900', 'THE FIRST MILK CHOCOLATE BAR', 'price: 5 cents', None),
 ('so in nineteen hundred and three he', '1903', 'THE FACTORY IN THE CORNFIELD', 'Derry Township, Pennsylvania', None),
 ('in nineteen oh nine milton and kitty', '1909', 'THE ORPHAN SCHOOL', 'Hershey Industrial School', None),
 ('in nineteen twenty-nine the american stock', '1929', 'THE GREAT CRASH', 'Hershey keeps his workers', None),
 ('milton hershey died on the thirteenth', '1945', 'MILTON HERSHEY DIES', 'age 88', None)]
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
EMPH = [('for one million dollars', '$1 MILLION', 'FOR THE CARAMELS'), ('it cost five cents', 'FIVE CENTS', 'A BAR'), ('about sixty million dollars', '$60 MILLION', 'GIVEN AWAY'), ('hold six hundred calories', '600 CALORIES', 'PER BAR'), ('twenty-seven million visitors', '27 MILLION', 'VISITORS')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect', 9: 'reflect'}
TRG = [('april nineteen twelve', 'tense'), ('milton snavely hershey was born on', 'sad'), ('in eighteen seventy-six the united states', 'drive'), ('the wilderness years of milton hershey', 'wonder'), ('he went back to lancaster the', 'triumph'), ('in eighteen ninety-three chicago hosted the', 'dark'), ('now hershey needed more of everything', 'sad'), ('but in the middle of the', 'wonder'), ('in nineteen twenty-nine the american stock', 'reflect'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
