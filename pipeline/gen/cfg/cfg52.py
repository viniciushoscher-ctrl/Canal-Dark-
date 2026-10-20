#--KEY
KEY = ['academy', 'alberghettino', 'albizzi', 'angelico', 'august', 'bardi', 'bicci', 'bruges', 'brunelleschi', 'careggi', 'cathedral', 'catherine', 'church', 'contessina', 'cosimo', 'david', 'donatello', 'dukes', 'europe', 'father', 'fatherland', 'ficino', 'filippo', 'florence', 'france', 'francesco', 'geneva', 'giorgio', 'giovanni', 'gonfaloniere', 'gouty', 'grand', 'greek', 'italian', 'italy', 'latin', 'lippi', 'lodi', 'london', 'lorenzo', 'magnificent', 'marie', 'marsilio', 'medici', 'milan', 'mugello', 'october', 'padua', 'palazzo', 'pater']
#--CH
CH = [('CHAPTER 1', "THE BANKER'S", 'SON'), ('CHAPTER 2', 'THE MOST INNOVATIVE', 'BANK IN EUROPE'), ('CHAPTER 3', 'THE PRISONER', 'OF THE PALAZZO'), ('CHAPTER 4', 'THE FATHER', 'OF THE COUNTRY'), ('CHAPTER 5', 'THE PATRON', 'OF THE RENAISSANCE'), ('CHAPTER 6', 'A QUIET', 'AND SAD OLD AGE'), ('CHAPTER 7', 'THE FALL AND', 'RETURN OF THE MEDICI'), ('THE LESSON', 'THE LESSONS', "OF COSIMO DE' MEDICI")]
CARDS = [('born on the twenty-seventh of september', '1389', 'COSIMO IS BORN', 'Florence, Italy', None),
 ('by the time giovanni died in fourteen twenty-nine', '1429', 'COSIMO INHERITS THE BANK', 'Giovanni dies', None),
 ('in fourteen thirty-three the albizzi struck', '1433', 'COSIMO IS ARRESTED', 'Palazzo Vecchio', None),
 ('on the sixth of october fourteen thirty-four', '1434', 'COSIMO RETURNS', 'father of the country', None),
 ('in fourteen fifty-four the peace of lodi', '1454', 'THE PEACE OF LODI', 'Cosimo\'s diplomacy', None),
 ('giovanni his favorite died young in fourteen sixty-three', '1463', 'GIOVANNI DIES', 'Cosimo is heartbroken', None),
 ('he died on the first of august fourteen sixty-four', '1464', 'COSIMO DIES', 'Careggi, age 74', None),
 ('by fourteen ninety-four the bank had collapsed', '1494', 'THE MEDICI BANK COLLAPSES', 'the family is exiled', None),
 ('in fifteen sixty-nine they became the grand dukes of tuscany', '1569', 'GRAND DUKES OF TUSCANY', 'two centuries of rule', None)]
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
EMPH = [('thirty years','30 YEARS','RULING FLORENCE')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('fourteen thirty-three', 'tense'), ("cosimo di giovanni de' medici was", 'sad'), ('cosimo was a very different man', 'drive'), ('but wealth made him dangerous', 'wonder'), ('in fourteen thirty-four a new government', 'triumph'), ('but the story of cosimo is', 'dark'), ('cosimo had a troubled family life', 'sad'), ('but the medici bank did not', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
