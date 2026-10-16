#--KEY
KEY = ['africa', 'african', 'akron', 'america', 'american', 'americans', 'asia', 'beach', 'benjamin', 'bridgestone', 'british', 'burroughs', 'catherine', 'central', 'chicago', 'clay', 'columbiana', 'company', 'congress', 'december', 'depression', 'detroit', 'dutch', 'edison', 'february', 'firestone', 'first', 'florida', 'ford', 'goodrich', 'goodyear', 'great', 'harbel', 'harvey', 'henry', 'idabelle', 'indianapolis', 'japanese', 'john', 'junior', 'league', 'liberia', 'liberian', 'liberians', 'martha', 'miami', 'model', 'motor', 'nations', 'ohio']
#--CH
CH = [('CHAPTER 1', 'FARM BOY', 'FROM OHIO'), ('CHAPTER 2', 'CHICAGO', 'TO AKRON'), ('CHAPTER 3', 'FORD', 'AND INDY'), ('CHAPTER 4', 'FIRESTONE', 'PARK'), ('CHAPTER 5', 'RUBBER', 'MONOPOLY'), ('CHAPTER 6', 'THE LIBERIA', 'LEASE'), ('CHAPTER 7', 'DEPRESSION', 'AND DEATH'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('harvey samuel firestone was born on december', '1868', 'HARVEY FIRESTONE IS BORN', 'Columbiana County, Ohio', None),
 ('in nineteen hundred at the age of thirty-one', '1900', 'FIRESTONE TIRE & RUBBER', 'founded in Akron, Ohio', None),
 ('the breakthrough came in nineteen oh six', '1906', 'THE FORD ORDER', 'tires for the new Ford cars', None),
 ('in nineteen eleven the first indianapolis', '1911', 'FIRST INDY 500', 'on Firestone tires', None),
 ('in nineteen twenty-two it introduced a plan', '1922', 'BRITISH RUBBER PLAN', 'prices soar', None),
 ('in nineteen twenty-six firestone signed the famous', '1926', 'THE LIBERIA LEASE', 'one million acres', None),
 ('in nineteen thirty an international commission', '1930', 'LEAGUE OF NATIONS REPORT', 'forced labor in Liberia', None),
 ('the great depression struck in nineteen twenty-nine', '1929', 'GREAT DEPRESSION', 'car sales collapse', None),
 ('on february seventh nineteen thirty-eight harvey', '1938', 'HARVEY FIRESTONE DIES', 'Miami Beach, age 69', None)]
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
EMPH = [('one million acres','1 MILLION','ACRES IN LIBERIA'),('six cents an acre','6 CENTS','AN ACRE'),('ninety-nine years','99 YEARS','LEASE TERM'),('more than a dollar','OVER $1','A POUND OF RUBBER')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen twenty-six', 'tense'), ('harvey samuel firestone was born on', 'sad'), ('in the eighteen nineties firestone moved', 'drive'), ('the first years were hard', 'wonder'), ('by the end of the nineteen', 'triumph'), ('after the first world war there', 'dark'), ('the liberian plantation in a place', 'sad'), ('but success was not easy at', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
