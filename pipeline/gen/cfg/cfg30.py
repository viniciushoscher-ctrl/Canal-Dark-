#--KEY
KEY = ['america', 'august', 'chicago', 'christmas', 'clock', 'columbian', 'company', 'conway', 'cooley', 'england', 'exposition', 'field', 'fire', 'fort', 'frango', 'great', 'haymarket', 'history', 'january', 'junior', 'lake', 'leiter', 'levi', 'macy', 'marshall', 'massachusetts', 'midwest', 'museum', 'nannie', 'natural', 'october', 'palmer', 'pittsfield', 'potter', 'room', 'sheridan', 'state', 'street', 'tiffany', 'twentieth', 'university', 'wadsworth', 'walnut', 'world']
#--CH
CH = [('CHAPTER 1', 'THE CLERK', 'FROM MASSACHUSETTS'), ('CHAPTER 2', 'THE PARTNER', 'IN CHICAGO'), ('CHAPTER 3', 'THE GREAT', 'FIRE'), ('CHAPTER 4', 'GIVE THE LADY', 'WHAT SHE WANTS'), ('CHAPTER 5', 'THE RICHEST MAN', 'IN CHICAGO'), ('CHAPTER 6', 'LOSSES AND', 'LEGACY'), ('THE LESSON', 'SERVICE', 'BUILDS EMPIRES')]
CARDS = [('marshall field was born on august eighteenth', '1834', 'FIELD', 'Marshall Field was born on August', None),
 ('in eighteen sixty-five he met a rising', '1865', 'POTTER PALMER', 'In eighteen sixty-five, he met a r', None),
 ('by eighteen seventy-one the firm had sales', '1871', 'STATE STREET', 'By eighteen seventy-one, the firm', None),
 ('on the night of october eighth eighteen', '1871', 'OCTOBER', 'On the night of October eighth, ei', None),
 ('in eighteen eighty-one field bought out leiter', '1881', 'FIELD', 'In eighteen eighty-one, Field boug', None),
 ('his wife nannie died in eighteen ninety-six', '1896', 'NANNIE', 'His wife Nannie died in eighteen n', None)]
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
DEF = {0: 'tense', 1: 'sad', 2: 'drive', 3: 'wonder', 4: 'triumph', 5: 'dark', 6: 'reflect', 7: 'reflect'}
TRG = [('october eighteen seventy-one', 'tense'), ('marshall field was born on august', 'sad'), ('chicago was a booming muddy frontier', 'drive'), ('the store on state street became', 'wonder'), ('on the night of october eighth', 'triumph'), ('in eighteen eighty-one field bought out', 'dark'), ("but field's private life was lonely", 'reflect'), ("marshall field's story holds two lessons", 'reflect')]
TWISTS = []
#--NSC
74
#--MAP
MAPBRT = []
#--KW
{}
