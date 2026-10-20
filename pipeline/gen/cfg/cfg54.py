#--KEY
KEY = ['adolf', 'allies', 'anton', 'august', 'austria', 'austrian', 'austro', 'beetle', 'bela', 'benz', 'bohemia', 'boxster', 'cayenne', 'daimler', 'dean', 'depression', 'doctor', 'egger', 'empire', 'european', 'exhibition', 'exposition', 'ferdinand', 'ferry', 'first', 'french', 'german', 'germany', 'gmund', 'great', 'henry', 'hitler', 'hungarian', 'james', 'january', 'kubelwagen', 'lohner', 'maffersdorf', 'mans', 'maus', 'mercedes', 'nazi', 'paris', 'piech', 'porsche', 'prince', 'second', 'september', 'states', 'steyr']
#--CH
CH = [('CHAPTER 1', "THE TINSMITH'S", 'SON'), ('CHAPTER 2', 'THE DOCTOR', 'PORSCHE'), ('CHAPTER 3', "THE PEOPLE'S", 'CAR'), ('CHAPTER 4', 'TANKS AND', 'FORCED LABOR'), ('CHAPTER 5', 'THE FIRST', 'PORSCHE'), ('CHAPTER 6', 'THE NINE ELEVEN', 'AND LE MANS'), ('CHAPTER 7', 'THE TAKEOVER', 'THAT FAILED'), ('THE LESSON', 'THE LESSONS', 'OF FERDINAND PORSCHE')]
CARDS = [('born on the third of september eighteen seventy-five', '1875', 'FERDINAND PORSCHE IS BORN', 'Bohemia', None),
 ('there in nineteen hundred he built the lohner-porsche', '1900', 'THE LOHNER-PORSCHE', 'the first hybrid car', None),
 ('in nineteen oh five he became the technical director', '1905', 'AUSTRO-DAIMLER', 'technical director', None),
 ('in nineteen thirty-one he opened his own engineering office', '1931', 'PORSCHE OPENS HIS OFFICE', 'Stuttgart', None),
 ('in nineteen thirty-four he gave porsche the job', '1934', 'HITLER ORDERS THE PEOPLE\'S CAR', 'the Beetle', None),
 ('when the second world war began in nineteen thirty-nine', '1939', 'WORLD WAR II BEGINS', 'Volkswagen goes to war', None),
 ('in nineteen forty-eight the first car to carry the porsche name', '1948', 'THE FIRST PORSCHE', 'the 356', None),
 ('ferdinand porsche died on the thirtieth of january', '1951', 'FERDINAND PORSCHE DIES', 'age 75', None),
 ('in nineteen sixty-four the company launched a new model', '1964', 'THE PORSCHE 911', 'the most famous sports car', None)]
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
EMPH = [('more than twenty-one million cars','21 MILLION','BEETLES SOLD'),('seventy-five billion euros','€75 BILLION','IPO VALUE')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('nineteen hundred', 'tense'), ('ferdinand porsche was born on the', 'sad'), ("porsche's fame grew", 'drive'), ('porsche had a dream', 'wonder'), ('when the second world war began', 'triumph'), ('after the war porsche was held', 'dark'), ('ferry porsche took the company forward', 'sad'), ('in the two thousands porsche attempted', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
