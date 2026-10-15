#!/usr/bin/env python3
"""Video 3 Carnegie - mesma edicao em camadas do video 1, com tempos de palavra EXATOS (edge-tts)."""
import re, subprocess, glob, math, wave, os, sys, json, textwrap
import numpy as np

R = "/home/claude/canal-dark-"
B = "/home/claude/video_build5"
AUD = R + "/video5-narracao/audio"
IMG = sorted(glob.glob(os.environ.get("V3IMG", B + "/bright") + "/*.jpg"))
NAMES = ["00_hook","01_cap1","02_cap2","03_cap3","04_cap4","05_cap5","06_cap6","07_lesson"]
PLAN = None
TLIM = float(os.environ.get("TLIM", "0")) or None
FR = 25
os.chdir(B)
def sh(c):
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    if r.returncode:
        print("ERRO ffmpeg:", r.stderr[-1500:]); raise SystemExit(1)
    return r
dur = lambda f: float(sh(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {f}").stdout)

off = []; t0 = 0.0
for n in NAMES:
    sh(f"ffmpeg -y -v error -i {AUD}/{n}.mp3 -ar 44100 -ac 1 w_{n}.wav")
    off.append(t0); t0 += dur(f"w_{n}.wav")
T = t0
open("wl.txt", "w").write("\n".join(f"file 'w_{n}.wav'" for n in NAMES))
sh("ffmpeg -y -v error -f concat -safe 0 -i wl.txt -c copy narracao.wav")
print("duracao", round(T, 1), "min", round(T / 60, 2))
_d = [off[i + 1] - off[i] for i in range(len(NAMES) - 1)] + [T - off[-1]]
NSC = 86
PLAN = [max(1, int(round(NSC * x / T))) for x in _d]; PLAN[-1] += NSC - sum(PLAN)
print("PLAN", PLAN)

rot = open(R + "/video5-narracao/roteiro.txt", encoding="utf-8").read()
parts = re.split(r"^### (\S+)\n", rot, flags=re.M)[1:]
TXT = dict(zip(parts[::2], parts[1::2]))
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
WORDS = []
for ci, n in enumerate(NAMES):
    bw0 = json.load(open(f"{AUD}/{n}.json")); bw = []
    for b_ in bw0:
        sw = b_["w"].split()
        if len(sw) <= 1: bw.append(b_); continue
        tl = sum(len(x) + 1 for x in sw); p_ = b_["s"]
        for x in sw:
            dd = b_["d"] * (len(x) + 1) / tl; bw.append({"w": x, "s": p_, "d": dd}); p_ += dd
    toks = TXT[n].split(); j = 0; miss = 0
    for tk in toks:
        nt = norm(tk); acc = ""; k = j
        while k < len(bw) and len(acc) < len(nt) and k - j < 5:
            acc += norm(bw[k]["w"]); k += 1
        if acc == nt and k > j:
            WORDS.append((tk, off[ci] + bw[j]["s"], off[ci] + bw[k - 1]["s"] + bw[k - 1]["d"], ci)); j = k
        else:
            miss += 1; s_ = WORDS[-1][2] if WORDS else off[ci]
            WORDS.append((tk, s_, s_ + 0.25, ci))
    if miss: print("aviso", n, "palavras sem par:", miss)
for i in range(1, len(WORDS)):
    if WORDS[i][1] < WORDS[i-1][1]:
        WORDS[i] = (WORDS[i][0], WORDS[i-1][1], max(WORDS[i][2], WORDS[i-1][1] + .1), WORDS[i][3])
E = [w[2] for w in WORDS if re.search(r"[.!?][\"”']?$", w[0])]
print("palavras", len(WORDS), "frases", len(E))
def find(phrase, after=0.0):
    ph = [norm(x) for x in phrase.split()]; nw = [norm(w[0]) for w in WORDS]
    for i in range(len(nw) - len(ph) + 1):
        if nw[i:i+len(ph)] == ph and WORDS[i][1] >= after: return WORDS[i][1]
    print("!! nao achei:", phrase); return None


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
        n = max(1, int(round((b_ - a_) / 3.7)))
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
KEY = {"ford", "million", "billion", "dollar", "dollars", "wages", "wage", "factory", "assembly", "line", "model", "engine", "machine", "cars", "car", "richest", "failure", "collapsed", "fortune", "died", "lost", "power", "control", "bomber", "five-dollar", "price", "mother", "edison", "dodge", "rouge"}
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
with open("Ford_Video5_English.srt","w",encoding="utf-8") as f:
    for n_,(a,b,tx) in enumerate(cues,1): f.write(f"{n_}\n{srt_ts(a)} --> {srt_ts(b)}\n"+"\n".join(textwrap.wrap(tx,42))+"\n\n")

CH = [("CHAPTER 1", "THE FARM BOY WHO", "HATED FARMING"), ("CHAPTER 2", "THE FAILURES BEFORE", "THE FORTUNE"), ("CHAPTER 3", "THE CAR FOR", "EVERYONE"),
      ("CHAPTER 4", "THE FIVE-", "DOLLAR DAY"), ("CHAPTER 5", "THE PRICE", "OF CONTROL"), ("CHAPTER 6", "THE ARSENAL", "OF DEMOCRACY"), ("THE LESSON", "THE MARKET", "HE BUILT")]
CARDS = [("henry ford was born on july", "1863", "HENRY FORD IS BORN", "Greenfield Township, Michigan", None),
         ("in eighteen ninety-one he joined", "1891", "EDISON ILLUMINATING CO.", "chief engineer by 1893", None),
         ("in june eighteen ninety-six", "1896", "THE QUADRICYCLE", "Ford's first car", None),
         ("in october nineteen hundred and one he beat", "1901", "FORD BEATS WINTON", "the race that opened the door", None),
         ("in june nineteen oh-three", "1903", "FORD MOTOR COMPANY", "12 investors · about $28,000", None),
         ("in october nineteen oh-eight", "1908", "THE MODEL T", "$850", None),
         ("in nineteen thirteen at the highland park", "1913", "HIGHLAND PARK", "the moving assembly line", None),
         ("so on january fifth nineteen fourteen he announced", "1914", "THE FIVE-DOLLAR DAY", "double the going wage", None),
         ("in nineteen nineteen he bought out", "1919", "THE BUYOUT", "about $106 million", None),
         ("by nineteen twenty-seven sales had collapsed", "1927", "THE MODEL A", "after 19 years of the Model T", None),
         ("edsel died in nineteen forty-three", "1943", "EDSEL FORD DIES", "aged 49", None),
         ("henry ford died on april seventh", "1947", "HENRY FORD DIES", "aged 83", None)]
QUOTES = []
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
exec(open("part3_ford.py", encoding="utf-8").read())

def FFg(tag, idx=0):
    fl = sorted(glob.glob(R + "/video5-footage/clips/%s_*.mp4" % tag))
    return g_foot(fl[idx % len(fl)]) if fl else None
BRT = [("ten thousand men are standing", FFg("crowd"), 6.0), ("it is january fifth", FFg("detroit"), 5.0),
       ("steam engine moving down a country road", FFg("road"), 5.5), ("took a job in a machine shop", FFg("factory"), 5.5),
       ("a rattling four-wheeled machine", FFg("car"), 5.5), ("he went racing", FFg("car", 1), 5.5),
       ("the model t arrived", FFg("modelt"), 6.0), ("farmers stopped feeling isolated", FFg("farm"), 5.5),
       ("a moving line with each worker", FFg("assembly"), 6.0), ("about ninety-three minutes", g_time, 5.0),
       ("prices began to fall", g_price, 5.5), ("double the going wage", g_wage5, 4.8),
       ("half of all the cars in the world", g_share, 4.6), ("he built the giant river rouge complex", FFg("rouge"), 5.5),
       ("turned his factories into the arsenal", FFg("war"), 5.5), ("a bomber rolled off that line", g_bomber, 5.5),
       ("the stress had broken him", FFg("crowd", 1), 5.0), ("workers were bleeding", FFg("factory", 1), 5.0)] + MAPBRT
BR = []
for trg, fn, dd in BRT:
    st = find(trg)
    if st is None or fn is None or (TLIM and st > TLIM - 5): continue
    st += 0.25
    if any(abs(st - c) < 4 for c in chap_t): st += 3.8
    if any(abs(st - b[1]) < 5 for b in BR): continue
    BR.append((fn, st, dd))
BR_T = [b[1] for b in BR]

PHOTOS = [
 ('his name is henry ford', 'people/ford.jpg', '1863 – 1947', 'HENRY FORD', 'the man who put the world on wheels', True, 0),
 ('a year later his mother died', 'fotos/mary_0.jpg', 'HIS MOTHER', 'MARY FORD', 'her death in 1876 marked him forever', True, 0),
 ('joined the edison illuminating company', 'people/edison.jpg', '1891', 'THOMAS EDISON', 'Ford worked for his company', True, 0),
 ('a rattling four-wheeled machine', 'fotos/quad_0.jpg', '1896', 'THE QUADRICYCLE', "Ford's first car", True, 0),
 ('alexander winton', 'people/winton.jpg', '1901', 'ALEXANDER WINTON', 'the most famous driver in America', True, 0),
 ('ford motor company was born', 'fotos/motor1903_0.jpg', '1903', 'THE FIRST FORD CAR', 'Ford Model A of 1903', True, 0),
 ('the model t arrived', 'fotos/modelt_0.jpg', '1908', 'THE MODEL T', 'a car for the great multitude', True, 0),
 ('a moving line with each worker', 'fotos/line1_0.jpg', '1913', 'THE ASSEMBLY LINE', 'Highland Park, Michigan', True, 0),
 ('it was neither', 'fotos/fivedollar_0.jpg', 'JANUARY 1914', 'THE FIVE-DOLLAR DAY', 'crowds outside the Ford employment office', True, 0),
 ('including the dodge brothers', 'people/dodge1.jpg', '1919', 'JOHN DODGE', 'early investor, later a rival', True, 0),
 ('the giant river rouge complex', 'fotos/rouge1_0.jpg', '1920s', 'RIVER ROUGE', 'ore in one end, cars out the other', True, 0),
 ('the dearborn independent', 'fotos/dearborn_0.jpg', '1920s', 'THE DEARBORN INDEPENDENT', "a newspaper that spread hate", True, 0),
 ('general motors offered color', 'people/sloan.jpg', '1920s', 'ALFRED SLOAN', 'built General Motors into a rival', True, 0),
 ('his own son edsel', 'people/edsel.jpg', '1943', 'EDSEL FORD', 'died at only forty-nine', True, 0),
 ('at willow run near detroit', 'fotos/willow1_0.jpg', '1942', 'WILLOW RUN', 'a bomber plant almost a mile long', True, 0),
 ('his security chief harry bennett', 'people/bennett.jpg', '1937', 'HARRY BENNETT', 'Ford security chief', True, 0),
 ('the battle of the overpass', 'fotos/overpass_0.jpg', '1937', 'THE OVERPASS', 'River Rouge, May 1937', True, 0),
 ('only a family intervention', 'fotos/family_0.jpg', '1945', 'THE FORD FAMILY', 'Henry, Clara and Edsel', True, 0),
 ('his wife clara', 'people/clara.jpg', '1945', 'CLARA FORD', 'forced the handover of power', True, 0),
 ('his grandson henry the second', 'people/henry2.jpg', '1945', 'HENRY FORD II', 'saved the company', True, 0),
 ('henry ford died on april seventh', 'people/ford.jpg', '1863 – 1947', 'HENRY FORD', 'the empire that put the world on wheels', True, 0)]
PH = []
for ph_, fn_, kk, big, sub_, gray, cb in PHOTOS:
    pth = R + "/video5-commons/" + fn_
    if not os.path.exists(pth): continue
    a = find(ph_)
    if a is None or (TLIM and a > TLIM - 6): continue
    a += 0.2
    if any(abs(a - c) < 4 for c in chap_t): a += 3.8
    if any(b0_ - 0.5 < a < b0_ + b[2] + 0.5 or a < b0_ - 0.5 < a + 6 for b0_, b in zip(BR_T, BR)): continue
    if any(abs(a - p[1]) < 5.2 for p in PH): continue
    PH.append((pth, a, 4.8, gray, cb)); e = a + 4.8
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

EMPH = [("it made him the richest industrialist", "THE RICHEST", "INDUSTRIALIST"), ("why does a human being have to do", "WHY NOT", "A MACHINE?"),
        ("his first company collapsed", "FAILURE", "NUMBER ONE"), ("he beat the most famous driver", "HE BEAT", "THE BEST"),
        ("a motor car for the great multitude", "A CAR FOR", "THE MULTITUDE"), ("it cost eight hundred and fifty dollars", "$850", "THE MODEL T"),
        ("two hundred and sixty dollars", "$260", "AND FALLING"), ("the company belonged to henry ford alone", "HIS", "ALONE"),
        ("every single hour", "EVERY HOUR", "ONE BOMBER"), ("someone brave enough to tell him", "TELL HIM", "HE IS WRONG"),
        ("the best customer the company can ever have", "THE BEST", "CUSTOMER")]
emph_t = []
for ph_, l1, l2 in EMPH:
    a = find(ph_)
    if a is None or (TLIM and a > TLIM - 4): continue
    a -= 0.05
    if any(abs(a - c) < 4.2 for c in chap_t + card_t) or any(b0_ - 0.5 < a < b0_ + b[2] + 0.5 for b0_, b in zip(BR_T, BR)) or any(p0 - 4.5 < a < p1 + 0.3 for p0, p1 in PHT): continue
    if any(abs(a - x) < 8 for x in emph_t): continue
    emph_t.append(a); e = a + 2.6
    events.append((a - 0.05, e, "Dim", 0, "{\\fad(120,350)\\an7\\pos(0,0)\\1c&H000000&\\1a&H30&\\p1}m 0 0 l 1280 0 1280 720 0 720{\\p0}"))
    events.append((a - 0.03, a + 0.18, "Dim", 4, "{\\an7\\pos(0,0)\\1c&HFFFFFF&\\1a&H60&\\fad(0,170)\\p1}m 0 0 l 1280 0 1280 720 0 720{\\p0}"))
    events.append((a, e, "Emph", 4, "{\\an5\\fad(80,350)\\blur12\\fscx150\\fscy150\\pos(640,300)\\t(0,260,\\blur0\\fscx100\\fscy100)\\t(260,2600,\\fscx106\\fscy106)}%s" % l1))
    events.append((a + 0.12, e, "EmphG", 4, "{\\an5\\fad(80,350)\\blur12\\fscx150\\fscy150\\pos(640,430)\\t(0,260,\\blur0\\fscx100\\fscy100)\\t(260,2600,\\fscx106\\fscy106)}%s" % l2))
    events.append((a + 0.2, e, "Bar", 2, "{\\an7\\fad(120,350)\\pos(590,505)\\p1\\fscx0\\t(0,500,\\fscx100)}m 0 0 l 100 0 100 5 0 5{\\p0}"))

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
Style: Emph,Poppins,118,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,5,4,5,0,0,0,1
Style: EmphG,Poppins,118,%s,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,5,4,5,0,0,0,1
Style: Quote,Lora,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,-1,0,0,100,100,0,0,1,0,3,5,0,0,0,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
""" % (GOLD, GOLD, GOLD)
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
DEF = {0: "tense", 1: "sad", 2: "drive", 3: "wonder", 4: "upbeat", 5: "dark", 6: "drive", 7: "reflect"}
TRG = [("inside one man has just made", "tense"), ("his name is henry ford", "dark"), ("henry ford was born", "wonder"), ("a year later his mother died", "sad"),
       ("then came the failures", "dark"), ("he went racing", "drive"), ("in june nineteen oh-three", "triumph"), ("the model t arrived", "triumph"),
       ("but ford noticed something", "tense"), ("a moving line", "drive"), ("but the line had a hidden cost", "dark"), ("the press called it", "wonder"),
       ("it was neither", "triumph"), ("by the early nineteen twenties", "triumph"), ("but the same man who understood", "dark"),
       ("edsel died in nineteen forty-three", "sad"), ("then the world changed again", "tense"), ("at willow run", "drive"),
       ("only a family intervention", "tense"), ("the young grandson saved", "triumph"), ("henry ford died on april seventh", "sad"),
       ("his story gives two lessons", "reflect"), ("every great builder needs", "triumph")]
TWISTS = ["and the secret behind that decision", "it was neither", "but the same man who understood", "edsel died in nineteen forty-three", "every great builder needs one thing"]
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
    zs = {0: f"1+0.26*{e}", 1: f"1.26-0.26*{e}", 2: "1.24", 3: "1.24", 4: "1.28", 5: "1.28", 6: f"1+0.3*{e}"}[mv]
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
jobs = [j for j in jobs if not (os.path.exists(j[0]) and os.path.getsize(j[0]) > 20000)] if os.environ.get('REUSE') else jobs
with ThreadPoolExecutor(2) as ex: list(ex.map(lambda j: sh(j[1]), jobs))
print("clips ok", len(jobs))
chap_files = []
for ci, ids in sorted(chap_shots.items()):
    outc = f"chap{ci:02d}.mp4"
    if os.environ.get("REUSE") and os.path.exists(outc) and ci < int(os.environ.get("REUSE")): chap_files.append(outc); continue
    ins = " ".join(f"-i clips3/c{n_+1:03d}.mp4" for n_ in ids)
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

# ================= b-roll graficos + fotos + mixagem final =================
def make(name, fn, dur):
    nfr = int(dur * FR); pr = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1920x1080", "-r", str(FR), "-i", "-",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", name], stdin=subprocess.PIPE)
    for i in range(nfr):
        u = i / (nfr - 1); fr = np.asarray(fn(u), np.float32) * min(1, u * 9, (1 - u) * 9)
        pr.stdin.write(np.clip(fr, 0, 255).astype(np.uint8).tobytes())
    pr.stdin.close(); pr.wait()
cut_in = []
for j, (fn, st, dd) in enumerate(BR):
    if not (os.environ.get("REUSE") and os.path.exists(f"broll{j}.mp4") and os.path.getsize(f"broll{j}.mp4") > 1000): make(f"broll{j}.mp4", fn, dd)
    cut_in.append((f"broll{j}.mp4", st, st + dd))
print("b-roll grafico:", [round(c[1], 1) for c in cut_in])

# fotos reais: placas documentais (moldura + fundo desfocado + push lento)
exec(open("plates.py", encoding="utf-8").read().split('if __name__')[0])
for j, (pth, a_, d_, gray_, cb_) in enumerate(PH):
    if os.environ.get("REUSE") and os.path.exists(f"photo{j}.mp4") and os.path.getsize(f"photo{j}.mp4") > 1000:
        cut_in.append((f"photo{j}.mp4", a_, a_ + d_)); continue
    plate(pth, f"plate{j}.png", gray_, cb_)
    nf = int(d_ * FR); u = f"(on/{nf})"; e = f"(3*{u}*{u}-2*{u}*{u}*{u})"
    sh(f"ffmpeg -y -v error -loop 1 -i plate{j}.png -vf \"zoompan=z='1.0+0.10*{e}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={nf}:s=1920x1080:fps={FR},"
       f"eq=contrast=1.05,vignette=PI/3.4,noise=alls=10:allf=t,fade=t=in:st=0:d=0.4,fade=t=out:st={d_-0.4:.2f}:d=0.4,format=yuv420p\" "
       f"-frames:v {nf} -c:v libx264 -preset veryfast -crf 17 photo{j}.mp4")
    cut_in.append((f"photo{j}.mp4", a_, a_ + d_))

GR = "eq=contrast=1.07:saturation=1.0,curves=all='0/0 0.25/0.21 0.75/0.8 1/1',vignette=PI/4.5,noise=alls=4:allf=t"
OUT = "Ford_Video5_Final.mp4" if not TLIM else "test_v4.mp4"
SEG = 150.0; segf = []; t0 = 0.0; k_ = 0
while t0 < TT - 0.01:
    t1 = min(TT, t0 + (SEG if k_ < 6 else 45.0)); dseg = t1 - t0
    with open(f"cap_{k_}.ass", "w", encoding="utf-8") as f:
        f.write(hdr)
        for st, en, sty, lay, tx in events:
            if en <= t0 or st >= t1: continue
            f.write("Dialogue: %d,%s,%s,%s,,0,0,0,,%s\n" % (lay, ts(max(st, t0) - t0), ts(min(en, t1) - t0), sty, tx))
    sel = [(nm, st, en) for nm, st, en in cut_in if en > t0 + 0.05 and st < t1 - 0.05]
    sel.sort(key=lambda x: x[1])
    ins_ = ""
    for nm, st, en in sel:
        ins_ += (f"-itsoffset {st - t0:.2f} -i {nm} " if st >= t0 else f"-ss {t0 - st:.2f} -i {nm} ")
    ch = f"[0:v]{GR}[g0];[g0][1:v]blend=c0_mode=screen:c0_opacity=0.30:c1_mode=normal:c1_opacity=0:c2_mode=normal:c2_opacity=0[b0]"; last = "b0"
    for j, (nm, st, en) in enumerate(sel):
        ch += f";[{last}][{2 + j}:v]overlay=enable='between(t,{max(st - t0, 0):.2f},{en - t0:.2f})':eof_action=pass[b{j + 1}]"; last = f"b{j + 1}"
    ch += f";[{last}]ass=cap_{k_}.ass[v]"
    sg = f"seg{k_:02d}.mp4"
    if os.path.exists(sg) and os.path.getsize(sg) > 100000: segf.append(sg); t0 = t1; k_ += 1; continue
    sh(f"ffmpeg -y -v error -stats -ss {t0:.2f} -t {dseg:.2f} -i base.mp4 -stream_loop -1 -i dust.mp4 {ins_}-filter_complex \"{ch}\" -map '[v]' "
       f"-c:v libx264 -preset veryfast -crf 22 -maxrate 8M -bufsize 16M -pix_fmt yuv420p -t {dseg:.2f} {sg}")
    segf.append(sg); t0 = t1; k_ += 1; print("segmento", k_, flush=True)
open("lists.txt", "w").write("\n".join(f"file '{x}'" for x in segf))
sh("ffmpeg -y -v error -f concat -safe 0 -i lists.txt -c copy video_only.mp4")
sh(f"ffmpeg -y -v error -i narracao.wav -i bed.wav -filter_complex \"[0:a]apad=pad_dur=5,loudnorm=I=-16:TP=-1.5:LRA=9,asplit=2[n][k];"
   f"[1:a]aecho=0.8:0.5:60:0.25[bed];[bed][k]sidechaincompress=threshold=0.03:ratio=5:attack=15:release=350[duck];"
   f"[n][duck]amix=inputs=2:duration=first:normalize=0[a]\" -map '[a]' -c:a aac -b:a 192k -t {TT:.2f} audio_final.m4a")
sh(f"ffmpeg -y -v error -i video_only.mp4 -i audio_final.m4a -c copy -t {TT:.2f} -movflags +faststart {OUT}")
print("FINAL", os.path.getsize(OUT) // 1024, "KB")
open("timeline.txt", "w").write("capitulos: " + " ".join(f"{c:.1f}" for c in chap_t) + "\ncartoes: " + " ".join(f"{c:.1f}" for c in card_t) + "\nbroll: " + " ".join(f"{c[1]:.1f}" for c in cut_in) + "\n")
