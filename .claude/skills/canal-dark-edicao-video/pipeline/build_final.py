#!/usr/bin/env python3
"""Video 1 Rockefeller - edicao em camadas: imagens com movimento + legendas animadas (ASS)
+ cartoes de dados + titulos de capitulo + trilha/SFX sintetizados. Tudo local (ffmpeg + numpy)."""
import re, subprocess, glob, math, wave, os, sys
import numpy as np

B = "/home/claude/video_build"
IMG = sorted(glob.glob("/home/claude/canal-dark-/video1-imagens/imagens/*.jpg"))
P1, P2 = "/home/claude/Rockefeller_Video1_Narration_Part1.mp3", "/home/claude/Rockefeller_Video1_Narration_Part2.mp3"
TXT = open("/home/claude/Rockefeller_Video1_Narration_Clean.txt", encoding="utf-8").read()
FR = 25
os.chdir(B)
sh = lambda c: subprocess.run(c, shell=True, check=True, capture_output=True, text=True)

# ---------- 1. narracao + pausas ----------
dur = lambda f: float(sh(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {f}").stdout)
D1, D2 = dur(P1), dur(P2); T = D1 + D2
sh(f"ffmpeg -y -v error -i {P1} -i {P2} -filter_complex '[0:a][1:a]concat=n=2:v=0:a=1' narracao.wav")
log = subprocess.run("ffmpeg -hide_banner -i narracao.wav -af silencedetect=noise=-32dB:d=0.22 -f null -",
                     shell=True, capture_output=True, text=True).stderr
ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
SIL = [(a + b) / 2 for a, b in zip(ss, se)]
print("duracao", round(T, 1), "pausas", len(SIL))

# ---------- 2. frases ----------
t = TXT.replace("U.S.", "U§S§").replace("D. Rockefeller", "D§ Rockefeller")
sents = []
for para in re.split(r"\n\s*\n", t):
    para = " ".join(para.split())
    if not para: continue
    for s in re.split(r'(?<=[.!?]["”])\s+|(?<=[.!?])\s+', para):
        s = s.replace("§", ".").strip()
        if s: sents.append(s)
n = len(sents)
chars = [len(s) + 1 for s in sents]
cum = np.cumsum(chars); L = cum[-1]
cut = min(4900, L - 1)  # parte 1 = primeiros 4900 caracteres
def pred(c):  # caracteres -> segundos (linear por parte)
    return D1 * c / cut if c <= cut else D1 + D2 * (c - cut) / (L - cut)
E = []  # fim de cada frase
prev = 0.0
for i in range(n):
    p = pred(cum[i])
    if i == n - 1: E.append(T); break
    c = [x for x in SIL if abs(x - p) <= 1.3 and x > prev + 0.9]
    e = min(c, key=lambda x: abs(x - p)) if c else max(p, prev + 0.9)
    E.append(e); prev = e
S0 = [0.0] + E[:-1]
print("frases", n)
K = len(IMG)
bounds = [0.0]
for k in range(1, K):
    target = k * T / K
    c = [x for x in E[:-1] if x > bounds[-1] + 4.0]
    bounds.append(min(c, key=lambda x: abs(x - target)) if c else target)
bounds.append(T)
SHOTS = []  # (indice_img, tipo, inicio, fim)
for k in range(K):
    a_, b_ = bounds[k], bounds[k + 1]
    c_ = [x for x in E if a_ + 3.2 < x < b_ - 3.2]
    if b_ - a_ >= 7 and c_:
        m_ = min(c_, key=lambda x: abs(x - (a_ + b_) / 2))
        SHOTS += [(k, "wide", a_, m_), (k, "tight", m_, b_)]
    else:
        SHOTS.append((k, "wide", a_, b_))
print("planos", len(SHOTS))

# ---------- 3. legendas (ASS) ----------
def ts(x):
    x = max(x, 0); h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"
GOLD, WHITE = "&H0042C5F5&", "&H00FFFFFF&"
KEY = {"billionaire", "billion", "million", "percent", "monopoly", "government", "richer", "supreme", "court",
       "twist", "massacre", "control", "empire", "refining", "system", "ninety", "twenty-two", "thirty-four",
       "rockefeller", "tarbell", "destroy", "cash", "bankruptcy", "chaos", "genius", "philanthropy", "fivefold",
       "dimes", "foundation", "architecture", "indicted"}
def is_key(w):
    k = re.sub(r"[^\w-]", "", w.lower())
    return any(ch.isdigit() for ch in k) or k in KEY
events = []
for i, s in enumerate(sents):
    words = s.split()
    wl = np.array([len(w) + 1.5 for w in words], float)
    a, b = S0[i], E[i] - 0.05
    edges = a + (b - a) * np.concatenate([[0], np.cumsum(wl) / wl.sum()])
    groups, cur = [], []
    for j, w in enumerate(words):
        cur.append(j)
        end = re.search(r"[,.;:!?—]$|—$", w) is not None
        if len(cur) >= 3 or end or sum(len(words[x]) for x in cur) > 17:
            groups.append(cur); cur = []
    if cur: groups.append(cur)
    for gi, g in enumerate(groups):
        st = edges[g[0]]
        en = edges[groups[gi + 1][0]] if gi + 1 < len(groups) else b + 0.05
        txt = " ".join(
            ("{\\c%s}%s{\\c%s}" % (GOLD, words[j].upper(), WHITE)) if is_key(words[j]) else words[j].upper()
            for j in g)
        txt = "{\\fscx88\\fscy88\\t(0,110,\\fscx106\\fscy106)\\t(110,200,\\fscx100\\fscy100)\\fad(40,50)}" + txt
        events.append((st, en, "Cap", 5, txt))

# ---------- 4. cartoes e titulos ----------
def find(sub):
    for i, s in enumerate(sents):
        if sub in s: return i
    print("!! nao achei:", sub); return None
CH = [("Rockefeller was born in 1839", "CHAPTER 1", "THE BOY WHO", "TRACKED EVERY PENNY"),
      ("By his early twenties", "CHAPTER 2", "THE OIL RUSH NOBODY", "WAS ORGANIZING"),
      ("What happened next earned", "CHAPTER 3", "THE CLEVELAND", "MASSACRE"),
      ("Power at that scale", "CHAPTER 4", "THE MOST HATED", "MAN IN AMERICA"),
      ("Here's the twist", "CHAPTER 5", "THE BREAKUP THAT", "MADE HIM RICHER"),
      ("What Rockefeller did next", "CHAPTER 6", "THE SECOND EMPIRE:", "GIVING IT ALL AWAY"),
      ("In his final decades", "CHAPTER 7", "THE FINAL", "YEARS"),
      ("real genius was never oil", "THE LESSON", "THE REAL", "GENIUS")]
CARDS = [("became the first billionaire", "1916", "FIRST BILLIONAIRE", "in human history", None),
         ("ninety percent of all the oil", "AT HIS PEAK", "90%", "of all U.S. oil refined", 90),
         ("This is the story of John D", "THE STORY OF", "JOHN D. ROCKEFELLER", "the man who chased the system", None),
         ("Rockefeller was born in 1839", "1839", "ROCKEFELLER IS BORN", "rural New York", None),
         ("By sixteen", "AGE 16", "FIRST JOB", "assistant bookkeeper, Cleveland", None),
         ("built a refinery in Cleveland in 1863", "1863", "FIRST REFINERY", "Cleveland, Ohio", None),
         ("In 1870, he folded", "1870", "STANDARD OIL IS BORN", "partnerships folded into one", None),
                  ("Pennsylvania indicted", "1879", "FIRST INDICTMENT", "for monopolizing the oil trade", None),
         ("Then came the writer", "THE JOURNALIST", "IDA TARBELL", "her series defined his legacy", None),
                  ("held over 25%", "OWNERSHIP", "25%+ OF THE STOCK", "carried into all 34 companies", 25),
                  ("80 million dollars to build", "PHILANTHROPY", "$80 MILLION", "University of Chicago", None),
         ("530 million dollars", "GIVEN AWAY", "$530 MILLION", "over his lifetime", None),
         ("He died in 1937", "1937", "DIES AT 97", "five weeks short of 98", None)]
chap_t = []
for sub, k, l1, l2 in CH:
    i = find(sub)
    if i is None: continue
    a = S0[i] + 0.15; chap_t.append(a); e = a + 3.4
    events.append((a, e, "Dim", 0, "{\\fad(250,500)\\an7\\pos(0,0)\\1c&H000000&\\1a&H50&\\p1}m 0 0 l 1280 0 1280 720 0 720{\\p0}"))
    events.append((a, e, "Kick", 3, "{\\an7\\fad(250,400)\\move(70,236,90,236,0,600)}%s" % k))
    events.append((a, e, "Bar", 2, "{\\an7\\fad(250,400)\\pos(90,284)\\p1\\fscx0\\t(0,700,\\fscx100)}m 0 0 l 90 0 90 5 0 5{\\p0}"))
    events.append((a, e, "Big", 3, "{\\an7\\fad(250,400)\\move(60,300,90,300,0,600)}%s" % l1))
    events.append((a, e, "Big", 3, "{\\an7\\fad(250,400)\\move(60,388,90,388,100,700)}%s" % l2))
card_t = []; last_end = 0.0
for sub, lab, big, sub2, bar in CARDS:
    i = find(sub)
    if i is None: continue
    a = S0[i] + 0.25
    if any(abs(a - c) < 3.6 for c in chap_t): a = max(c for c in chap_t if abs(a - c) < 3.6) + 3.6
    if a < last_end + 0.2: continue
    e = a + min(max(E[i] - a, 3.2), 5.2); last_end = e; card_t.append(a)
    w = max(260, int(len(big) * 37 + 90))
    events.append((a, e, "Dim", 1, "{\\an7\\fad(180,300)\\move(-%d,56,40,56,0,380)\\1c&H0E0B09&\\1a&H38&\\p1}m 0 0 l %d 0 %d 158 0 158{\\p0}" % (w, w, w)))
    events.append((a, e, "Dim", 2, "{\\an7\\fad(180,300)\\move(-%d,56,40,56,0,380)\\1c%s\\p1}m 0 0 l 6 0 6 158 0 158{\\p0}" % (w, GOLD)))
    events.append((a, e, "Kick", 3, "{\\an7\\fad(180,300)\\move(%d,68,60,68,0,380)}%s" % (-w + 20, lab)))
    events.append((a, e, "Cardbig", 3, "{\\an7\\fad(180,300)\\move(%d,98,60,98,40,420)}%s" % (-w + 20, big)))
    events.append((a, e, "Sub", 3, "{\\an7\\fad(180,300)\\move(%d,164,60,164,80,460)}%s" % (-w + 20, sub2)))
    if bar:
        events.append((a, e, "Dim", 2, "{\\an7\\fad(180,300)\\pos(40,228)\\1c&H3A3530&\\1a&H20&\\p1}m 0 0 l %d 0 %d 12 0 12{\\p0}" % (w, w)))
        events.append((a, e, "Dim", 3, "{\\an7\\fad(180,300)\\pos(40,228)\\1c%s\\p1\\fscx0\\t(250,1300,\\fscx%d)}m 0 0 l %d 0 %d 12 0 12{\\p0}" % (GOLD, bar, w, w)))
for sh_ in SHOTS[1:]:  # flash de luz em cada corte (mais forte quando troca a imagem)
    b0 = sh_[2]; major = sh_[1] == "wide"
    events.append((b0 - 0.03, b0 + (0.20 if major else 0.12), "Dim", 0, "{\\an7\\pos(0,0)\\1c&HFFFFFF&\\1a&H%s&\\fad(0,%d)\\p1}m 0 0 l 1280 0 1280 720 0 720{\\p0}" % ("78" if major else "B0", 200 if major else 120)))
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

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
""" % (GOLD, GOLD)
with open("captions.ass", "w", encoding="utf-8") as f:
    f.write(hdr)
    for st, en, sty, lay, tx in events:
        f.write("Dialogue: %d,%s,%s,%s,,0,0,0,,%s\n" % (lay, ts(st), ts(en), sty, tx))
print("eventos", len(events), "capitulos", len(chap_t), "cartoes", len(card_t))

# ---------- 5. trilha + SFX ----------
SR = 44100; N = int(T * SR); tt = np.arange(N) / SR
def ss_(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
def pad(ts, notes, bright=0.0):
    y = 0
    for f in notes:
        y = y + np.sin(2*np.pi*f*ts) + np.sin(2*np.pi*f*1.004*ts + 1) * 0.6 + bright * 0.4 * np.sin(2*np.pi*2*f*ts)
    return y * (0.75 + 0.25 * np.sin(2*np.pi*ts/13))
def arp(ts, notes, bpm):
    st = ts * bpm / 60 * 2; i = st.astype(int) % len(notes); ph = st % 1
    return np.sin(2*np.pi*np.array(notes)[i]*ts) * np.exp(-ph*5)
def pulse(ts, bpm, f):
    ph = (ts * bpm / 60) % 1
    return np.sin(2*np.pi*f*ph*60/bpm) * np.exp(-ph*9)
# (pad notas, brilho, arpejo (notas,bpm) ou None, pulso (bpm,f) ou None, peso arpejo, peso pulso)
SC = [([55, 82.41, 110], 0, None, (50, 48), 0, 1.6),                                  # abertura: batida de coracao
      ([110, 130.81, 164.81], 0.2, ([220, 261.63, 329.63, 261.63], 40), None, 0.5, 0),     # cap 1: infancia, intimista
      ([98, 116.54, 146.83], 0.3, ([196, 233.08, 293.66, 392], 60), None, 0.6, 0),         # cap 2: corrida do petroleo, crescendo
      ([55, 77.78, 110], 0, None, (70, 45), 0, 2.2),                                       # cap 3: massacre, batida sombria
      ([73.42, 87.31, 110], 0.4, ([293.66, 349.23, 440, 349.23], 84), (84, 40), 0.5, 0.8), # cap 4: homem mais odiado, tenso
      ([130.81, 164.81, 196, 261.63], 1.0, ([523.25, 659.25, 783.99, 659.25], 96), None, 0.9, 0),  # cap 5: virada, acordes maiores
      ([87.31, 130.81, 174.61, 220], 0.7, ([349.23, 440, 523.25, 440], 50), None, 0.6, 0), # cap 6: filantropia, caloroso
      ([110, 130.81, 164.81, 196], 0.3, ([329.63, 392, 329.63, 261.63], 36), None, 0.5, 0), # cap 7: anos finais, sereno
      ([55, 82.41, 110, 164.81], 0.2, None, (45, 48), 0, 0.7)]                             # fechamento: reflexivo
edges = [0.0] + list(chap_t) + [T]
music = np.zeros(N, np.float32)
for k, (notes, br, ar, pu, wa, wp) in enumerate(SC):
    a0, b0 = edges[k], edges[k + 1]
    i0, i1 = int(max(0, a0 - 2.5) * SR), int(min(T, b0 + 2.5) * SR)
    ts = tt[i0:i1]
    y = pad(ts, notes, br) / (len(notes) * 1.6)
    if ar: y = y + wa * 0.5 * arp(ts, *ar)
    if pu: y = y + wp * 0.45 * pulse(ts, *pu)
    y = y / (np.sqrt(np.mean(y ** 2)) + 1e-9) * 0.012
    wgt = ss_((ts - (a0 - 1.5)) / 3.0) if k > 0 else 1.0
    if k < len(SC) - 1: wgt = wgt * (1 - ss_((ts - (b0 - 1.5)) / 3.0))
    music[i0:i1] += (y * wgt).astype(np.float32)
music *= np.clip(tt / 3, 0, 1) * np.clip((T - tt) / 4, 0, 1)
L = music.astype(np.float64); R = np.roll(L, 40)
rng = np.random.default_rng(3)
def add(sig, t0, amp):
    i0 = int(t0 * SR); i1 = min(N, i0 + len(sig))
    if i0 < N:
        L[i0:i1] += sig[:i1 - i0] * amp; R[i0:i1] += sig[:i1 - i0] * amp
def whoosh():
    m = int(0.55 * SR); x = rng.standard_normal(m); x = x[1:] - x[:-1]; x = np.append(x, 0)
    return x * np.sin(np.pi * np.linspace(0, 1, m)) ** 2
def impact():
    m = int(1.0 * SR); q = np.arange(m) / SR
    return (np.sin(2 * np.pi * 52 * q) * np.exp(-q * 5) + 0.5 * np.sin(2 * np.pi * 104 * q) * np.exp(-q * 9)
            + 0.15 * rng.standard_normal(m) * np.exp(-q * 14))
def thump():
    m = int(0.3 * SR); q = np.arange(m) / SR
    return np.sin(2 * np.pi * 68 * q) * np.exp(-q * 16) + 0.1 * rng.standard_normal(m) * np.exp(-q * 40)
for sh_ in SHOTS[1:]:  # som em cada corte
    major = sh_[1] == "wide"
    add(whoosh()[:int(0.3 * SR)], max(0, sh_[2] - 0.2), 0.05 if major else 0.03); add(thump(), sh_[2], 0.11 if major else 0.06)
for c in chap_t: add(impact(), c, 0.22); add(whoosh(), max(0, c - 0.3), 0.07)
for c in card_t: add(whoosh(), max(0, c - 0.05), 0.05)
pcm = (np.clip(np.stack([L, R], 1), -0.98, 0.98) * 32767).astype("<i2")
with wave.open("bed.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

# ---------- 6. planos (largo + fechado) ----------
os.makedirs("clips2", exist_ok=True)
REG = [(0.02, 0.02), (0.30, 0.02), (0.02, 0.30), (0.30, 0.30), (0.16, 0.16)]
lst = []
for n_, (k, typ, a_, b_) in enumerate(SHOTS):
    d = b_ - a_; nf = max(int(round(d * FR)), 2); out = f"clips2/c{n_+1:03d}.mp4"
    if typ == "wide":
        v = k % 4
        z = {0: f"1+0.14*on/{nf}", 1: f"1.14-0.14*on/{nf}", 2: f"1+0.12*on/{nf}", 3: f"1+0.12*on/{nf}"}[v]
        x = {0: "iw/2-(iw/zoom/2)", 1: "iw/2-(iw/zoom/2)", 2: f"(iw-iw/zoom)*(1-on/{nf})", 3: f"(iw-iw/zoom)*(on/{nf})"}[v]
        pre = "crop=iw*0.94:ih*0.94:0:0"
    else:
        rx, ry = REG[k % 5]
        z = f"1.0+0.10*on/{nf}" if k % 2 == 0 else f"1.10-0.10*on/{nf}"; x = "iw/2-(iw/zoom/2)"
        pre = f"crop=iw*0.62:ih*0.62:iw*{rx}:ih*{ry}"
    vf = (f"{pre},scale=2000:1125,zoompan=z='{z}':x='{x}':y='ih/2-(ih/zoom/2)':d={nf}:s=1280x720:fps={FR},"
          f"fade=t=in:st=0:d=0.12,fade=t=out:st={max(d-0.12,0):.3f}:d=0.12,format=yuv420p")
    sh(f"ffmpeg -y -v error -loop 1 -i '{IMG[k]}' -vf \"{vf}\" -frames:v {nf} -c:v libx264 -preset veryfast -crf 19 {out}")
    lst.append(f"file '{out}'")
open("list2.txt", "w").write("\n".join(lst))
sh("ffmpeg -y -v error -f concat -safe 0 -i list2.txt -c copy base.mp4")
print("base ok", len(SHOTS), "planos")

# ---------- 6b. b-roll: graficos animados em tela cheia ----------
from PIL import Image, ImageDraw, ImageFont
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"; FI = "/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf"
fnt = lambda sz, f=FB: ImageFont.truetype(f, sz)
GOLDc = (245, 197, 66); W_ = (245, 245, 245); BG = (11, 11, 15)
ease = lambda u: u * u * (3 - 2 * u)
def base(kick, big=None, sub=None):
    im = Image.new("RGB", (1280, 720), BG); d = ImageDraw.Draw(im)
    for gx in range(0, 1280, 80): d.line([(gx, 0), (gx, 720)], fill=(20, 20, 26), width=1)
    for gy in range(0, 720, 80): d.line([(0, gy), (1280, gy)], fill=(20, 20, 26), width=1)
    d.text((90, 70), kick, font=fnt(26), fill=GOLDc); d.rectangle([90, 112, 180, 117], fill=GOLDc)
    if big: d.text((90, 132), big, font=fnt(60), fill=W_)
    if sub: d.text((90, 214), sub, font=fnt(30, FI), fill=(200, 200, 200))
    return im, d
def f_oil(u):
    im, d = base("THE CIVIL WAR OIL RUSH", "PRICE PER BARREL", "swung from 35 cents to nearly 14 dollars")
    x0, x1, y0, y1 = 140, 1140, 540, 290
    d.line([(x0, y0), (x1, y0)], fill=(70, 70, 80), width=3); d.line([(x0, y0), (x0, y1 - 20)], fill=(70, 70, 80), width=3)
    pts = []
    for i in range(int(200 * ease(min(u * 1.15, 1))) + 1):
        t = i / 200; v = 0.04 + 0.88 * t ** 2.4 + 0.08 * math.sin(16 * t) * t
        pts.append((x0 + (x1 - x0) * t, y0 - (y0 - y1) * v))
    if len(pts) > 1: d.line(pts, fill=GOLDc, width=7, joint="curve")
    if pts: px, py = pts[-1]; d.ellipse([px - 11, py - 11, px + 11, py + 11], fill=W_)
    d.text((x0 + 10, y0 - 70), "35¢", font=fnt(46), fill=W_)
    if u > 0.8: d.text((x1 - 150, y1 - 60), "$14", font=fnt(60), fill=GOLDc)
    return im
def f_split(u):
    im, d = base("1911 · SUPREME COURT RULING", "ONE EMPIRE. 34 PIECES.")
    cols, rows = 7, 5; cx, cy = 640, 400
    e = ease(np.clip((u - 0.3) / 0.45, 0, 1))
    for i in range(34):
        r_, c_ = divmod(i, cols)
        gx, gy = 340 + c_ * 100, 270 + r_ * 62
        sx, sy = cx - 150 + (c_ / cols) * 300, cy - 150 + (r_ / rows) * 300
        x, y = sx + (gx - sx) * e, sy + (gy - sy) * e; sz = 300 / 7 - 2 + (-12 * e)
        col = (int(180 + 65 * (i / 34)), int(140 + 57 * (i / 34)), int(40 + 26 * (i / 34)))
        d.rounded_rectangle([x, y, x + sz, y + sz], radius=4, fill=col)
    if u < 0.3: d.text((540, 540), "STANDARD OIL", font=fnt(34), fill=W_)
    elif u > 0.75: d.text((985, 400), "1 TO 34", font=fnt(54), fill=GOLDc)
    return im
def f_rivals(u):
    im, d = base("1872 · THE CLEVELAND MASSACRE", "RIVALS ABSORBED")
    n_abs = int(22 * ease(np.clip((u - 0.25) / 0.6, 0, 1)))
    for i in range(26):
        c_, r_ = i % 13, i // 13; x, y = 180 + c_ * 78, 290 + r_ * 100
        gone = i < n_abs
        col = (45, 45, 52) if gone else (W_ if i >= 22 else (200, 160, 60))
        d.ellipse([x, y, x + 56, y + 56], fill=col)
        if gone: d.line([(x + 14, y + 14), (x + 42, y + 42)], fill=(90, 90, 100), width=4); d.line([(x + 42, y + 14), (x + 14, y + 42)], fill=(90, 90, 100), width=4)
    d.text((90, 500), "%d" % n_abs, font=fnt(90), fill=GOLDc); d.text((230, 532), "of 26 absorbed", font=fnt(34, FI), fill=(210, 210, 210))
    return im
def f_wealth(u):
    im, d = base("THE FIRST BILLIONAIRE", "FORTUNE", "1913 to 1916")
    base_y = 548
    for (x, h, lab, val, yr) in [(380, 0.45, "$900M", 900, "1913"), (760, 1.0, "$1B+", 1000, "1916")]:
        hh = 250 * h * ease(np.clip((u - 0.1) / 0.6, 0, 1)); d.rectangle([x, base_y - hh, x + 200, base_y], fill=GOLDc if h == 1.0 else (150, 120, 45))
        d.text((x + 10, base_y + 4), yr, font=fnt(34), fill=W_)
        if hh > 60: d.text((x + 8, base_y - hh - 64), lab, font=fnt(48), fill=W_)
    return im
def make(name, fn, dur=4.2):
    nfr = int(dur * FR); pr = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1280x720", "-r", str(FR), "-i", "-",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", name], stdin=subprocess.PIPE)
    for i in range(nfr):
        u = i / (nfr - 1); fr = np.asarray(fn(u), np.float32) * min(1, u * 9, (1 - u) * 9)
        pr.stdin.write(np.clip(fr, 0, 255).astype(np.uint8).tobytes())
    pr.stdin.close(); pr.wait()
CUT = [("35 cents", f_oil), ("twenty-two of its twenty-six", f_rivals), ("34 separate companies", f_split), ("900 million dollars", f_wealth)]
cut_in = []
for j, (sub, fn) in enumerate(CUT):
    i = find(sub)
    if i is None: continue
    st = S0[i] + 0.7
    if any(abs(st - c) < 4 for c in chap_t): st += 3.8
    make(f"broll{j}.mp4", fn); cut_in.append((f"broll{j}.mp4", st, st + 4.2))
print("b-roll grafico:", [round(c[1], 1) for c in cut_in])

# ---------- 7. final: vinheta + granulado + b-roll + camadas + audio ----------
ins = " ".join(f"-itsoffset {st:.2f} -i {nm}" for nm, st, en in cut_in)
chain = "[0:v]vignette=PI/5,noise=alls=3:allf=t[b0]"; last = "b0"
for j, (nm, st, en) in enumerate(cut_in):
    chain += f";[{last}][{3+j}:v]overlay=enable='between(t,{st:.2f},{en:.2f})':eof_action=pass[b{j+1}]"; last = f"b{j+1}"
chain += f";[{last}]ass=captions.ass[v];[1:a]apad=pad_dur=5,loudnorm=I=-16:TP=-1.5:LRA=9[n];[n][2:a]amix=inputs=2:duration=first:normalize=0[a]"
sh(f"ffmpeg -y -v error -i base.mp4 -i narracao.wav -i bed.wav {ins} -filter_complex \"{chain}\" "
   f"-map '[v]' -map '[a]' -c:v libx264 -preset veryfast -crf 25 -pix_fmt yuv420p -c:a aac -b:a 192k -t {T:.2f} Rockefeller_Video1_Final.mp4")
print("FINAL", os.path.getsize("Rockefeller_Video1_Final.mp4") // 1024, "KB")
with open("timeline.txt", "w") as f:
    f.write("capitulos: " + " ".join(f"{c:.1f}" for c in chap_t) + "\ncartoes: " + " ".join(f"{c:.1f}" for c in card_t) + "\nbroll: " + " ".join(f"{c[1]:.1f}" for c in cut_in) + "\n")
