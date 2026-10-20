#--KEY
KEY = ['amschel', 'austria', 'austrian', 'baron', 'belgium', 'benjamin', 'bonaparte', 'british', 'canal', 'chateau', 'chemin', 'christian', 'commons', 'company', 'disraeli', 'duke', 'edmond', 'egyptian', 'england', 'english', 'europe', 'exchange', 'france', 'frankfurt', 'french', 'german', 'germany', 'gutle', 'hanover', 'hebrew', 'hesse', 'house', 'italy', 'james', 'jewish', 'judengasse', 'judeo', 'june', 'kassel', 'lafite', 'lane', 'lionel', 'london', 'lords', 'louis', 'manchester', 'manor', 'mayer', 'minister', 'naples']
#--CH
CH = [('CHAPTER 1', 'THE GHETTO', 'OF FRANKFURT'), ('CHAPTER 2', 'THE FIVE', 'BROTHERS'), ('CHAPTER 3', 'THE MAN WHO', 'BEAT NAPOLEON'), ('CHAPTER 4', 'THE BANKERS', 'OF KINGS'), ('CHAPTER 5', 'BARONS', 'AND LORDS'), ('CHAPTER 6', 'THE LIE', 'AND THE FALL'), ('CHAPTER 7', 'THE LEGACY', 'OF A DYNASTY'), ('THE LESSON', 'THE LESSONS', 'OF THE ROTHSCHILDS')]
CARDS = [('born in this ghetto in seventeen forty-four', '1744', 'MAYER ROTHSCHILD IS BORN', 'Frankfurt ghetto', None),
 ('mayer amschel died in eighteen twelve', '1812', 'MAYER AMSCHEL DIES', 'the five brothers promise unity', None),
 ('born in seventeen seventy-seven', '1777', 'NATHAN ROTHSCHILD IS BORN', 'the most talented brother', None),
 ('to london in eighteen oh nine', '1809', 'NATHAN MOVES TO LONDON', 'bank founded', None),
 ('the eighteenth of june eighteen fifteen', '1815', 'THE BATTLE OF WATERLOO', 'the bond market holds its breath', None),
 ('in eighteen twenty-two the austrian emperor', '1822', 'THE FIVE BROTHERS BECOME BARONS', 'Austrian emperor', None),
 ('in eighteen seventy-five when prime minister benjamin disraeli', '1875', 'THE SUEZ CANAL DEAL', '£4 million overnight', None),
 ('in eighteen fifty-eight the law was changed', '1858', 'FIRST JEWISH MP', 'Lionel de Rothschild', None),
 ('in nineteen thirty-eight when nazi germany took over austria', '1938', 'THE VIENNA BRANCH IS SEIZED', 'Louis Rothschild imprisoned', None)]
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
EMPH = [('four million pounds','£4 MILLION','FOR THE SUEZ CANAL'),('ten children five sons and five daughters','10 CHILDREN','5 SONS, 5 DAUGHTERS')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('the eighteenth of june eighteen fifteen', 'tense'), ('the story begins in frankfurt germany', 'sad'), ('when the french armies swept over', 'drive'), ('the most talented of the five', 'wonder'), ('in the following decades the rothschilds', 'triumph'), ('the family also won something their', 'dark'), ('but the rothschilds also became the', 'sad'), ('today the rothschild name lives on', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
