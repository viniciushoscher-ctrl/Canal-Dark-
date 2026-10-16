#--KEY
KEY = ['america', 'american', 'argentina', 'autonomous', 'bell', 'bill', 'brazil', 'carlos', 'carso', 'city', 'colombia', 'dali', 'domit', 'east', 'empire', 'forbes', 'foundation', 'france', 'gates', 'grupo', 'haddad', 'houston', 'inbursa', 'january', 'latin', 'lebanese', 'linda', 'mexican', 'mexicans', 'mexico', 'miami', 'movil', 'museum', 'national', 'ottoman', 'portillo', 'revolution', 'rodin', 'sanborns', 'slim', 'soumaya', 'southwestern', 'spanish', 'star', 'states', 'switzerland', 'telecom', 'telmex', 'times', 'united']
#--CH
CH = [('CHAPTER 1', 'THE LEBANESE', 'SON'), ('CHAPTER 2', 'THE MATHEMATICS', 'STUDENT'), ('CHAPTER 3', 'THE CRASH', 'OF 1982'), ('CHAPTER 4', 'THE PHONE', 'COMPANY'), ('CHAPTER 5', 'THE SECOND', 'CRASH'), ('CHAPTER 6', 'THE RICHEST', 'MAN ALIVE'), ('CHAPTER 7', 'THE LATE', 'YEARS'), ('THE LESSON', 'THE LESSON', 'WHAT HE TAUGHT US')]
CARDS = [('carlos slim helu was born on the twenty-eighth', '1940', 'CARLOS SLIM IS BORN', 'Mexico City', None),
 ('in nineteen sixty-five at the age of', '1965', 'CARSO IS FOUNDED', 'real estate', None),
 ('but in nineteen eighty-two oil prices fell', '1982', 'MEXICO DEFAULTS', 'he buys while others flee', None),
 ('in nineteen ninety the mexican government decided', '1990', 'THE TELMEX AUCTION', 'a monopoly for sale', None),
 ('in nineteen ninety-four the peso collapsed again', '1994', 'THE PESO COLLAPSES', 'he buys again', None),
 ('in two thousand he spun off', '2000', 'AMERICA MOVIL', 'mobile across Latin America', None),
 ('in two thousand and ten a list published', '2010', 'RICHEST MAN ALIVE', 'passing Bill Gates', None),
 ('his wife soumaya died in nineteen ninety-nine', '1999', 'SOUMAYA DIES', 'the Soumaya Museum', None)]
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
EMPH = [('about one point seven six billion dollars','$1.76 BILLION','FOR TELMEX'),('more than fifty billion dollars','$50 BILLION','RICHEST MAN ALIVE')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('september nineteen eighty-two', 'tense'), ('carlos slim hel was born on', 'sad'), ('slim studied civil engineering at the', 'drive'), ('mexico in the nineteen seventies had', 'wonder'), ('by the end of the nineteen', 'triumph'), ('in the nineteen nineties mexico suffered', 'dark'), ('in two thousand and ten a', 'sad'), ('in his later years slim began', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
