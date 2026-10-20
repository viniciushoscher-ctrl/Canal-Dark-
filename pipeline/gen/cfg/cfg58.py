#--KEY
KEY = ['amancio', 'antonio', 'arbas', 'argentina', 'arteixo', 'asia', 'atlantic', 'bangladesh', 'bear', 'bershka', 'brazil', 'buffett', 'busdongo', 'civil', 'confecciones', 'coruna', 'diseno', 'dutti', 'flora', 'forbes', 'gala', 'galicia', 'gaona', 'germany', 'home', 'inditex', 'industria', 'isla', 'josefa', 'july', 'leon', 'madrid', 'maja', 'march', 'marcos', 'marta', 'massimo', 'mera', 'morocco', 'ortega', 'oysho', 'pablo', 'paris', 'perez', 'plaza', 'porto', 'portugal', 'pull', 'rana', 'rosalia']
#--CH
CH = [('CHAPTER 1', 'A BOY', 'FROM LEON'), ('CHAPTER 2', 'THE SEAMSTRESS', 'AND THE SEWING MACHINE'), ('CHAPTER 3', 'THE FIRST', 'ZARA'), ('CHAPTER 4', 'THE GLOBAL', 'EXPANSION'), ('CHAPTER 5', 'THE SECRET', 'OF SPEED'), ('CHAPTER 6', 'THE RICHEST', 'MAN'), ('CHAPTER 7', 'THE PRIVATE', 'LIFE'), ('THE LESSON', 'THE LESSONS', 'OF ORTEGA')]
CARDS = [('amancio ortega gaona was born on the twenty-eighth of march', '1936', 'AMANCIO ORTEGA IS BORN', 'Leon, Spain', None),
 ('in nineteen sixty-three at the age of twenty-seven', '1963', 'HIS FIRST WORKSHOP', 'bathrobes and nightgowns', None),
 ('in nineteen seventy-five he opened the first zara store', '1975', 'THE FIRST ZARA', 'La Coruna, Spain', None),
 ('in nineteen eighty-five ortega formed a holding company', '1985', 'INDITEX IS FOUNDED', 'Industria de Diseno Textil', None),
 ('in nineteen eighty-eight he opened the first zara outside spain', '1988', 'FIRST STORE ABROAD', 'Porto, Portugal', None),
 ('in two thousand and one inditex went public', '2001', 'INDITEX GOES PUBLIC', 'Madrid stock exchange', None),
 ('in two thousand and thirteen the collapse of the rana plaza', '2013', 'RANA PLAZA COLLAPSE', 'Bangladesh', None),
 ('in two thousand and fifteen he was briefly the richest man', '2015', 'RICHEST MAN ON EARTH', 'about $80 billion', None)]
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
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen forty-eight', 'tense'), ('amancio ortega gaona was born on', 'sad'), ('in nineteen sixty-three at the age', 'drive'), ('the first zara shop was modest', 'wonder'), ('in nineteen eighty-five ortega formed a', 'triumph'), ('the secret was in the details', 'dark'), ("as inditex grew so did ortega's", 'sad'), ("ortega's personal life was mostly private", 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
