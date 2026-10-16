#--KEY
KEY = ['adidas', 'america', 'american', 'americans', 'army', 'asia', 'bank', 'bill', 'blue', 'bowerman', 'california', 'cameras', 'carolina', 'carolyn', 'cleveland', 'coast', 'cristiano', 'davidson', 'eugene', 'february', 'first', 'german', 'greek', 'hampson', 'health', 'high', 'incorporated', 'james', 'japan', 'japanese', 'jeff', 'johnson', 'jordan', 'knight', 'kobe', 'lota', 'matthew', 'michael', 'monica', 'national', 'nike', 'north', 'olympic', 'onitsuka', 'oregon', 'penny', 'phil', 'plymouth', 'portland', 'puma']
#--CH
CH = [('CHAPTER 1', 'THE SHY', 'RUNNER'), ('CHAPTER 2', 'THE STANFORD', 'PAPER'), ('CHAPTER 3', 'BLUE RIBBON', 'SPORTS'), ('CHAPTER 4', 'THE SWOOSH', 'IS BORN'), ('CHAPTER 5', 'THE RUNNING', 'BOOM'), ('CHAPTER 6', 'AIR JORDAN', 'AND BEYOND'), ('CHAPTER 7', 'SHOE DOG', 'AND LEGACY'), ('THE LESSON', 'THE LESSON', 'WHAT HE TAUGHT US')]
CARDS = [('philip hampson knight was born on the twenty-fourth', '1938', 'PHIL KNIGHT IS BORN', 'Portland, Oregon', None),
 ('after graduating from oregon in nineteen fifty-nine', '1959', 'THE STANFORD PAPER', 'Japanese shoes vs. German shoes', None),
 ('in nineteen sixty-four they formed blue ribbon sports', '1964', 'BLUE RIBBON SPORTS', 'five hundred dollars each', None),
 ('in nineteen seventy-one bowerman who had been', '1971', 'THE WAFFLE SOLE', 'a waffle iron prototype', None),
 ('in nineteen seventy-two the first nike shoes', '1972', 'NIKE DEBUTS', 'Olympic Trials, Eugene', None),
 ('in nineteen seventy-eight blue ribbon sports was officially', '1978', 'NIKE, INC.', 'name made official', None),
 ('in nineteen eighty the company went public', '1980', 'NIKE GOES PUBLIC', 'Knight a billionaire', None),
 ('in nineteen eighty-four he took a huge gamble', '1984', 'MICHAEL JORDAN SIGNS', 'a rookie from North Carolina', None),
 ('in nineteen eighty-eight nike launched a new', '1988', 'JUST DO IT', 'three words', None),
 ('in two thousand and sixteen he published a memoir', '2016', 'SHOE DOG', 'a bestselling memoir', None)]
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
EMPH = [('about one hundred and fifty million dollars','$150 MILLION','NIKE SALES, 1979'),('more than one hundred billion dollars','$100 BILLION','NIKE TODAY')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen sixty-two', 'tense'), ('philip hampson knight was born on', 'sad'), ('after graduating from oregon in nineteen', 'drive'), ('back in oregon knight ordered a', 'wonder'), ('by the end of the nineteen', 'triumph'), ('the nineteen seventies were the years', 'dark'), ('the air jordan released in nineteen', 'sad'), ('in two thousand and four at', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
