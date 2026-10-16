#--KEY
KEY = ['america', 'american', 'bethlehem', 'booking', 'boston', 'brahmins', 'britain', 'british', 'cape', 'catholic', 'chicago', 'columbia', 'commission', 'company', 'december', 'delano', 'department', 'depression', 'dewar', 'east', 'england', 'exchange', 'film', 'first', 'fitz', 'fitzgerald', 'fore', 'france', 'franklin', 'germany', 'gloria', 'gordon', 'great', 'harvard', 'hitler', 'hollywood', 'honey', 'house', 'irish', 'january', 'john', 'joseph', 'junior', 'kathleen', 'kennedy', 'kennedys', 'latin', 'london', 'maritime', 'mart']
#--CH
CH = [('CHAPTER 1', 'THE IRISH', 'OUTSIDER'), ('CHAPTER 2', 'BANKER AT', 'TWENTY-FIVE'), ('CHAPTER 3', 'MOVIE', 'MOGUL'), ('CHAPTER 4', 'THE SHOESHINE', 'BOY'), ('CHAPTER 5', 'FOX IN THE', 'HENHOUSE'), ('CHAPTER 6', 'THE FALL IN', 'LONDON'), ('CHAPTER 7', 'THE PRICE', 'OF DYNASTY'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('joseph patrick kennedy was born on the sixth', '1888', 'JOSEPH KENNEDY IS BORN', 'East Boston, Massachusetts', None),
 ('in nineteen fourteen an opportunity appeared', '1914', 'BANK PRESIDENT AT 25', 'Columbia Trust, Boston', None),
 ('in nineteen twenty-six he bought a small chain', '1926', 'KENNEDY GOES TO HOLLYWOOD', 'theatres, then studios', None),
 ('in nineteen twenty-nine the stock market was soaring', '1929', 'THE GREAT CRASH', 'Kennedy sells in time', None),
 ('then in nineteen thirty-four roosevelt made', '1934', 'FIRST SEC CHAIRMAN', 'regulating Wall Street', None),
 ('in nineteen thirty-eight he gave him the job', '1938', 'AMBASSADOR TO BRITAIN', 'London', None),
 ('then in november nineteen forty he gave', '1940', 'THE FATAL INTERVIEW', 'he resigns', None),
 ('in nineteen forty-five he bought the merchandise mart', '1945', 'MERCHANDISE MART', 'bought for about $13 million', None),
 ('he died on the eighteenth of november', '1969', 'JOSEPH KENNEDY DIES', 'age 81', None)]
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
EMPH = [('youngest bank president','YOUNGEST','BANK PRESIDENT IN AMERICA'),('about thirteen million dollars','$13 MILLION','MERCHANDISE MART')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('november nineteen sixty', 'tense'), ('joseph patrick kennedy was born on', 'sad'), ('in nineteen fourteen an opportunity appeared', 'drive'), ("but kennedy's real ambition was not", 'wonder'), ('in nineteen twenty-nine the stock market', 'triumph'), ('kennedy supported roosevelt and gave money', 'dark'), ('in nineteen thirty-seven roosevelt gave him', 'sad'), ('joseph kennedy junior the oldest was', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
