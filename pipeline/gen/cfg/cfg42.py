#--KEY
KEY = ['agency', 'america', 'american', 'ampex', 'apple', 'area', 'august', 'bill', 'california', 'catz', 'central', 'champaign', 'chicago', 'city', 'codd', 'development', 'edgar', 'ellison', 'elon', 'england', 'florence', 'francisco', 'gates', 'hawaiian', 'hurd', 'hyperion', 'illinois', 'institute', 'intelligence', 'java', 'jewish', 'jobs', 'joseph', 'laboratories', 'lanai', 'larry', 'lillian', 'louis', 'march', 'mark', 'microsoft', 'microsystems', 'miner', 'musk', 'oates', 'oracle', 'oxford', 'russian', 'safra', 'side']
#--CH
CH = [('CHAPTER 1', 'THE ADOPTED', 'BOY'), ('CHAPTER 2', 'THE RELATIONAL', 'IDEA'), ('CHAPTER 3', 'THE FOUNDING', 'OF ORACLE'), ('CHAPTER 4', 'THE NEAR', 'COLLAPSE'), ('CHAPTER 5', 'THE WAR', 'OF ACQUISITIONS'), ('CHAPTER 6', "THE AMERICA'S", 'CUP'), ('CHAPTER 7', 'THE PASSING', 'OF THE CROWN'), ('THE LESSON', 'THE LESSON', 'WHAT HE TAUGHT US')]
CARDS = [('lawrence joseph ellison was born on the seventeenth', '1944', 'LARRY ELLISON IS BORN', 'New York City', None),
 ('in the early nineteen seventies he landed', '1970', 'THE RELATIONAL IDEA', 'Edgar Codd at IBM', None),
 ('in nineteen seventy-seven at the age of', '1977', 'ORACLE IS FOUNDED', 'Software Development Laboratories', None),
 ('oracle went public in march nineteen eighty-six', '1986', 'ORACLE GOES PUBLIC', 'Ellison becomes a billionaire', None),
 ('then in nineteen ninety the empire almost', '1990', 'THE NEAR COLLAPSE', 'first loss', None),
 ('in two thousand and four after an exhausting', '2004', 'PEOPLESOFT', 'a $10 billion takeover', None),
 ('in two thousand and ten it bought sun', '2010', 'SUN MICROSYSTEMS', 'Java and MySQL', None),
 ('then came the comeback in san francisco', '2013', "THE AMERICA'S CUP", 'down eight to one', None),
 ('in two thousand and fourteen at the age of', '2014', 'ELLISON STEPS DOWN', 'age 69', None)]
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
EMPH = [('for more than ten billion dollars','$10 BILLION','PEOPLESOFT'),('for about seven billion dollars','$7 BILLION','SUN MICROSYSTEMS'),('for a reported three hundred million dollars','$300 MILLION','FOR LANAI')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('september two thousand and thirteen', 'tense'), ('lawrence joseph ellison was born on', 'sad'), ('in nineteen sixty-six california was a', 'drive'), ('in nineteen seventy-seven at the age', 'wonder'), ('oracle went public in march nineteen', 'triumph'), ('ellison was famous for his friendship', 'dark'), ('meanwhile ellison built a life that', 'sad'), ('in two thousand and fourteen at', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
