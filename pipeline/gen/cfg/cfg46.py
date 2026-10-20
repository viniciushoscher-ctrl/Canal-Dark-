#--KEY
KEY = ['america', 'american', 'april', 'average', 'beasley', 'boston', 'capital', 'carolyn', 'catholic', 'century', 'city', 'electric', 'fortune', 'francis', 'general', 'grace', 'gutoff', 'illinois', 'immelt', 'industrial', 'institute', 'irish', 'jack', 'jane', 'jeff', 'john', 'jones', 'junior', 'management', 'manager', 'march', 'massachusetts', 'motorola', 'neutron', 'noryl', 'november', 'peabody', 'pittsfield', 'reuben', 'september', 'sigma', 'straight', 'university', 'welch', 'winning', 'work', 'york']
#--CH
CH = [('CHAPTER 1', 'THE STUTTERING', 'BOY'), ('CHAPTER 2', 'THE PLASTICS', 'ENGINEER'), ('CHAPTER 3', 'THE YOUNGEST', 'CHAIRMAN'), ('CHAPTER 4', 'NEUTRON', 'JACK'), ('CHAPTER 5', 'WORK-OUT AND', 'SIX SIGMA'), ('CHAPTER 6', 'MANAGER OF', 'THE CENTURY'), ('CHAPTER 7', 'THE FALL', 'OF AN ICON'), ('THE LESSON', 'THE LESSON', 'WHAT HE TAUGHT US')]
CARDS = [('john francis welch junior was born on the nineteenth', '1935', 'JACK WELCH IS BORN', 'Peabody, Massachusetts', None),
 ('in nineteen sixty he joined general electric', '1960', 'JOINS GENERAL ELECTRIC', 'plastics division', None),
 ('in nineteen sixty-eight at the age of thirty-two', '1968', 'YOUNGEST GENERAL MANAGER', 'age 32', None),
 ('on the first of april nineteen eighty-one at the age', '1981', 'CHAIRMAN OF GE', 'age 45', None),
 ('in nineteen eighty-six he bought rca', '1986', 'GE BUYS RCA', 'and NBC, for $6.5 billion', None),
 ('in nineteen eighty-nine he launched a program called work-out', '1989', 'THE WORK-OUT PROGRAM', 'cutting bureaucracy', None),
 ('in two thousand fortune magazine named him', '2000', 'MANAGER OF THE CENTURY', 'Fortune magazine', None),
 ('in september two thousand and one he retired', '2001', 'WELCH RETIRES', 'Jeff Immelt takes over', None),
 ('he died on the first of march two thousand and twenty', '2020', 'JACK WELCH DIES', 'age 84', None)]
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
EMPH = [('more than a hundred thousand jobs','100,000+','JOBS CUT'),('about four hundred billion dollars','$400 BILLION','GE BY 2001')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen fifty-nine', 'tense'), ('john francis welch junior was born', 'sad'), ('welch studied chemical engineering at the', 'drive'), ('in the nineteen seventies general electric', 'wonder'), ('in the first years of the', 'triumph'), ('welch knew that cutting was not', 'dark'), ('welch was a celebrity', 'sad'), ('after his retirement welch wrote two', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
