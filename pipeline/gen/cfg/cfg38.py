#--KEY
KEY = ['akio', 'america', 'american', 'americans', 'august', 'avenue', 'betamax', 'columbia', 'corporation', 'electric', 'engineering', 'english', 'europe', 'exchange', 'fifth', 'ibuka', 'imperial', 'january', 'japan', 'japanese', 'july', 'kogyo', 'kosugi', 'latin', 'made', 'masaru', 'morita', 'nagoya', 'navy', 'nihonbashi', 'october', 'osaka', 'philips', 'pictures', 'records', 'sony', 'states', 'stock', 'telecommunications', 'tokyo', 'totsuko', 'trinitron', 'tsushin', 'united', 'university', 'walkman', 'west', 'western', 'york']
#--CH
CH = [('CHAPTER 1', 'SAKE HEIR', 'ENGINEER'), ('CHAPTER 2', 'THE DEPARTMENT STORE', 'STARTUP'), ('CHAPTER 3', 'THE TAPE', 'RECORDER'), ('CHAPTER 4', 'THE POCKET', 'RADIO'), ('CHAPTER 5', 'THE AMERICAN', 'DREAM'), ('CHAPTER 6', 'THE WALKMAN', 'YEARS'), ('CHAPTER 7', 'MADE IN', 'JAPAN'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('akio morita was born on the twenty-sixth of january', '1921', 'AKIO MORITA IS BORN', 'Nagoya, Japan', None),
 ('in nineteen forty-six the two men registered', '1946', 'TOKYO TSUSHIN KOGYO', 'about 20 employees', None),
 ('in nineteen fifty-three he took a trip', '1953', 'THE TRANSISTOR LICENSE', 'Western Electric, $25,000', None),
 ('after two years of hard work in nineteen fifty-five', '1955', 'THE TR-55 RADIO', 'the first Japanese transistor radio', None),
 ('and in nineteen fifty-eight the company chose', '1958', 'THE NAME SONY', 'from sonus, Latin for sound', None),
 ('in nineteen sixty he opened the sony corporation', '1960', 'SONY OF AMERICA', 'New York', None),
 ('in nineteen seventy-five sony launched the betamax', '1975', 'THE BETAMAX', 'loses to VHS', None),
 ('it went on sale on the first of july', '1979', 'THE WALKMAN', 'goes on sale', None),
 ('in nineteen eighty-eight sony bought cbs records', '1988', 'SONY BUYS CBS RECORDS', 'about $2 billion', None),
 ('akio morita died on the third of october', '1999', 'AKIO MORITA DIES', 'age 78', None)]
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
EMPH = [('twenty-five thousand dollars','$25,000','FOR THE TRANSISTOR'),('about two billion dollars','$2 BILLION','CBS RECORDS'),('about three point four billion dollars','$3.4 BILLION','COLUMBIA PICTURES')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('september nineteen forty-five', 'tense'), ('akio morita was born on the', 'sad'), ('the man was masaru ibuka an', 'drive'), ('the first years were a struggle', 'wonder'), ('at the time the transistor was', 'triumph'), ('morita understood something that most japanese', 'dark'), ('then came the invention that made', 'sad'), ('by the nineteen eighties akio morita', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
