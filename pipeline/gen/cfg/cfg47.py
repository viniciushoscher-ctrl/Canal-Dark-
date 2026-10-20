#--KEY
KEY = ['alfred', 'almanack', 'american', 'angeles', 'army', 'barbara', 'benjamin', 'berkshire', 'buffett', 'burlington', 'california', 'caltech', 'candies', 'capitalism', 'charlie', 'coca', 'cola', 'company', 'corporation', 'corps', 'daily', 'ernest', 'express', 'fargo', 'franklin', 'geico', 'gillette', 'good', 'graham', 'harvard', 'hathaway', 'hospital', 'january', 'journal', 'michigan', 'munger', 'nebraska', 'northern', 'november', 'olson', 'omaha', 'pasadena', 'poor', 'post', 'richard', 'samaritan', 'santa', 'school', 'second', 'stanford']
#--CH
CH = [('CHAPTER 1', 'A BOY', 'FROM OMAHA'), ('CHAPTER 2', 'THE LAWYER', 'WHO INVESTED'), ('CHAPTER 3', 'THE FRIENDSHIP', 'WITH BUFFETT'), ('CHAPTER 4', 'THE BERKSHIRE', 'MACHINE'), ('CHAPTER 5', 'THE MAN', 'BEHIND THE MONEY'), ('CHAPTER 6', 'THE WOODSTOCK', 'OF CAPITALISM'), ('CHAPTER 7', 'THE LAST', 'YEARS'), ('THE LESSON', 'THE LESSONS', 'OF MUNGER')]
CARDS = [('charles thomas munger was born on the first of january', '1924', 'CHARLIE MUNGER IS BORN', 'Omaha, Nebraska', None),
 ('in nineteen forty-two he joined the army air corps', '1942', 'ARMY AIR CORPS', 'weather officer', None),
 ('in nineteen fifty-nine at a dinner party in omaha', '1959', 'HE MEETS WARREN BUFFETT', 'dinner in Omaha', None),
 ('in nineteen sixty-two he left to form his own firm', '1962', 'MUNGER, TOLLES AND OLSON', 'his own law firm', None),
 ('they found see\'s candies', '1972', 'SEE\'S CANDIES', 'a turning point', None),
 ('in nineteen seventy-eight munger became the vice chairman', '1978', 'VICE CHAIRMAN OF BERKSHIRE', 'with Warren Buffett', None),
 ('in two thousand and eight during the financial crisis', '2008', 'FINANCIAL CRISIS', 'Berkshire holds firm', None),
 ('charlie munger died on the twenty-eighth of november', '2023', 'CHARLIE MUNGER DIES', 'age 99', None)]
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
TRG = [('nineteen fifty-five', 'tense'), ('charles thomas munger was born on', 'sad'), ('munger moved to california where he', 'drive'), ('buffett and munger became close friends', 'wonder'), ('under their leadership berkshire invested in', 'triumph'), ("munger's life was never only about", 'dark'), ('by the nineteen nineties and two', 'sad'), ('charlie munger died on the twenty-eighth', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
