#--KEY
KEY = ['alfred', 'america', 'american', 'auto', 'bearing', 'brooklyn', 'brown', 'buick', 'cadillac', 'california', 'charles', 'chevrolet', 'city', 'company', 'connecticut', 'detroit', 'donaldson', 'durant', 'earl', 'february', 'flint', 'ford', 'foundation', 'general', 'harley', 'haven', 'hyatt', 'institute', 'irene', 'jersey', 'junior', 'kettering', 'management', 'massachusetts', 'michigan', 'model', 'motors', 'newark', 'oakland', 'oldsmobile', 'organizational', 'pont', 'pontiac', 'pritchard', 'roller', 'school', 'sloan', 'study', 'technology', 'united']
#--CH
CH = [('CHAPTER 1', 'BOY FROM', 'NEW HAVEN'), ('CHAPTER 2', 'BEARINGS', 'AND DEBT'), ('CHAPTER 3', 'THE DURANT', 'PROBLEM'), ('CHAPTER 4', 'THE PLAN', 'THAT RAN GM'), ('CHAPTER 5', 'A CAR FOR', 'EVERY PURSE'), ('CHAPTER 6', 'THE COLD', 'GENIUS'), ('CHAPTER 7', 'GIVING', 'AND LEGACY'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('alfred pritchard sloan junior was born on may', '1875', 'ALFRED SLOAN IS BORN', 'New Haven, Connecticut', None),
 ('by eighteen ninety-nine the hyatt company was', '1899', 'HYATT ROLLER BEARING', 'on the edge of bankruptcy', None),
 ('in nineteen sixteen the owner of a new', '1916', 'UNITED MOTORS', 'Sloan sells for $13.5 million', None),
 ('in nineteen twenty the postwar economy collapsed', '1920', 'POSTWAR COLLAPSE', 'GM near the edge', None),
 ('in nineteen twenty sloan wrote a study', '1920', 'THE ORGANIZATIONAL STUDY', 'decentralized, with control', None),
 ('by nineteen thirty-one it was selling more cars', '1931', 'GM PASSES FORD', 'number one for decades', None),
 ('in the winter of nineteen thirty-six autoworkers', '1936', 'FLINT SIT-DOWN STRIKE', 'lasts 44 days', None),
 ('in nineteen fifty-five general motors became', '1955', 'FIRST $1 BILLION YEAR', 'General Motors profit', None),
 ('alfred sloan died on february seventeenth', '1966', 'ALFRED SLOAN DIES', 'New York City, age 90', None)]
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
EMPH = [('thirteen and a half million dollars','$13.5 MILLION','UNITED MOTORS SALE'),('forty-four days','44 DAYS','FLINT SIT-DOWN'),('more than one billion dollars','$1 BILLION','IN ONE YEAR')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen twenty-one', 'tense'), ('alfred pritchard sloan junior was born', 'sad'), ('by eighteen ninety-nine the hyatt company', 'drive'), ('he might have retired', 'wonder'), ('in nineteen twenty sloan wrote a', 'triumph'), ('sloan looked at the market and', 'dark'), ('by the end of the nineteen', 'sad'), ('sloan stepped down as president in', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
