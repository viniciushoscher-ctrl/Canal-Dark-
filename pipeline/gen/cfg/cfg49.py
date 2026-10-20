#--KEY
KEY = ['africa', 'african', 'andalusian', 'arab', 'atlantic', 'atlas', 'bakr', 'bambuk', 'battuta', 'bure', 'cairo', 'catalan', 'celebrity', 'djinguereber', 'east', 'egypt', 'egyptian', 'empire', 'europe', 'europeans', 'great', 'guinea', 'hajj', 'ishaq', 'islam', 'islamic', 'july', 'keita', 'maghan', 'majorca', 'mali', 'mandinka', 'mansa', 'mecca', 'medina', 'middle', 'moroccan', 'mosque', 'musa', 'muslim', 'niani', 'niger', 'ocean', 'portuguese', 'river', 'sahara', 'sahili', 'sankore', 'second', 'sinai']
#--CH
CH = [('CHAPTER 1', 'THE KING OF', 'MALI'), ('CHAPTER 2', 'THE LAND', 'OF GOLD AND SALT'), ('CHAPTER 3', 'THE PILGRIMAGE', 'TO MECCA'), ('CHAPTER 4', 'THE SCHOLARS', 'AND THE ARCHITECTS'), ('CHAPTER 5', 'THE CITY OF', 'TIMBUKTU'), ('CHAPTER 6', 'THE RICHEST', 'MAN WHO EVER LIVED'), ('CHAPTER 7', 'THE FADING', 'OF AN EMPIRE'), ('THE LESSON', 'THE LESSONS', 'OF MANSA MUSA')]
CARDS = [('around twelve thirty-five', '1235', 'SUNDIATA FOUNDS MALI', 'the empire is born', None),
 ('musa was probably born around twelve eighty', '1280', 'MANSA MUSA IS BORN', 'Mali, West Africa', None),
 ('around thirteen twelve the throne of mali', '1312', 'MUSA BECOMES MANSA', 'ruler of Mali', None),
 ('he set out on the pilgrimage to mecca', '1324', 'THE PILGRIMAGE TO MECCA', 'a 4,000-mile journey', None),
 ('when he reached cairo in july thirteen twenty-four', '1324', 'MUSA REACHES CAIRO', 'gold prices collapse', None),
 ('in thirteen seventy-five the famous catalan atlas', '1375', 'THE CATALAN ATLAS', 'Musa on the map', None),
 ('mansa musa probably died around thirteen thirty-seven', '1337', 'MANSA MUSA DIES', 'the empire weakens', None),
 ('in two thousand and twelve a website called celebrity net worth', '2012', 'ESTIMATED WEALTH', '$400 billion', None)]
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
EMPH = [('sixty thousand men and women','60,000 PEOPLE','IN THE CARAVAN'),('three hundred pounds of gold dust','300 LB OF GOLD','PER CAMEL'),('four hundred billion dollars','$400 BILLION','ESTIMATED WEALTH')]
#--MUSIC
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'sad', 7: 'wonder', 8: 'reflect'}
TRG = [('cairo the year thirteen twenty-four', 'tense'), ('the empire of mali was born', 'sad'), ('why was mali so rich', 'drive'), ('mansa musa was a devout muslim', 'wonder'), ('but the journey was more than', 'triumph'), ('timbuktu changed under mansa musa', 'dark'), ('how rich was mansa musa', 'sad'), ('mansa musa probably died around thirteen', 'wonder'), ('so what can we learn from', 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
