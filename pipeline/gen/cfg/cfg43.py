#--KEY
KEY = ['america', 'bloomberg', 'boston', 'brothers', 'business', 'charlotte', 'city', 'democratic', 'eagle', 'february', 'harvard', 'henry', 'hopkins', 'innovative', 'jewish', 'johns', 'lynch', 'market', 'massachusetts', 'medford', 'merrill', 'michael', 'news', 'november', 'phibro', 'philanthropies', 'republican', 'rubens', 'salomon', 'school', 'scout', 'september', 'street', 'systems', 'university', 'wall', 'william', 'york']
#--CH
CH = [('CHAPTER 1', 'THE EAGLE', 'SCOUT'), ('CHAPTER 2', 'THE SALOMON', 'YEARS'), ('CHAPTER 3', 'THE FIRING', 'OF 1981'), ('CHAPTER 4', 'THE BLOOMBERG', 'TERMINAL'), ('CHAPTER 5', 'THE MEDIA', 'EMPIRE'), ('CHAPTER 6', 'MAYOR', 'BLOOMBERG'), ('CHAPTER 7', 'THE LATER', 'YEARS'), ('THE LESSON', 'THE LESSON', 'WHAT HE TAUGHT US')]
CARDS = [('michael rubens bloomberg was born on the fourteenth', '1942', 'MICHAEL BLOOMBERG IS BORN', 'Boston, Massachusetts', None),
 ('in nineteen sixty-six bloomberg was hired', '1966', 'SALOMON BROTHERS', 'a basement clerk', None),
 ('by nineteen seventy-two he was a partner', '1972', 'PARTNER AT THIRTY', 'head of equities', None),
 ('then in nineteen eighty-one his world', '1981', 'FIRED AT 39', 'Phibro buys Salomon', None),
 ('in nineteen eighty-two merrill agreed', '1982', 'MERRILL LYNCH SIGNS', 'twenty-two terminals', None),
 ('in nineteen ninety he made another bold', '1990', 'BLOOMBERG NEWS', 'news inside the terminal', None),
 ('in nineteen ninety-seven called bloomberg by bloomberg', '1997', 'BLOOMBERG BY BLOOMBERG', 'a memoir', None),
 ('in two thousand and one bloomberg decided', '2001', 'MAYOR OF NEW YORK', 'elected after 9/11', None),
 ('in two thousand and twenty at the age of', '2020', 'PRESIDENTIAL CAMPAIGN', 'age 77', None)]
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
EMPH = [('about ten million dollars','$10 MILLION','FIRING PAYOFF'),('about thirty million dollars','$30 MILLION','MERRILL INVESTS')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('august nineteen eighty-one', 'tense'), ('michael rubens bloomberg was born on', 'sad'), ('in nineteen sixty-six bloomberg was hired', 'drive'), ('then in nineteen eighty-one his world', 'wonder'), ('merrill lynch one of the largest', 'triumph'), ('by the end of the nineteen', 'dark'), ('in two thousand and one bloomberg', 'sad'), ('after he left office bloomberg returned', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
