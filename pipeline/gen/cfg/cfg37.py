#--KEY
KEY = ['agunnaryd', 'american', 'antarctica', 'billy', 'britain', 'christmas', 'curtain', 'dealer', 'elmtaryd', 'feodor', 'france', 'furniture', 'germany', 'gillis', 'ingvar', 'iron', 'january', 'kamprad', 'liechtenstein', 'lundgren', 'march', 'mathias', 'netherlands', 'philadelphia', 'poland', 'scandinavia', 'states', 'stichting', 'stockholm', 'sweden', 'swedish', 'switzerland', 'testament', 'united', 'volvo']
#--CH
CH = [('CHAPTER 1', 'FARM BOY', 'FROM SMALAND'), ('CHAPTER 2', 'I-K-E-A', 'IS BORN'), ('CHAPTER 3', 'THE TABLE', 'LEGS'), ('CHAPTER 4', 'POLAND', 'AND THE STORE'), ('CHAPTER 5', 'GOING', 'GLOBAL'), ('CHAPTER 6', 'THE FRUGAL', 'BILLIONAIRE'), ('CHAPTER 7', 'THE LAST', 'YEARS'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('ingvar feodor kamprad was born on the thirtieth', '1926', 'INGVAR KAMPRAD IS BORN', 'Elmtaryd farm, Småland', None),
 ('in nineteen forty-three when ingvar was seventeen', '1943', 'IKEA IS FOUNDED', 'Ingvar, Elmtaryd, Agunnaryd', None),
 ('so in nineteen fifty-three kamprad opened a showroom', '1953', 'THE ÄLMHULT SHOWROOM', 'try before you buy', None),
 ('then came the table in nineteen fifty-six', '1956', 'THE FLAT PACK IS BORN', 'table legs come off', None),
 ('in nineteen fifty-eight he opened the first real ikea', '1958', 'FIRST IKEA STORE', 'Älmhult, Sweden', None),
 ('in nineteen sixty-five he opened a huge store', '1965', 'THE STOCKHOLM STORE', 'crowds shut the doors', None),
 ('in nineteen seventy-three ikea opened its first store', '1973', 'FIRST STORE ABROAD', 'Switzerland', None),
 ('in nineteen ninety-four a swedish journalist', '1994', 'THE FASCIST PAST', 'a public apology', None),
 ('he died on the twenty-seventh of january', '2018', 'INGVAR KAMPRAD DIES', 'age 91', None)]
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
EMPH = [('at the age of five','AGE 5','FIRST MATCH SALES'),('seventeen year old','AGE 17','IKEA FOUNDED')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen fifty-six', 'tense'), ('ingvar feodor kamprad was born on', 'sad'), ('in nineteen forty-three when ingvar was', 'drive'), ('in nineteen fifty-one he made an', 'wonder'), ('the boycott gave kamprad an even', 'triumph'), ('in nineteen seventy-three ikea opened its', 'dark'), ("everything about kamprad's personal life was", 'sad'), ('in nineteen eighty-six kamprad stepped down', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
