#--KEY
KEY = ['airflow', 'alen', 'america', 'american', 'april', 'august', 'auto', 'bernice', 'breer', 'brothers', 'buick', 'building', 'carl', 'charles', 'chevrolet', 'chicago', 'chrysler', 'colorado', 'company', 'corporation', 'della', 'depression', 'detroit', 'durant', 'east', 'elizabeth', 'ellis', 'flint', 'ford', 'forker', 'forty', 'fred', 'general', 'great', 'henry', 'iowa', 'january', 'jersey', 'kansas', 'locomobile', 'locomotive', 'manhattan', 'maxwell', 'michigan', 'motors', 'musketeers', 'nash', 'neck', 'october', 'oelwein']
#--CH
CH = [('CHAPTER 1', 'KANSAS', 'RAILROAD BOY'), ('CHAPTER 2', 'THE LOCOMOBILE', 'GAMBLE'), ('CHAPTER 3', 'BUICK', 'AND DURANT'), ('CHAPTER 4', 'THE THREE', 'MUSKETEERS'), ('CHAPTER 5', 'THE BIG', 'THREE'), ('CHAPTER 6', 'THE TALLEST', 'BUILDING'), ('CHAPTER 7', 'AIRFLOW', 'AND FAREWELL'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('walter percy chrysler was born on the second', '1875', 'WALTER CHRYSLER IS BORN', 'Wamego, Kansas', None),
 ('by nineteen oh eight he was thirty-three', '1908', 'THE LOCOMOBILE', 'bought for $5,000', None),
 ('when he arrived in flint in nineteen eleven', '1911', 'BUICK WORKS MANAGER', 'Flint, Michigan', None),
 ('in nineteen sixteen durant made him president', '1916', 'PRESIDENT OF BUICK', 'salary: $500,000 a year', None),
 ('in january of nineteen twenty-four at the new york', '1924', 'THE CHRYSLER SIX', '32,000 sold in year one', None),
 ('in nineteen twenty-five chrysler reorganized', '1925', 'CHRYSLER CORPORATION', 'built from Maxwell', None),
 ('he made the deal', '1928', 'DODGE BROTHERS BOUGHT', 'about $170 million', None),
 ('in october of nineteen twenty-nine the spire', '1929', 'THE SPIRE RISES', '1,046 feet tall', None),
 ('walter chrysler died on the eighteenth of august', '1940', 'WALTER CHRYSLER DIES', 'Great Neck, New York', None)]
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
EMPH = [('five cents an hour','5 CENTS','AN HOUR'),('about one hundred and seventy million dollars','$170 MILLION','DODGE DEAL'),('one thousand and forty-six feet','1,046 FEET','TALLEST ON EARTH'),('more than thirty-two thousand cars','32,000 CARS','FIRST YEAR')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('october nineteen twenty-nine', 'tense'), ('walter percy chrysler was born on', 'sad'), ('for the next fifteen years chrysler', 'drive'), ('chrysler was now obsessed', 'wonder'), ('retirement lasted about a year', 'triumph'), ('in nineteen twenty-five chrysler reorganized the', 'dark'), ('and now with money and fame', 'sad'), ('the timing could not have been', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
