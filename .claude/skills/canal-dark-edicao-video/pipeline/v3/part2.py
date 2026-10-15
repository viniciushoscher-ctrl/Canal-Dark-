
# ================= v3: planos mais curtos, movimentos variados, transicoes xfade =================
cum = np.cumsum([0] + PLAN)
chap_start = off[1:]
WS = np.array([w[1] for w in WORDS])
Ea = np.array(E)
SHOTS = []   # (img_k, sub_idx, a, b, first_of_image, chapter)
for ci in range(len(NAMES)):
    ks = [k for k in range(len(IMG)) if cum[ci] <= int(re.match(r"(\d+)", os.path.basename(IMG[k])).group(1)) - 1 < cum[ci + 1]]
    if not ks: continue
    a0, b0 = off[ci], (off[ci + 1] if ci + 1 < len(NAMES) else T)
    bnd = [a0]
    for q in range(1, len(ks)):
        tg = a0 + (b0 - a0) * q / len(ks)
        c = Ea[(Ea > bnd[-1] + 3.0) & (Ea < b0 - 2.5)]
        bnd.append(float(c[np.argmin(abs(c - tg))]) if len(c) and abs(c - tg).min() < 3.0 else tg)
    bnd.append(b0)
    for q, k in enumerate(ks):
        a_, b_ = bnd[q], bnd[q + 1]
        n = max(1, int(round((b_ - a_) / 4.4)))
        sub = [a_]
        for i in range(1, n):
            tg = a_ + (b_ - a_) * i / n; j = int(np.argmin(abs(WS - tg)))
            sub.append(float(WS[j]) if abs(WS[j] - tg) < 0.6 and WS[j] > sub[-1] + 1.5 else tg)
        sub.append(b_)
        for i in range(n): SHOTS.append((k, i, sub[i], sub[i + 1], i == 0, ci))
if TLIM:
    SHOTS = [s for s in SHOTS if s[2] < TLIM]
    s_ = SHOTS[-1]; SHOTS[-1] = (s_[0], s_[1], s_[2], min(s_[3], TLIM), s_[4], s_[5])
TT = min(T, TLIM) if TLIM else T
print("imagens", len(IMG), "planos", len(SHOTS))

def ts(x):
    x = max(x, 0); h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"
GOLD, WHITE = "&H0042C5F5&", "&H00FFFFFF&"
KEY = {"carnegie", "steel", "million", "millions", "richest", "fortune", "empire", "railroad", "frick", "homestead", "twist",
       "billion", "disgraced", "crushed", "gold", "war", "pinkerton", "union", "libraries", "library", "morgan", "dollar", "dollars",
       "poor", "rich", "wealth", "strike", "dead", "killed", "gave", "away"}
def is_key(w):
    k = re.sub(r"[^\w-]", "", w.lower())
    return any(ch.isdigit() for ch in k) or k in KEY
events = []
groups, cur = [], []
for i, w in enumerate(WORDS):
    cur.append(i)
    end = re.search(r"[,.;:!?—]$", w[0]) is not None
    gap = i + 1 < len(WORDS) and WORDS[i + 1][1] - w[2] > 0.5
    if len(cur) >= 3 or end or gap or sum(len(WORDS[x][0]) for x in cur) > 17:
        groups.append(cur); cur = []
if cur: groups.append(cur)
for gi, g in enumerate(groups):
    st = WORDS[g[0]][1] - 0.04
    nxt = WORDS[groups[gi + 1][0]][1] - 0.02 if gi + 1 < len(groups) else T
    en = min(nxt, WORDS[g[-1]][2] + 0.45)
    txt = " ".join(("{\\c%s}%s{\\c%s}" % (GOLD, WORDS[j][0].upper(), WHITE)) if is_key(WORDS[j][0]) else WORDS[j][0].upper() for j in g)
    txt = "{\\fscx86\\fscy86\\t(0,120,\\fscx107\\fscy107)\\t(120,210,\\fscx100\\fscy100)\\fad(40,50)}" + txt
    events.append((st, en, "Cap", 5, txt))

