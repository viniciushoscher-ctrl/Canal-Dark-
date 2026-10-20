#--KEY
KEY = ['adolf', 'alfred', 'alfried', 'allies', 'amalie', 'american', 'april', 'arndt', 'austria', 'battle', 'belgium', 'bertha', 'british', 'cold', 'commissioner', 'crystal', 'denmark', 'english', 'essen', 'europe', 'exhibition', 'first', 'france', 'franco', 'french', 'friedrich', 'general', 'german', 'germany', 'great', 'gustav', 'helene', 'hermann', 'high', 'hitler', 'hugel', 'italy', 'japan', 'john', 'july', 'krupp', 'london', 'nazi', 'nuremberg', 'october', 'palace', 'paris', 'prussia', 'prussian', 'regulations']
#--CH
CH = [('CHAPTER 1', 'A BOY', 'AT FOURTEEN'), ('CHAPTER 2', 'THE STEEL', 'SECRET'), ('CHAPTER 3', 'THE RAILWAY', 'TIRE'), ('CHAPTER 4', 'THE CANNON', 'KING'), ('CHAPTER 5', 'A CITY', 'OF STEEL'), ('CHAPTER 6', 'THE GREAT', 'WAR'), ('CHAPTER 7', 'THE FALL', 'AND RETURN'), ('THE LESSON', 'THE LESSONS', 'OF KRUPP')]
CARDS = [('alfred krupp was born on the twenty-sixth of april', '1812', 'ALFRED KRUPP IS BORN', 'Essen, Germany', None),
 ('in eighteen thirty-eight he developed a machine', '1838', 'THE SPOON ROLLER', 'a modest hit', None),
 ('in eighteen fifty-one at the great exhibition', '1851', 'GREAT EXHIBITION', 'Crystal Palace, London', None),
 ('in eighteen fifty-five he showed a breech-loading', '1855', 'STEEL CANNON', 'Paris', None),
 ('alfred krupp died on the fourteenth of july', '1887', 'ALFRED KRUPP DIES', 'age 75', None),
 ('when adolf hitler came to power in nineteen thirty-three', '1933', 'HITLER COMES TO POWER', 'Gustav Krupp', None),
 ('in nineteen fifty-one the american high commissioner', '1951', 'ALFRIED RELEASED', 'John McCloy', None),
 ('in nineteen sixty-seven alfried died', '1967', 'ALFRIED DIES', 'the family line ends', None)]
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
TRG = [('eighteen hundred and twenty-six', 'tense'), ('alfred krupp was born on the', 'sad'), ('in those first years the factory', 'drive'), ('the breakthrough came with the railroads', 'wonder'), ('then alfred discovered his real market', 'triumph'), ('by the eighteen seventies krupp was', 'dark'), ("alfred's son friedrich alfred krupp took", 'sad'), ('but the story was not over', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
