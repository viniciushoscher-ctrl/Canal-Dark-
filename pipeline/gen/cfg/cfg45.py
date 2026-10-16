#--KEY
KEY = ['academy', 'alto', 'america', 'american', 'analytica', 'atari', 'bitcoin', 'california', 'cambridge', 'cameron', 'chan', 'college', 'columbia', 'commission', 'congress', 'cornell', 'coursematch', 'divya', 'dobbs', 'eduardo', 'edward', 'elliot', 'exeter', 'facebook', 'facemash', 'february', 'federal', 'feed', 'ferry', 'frances', 'google', 'harvard', 'haugen', 'house', 'hughes', 'initiative', 'instagram', 'karen', 'kirkland', 'latin', 'march', 'mark', 'mercy', 'messenger', 'meta', 'moskovitz', 'napster', 'narendra', 'network', 'news']
#--CH
CH = [('CHAPTER 1', 'THE CODING', 'PRODIGY'), ('CHAPTER 2', 'THE DORM', 'ROOM'), ('CHAPTER 3', 'THE PALO ALTO', 'SUMMER'), ('CHAPTER 4', 'THE LAWSUITS', 'AND THE FEED'), ('CHAPTER 5', 'THE EMPIRE', 'OF APPS'), ('CHAPTER 6', 'THE DARK', 'SIDE'), ('CHAPTER 7', 'THE META', 'GAMBLE'), ('THE LESSON', 'THE LESSON', 'WHAT HE TAUGHT US')]
CARDS = [('mark elliot zuckerberg was born on the fourteenth', '1984', 'MARK ZUCKERBERG IS BORN', 'White Plains, New York', None),
 ('on the fourth of february two thousand and four', '2004', 'THE FACEBOOK LAUNCHES', 'Harvard dorm room', None),
 ('in two thousand and six yahoo offered to buy', '2006', 'YAHOO OFFERS $1 BILLION', 'Zuckerberg says no', None),
 ('in two thousand and eight facebook paid them about sixty-five million', '2008', 'THE WINKLEVOSS SETTLEMENT', 'about $65 million', None),
 ('in two thousand and twelve facebook went public', '2012', 'FACEBOOK GOES PUBLIC', 'raising $16 billion', None),
 ('in two thousand and fourteen he bought whatsapp', '2014', 'WHATSAPP ACQUIRED', 'for $19 billion', None),
 ('in march two thousand and eighteen journalists revealed', '2018', 'CAMBRIDGE ANALYTICA', '87 million users affected', None),
 ('in two thousand and nineteen the federal trade commission', '2019', 'THE $5 BILLION FINE', 'FTC privacy penalty', None),
 ('in october two thousand and twenty-one zuckerberg announced', '2021', 'FACEBOOK BECOMES META', 'the metaverse bet', None)]
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
EMPH = [('twenty-two thousand votes','22,000','VOTES IN HOURS'),('more than three billion people','3 BILLION','DAILY USERS')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('october two thousand and three', 'tense'), ('mark elliot zuckerberg was born on', 'sad'), ('at harvard in two thousand and', 'drive'), ('he needed help and he found', 'wonder'), ('but there were two fights that', 'triumph'), ('in two thousand and six yahoo', 'dark'), ('but the empire had a dark', 'sad'), ('in october two thousand and twenty-one', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
