#!/usr/bin/env python3
"""uso: python3 prep_auto.py N cfg.py -> video_buildN/bright/NNN_real.jpg (foto da busca da propria frase; senao cartao). So midia publica."""
import sys, os, re, glob, json, subprocess, importlib.util
from PIL import Image, ImageOps, ImageDraw, ImageFont
import numpy as np
N = sys.argv[1]; cfg = open(sys.argv[2], encoding="utf-8").read(); R = "/home/claude/canal-dark-"
dst = f"/home/claude/video_build{N}/bright"; os.makedirs(dst, exist_ok=True)
for f in glob.glob(dst + "/*.jpg"): os.remove(f)
NSC = int(re.search(r"#--NSC\n(\d+)", cfg).group(1))
spec = importlib.util.spec_from_file_location("gq", R + "/pipeline/gen/gen_queries.py")
src = open(R + "/pipeline/gen/gen_queries.py", encoding="utf-8").read(); ns = {"re": re}
exec(src[src.index("U = "):src.index("STOP = ")], ns); yr = ns["yr"]
ns["NOUNS"] = re.search(r"NOUNS = \"(.*?)\"\.split", src).group(1).split()
src2 = open(R + "/pipeline/gen/prepgen.py", encoding="utf-8").read(); ns2 = {}
exec("import numpy as np\nfrom PIL import Image, ImageOps, ImageFilter, ImageStat\n" + src2[src2.index("def fit"):src2.index("for f in sorted(glob.glob(src")], ns2)
fit, bright = ns2["fit"], ns2["bright"]
rot = open(R + f"/video{N}-narracao/roteiro.txt", encoding="utf-8").read()
parts = re.split(r"^### (\S+)\n", rot, flags=re.M)[1:]; names = parts[::2]; txts = parts[1::2]
# frases com o mesmo corte do gen_queries
body = re.sub(r"^### .*$", "", rot, flags=re.M).replace("\n", " ")
allsent = [s.strip() for s in re.split(r"(?<=[.!?])\s+", body) if len(s.strip()) > 20]
def chapter_sents(txt):
    t = txt.replace("\n", " "); return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if len(s.strip()) > 20]
# indice global de cada frase
pos = 0; chs = []
for txt in txts:
    ss = chapter_sents(txt); idx = []
    for s in ss:
        try: k = allsent.index(s, pos)
        except ValueError: k = None
        if k is not None: pos = k + 1
        idx.append(k)
    chs.append(list(zip(idx, ss)))
dur = []
for n in names:
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", R + f"/video{N}-narracao/audio/{n}.mp3"], capture_output=True, text=True).stdout
    dur.append(float(d))
T = sum(dur); PLAN = [max(1, int(round(NSC * x / T))) for x in dur]; PLAN[-1] += NSC - sum(PLAN)
# fotos por frase
by = {}; extra = []
for sub in ("f", "fotos", "people"):
    cj = R + f"/video{N}-commons/{sub}/credits.json"
    if not os.path.exists(cj): continue
    for c in json.load(open(cj)):
        fp = R + "/" + c["file"] if not c["file"].startswith("/") else c["file"]
        if not os.path.exists(fp): continue
        try: Image.open(fp).verify()
        except Exception: continue
        if sub == "f":
            q = c.get("query", "").lower(); ws = re.findall(r"[a-z]{4,}", q)
            if q.split()[0] in ns["NOUNS"] or not ws or not all(w in c.get("title", "").lower() for w in ws): continue
        m = re.search(r"/s(\d{3})_\d+\.jpg$", fp)
        (by.setdefault(int(m.group(1)), []).append(fp) if m and sub == "f" else extra.append((fp, set(re.findall(r"[a-z]{4,}", c.get("title", c.get("file", "")).lower())))))
NOUNS = set(ns["NOUNS"]) if "NOUNS" in ns else set()
VETO = set(open(R + f"/video{N}-imagens/veto.txt").read().split()) if os.path.exists(R + f"/video{N}-imagens/veto.txt") else set()
used = set(VETO); FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"; FI = "/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf"
def plate(year, t1, t2):
    rng = np.random.default_rng(abs(hash(t1)) % 9999); a = np.linspace(30, 12, 720)[:, None] * np.ones((720, 1280)) + rng.normal(0, 3, (720, 1280))
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGB"); d = ImageDraw.Draw(im)
    if year: d.text((640, 300), str(year), font=ImageFont.truetype(FB, 36), fill=(245, 197, 66), anchor="mm"); d.line((590, 330, 690, 330), fill=(245, 197, 66), width=3)
    d.text((640, 385), t1[:26].upper(), font=ImageFont.truetype(FB, 44), fill=(240, 240, 240), anchor="mm")
    d.text((640, 450), t2[:44], font=ImageFont.truetype(FI, 28), fill=(190, 190, 190), anchor="mm"); return im
def pick(k, sent):
    for d in (0, 1, -1, 2, -2):
        for f in by.get(k + d, []) if k is not None else []:
            if f not in used: return f
    w = set(re.findall(r"[a-z]{4,}", sent.lower())); best = None; bs = 0
    for f, tw in extra:
        if f in used: continue
        s = len(w & tw)
        if s > bs: bs, best = s, f
    return best
scene = 0; nf = 0; log = []
for c, (items, P) in enumerate(zip(chs, PLAN)):
    L = sum(len(s) for _, s in items) or 1
    for j in range(P):
        scene += 1; mid = (j + 0.5) / P * L; acc = 0; k, sent = items[-1] if items else (None, "")
        for kk, ss in items:
            acc += len(ss)
            if acc >= mid: k, sent = kk, ss; break
        f = pick(k, sent); y = yr(sent)
        if f: used.add(f); im = fit(ImageOps.autocontrast(Image.open(f).convert("RGB"), cutoff=0.3)); nf += 1; log.append((scene, "foto", os.path.basename(f), sent[:50]))
        else:
            ents = re.findall(r"[A-Z][a-z]{3,}(?: [A-Z][a-z]+)*", sent[1:]); im = plate(y, ents[0] if ents else "THE STORY", sent); log.append((scene, "CARTAO", "", sent[:50]))
        bright(im).save(dst + f"/{scene:03d}_real.jpg", quality=93)
open(f"/home/claude/video_build{N}/auto_log.txt", "w").write("\n".join("%03d %s %s | %s" % x for x in log))
print("cenas", scene, "fotos", nf, "cartoes", scene - nf)
