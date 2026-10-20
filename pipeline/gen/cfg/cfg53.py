#--KEY
KEY = ['adalgisa', 'alberto', 'alfa', 'alfonso', 'alfredo', 'allied', 'american', 'anselmo', 'ascari', 'august', 'baracca', 'bologna', 'championship', 'colombo', 'countess', 'daytona', 'dino', 'enzo', 'february', 'ferrari', 'fiat', 'first', 'florio', 'ford', 'formula', 'francesco', 'froilan', 'gioacchino', 'gonzalez', 'grand', 'italian', 'italy', 'jose', 'junior', 'lardi', 'laura', 'lina', 'mans', 'maranello', 'miglia', 'mille', 'modena', 'nuvolari', 'paolina', 'piero', 'portago', 'prix', 'ravenna', 'romeo', 'saturn']
#--CH
CH = [('CHAPTER 1', 'THE BOY AT THE', 'RACE IN BOLOGNA'), ('CHAPTER 2', 'THE REJECTED', 'TEST DRIVER'), ('CHAPTER 3', 'THE SCUDERIA', 'AND THE FIRST FERRARI'), ('CHAPTER 4', 'THE RACING', 'EMPEROR OF MARANELLO'), ('CHAPTER 5', 'THE PRICE', 'OF WINNING'), ('CHAPTER 6', 'FORD VERSUS', 'FERRARI'), ('CHAPTER 7', 'THE LAST', 'YEARS OF A LEGEND'), ('THE LESSON', 'THE LESSONS', 'OF ENZO FERRARI')]
CARDS = [('born on the eighteenth of february eighteen ninety-eight', '1898', 'ENZO FERRARI IS BORN', 'Modena, Italy', None),
 ('in nineteen sixteen his father and brother both died', '1916', 'FATHER AND BROTHER DIE', 'Enzo is seventeen', None),
 ('in nineteen twenty he joined alfa romeo', '1920', 'JOINS ALFA ROMEO', 'racing driver', None),
 ('in nineteen twenty-nine at the age of thirty-one', '1929', 'SCUDERIA FERRARI', 'founded in Modena', None),
 ('in nineteen forty-seven the first car to carry the ferrari name', '1947', 'THE FIRST FERRARI', 'the 125 S', None),
 ('in nineteen fifty ferrari entered the new formula one', '1950', 'FORMULA ONE DEBUT', 'still racing today', None),
 ('in nineteen fifty-seven during the mille miglia', '1957', 'THE MILLE MIGLIA CRASH', 'the race is banned', None),
 ('in nineteen sixty-three the american carmaker ford', '1963', 'FORD MAKES AN OFFER', 'Enzo walks away', None),
 ('he died on the fourteenth of august', '1988', 'ENZO FERRARI DIES', 'age 90', None)]
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
EMPH = [('fifty percent of the company to fiat','50% TO FIAT','1969')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen twenty-nine', 'tense'), ('enzo anselmo ferrari was born on', 'sad'), ('after the war enzo went to', 'drive'), ('in nineteen twenty-nine at the age', 'wonder'), ('enzo ferrari had a simple business', 'triumph'), ('the cost of winning was high', 'dark'), ('by the early nineteen sixties ferrari', 'sad'), ('in his last years enzo ferrari', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
