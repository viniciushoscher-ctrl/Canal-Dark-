#--KEY
KEY = ['america', 'asia', 'australia', 'bank', 'beijing', 'bijing', 'britain', 'british', 'canadian', 'chaozhou', 'cheung', 'china', 'chinese', 'electric', 'english', 'europe', 'flower', 'foundation', 'german', 'guangdong', 'hong', 'hongkong', 'husky', 'hutchison', 'italian', 'italy', 'japan', 'july', 'king', 'kong', 'mannesmann', 'orange', 'plastic', 'river', 'shanghai', 'shantou', 'shing', 'states', 'superman', 'three', 'united', 'university', 'victor', 'watsons', 'west', 'whampoa', 'yangtze', 'yunjing', 'zhuang']
#--CH
CH = [('CHAPTER 1', 'ESCAPE FROM', 'CHAOZHOU'), ('CHAPTER 2', 'THE BOY', 'WHO WORKED'), ('CHAPTER 3', 'THE PLASTIC', 'FLOWER KING'), ('CHAPTER 4', 'THE 1967', 'GAMBLE'), ('CHAPTER 5', 'THE HUTCHISON', 'TAKEOVER'), ('CHAPTER 6', 'ORANGE AND', 'THE WORLD'), ('CHAPTER 7', 'THE HANDOVER', 'AND AFTER'), ('THE LESSON', 'THE LESSON', 'WHAT HE TAUGHT US')]
CARDS = [('li ka-shing was born on the twenty-ninth', '1928', 'LI KA-SHING IS BORN', 'Chaozhou, China', None),
 ('then in nineteen forty-three his father died', '1943', 'HIS FATHER DIES', 'Hong Kong', None),
 ('in nineteen fifty at the age of', '1950', 'CHEUNG KONG FOUNDED', 'Hong Kong', None),
 ('the turning point came in nineteen fifty-seven', '1957', 'PLASTIC FLOWERS', 'the turning point', None),
 ('in nineteen sixty-seven hong kong was shaken', '1967', 'THE RIOTS', 'he buys while others sell', None),
 ('in nineteen seventy-nine li made a bold', '1979', 'HUTCHISON WHAMPOA', 'first Chinese takeover', None),
 ('in nineteen ninety-four his company launched orange', '1994', 'ORANGE LAUNCHES', 'mobile network, Britain', None),
 ('in two thousand and eighteen at the age of', '2018', 'LI RETIRES', 'age 89', None)]
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
EMPH = [('six hundred and thirty-nine million hong kong dollars','HK$639 MILLION','FOR HUTCHISON'),('for about fourteen billion dollars','$14 BILLION','ORANGE SOLD')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen forty-three', 'tense'), ('li ka-shing was born on the', 'sad'), ('at fifteen li ka-shing became the', 'drive'), ('the first years of cheung kong', 'wonder'), ('in the nineteen fifties and sixties', 'triumph'), ('by the end of the nineteen', 'dark'), ('in the nineteen nineties he made', 'sad'), ('in two thousand and fifteen at', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
