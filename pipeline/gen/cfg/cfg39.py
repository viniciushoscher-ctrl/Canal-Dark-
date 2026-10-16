#--KEY
KEY = ['accord', 'america', 'american', 'august', 'british', 'civic', 'clean', 'company', 'dream', 'fujisawa', 'gihei', 'hamamatsu', 'honda', 'hondas', 'irish', 'isle', 'italian', 'japan', 'japanese', 'kanto', 'marysville', 'mika', 'motor', 'november', 'ohio', 'seiki', 'shokai', 'soichiro', 'states', 'super', 'takeo', 'tokai', 'tokyo', 'toyota', 'type', 'united']
#--CH
CH = [('CHAPTER 1', "BLACKSMITH'S", 'SON'), ('CHAPTER 2', 'THE REPAIR', 'APPRENTICE'), ('CHAPTER 3', 'YEAR OF', 'IDLENESS'), ('CHAPTER 4', 'THE ODD', 'PARTNERSHIP'), ('CHAPTER 5', 'THE SUPER', 'CUB'), ('CHAPTER 6', 'CARS AND', 'THE CVCC'), ('CHAPTER 7', 'THE EARLY', 'RETIREMENT'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('soichiro honda was born on the seventeenth', '1906', 'SOICHIRO HONDA IS BORN', 'near Hamamatsu, Japan', None),
 ('at the age of fifteen in nineteen twenty-two', '1922', 'APPRENTICE AT ART SHOKAI', 'Tokyo', None),
 ('in nineteen forty-five an earthquake', '1945', 'THE FACTORY IS LOST', 'sold to Toyota', None),
 ('in nineteen forty-eight honda formally founded', '1948', 'HONDA MOTOR COMPANY', 'Hamamatsu', None),
 ('then in nineteen forty-nine he met', '1949', 'THE FUJISAWA PARTNERSHIP', 'engineer and businessman', None),
 ('then in nineteen fifty-eight honda released', '1958', 'THE SUPER CUB', 'over 100 million built', None),
 ('and in nineteen sixty-one they took', '1961', 'ISLE OF MAN TT', 'Hondas take 1st to 5th', None),
 ('in nineteen seventy-two honda put it', '1972', 'THE HONDA CIVIC', 'with the CVCC engine', None),
 ('soichiro honda died on the fifth of august', '1991', 'SOICHIRO HONDA DIES', 'age 84', None)]
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
EMPH = [('four hundred and fifty thousand yen','450,000 YEN','FOR THE FACTORY'),('over one hundred million units','100 MILLION','SUPER CUBS BUILT')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('june nineteen sixty-one', 'tense'), ('soichiro honda was born on the', 'sad'), ('honda spent six years at art', 'drive'), ('then came the war', 'wonder'), ('in nineteen forty-eight honda formally founded', 'triumph'), ('then in nineteen fifty-eight honda released', 'dark'), ('honda was now ready for the', 'sad'), ('in nineteen seventy-three at the age', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
