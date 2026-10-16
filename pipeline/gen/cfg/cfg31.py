#--KEY
KEY = ['abraham', 'academy', 'america', 'american', 'atlantic', 'baltimore', 'brazil', 'british', 'chicago', 'cincinnati', 'civil', 'congress', 'council', 'county', 'crystal', 'cyrus', 'democrat', 'edwin', 'england', 'essex', 'europe', 'exposition', 'february', 'fire', 'fowler', 'france', 'french', 'germany', 'grand', 'great', 'grove', 'hall', 'harvester', 'haymarket', 'honor', 'hussey', 'illinois', 'international', 'iowa', 'irish', 'john', 'june', 'kansas', 'lake', 'lincoln', 'london', 'manny', 'medal', 'michigan', 'midwest']
#--CH
CH = [('CHAPTER 1', 'THE BOY FROM', 'WALNUT GROVE'), ('CHAPTER 2', 'THE MACHINE', 'THAT WORKED'), ('CHAPTER 3', 'THE DECADE', 'OF DEBT'), ('CHAPTER 4', 'THE MUDDY TOWN', 'CALLED CHICAGO'), ('CHAPTER 5', 'THE CRYSTAL', 'PALACE TEST'), ('CHAPTER 6', 'THE PATENT WARS', 'AND LINCOLN'), ('CHAPTER 7', 'FIRE', 'AND LEGACY'), ('THE LESSON', 'WHAT HE', 'TAUGHT US')]
CARDS = [('cyrus hall mccormick was born on february', '1809', 'CYRUS McCORMICK IS BORN', 'Walnut Grove, Virginia', None),
 ('in the summer of eighteen thirty-one in', '1831', 'THE FIRST REAPER', 'built in a family workshop', None),
 ('then in eighteen thirty-seven a financial panic', '1837', 'THE PANIC OF 1837', 'banks fail, iron collapses', None),
 ('in eighteen forty-seven cyrus mccormick looked at', '1847', 'THE MOVE TO CHICAGO', 'population: about 16,000', None),
 ("in eighteen fifty-one the world's first great", '1851', 'THE GREAT EXHIBITION', 'Crystal Palace, London', None),
 ('in eighteen fifty-eight at the age of', '1858', 'MARRIAGE TO NETTIE', 'Nancy Fowler, age 23', None),
 ('then in october of eighteen seventy-one came', '1871', 'THE GREAT CHICAGO FIRE', 'the factory burns to the ground', None),
 ('he died on may thirteenth eighteen eighty-four', '1884', 'CYRUS McCORMICK DIES', 'age 75 - fortune ~$10 million', None),
 ('and in nineteen oh two the company', '1902', 'INTERNATIONAL HARVESTER', 'merger arranged by J.P. Morgan', None)]
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
EMPH = [('cut perhaps two acres', '2 ACRES', 'A DAY BY HAND'), ('cut six acres of oats', '6 ACRES', 'BEFORE SUNDOWN'), ('he sold exactly two', 'ONLY TWO', 'MACHINES SOLD'), ('about five hundred reapers', '500 REAPERS', 'IN YEAR ONE'), ('around ten million dollars', '$10 MILLION', 'FORTUNE'), ('modern marketing', 'MODERN', 'MARKETING')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('june eighteen thirty-one', 'tense'), ('cyrus hall mccormick was born on', 'sad'), ('cyrus was twenty-one years old and', 'drive'), ('the next decade nearly broke him', 'wonder'), ('in eighteen forty-seven cyrus mccormick looked', 'triumph'), ("in eighteen fifty-one the world's first", 'dark'), ('between eighteen forty-eight and the middle', 'sad'), ('in eighteen fifty-eight at the age', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
