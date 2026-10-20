#--KEY
KEY = ['alibaba', 'alipay', 'april', 'baba', 'beijing', 'china', 'chinese', 'covid', 'cultural', 'daniel', 'english', 'exchange', 'francisco', 'group', 'hangzhou', 'harvard', 'hope', 'institute', 'internet', 'jack', 'january', 'japan', 'japanese', 'lake', 'mall', 'masayoshi', 'november', 'october', 'pages', 'revolution', 'river', 'seattle', 'september', 'shanghai', 'singles', 'states', 'stock', 'taobao', 'teachers', 'tmall', 'united', 'west', 'western', 'yangtze', 'york', 'zedong', 'zhang']
#--CH
CH = [('CHAPTER 1', 'A POOR BOY', 'FROM HANGZHOU'), ('CHAPTER 2', 'THE TEACHER', 'WHO FAILED'), ('CHAPTER 3', 'THE NAME', 'ALIBABA'), ('CHAPTER 4', 'THE EBAY', 'KILLER'), ('CHAPTER 5', 'THE BIGGEST', 'IPO EVER'), ('CHAPTER 6', 'THE SPEECH', 'THAT CHANGED EVERYTHING'), ('CHAPTER 7', 'THE RETURN', 'OF JACK MA'), ('THE LESSON', 'THE LESSONS', 'OF JACK MA')]
CARDS = [('jack ma was born ma yun on the tenth of september', '1964', 'JACK MA IS BORN', 'Hangzhou, China', None),
 ('he graduated in nineteen eighty-eight', '1988', 'ENGLISH TEACHER', 'Hangzhou', None),
 ('in nineteen ninety-five a local government sent him', '1995', 'FIRST TRIP TO AMERICA', 'he sees the Internet', None),
 ('but in nineteen ninety-nine he was ready', '1999', 'ALIBABA IS FOUNDED', 'eighteen people, one apartment', None),
 ('but in two thousand ma met a young japanese investor', '2000', 'MASAYOSHI SON', 'twenty million dollars', None),
 ('in two thousand and three ma started a new site', '2003', 'TAOBAO IS LAUNCHED', 'against eBay', None),
 ('in two thousand and nine ma launched singles day', '2009', 'SINGLES DAY', 'November 11', None),
 ('on the nineteenth of september two thousand and fourteen', '2014', 'THE LARGEST IPO EVER', '$25 billion', None)]
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
TRG = [('nineteen ninety-nine', 'tense'), ('jack ma was born ma yun', 'sad'), ('ma taught for five years with', 'drive'), ('the name alibaba was a stroke', 'wonder'), ('in two thousand and three ma', 'triumph'), ('on the nineteenth of september two', 'dark'), ('then everything changed', 'sad'), ('in two thousand and twenty-three ma', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
