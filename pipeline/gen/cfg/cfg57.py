#--KEY
KEY = ['alain', 'america', 'american', 'arnault', 'asia', 'belgian', 'belgium', 'bernard', 'bois', 'boulogne', 'boussac', 'british', 'bulgari', 'cashmere', 'catholic', 'celine', 'chandon', 'chevalier', 'chinese', 'christian', 'city', 'dame', 'dior', 'ecole', 'elon', 'etienne', 'europe', 'european', 'fendi', 'ferinel', 'ferret', 'fondation', 'forbes', 'france', 'francois', 'frank', 'french', 'frenchman', 'galliano', 'gehry', 'givenchy', 'group', 'gucci', 'guinness', 'hennessy', 'henry', 'italy', 'jacobs', 'january', 'jean']
#--CH
CH = [('CHAPTER 1', 'A BOY', 'FROM ROUBAIX'), ('CHAPTER 2', 'THE ESCAPE', 'TO AMERICA'), ('CHAPTER 3', 'THE BRAND', 'HUNTER'), ('CHAPTER 4', 'THE EMPIRE', 'OF LUXURY'), ('CHAPTER 5', 'THE LUXURY', 'RULES'), ('CHAPTER 6', 'THE RICHEST', 'MAN'), ('CHAPTER 7', 'THE FAMILY', 'OF LVMH'), ('THE LESSON', 'THE LESSONS', 'OF ARNAULT')]
CARDS = [('bernard jean etienne arnault was born on the fifth of march', '1949', 'BERNARD ARNAULT IS BORN', 'Roubaix, France', None),
 ('he became the chief executive in nineteen seventy-eight', '1978', 'CEO AT TWENTY-NINE', 'family construction firm', None),
 ('in nineteen eighty-one france elected a socialist president', '1981', 'FRANCE TURNS SOCIALIST', 'Francois Mitterrand', None),
 ('by nineteen eighty-nine after a vicious fight he had taken control', '1989', 'ARNAULT TAKES CONTROL', 'LVMH', None),
 ('in nineteen ninety-nine he took on the gucci group', '1999', 'THE GUCCI BATTLE', 'against Francois Pinault', None),
 ('in two thousand and fourteen he opened the fondation louis vuitton', '2014', 'FONDATION LOUIS VUITTON', 'designed by Frank Gehry', None),
 ('after the fire at notre dame in two thousand and nineteen', '2019', 'NOTRE DAME FIRE', '200 million euros pledged', None)]
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
TRG = [('nineteen eighty-four', 'tense'), ('bernard jean etienne arnault was born', 'sad'), ('in nineteen eighty-one france elected a', 'drive'), ('arnault realized that great brands were', 'wonder'), ('under arnault lvmh became a machine', 'triumph'), ('arnault was a very different kind', 'dark'), ('in the two thousand and tens', 'sad'), ('today bernard arnault is in his', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