def srt_ts(x): h=int(x//3600); m=int(x%3600//60); s=x-h*3600-m*60; return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s-int(s))*1000)):03d}".replace(",1000",",999")
cues=[]; cs=0
for i,w in enumerate(WORDS):
    if re.search(r"[.!?][\"”']?$", w[0]) or i==len(WORDS)-1 or (i-cs>=13 and re.search(r"[,;:]$",w[0])):
        seg=WORDS[cs:i+1]; cues.append((seg[0][1],seg[-1][2]+0.1," ".join(x[0] for x in seg))); cs=i+1
with open("Carnegie_Video3_English.srt","w",encoding="utf-8") as f:
    for n_,(a,b,tx) in enumerate(cues,1): f.write(f"{n_}\n{srt_ts(a)} --> {srt_ts(b)}\n"+"\n".join(textwrap.wrap(tx,42))+"\n\n")

CH = [("CHAPTER 1", "THE WEAVER'S", "SON"), ("CHAPTER 2", "THE TELEGRAPH", "BOY"), ("CHAPTER 3", "THE FIRST", "FORTUNE"),
      ("CHAPTER 4", "THE STEEL", "BET"), ("CHAPTER 5", "THE", "MACHINE"), ("CHAPTER 6", "THE BATTLE OF", "HOMESTEAD"),
      ("CHAPTER 7", "THE RICHEST MAN", "ON EARTH"), ("CHAPTER 8", "THE GOSPEL", "OF WEALTH"), ("THE LESSON", "WHAT HE REALLY", "BUILT")]
CARDS = [("this is the story of andrew carnegie", "THE STORY OF", "ANDREW CARNEGIE", "the Steel King", None),
         ("was born on november", "1835", "CARNEGIE IS BORN", "Dunfermline, Scotland", None),
         ("sailed to pennsylvania", "1848", "THE CROSSING", "a twelve-year-old immigrant", None),
         ("in eighteen fifty-three", "1853", "PRIVATE SECRETARY", "Pennsylvania Railroad", None),
         ("he left the railroad in eighteen sixty-five", "1865", "LEAVES THE RAILROAD", "already wealthy", None),
         ("in eighteen seventy-two", "1872", "THE BESSEMER PROCESS", "England", None),
         ("opened in eighteen seventy-five", "1875", "EDGAR THOMSON WORKS", "Braddock, Pennsylvania", None),
         ("in eighteen eighty-nine he brought", "1889", "HENRY CLAY FRICK", "becomes chairman", None),
         ("in eighteen ninety-two", "1892", "HOMESTEAD", "the strike that broke a union", None),
         ("in nineteen oh-one", "1901", "UNITED STATES STEEL", "the first $1 billion company", None),
         ("years earlier in eighteen eighty-nine", "1889", "THE GOSPEL OF WEALTH", "an essay that shocked the rich", None),
         ("he died in nineteen nineteen", "1919", "CARNEGIE DIES", "about 90% of his fortune given away", None)]
QUOTES = [("congratulations mr carnegie", "\"You are now the richest\\Nman in the world.\"", "J.P. MORGAN, 1901  ·  as the story goes"),
          ("the man who dies thus rich", "\"The man who dies thus rich\\Ndies disgraced.\"", "ANDREW CARNEGIE  ·  The Gospel of Wealth, 1889")]
chap_t = []
for ci_, (k, l1, l2) in enumerate(CH):
    a = chap_start[ci_] + 0.15
    if TLIM and a > TLIM: continue
    chap_t.append(a); e = a + 3.4
    events.append((a, e, "Dim", 0, "{\\fad(250,500)\\an7\\pos(0,0)\\1c&H000000&\\1a&H50&\\p1}m 0 0 l 1280 0 1280 720 0 720{\\p0}"))
    events.append((a, e, "Kick", 3, "{\\an7\\fad(250,400)\\move(70,236,90,236,0,600)}%s" % k))
    events.append((a, e, "Bar", 2, "{\\an7\\fad(250,400)\\pos(90,284)\\p1\\fscx0\\t(0,700,\\fscx100)}m 0 0 l 90 0 90 5 0 5{\\p0}"))
    events.append((a, e, "Big", 3, "{\\an7\\fad(250,400)\\move(60,300,90,300,0,600)}%s" % l1))
    events.append((a, e, "Big", 3, "{\\an7\\fad(250,400)\\move(60,388,90,388,100,700)}%s" % l2))

import importlib
exec(open("part3_graphics.py", encoding="utf-8").read())

BRT = [("fifty-three years later", g_counter, 4.4), ("sailed to pennsylvania", g_route, 4.2), ("two dollars and fifty cents", g_wage, 4.0),
       ("more steel than all of great britain", g_steel, 4.0), ("the pay was falling", g_wp, 4.2),
       ("three hundred armed pinkerton", g_pink, 4.2), ("scribbled a number", g_deal, 4.0),
       ("first billion-dollar corporation", g_billion, 4.0), ("more than two thousand five hundred", g_libs, 4.4),
       ("roughly ninety percent", g_donut, 4.2)]
BR = []
for trg, fn, dd in BRT:
    st = find(trg)
    if st is None or (TLIM and st > TLIM - 5): continue
    st += 0.25
    if any(abs(st - c) < 4 for c in chap_t): st += 3.8
    if any(abs(st - b[1]) < 5 for b in BR): continue
    BR.append((fn, st, dd))
BR_T = [b[1] for b in BR]

PHOTOS = [("his name was andrew carnegie", "carnegie_retrato.png", "1835 – 1919", "ANDREW CARNEGIE", "the Scottish-born Steel King", True, 0),
          ("was a handloom weaver", "casa_dunfermline.png", "BIRTHPLACE", "DUNFERMLINE, SCOTLAND", "the weaver's cottage", True, 0),
          ("taught himself to read the telegraph", "carnegie_16_anos.png", "c. 1851", "CARNEGIE AT 16", "with his younger brother Thomas", True, 80),
          ("bridge-building firm", "eads_bridge.png", "1874", "EADS BRIDGE", "St. Louis · built with Carnegie steel", True, 52),
          ("he named it the edgar thomson works", "edgar_thomson.png", "BRADDOCK, PENNSYLVANIA", "EDGAR THOMSON WORKS", "the mill that built an empire, 1891", True, 52),
          ("carnegie's genius was control", "carnegie_1878.png", "c. 1878", "CARNEGIE IN HIS FORTIES", "the steel king rises", True, 48),
          ("universities research institutes", "syracuse.png", "A LIVING LEGACY", "CARNEGIE LIBRARY", "Syracuse University", False, 0),
          ("andrew carnegie was two men at once", "carnegie_retrato.png", "1835 – 1919", "ANDREW CARNEGIE", "two men at once", True, 0)]
PH = []
for ph_, fn_, kk, big, sub_, gray, cb in PHOTOS:
    pth = R + "/video3-fotos/" + fn_
    if not os.path.exists(pth): continue
    a = find(ph_)
    if a is None or (TLIM and a > TLIM - 6): continue
    a += 0.2
    if any(abs(a - c) < 4 for c in chap_t): a += 3.8
    if any(b0_ - 0.5 < a < b0_ + b[2] + 0.5 or a < b0_ - 0.5 < a + 6 for b0_, b in zip(BR_T, BR)): continue
    if any(abs(a - p[1]) < 6.5 for p in PH): continue
    PH.append((pth, a, 5.5, gray, cb)); e = a + 5.5
    w = max(300, int(len(big) * 33 + 90))
    events.append((a + 0.35, e, "Dim", 1, "{\\an7\\fad(180,300)\\move(-%d,56,40,56,0,380)\\1c&H0E0B09&\\1a&H38&\\p1}m 0 0 l %d 0 %d 158 0 158{\\p0}" % (w, w, w)))
    events.append((a + 0.35, e, "Dim", 2, "{\\an7\\fad(180,300)\\move(-%d,56,40,56,0,380)\\1c%s\\p1}m 0 0 l 6 0 6 158 0 158{\\p0}" % (w, GOLD)))
    events.append((a + 0.35, e, "Kick", 3, "{\\an7\\fad(180,300)\\move(%d,68,60,68,0,380)}%s" % (-w + 20, kk)))
    events.append((a + 0.35, e, "Cardbig", 3, "{\\an7\\fad(180,300)\\move(%d,98,60,98,40,420)}%s" % (-w + 20, big)))
    events.append((a + 0.35, e, "Sub", 3, "{\\an7\\fad(180,300)\\move(%d,164,60,164,80,460)}%s" % (-w + 20, sub_)))
PHT = [(p[1], p[1] + p[2]) for p in PH]

card_t = []; last_end = 0.0
for sub, lab, big, sub2, bar in CARDS:
    a = find(sub)
    if a is None: continue
    a = a - 0.1
    if any(abs(a - c) < 3.6 for c in chap_t): a = max(c for c in chap_t if abs(a - c) < 3.6) + 3.6
    if a < last_end + 0.2 or any(b0_ - 0.5 < a < b0_ + b[2] + 0.5 for b0_, b in zip(BR_T, BR)) or any(p0 - 4.5 < a < p1 + 0.3 for p0, p1 in PHT): continue
    e = a + 4.2; last_end = e; card_t.append(a)
    w = max(260, int(len(big) * 37 + 90))
    events.append((a, e, "Dim", 1, "{\\an7\\fad(180,300)\\move(-%d,56,40,56,0,380)\\1c&H0E0B09&\\1a&H38&\\p1}m 0 0 l %d 0 %d 158 0 158{\\p0}" % (w, w, w)))
    events.append((a, e, "Dim", 2, "{\\an7\\fad(180,300)\\move(-%d,56,40,56,0,380)\\1c%s\\p1}m 0 0 l 6 0 6 158 0 158{\\p0}" % (w, GOLD)))
    events.append((a, e, "Kick", 3, "{\\an7\\fad(180,300)\\move(%d,68,60,68,0,380)}%s" % (-w + 20, lab)))
    events.append((a, e, "Cardbig", 3, "{\\an7\\fad(180,300)\\move(%d,98,60,98,40,420)}%s" % (-w + 20, big)))
    events.append((a, e, "Sub", 3, "{\\an7\\fad(180,300)\\move(%d,164,60,164,80,460)}%s" % (-w + 20, sub2)))

for ph_, big, src_ in QUOTES:
    a = find(ph_)
    if a is None or (TLIM and a > TLIM - 5): continue
    e = a + 4.6
    events.append((a - 0.2, e, "Dim", 0, "{\\fad(300,500)\\an7\\pos(0,0)\\1c&H000000&\\1a&H38&\\p1}m 0 0 l 1280 0 1280 720 0 720{\\p0}"))
    events.append((a, e, "Quote", 3, "{\\an5\\fad(350,500)\\pos(640,330)\\fscx92\\fscy92\\t(0,4600,\\fscx100\\fscy100)}%s" % big))
    events.append((a + 0.3, e, "Kick", 3, "{\\an5\\fad(300,500)\\pos(640,470)}%s" % src_))
    events.append((a, e, "Bar", 2, "{\\an7\\fad(300,500)\\pos(590,420)\\p1\\fscx0\\t(0,800,\\fscx100)}m 0 0 l 100 0 100 4 0 4{\\p0}"))

for sh_ in SHOTS[1:]:
    if not sh_[4]: continue
    b0 = sh_[2]
    events.append((b0 - 0.03, b0 + 0.16, "Dim", 0, "{\\an7\\pos(0,0)\\1c&HFFFFFF&\\1a&HA0&\\fad(0,150)\\p1}m 0 0 l 1280 0 1280 720 0 720{\\p0}"))
events.sort(key=lambda e: e[0])
hdr = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Poppins,58,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,1,0,1,4,2,2,60,60,58,1
Style: Dim,Poppins,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Kick,Poppins,26,%s,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,4,0,1,0,0,7,0,0,0,1
Style: Big,Poppins,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,1,0,1,0,3,7,0,0,0,1
Style: Bar,Poppins,20,%s,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Cardbig,Poppins,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,1,0,1,0,0,7,0,0,0,1
Style: Sub,Lora,30,&H00D8D8D8,&H00FFFFFF,&H00000000,&H00000000,0,-1,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Quote,Lora,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,-1,0,0,100,100,0,0,1,0,3,5,0,0,0,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
""" % (GOLD, GOLD)
with open("captions.ass", "w", encoding="utf-8") as f:
    f.write(hdr)
    for st, en, sty, lay, tx in events:
        f.write("Dialogue: %d,%s,%s,%s,,0,0,0,,%s\n" % (lay, ts(st), ts(en), sty, tx))
print("eventos", len(events), "capitulos", len(chap_t), "cartoes", len(card_t), "broll", len(BR), "fotos", len(PH))

# ================= trilha + SFX =================
SR = 44100; N = int(T * SR); tt = np.arange(N) / SR
def ss_(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
def pad(t_, notes, bright=0.0):
    y = 0
    for f in notes:
        y = y + np.sin(2*np.pi*f*t_) + np.sin(2*np.pi*f*1.004*t_ + 1) * 0.6 + bright * 0.4 * np.sin(2*np.pi*2*f*t_)
    return y * (0.75 + 0.25 * np.sin(2*np.pi*t_/13))
def arp(t_, notes, bpm):
    st = t_ * bpm / 60 * 2; i = st.astype(int) % len(notes); ph = st % 1
    return np.sin(2*np.pi*np.array(notes)[i]*t_) * np.exp(-ph*5)
def pulse(t_, bpm, f):
    ph = (t_ * bpm / 60) % 1
    return np.sin(2*np.pi*f*ph*60/bpm) * np.exp(-ph*9)
SC = [([55, 82.41, 110], 0, None, (50, 48), 0, 1.6),
      ([110, 130.81, 164.81], 0.2, ([220, 261.63, 329.63, 261.63], 40), None, 0.5, 0),
      ([98, 116.54, 146.83], 0.3, ([196, 233.08, 293.66, 392], 60), None, 0.6, 0),
      ([130.81, 164.81, 196, 261.63], 0.8, ([392, 493.88, 587.33, 493.88], 72), None, 0.7, 0),
      ([55, 77.78, 110], 0, None, (70, 45), 0, 2.2),
      ([73.42, 87.31, 110], 0.4, ([293.66, 349.23, 440, 349.23], 84), (84, 40), 0.5, 0.8),
      ([55, 73.42, 98], 0.2, ([220, 261.63, 311.13, 261.63], 96), (96, 42), 0.5, 1.2),
      ([87.31, 130.81, 174.61, 220], 0.7, ([349.23, 440, 523.25, 440], 50), None, 0.6, 0),
      ([55, 82.41, 110, 164.81], 0.2, ([261.63, 329.63, 392, 329.63], 44), (44, 46), 0.4, 0.8),
      ([110, 130.81, 164.81, 196], 0.3, ([329.63, 392, 329.63, 261.63], 36), None, 0.5, 0)]

rng = np.random.default_rng(3)
def whoosh(dur=0.55):
    m = int(dur * SR); x = rng.standard_normal(m); x = x[1:] - x[:-1]; x = np.append(x, 0)
    return x * np.sin(np.pi * np.linspace(0, 1, m)) ** 2
def impact():
    m = int(1.2 * SR); q = np.arange(m) / SR
    return (np.sin(2 * np.pi * 50 * q) * np.exp(-q * 4) + 0.5 * np.sin(2 * np.pi * 100 * q) * np.exp(-q * 8)
            + 0.15 * rng.standard_normal(m) * np.exp(-q * 12))
def thump():
    m = int(0.3 * SR); q = np.arange(m) / SR
    return np.sin(2 * np.pi * 66 * q) * np.exp(-q * 16) + 0.1 * rng.standard_normal(m) * np.exp(-q * 40)
def riser(dur=2.6):
    m = int(dur * SR); q = np.arange(m) / SR; u_ = q / dur
    ph = 2 * np.pi * np.cumsum(180 + 1900 * u_ ** 2) / SR
    return (np.sin(ph) * 0.5 + 0.5 * np.sin(ph * 1.5)) * u_ ** 2.2
def tick():
    m = int(0.05 * SR); q = np.arange(m) / SR
    return np.sin(2 * np.pi * 1800 * q) * np.exp(-q * 90)

# ---- musica por emocao: segue a fala (triste, tensa, animada, triunfal...) ----
def mid(m): return 440 * 2 ** ((m - 69) / 12)
def pl(f, dur=1.8, k=2.2):
    m = int(dur * SR); q = np.arange(m) / SR
    return (np.sin(2*np.pi*f*q) + 0.45*np.sin(4*np.pi*f*q)*np.exp(-q*3) + 0.2*np.sin(6*np.pi*f*q)*np.exp(-q*5)) * np.exp(-q*k) * np.minimum(1, q*300)
MOODS = {
 "sad":    dict(bpm=54, prog=[[57,60,64],[53,57,60],[60,64,67],[55,59,62]], pad=1.0, arp=[0,1,2,1], st=2, pg=0.9, k=1.6, bass=1, oct=0, gain=1.0),
 "reflect":dict(bpm=60, prog=[[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,65]], pad=0.7, arp=[0,2,1,3,2,1], st=2, pg=0.8, k=1.8, oct=0, gain=1.0),
 "wonder": dict(bpm=72, prog=[[62,66,69],[57,61,64],[59,62,66],[55,59,62]], pad=0.9, arp=[0,1,2,3,2,1], st=2, pg=0.8, k=1.4, oct=1, gain=1.0),
 "upbeat": dict(bpm=104, prog=[[60,64,67],[55,59,62],[57,60,64],[53,57,60]], pad=0.5, arp=[0,1,2,1,0,1,2,1], st=2, pg=1.0, k=3.0, bass=1, hat=1, oct=1, gain=1.1),
 "triumph":dict(bpm=84, prog=[[60,64,67],[53,57,60],[55,59,62],[60,64,67]], pad=1.5, arp=[0,2,1,2], st=2, pg=0.6, k=1.8, timp=1, saw=1, oct=1, gain=1.2),
 "tense":  dict(bpm=76, prog=[[45,48,51],[45,48,51],[43,46,49],[44,47,50]], pad=1.0, arp=[], drone=1, heart=1, gain=1.0),
 "dark":   dict(bpm=60, prog=[[38,41,45],[34,38,41],[43,46,50],[45,49,52]], pad=1.2, arp=[0,2], st=1, pg=0.7, k=2.5, drone=1, hit=1, gain=1.1),
 "drive":  dict(bpm=112, prog=[[45,48,52],[45,48,52],[41,45,48],[43,47,50]], pad=0.6, arp=[0,0,2,0,1,0,2,1], st=2, pg=0.7, k=5.0, bass=1, hat=1, tick=1, gain=1.2),
}
def render_mood(name, dur):
    P = MOODS[name]; n = int((dur + 3) * SR); y = np.zeros(n)
    bar = 4 * 60 / P["bpm"]; beat = 60 / P["bpm"]
    def put(sig, t0, a=1.0):
        i0 = int(t0 * SR)
        if 0 <= i0 < n: seg = sig[:n - i0]; y[i0:i0 + len(seg)] += seg * a
    for b in range(int((dur + 3) / bar) + 1):
        ch = P["prog"][b % len(P["prog"])]; t0 = b * bar
        m = int(bar * 1.3 * SR); qq = np.arange(m) / SR
        env = np.minimum(1, qq / 0.9) * np.minimum(1, (bar * 1.3 - qq) / 0.9)
        padw = 0
        for nt in ch:
            f = mid(nt - 12)
            w = np.sin(2*np.pi*f*qq) + 0.5*np.sin(2*np.pi*f*1.003*qq + 1)
            if P.get("saw"): w = w + sum(np.sin(2*np.pi*f*h*qq) / h for h in range(2, 6))
            padw = padw + w
        put(padw * env * P["pad"] * 0.12, t0)
        if P.get("drone"):
            f = mid(ch[0] - 12); dr = (np.sin(2*np.pi*f*qq) + 0.6*np.sin(2*np.pi*f*1.0595*qq)) * (0.8 + 0.2*np.sin(2*np.pi*5*qq)) * env
            put(dr * 0.12, t0)
        if P.get("arp"):
            ext = ch + [x + 12 for x in ch]; sd = beat / P.get("st", 2)
            for s_ in range(int(bar / sd)):
                put(pl(mid(ext[P["arp"][s_ % len(P["arp"])] % len(ext)] + 12 * P.get("oct", 0)), 1.8, P["k"]), t0 + s_ * sd, P["pg"] * 0.22)
        if P.get("bass"):
            for bt in range(4): put(pl(mid(ch[0] - 24), 0.7, 5.0), t0 + bt * beat, 0.35)
        if P.get("timp"): put(thump(), t0, 0.5); put(thump(), t0 + 2 * beat, 0.3)
        if P.get("hat"):
            for bt in range(8):
                hh = rng.standard_normal(int(0.03 * SR)); hh = (hh[1:] - hh[:-1]); put(np.append(hh, 0) * np.linspace(1, 0, len(hh) + 1), t0 + bt * beat / 2 + beat / 4, 0.06)
        if P.get("heart"):
            for bt in range(4): put(thump(), t0 + bt * beat, 0.5); put(thump(), t0 + bt * beat + 0.2, 0.3)
        if P.get("tick"):
            for q_ in range(16): put(tick(), t0 + q_ * beat / 4, 0.05)
        if P.get("hit"): put(impact()[:int(1.2 * SR)], t0, 0.35)
    r_ = np.sqrt(np.mean(y[:int(dur * SR)] ** 2)) + 1e-9
    return y / r_ * 0.022 * P.get("gain", 1.0)
# linha emocional do texto: (frase, humor)
DEF = {0: "tense", 1: "sad", 2: "upbeat", 3: "upbeat", 4: "wonder", 5: "drive", 6: "tense", 7: "upbeat", 8: "reflect", 9: "reflect"}
TRG = [("fifty-three years later", "triumph"), ("was it generosity", "tense"), ("to understand the man who gave", "dark"),
       ("in eighteen forty-eight", "wonder"), ("his first job was", "dark"), ("but the boy had something", "wonder"),
       ("then came the civil war", "tense"), ("by the time he left the railroad", "triumph"), ("but iron was only the beginning", "wonder"),
       ("back in pittsburgh", "drive"), ("but efficiency has a price", "dark"), ("something was going to break", "tense"),
       ("the workers were waiting", "dark"), ("carnegie was thousands of miles", "sad"), ("the public never forgot", "dark"),
       ("morgan wanted to merge", "tense"), ("in nineteen oh-one", "triumph"), ("carnegie had reached the very top", "reflect"),
       ("and then at sixty-six", "tense"), ("now he meant it", "wonder"), ("by the time he died", "triumph"),
       ("but the twist is what", "sad"), ("the question follows him", "dark"), ("the poor weaver's son", "triumph"),
       ("which one will history remember", "reflect")]
TWISTS = ["but the twist is what", "something was going to break", "and then at sixty-six", "was it generosity", "carnegie was thousands of miles"]
segs = [(chap_start[i - 1] if i > 0 else 0.0, DEF[i]) for i in range(len(NAMES)) if i == 0 or chap_start[i - 1] < T]
for ph_, mo in TRG:
    t_ = find(ph_)
    if t_ is not None: segs.append((t_ - 0.3, mo))
segs.sort(key=lambda x: x[0])
cl_ = []
for t_, mo in segs:
    if cl_ and t_ - cl_[-1][0] < 2.0: cl_[-1] = (cl_[-1][0], mo)
    else: cl_.append((t_, mo))
segs = [s for s in cl_ if not TLIM or s[0] < TLIM]
print("humores:", [(round(a, 1), m) for a, m in segs])
music = np.zeros(N, np.float32)
for si, (a0, mo) in enumerate(segs):
    b0 = segs[si + 1][0] if si + 1 < len(segs) else T
    seg = render_mood(mo, b0 - a0 + 3.0)
    i0 = int(max(0, a0 - 1.2) * SR); i1 = min(N, int(min(T, b0 + 1.2) * SR))
    y = seg[:i1 - i0] if a0 - 1.2 >= 0 else seg[:i1 - i0]
    t_ = tt[i0:i1]
    wgt = ss_((t_ - (a0 - 1.2)) / 2.4) if si > 0 else 1.0
    if si < len(segs) - 1: wgt = wgt * (1 - ss_((t_ - (b0 - 1.2)) / 2.4))
    music[i0:i0 + len(y)] += (y[:len(t_)] * wgt).astype(np.float32)
music *= np.clip(tt / 3, 0, 1) * np.clip((T - tt) / 4, 0, 1)
for ph_ in TWISTS:  # silencio dramatico antes da reviravolta
    t_ = find(ph_)
    if t_ is not None: music *= 1 - 0.85 * np.clip(1 - np.abs(tt - (t_ - 0.45)) / 0.45, 0, 1)
twist_t = [find(p) for p in TWISTS if find(p) is not None]
L = music.astype(np.float64); R_ = np.roll(L, 40)
def add(sig, t0, amp):
    i0 = int(t0 * SR); i1 = min(N, i0 + len(sig))
    if i0 < N and i0 >= 0:
        L[i0:i1] += sig[:i1 - i0] * amp; R_[i0:i1] += sig[:i1 - i0] * amp
for sh_ in SHOTS[1:]:
    major = sh_[4]
    add(whoosh()[:int(0.3 * SR)], max(0, sh_[2] - 0.2), 0.06 if major else 0.035); add(thump(), sh_[2], 0.12 if major else 0.06)
for c in chap_t: add(impact(), c, 0.24); add(riser(), max(0, c - 2.6), 0.07); add(whoosh(), max(0, c - 0.3), 0.07)
for c in card_t: add(whoosh(), max(0, c - 0.05), 0.05)
for c in twist_t: add(impact(), c - 0.05, 0.3); add(riser(0.9), max(0, c - 0.95), 0.08)
for fn_, st_, dd_ in BR:
    add(riser(1.2), max(0, st_ - 1.2), 0.05); add(impact(), st_, 0.14)
    for q in range(int(dd_ * 3)): add(tick(), st_ + 0.5 + q * 0.3, 0.03)
for pth_, a_, d_, g_, c_ in PH: add(whoosh(), max(0, a_ - 0.1), 0.06); add(thump(), a_, 0.1)
pcm = (np.clip(np.stack([L, R_], 1), -0.98, 0.98) * 32767).astype("<i2")
with wave.open("bed.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

# ================= planos: 1080p, movimentos, xfade por capitulo =================
os.makedirs("clips3", exist_ok=True)
REG = [(0.02, 0.02), (0.30, 0.02), (0.02, 0.30), (0.30, 0.30), (0.16, 0.16)]
def trans_for(prev, nxt, idx):
    if nxt[1] > 0: return ("fade", 0.30)
    pb = "_bw" in os.path.basename(IMG[prev[0]]); nb = "_bw" in os.path.basename(IMG[nxt[0]])
    if pb and not nb: return ("fadewhite", 0.40)
    return [("fadeblack", 0.40), ("hblur", 0.40), ("dissolve", 0.40), ("smoothleft", 0.40), ("zoomin", 0.45), ("fade", 0.40)][idx % 6]
jobs = []
chap_shots = {}
for n_, s in enumerate(SHOTS): chap_shots.setdefault(s[5], []).append(n_)
OV = {}
for ci, ids in chap_shots.items():
    for p, n_ in enumerate(ids):
        OV[n_] = trans_for(SHOTS[n_], SHOTS[ids[p + 1]], n_) if p + 1 < len(ids) else None
for n_, (k, i, a_, b_, first, ci) in enumerate(SHOTS):
    ov = OV[n_][1] if OV[n_] else 0.0
    d = b_ - a_ + ov; nf = max(int(round(d * FR)), 3); out = f"clips3/c{n_+1:03d}.mp4"
    u = f"(on/{nf})"; e = f"(3*{u}*{u}-2*{u}*{u}*{u})"
    mv = (k + i * 3 + n_) % 7
    zs = {0: f"1+0.16*{e}", 1: f"1.16-0.16*{e}", 2: "1.18", 3: "1.18", 4: "1.2", 5: "1.2", 6: f"1+0.2*{e}"}[mv]
    xs = {0: "iw/2-(iw/zoom/2)", 1: "iw/2-(iw/zoom/2)", 2: f"(iw-iw/zoom)*{e}", 3: f"(iw-iw/zoom)*(1-{e})", 4: "iw/2-(iw/zoom/2)",
          5: "iw/2-(iw/zoom/2)", 6: f"(iw-iw/zoom)*(0.3+0.5*{e})"}[mv]
    ys = {0: "ih/2-(ih/zoom/2)", 1: "ih/2-(ih/zoom/2)", 2: "ih/2-(ih/zoom/2)", 3: "ih/2-(ih/zoom/2)", 4: f"(ih-ih/zoom)*(1-{e})",
          5: f"(ih-ih/zoom)*{e}", 6: f"(ih-ih/zoom)*(0.6-0.4*{e})"}[mv]
    if i % 2 == 0: pre = "crop=iw*0.94:ih*0.94:0:0"
    else:
        rx, ry = REG[(k + i) % 5]; pre = f"crop=iw*0.66:ih*0.66:iw*{rx}:ih*{ry}"
    vf = (f"{pre},scale=2880:1620:flags=bicubic,zoompan=z='{zs}':x='{xs}':y='{ys}':d={nf}:s=1920x1080:fps={FR},"
          f"unsharp=5:5:0.6,format=yuv420p")
    jobs.append((out, f"ffmpeg -y -v error -loop 1 -i '{IMG[k]}' -vf \"{vf}\" -frames:v {nf} -c:v libx264 -preset veryfast -crf 17 {out}"))
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(2) as ex: list(ex.map(lambda j: sh(j[1]), jobs))
print("clips ok", len(jobs))
chap_files = []
for ci, ids in sorted(chap_shots.items()):
    outc = f"chap{ci:02d}.mp4"; ins = " ".join(f"-i clips3/c{n_+1:03d}.mp4" for n_ in ids)
    if len(ids) == 1: sh(f"ffmpeg -y -v error {ins} -c copy {outc}")
    else:
        parts_ = []; last = "[0:v]"; acc = 0.0
        for p in range(len(ids) - 1):
            n_ = ids[p]; tr, od = OV[n_]; acc += SHOTS[n_][3] - SHOTS[n_][2]
            o_ = "[vv]" if p == len(ids) - 2 else f"[x{p}]"
            parts_.append(f"{last}[{p+1}:v]xfade=transition={tr}:duration={od}:offset={acc:.3f}{o_}"); last = o_
        ch = ";".join(parts_)
        sh(f"ffmpeg -y -v error {ins} -filter_complex \"{ch}\" -map '[vv]' -c:v libx264 -preset veryfast -crf 17 -pix_fmt yuv420p {outc}")
    chap_files.append(outc)
open("listc.txt", "w").write("\n".join(f"file '{c}'" for c in chap_files))
sh("ffmpeg -y -v error -f concat -safe 0 -i listc.txt -c copy base.mp4")
print("base ok", len(SHOTS), "planos")

# poeira / riscos de filme (loop)
from PIL import Image, ImageDraw
if not os.path.exists("dust.mp4"):
    pr = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "gray", "-s", "1920x1080", "-r", str(FR), "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p", "dust.mp4"], stdin=subprocess.PIPE)
    rr = np.random.default_rng(11)
    for fr_ in range(200):
        im = Image.new("L", (1920, 1080), 0); d = ImageDraw.Draw(im)
        for _ in range(int(rr.integers(10, 30))):
            x, y = int(rr.integers(0, 1920)), int(rr.integers(0, 1080)); r = int(rr.integers(1, 4)); v = int(rr.integers(90, 220))
            d.ellipse([x, y, x + r, y + r], fill=v)
        if rr.random() < 0.35:
            x = int(rr.integers(0, 1920)); d.line([(x, 0), (x + int(rr.integers(-3, 3)), 1080)], fill=int(rr.integers(40, 110)), width=1)
        pr.stdin.write(np.asarray(im, np.uint8).tobytes())
    pr.stdin.close(); pr.wait()
