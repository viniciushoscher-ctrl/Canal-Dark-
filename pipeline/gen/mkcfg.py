#!/usr/bin/env python3
"""uso: mkcfg.py N 'L1|L2;...(7 titulos 'A,B')' -> cfg/cfgN.py e gfxN.py minimos a partir do roteiro (so midia real via prep_auto)"""
import sys, re
N = sys.argv[1]; titles = [t.split(",") for t in sys.argv[2].split(";")]
R = "/home/claude/canal-dark-"; txt = open(f"{R}/video{N}-narracao/roteiro.txt", encoding="utf-8").read()
secs = re.split(r"### \w+\n", txt)[1:]
U = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
T = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
def year(s):
    w = re.findall(r"[a-z'-]+", s.lower())
    for i in range(len(w) - 1):
        if w[i] in ("seventeen", "eighteen", "nineteen") and i + 1 < len(w):
            a = U[w[i]] * 100; b = w[i + 1]
            if b == "oh" and i + 2 < len(w) and w[i + 2] in U: return a + U[w[i + 2]]
            if b in T: return a + T[b]
            if "-" in b and b.split("-")[0] in T and b.split("-")[1] in U: return a + T[b.split("-")[0]] + U[b.split("-")[1]]
            if b in U and U[b] >= 10: return a + U[b]
    return None
def norm(s, n=5): return " ".join(re.sub(r"[^a-z0-9' -]", "", s.lower()).split()[:n])
KEY = set(); cards = []; trg = []; moods = ["tense", "sad", "drive", "wonder", "triumph", "dark", "reflect", "reflect"]
sents = []
for ci, sec in enumerate(secs):
    ss = [x.strip() for x in re.split(r"(?<=[.!?])\s+", sec.strip().replace("\n", " ")) if x.strip()]
    sents.append(ss)
    if ss: trg.append((norm(ss[0], 6), moods[ci]))
    for x in ss[:]:
        for w in re.findall(r"\b[A-Z][a-z]{3,}\b", x[1:]): KEY.add(w.lower())
        y = year(x)
        if y and len(cards) < 9 and ci > 0 and (not cards or cards[-1][0] != ci):
            ents = re.findall(r"[A-Z][a-z]{3,}(?: [A-Z][a-z]+)*", x[1:]); cards.append((ci, norm(x, 7), str(y), (ents[0] if ents else "THE STORY").upper()[:24], x[:34].rstrip(" ,.")))
CH = [("CHAPTER %d" % (i + 1) if i < 6 else "THE LESSON", t[0].strip(), t[1].strip()) for i, t in enumerate(titles)]
out = "#--KEY\nKEY = %r\n#--CH\nCH = %r\nCARDS = %s\n" % (sorted(KEY)[:50], CH, "[" + ",\n ".join("(%r, %r, %r, %r, None)" % (c[1], c[2], c[3], c[4]) for c in cards) + "]")
out += "#--BRT\nMAPBRT = []\nBRT = []\nAUTO = []\nif os.path.exists(\"autobrt.txt\"):\n    for _l in open(\"autobrt.txt\", encoding=\"utf-8\"):\n        if \"|\" in _l:\n            _p, _f = _l.rstrip(\"\\n\").split(\"|\", 1); AUTO.append((_p, g_foot(_f), 5.0))\nBRT = BRT + AUTO\nBRT = [b for b in BRT if b[1] is not None]\n"
out += "#--PHOTOS\nPHOTOS = []\n#--EMPH\nEMPH = []\n"
out += "#--MUSIC\nDEF = %r\nTRG = %r\nTWISTS = []\n" % ({i: moods[i] for i in range(8)}, trg)
out += "#--NSC\n74\n#--MAP\nMAPBRT = []\n#--KW\n{}\n"
open(f"{R}/pipeline/gen/cfg/cfg{N}.py", "w", encoding="utf-8").write(out)
open(f"{R}/pipeline/gen/cfg/gfx{N}.py", "w", encoding="utf-8").write("# graficos especificos: nenhum\n")
print(N, len(cards), "cartoes", len(KEY), "chaves")
