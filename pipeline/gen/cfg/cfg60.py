#--KEY
KEY = ['adam', 'alibaba', 'american', 'apple', 'arabia', 'august', 'beijing', 'berkeley', 'british', 'california', 'china', 'chinese', 'december', 'dhabi', 'exchange', 'fukushima', 'fund', 'grab', 'holdings', 'jack', 'japan', 'japanese', 'jobs', 'korea', 'korean', 'koreans', 'kyushu', 'march', 'masami', 'masayoshi', 'mitsunori', 'nasdaq', 'neumann', 'owaki', 'ryoma', 'sakamoto', 'saudi', 'second', 'september', 'sharp', 'sprint', 'stargate', 'states', 'steve', 'stock', 'tokyo', 'tosu', 'trade', 'uber', 'united']
#--CH
CH = [('CHAPTER 1', 'A BOY', 'FROM KYUSHU'), ('CHAPTER 2', 'THE BERKELEY', 'INVENTOR'), ('CHAPTER 3', 'THE BIRTH', 'OF SOFTBANK'), ('CHAPTER 4', 'THE BUBBLE', 'AND THE CRASH'), ('CHAPTER 5', 'THE ARM', 'BET'), ('CHAPTER 6', 'THE VISION', 'FUND'), ('CHAPTER 7', 'THE FUTURE', 'OF SOFTBANK'), ('THE LESSON', 'THE LESSONS', 'OF SON')]
CARDS = [('masayoshi son was born on the eleventh of august', '1957', 'MASAYOSHI SON IS BORN', 'Tosu, Japan', None),
 ('he then returned to japan and in nineteen eighty-one', '1981', 'SOFTBANK IS FOUNDED', 'at twenty-four', None),
 ('by nineteen ninety-four softbank was listed', '1994', 'SOFTBANK GOES PUBLIC', 'Tokyo Stock Exchange', None),
 ('in two thousand and one the nasdaq crashed', '2001', 'THE NASDAQ CRASH', 'shares fall 99%', None),
 ('in december two thousand he had invested twenty million dollars in alibaba', '2000', '$20 MILLION IN ALIBABA', 'Jack Ma', None),
 ('in two thousand and seven apple launched the iphone', '2007', 'THE IPHONE DEAL', 'Steve Jobs', None),
 ('in two thousand and sixteen son made a new bet', '2016', 'THE ARM BET', '$32 billion', None),
 ('in two thousand and nineteen wework\'s ipo collapsed', '2019', 'WEWORK COLLAPSES', 'Adam Neumann', None)]
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
TRG = [('december two thousand', 'tense'), ('masayoshi son was born on the', 'sad'), ('he enrolled in a high school', 'drive'), ('the early years were hard', 'wonder'), ('the bubble burst', 'triumph'), ('in two thousand and sixteen son', 'dark'), ('then came the pandemic and a', 'sad'), ('masayoshi son has a wife masami', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
