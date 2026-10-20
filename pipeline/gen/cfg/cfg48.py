#--KEY
KEY = ['africa', 'agriculture', 'alexander', 'american', 'asian', 'august', 'bank', 'berlin', 'black', 'britain', 'british', 'budapest', 'central', 'democratic', 'druckenmiller', 'eastern', 'economics', 'england', 'esperanto', 'europe', 'european', 'exchange', 'first', 'foundations', 'fund', 'george', 'german', 'germany', 'gyorgy', 'hungarian', 'hungary', 'jewish', 'jews', 'karl', 'london', 'mahathir', 'malaysia', 'march', 'mechanism', 'ministry', 'mohamad', 'nazi', 'nazis', 'open', 'orban', 'party', 'popper', 'quantum', 'rate', 'rogers']
#--CH
CH = [('CHAPTER 1', 'THE BOY WITH', 'A FALSE NAME'), ('CHAPTER 2', 'THE PORTER', 'WHO BECAME A TRADER'), ('CHAPTER 3', 'THE THEORY', 'OF REFLEXIVITY'), ('CHAPTER 4', 'THE MAN WHO BROKE', 'THE BANK OF ENGLAND'), ('CHAPTER 5', 'THE BETS', 'AND THE LOSSES'), ('CHAPTER 6', 'THE OPEN SOCIETY', 'AND ITS ENEMIES'), ('CHAPTER 7', 'A HERO', 'OR A VILLAIN'), ('THE LESSON', 'THE LESSONS', 'OF GEORGE SOROS')]
CARDS = [('was born gyorgy schwartz on the twelfth of august', '1930', 'GEORGE SOROS IS BORN', 'Budapest, Hungary', None),
 ('in march nineteen forty-four nazi germany occupied hungary', '1944', 'NAZIS OCCUPY HUNGARY', 'false papers save the family', None),
 ('in nineteen forty-seven at the age of seventeen', '1947', 'LEAVES FOR LONDON', 'LSE and Karl Popper', None),
 ('in nineteen fifty-six he moved to new york', '1956', 'WALL STREET', 'arbitrage trader', None),
 ('in nineteen seventy he partnered with a young trader', '1970', 'QUANTUM FUND BEGINS', 'with Jim Rogers', None),
 ('the sixteenth of september', '1992', 'BLACK WEDNESDAY', 'the pound crashes', None),
 ('in nineteen ninety-seven during the asian financial crisis', '1997', 'ASIAN FINANCIAL CRISIS', 'Mahathir blames Soros', None),
 ('in nineteen eighty-four he founded the first open society foundation', '1984', 'OPEN SOCIETY', 'first foundation in Hungary', None),
 ('in two thousand and eighteen the central european university', '2018', 'CEU LEAVES BUDAPEST', 'moves to Vienna', None)]
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
EMPH = [('more than ten billion dollars','$10 BILLION','THE POUND BET'),('about one billion dollars','$1 BILLION','IN ONE DAY'),('more than thirty-two billion dollars','$32 BILLION','GIVEN AWAY')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('the sixteenth of september nineteen ninety-two', 'tense'), ('george soros was born gyorgy schwartz', 'sad'), ('after the war hungary fell under', 'drive'), ('soros had a unique theory of', 'wonder'), ('by nineteen ninety-two britain had a', 'triumph'), ('soros did not stop there', 'dark'), ('in the next decades soros became', 'sad'), ('he married three times and has', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
