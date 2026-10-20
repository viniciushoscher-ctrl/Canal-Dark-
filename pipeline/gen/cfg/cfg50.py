#--KEY
KEY = ['albert', 'albrecht', 'anton', 'antwerp', 'archbishop', 'archduke', 'augsburg', 'austria', 'budapest', 'catholic', 'charles', 'church', 'coin', 'december', 'durer', 'elder', 'emperor', 'empire', 'europe', 'european', 'fifth', 'first', 'fondaco', 'france', 'francis', 'french', 'fugger', 'fuggerei', 'fuggers', 'german', 'germany', 'guard', 'habsburg', 'habsburgs', 'holy', 'house', 'hungary', 'italian', 'jakob', 'julius', 'king', 'krakow', 'lisbon', 'luther', 'mainz', 'march', 'martin', 'maximilian', 'philip', 'pope']
#--CH
CH = [('CHAPTER 1', 'THE SECOND SON', 'OF AUGSBURG'), ('CHAPTER 2', 'THE LESSON', 'OF VENICE'), ('CHAPTER 3', 'THE COPPER', 'AND SILVER KING'), ('CHAPTER 4', 'THE BANKER', 'OF THE HABSBURGS'), ('CHAPTER 5', 'THE MAN WHO', 'BOUGHT AN EMPEROR'), ('CHAPTER 6', 'INDULGENCES', 'AND THE FUGGEREI'), ('CHAPTER 7', 'THE RICHEST', 'MAN IN HISTORY'), ('THE LESSON', 'THE LESSONS', 'OF JAKOB FUGGER')]
CARDS = [('born on the sixth of march fourteen fifty-nine', '1459', 'JAKOB FUGGER IS BORN', 'Augsburg, Germany', None),
 ('returned to augsburg in fourteen seventy-eight', '1478', 'RETURNS FROM VENICE', 'double-entry bookkeeping', None),
 ('took control of the firm in fourteen ninety-four', '1494', 'TAKES THE FIRM', 'age 35', None),
 ('in fifteen oh six he lent money to pope julius the second', '1506', 'LENDS TO THE POPE', 'the Swiss Guard', None),
 ('in fifteen fourteen he started building', '1514', 'THE FUGGEREI', 'oldest social housing', None),
 ('in fifteen seventeen a monk named martin luther', '1517', 'LUTHER\'S 95 THESES', 'Wittenberg', None),
 ('in fifteen nineteen the holy roman emperor maximilian died', '1519', 'THE IMPERIAL ELECTION', 'Charles V is chosen', None),
 ('on the thirtieth of december fifteen twenty-five', '1525', 'JAKOB FUGGER DIES', 'age 66', None),
 ('in fifteen fifty-six king philip the second', '1556', 'SPAIN DEFAULTS', 'the Fugger decline', None)]
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
EMPH = [('five hundred and fifty thousand florins','550,000 FLORINS','THE BRIBE FOR CHARLES V'),('about two percent of the entire european economy','2% OF EUROPE','HIS FORTUNE')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen fifteen', 'tense'), ('jakob fugger was born on the', 'sad'), ('jakob returned to augsburg in fourteen', 'drive'), ('but the real genius of jakob', 'wonder'), ('in fifteen nineteen the holy roman', 'triumph'), ('there was another side to the', 'dark'), ('by fifteen twenty-three jakob fugger was', 'sad'), ('in fifteen fifty-six king philip the', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
