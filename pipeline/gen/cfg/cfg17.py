#--KEY
KEY = {"buffett", "warren", "berkshire", "hathaway", "omaha", "graham", "stock", "stocks", "invest", "investor", "insurance", "float", "moat", "patience", "million", "billion", "billions", "charity", "reputation", "market"}
#--CH
CH = [("CHAPTER 1", "THE BOY WHO", "SOLD GUM"), ("CHAPTER 2", "THE STUDENT OF", "BENJAMIN GRAHAM"), ("CHAPTER 3", "THE KITCHEN", "TABLE FUND"),
      ("CHAPTER 4", "THE DYING", "TEXTILE MILL"), ("CHAPTER 5", "THE BILLIONAIRE IN", "OMAHA"), ("CHAPTER 6", "BE GREEDY", "WHEN OTHERS FEAR"), ("THE LESSON", "TIME IS", "YOUR EDGE")]
CARDS = [("warren edward buffett was born on august", "1930", "BUFFETT IS BORN", "Omaha, Nebraska", None),
         ("buffett enrolled at columbia", "1950", "COLUMBIA", "student of Benjamin Graham", None),
         ("in nineteen sixty-nine with the market", "1969", "THE PARTNERSHIP CLOSES", "all the money returned", None),
         ("buffett took over berkshire in nineteen sixty-five", "1965", "BERKSHIRE HATHAWAY", "a dying textile mill", None),
         ("in nineteen ninety-one he faced a crisis", "1991", "THE SALOMON CRISIS", "interim chairman", None),
         ("in two thousand eight after the financial crisis", "2008", "THE CRISIS BETS", "Goldman Sachs and GE", None),
         ("buffett turned ninety in two thousand twenty", "2020", "AGE 90", "still working in Omaha", None)]
#--BRT
def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video%N-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("returned about twenty-nine percent", g_returns, 5.5), ("see's candies in nineteen seventy-two", g_sees, 5.5), ("worth about a trillion dollars", g_worth, 5.5),
       ("a stockbroker", FFg("office"), 5.0), ("candy company", FFg("candy"), 5.0), ("the washington post", FFg("nyc"), 5.5), ("television", FFg("tv"), 5.0),
       ("the market is a voting machine", FFg("nyc", 1), 5.5), ("dot-com bubble", FFg("office", 1), 5.0)] + MAPBRT
AUTO = []
if os.path.exists("autobrt.txt"):
    for _l in open("autobrt.txt", encoding="utf-8"):
        if "|" in _l:
            _p, _f = _l.rstrip("\n").split("|", 1); AUTO.append((_p, g_foot(_f), 5.0))
BRT = BRT + AUTO
BRT = [b for b in BRT if b[1] is not None]
#--PHOTOS
PHOTOS = [
 ('his name is warren buffett', 'people/buffett.jpg', '1930 –', 'WARREN BUFFETT', 'the oracle of Omaha', True, 0),
 ('his father howard', 'people/howard.jpg', '1903 – 1964', 'HOWARD BUFFETT', 'stockbroker and congressman', True, 0),
 ('cities service', 'fotos/cities_0.jpg', '1942', 'CITIES SERVICE', 'his first stock', True, 0),
 ('columbia university', 'fotos/columbia_0.jpg', '1950', 'COLUMBIA UNIVERSITY', 'where he met Graham', True, 0),
 ('benjamin graham', 'people/graham.jpg', '1894 – 1976', 'BENJAMIN GRAHAM', 'the father of value investing', True, 0),
 ('the partnership', 'fotos/omaha_0.jpg', '1956', 'OMAHA, NEBRASKA', 'where the partnership began', True, 0),
 ('berkshire hathaway', 'fotos/textile_0.jpg', '1965', 'BERKSHIRE HATHAWAY', 'a failing textile company', True, 0),
 ('see\'s candies', 'fotos/sees_0.jpg', '1972', "SEE'S CANDIES", 'bought for $25 million', True, 0),
 ('the washington post', 'fotos/wapo_0.jpg', '1973', 'THE WASHINGTON POST', 'another Buffett stake', True, 0),
 ('geico', 'fotos/geico_0.jpg', '1976', 'GEICO', 'the insurance engine', True, 0),
 ('coca-cola', 'fotos/coke_0.jpg', '1988', 'COCA-COLA', 'a classic moat', True, 0),
 ('charlie munger', 'people/munger.jpg', '1924 – 2023', 'CHARLIE MUNGER', 'his partner at Berkshire', True, 0),
 ('salomon brothers', 'fotos/salomon_0.jpg', '1991', 'SALOMON BROTHERS', 'the scandal he cleaned up', True, 0),
 ('goldman sachs and general electric', 'fotos/gs_0.jpg', '2008', 'GOLDMAN SACHS', 'a crisis bet', True, 0),
 ('bill gates', 'people/gates.jpg', '2010', 'BILL GATES', 'co-founder of the Giving Pledge', True, 0),
 ('the same omaha house', 'fotos/house_0.jpg', '1958', 'THE OMAHA HOUSE', 'bought for $31,500', True, 0)]
#--EMPH
EMPH = [("never lose money", "NEVER LOSE", "MONEY"), ("a voting machine", "A VOTING", "MACHINE"), ("a weighing machine", "A WEIGHING", "MACHINE"),
        ("charge them nothing unless he beats the market", "NO FEE UNLESS", "HE WINS"), ("be greedy when others are fearful", "BE GREEDY", "WHEN OTHERS FEAR"), ("patient honest and boring", "PATIENT.", "HONEST. BORING.")]
#--MUSIC
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "dark", 5: "triumph", 6: "upbeat", 7: "reflect"}
TRG = [("nineteen fifty-six a twenty-five-year-old", "tense"), ("warren edward buffett was born", "sad"), ("he was rejected by harvard", "drive"), ("buffett enrolled at columbia", "wonder"),
       ("the results were extraordinary", "triumph"), ("in nineteen sixty-nine with the market", "dark"), ("buffett took over berkshire", "drive"), ("insurance had a magical feature", "wonder"),
       ("in nineteen ninety-one he faced a crisis", "dark"), ("in two thousand eight", "triumph"), ("with bill gates he started", "upbeat"), ("the second is that character", "reflect")]
TWISTS = ["in nineteen sixty-nine with the market at a peak", "he closed the partnership", "he faced a crisis", "in two thousand eight after the financial crisis", "the second is that character"]
#--NSC
73
#--MAP
MAPBRT = [("warren edward buffett was born on august", lambda u: g_map(u, -95.93, 41.26, "OMAHA, NEBRASKA", "UNITED STATES  ·  1930"), 7.0)]
#--KW
{"A kitchen table in Omaha": "omaha_0", "A small gray house": "house_0", "A Nebraska street": "omaha_1", "Columbia University campus": "columbia_0", "A professor writing": "graham_0",
 "A failing textile mill": "textile_0", "Looms covered": "textile_1", "A candy shop": "sees_0", "A newspaper printing press": "wapo_0", "An insurance office": "geico_0",
 "A bottle of cola": "coke_0", "A trading floor in crisis": "salomon_0", "The dot-com boom": "dotcom_0", "A Wall Street crash": "dotcom_1", "A shareholder meeting": "meeting_0",
 "A financial crisis headline room": "gs_1", "Two billionaires on a stage": "pledge_0"}
