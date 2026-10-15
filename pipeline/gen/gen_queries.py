#!/usr/bin/env python3
"""uso: gen_queries.py N -> videoN-imagens/commons_f.txt (uma busca especifica por fato do roteiro)"""
import sys, re
N = sys.argv[1]; R = "/home/claude/canal-dark-"
rot = open(R + f"/video{N}-narracao/roteiro.txt", encoding="utf-8").read()
U = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
T = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
def yr(s):
    m = re.search(r"\b(1[89]\d\d|20[0-2]\d)\b", s)
    if m: return int(m.group(1))
    m = re.search(r"\b(nineteen|eighteen|twenty)[ -](oh-\w+|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)(?:[ -](?:one|two|three|four|five|six|seven|eight|nine))?)\b", s.lower())
    if not m: return None
    a = {"nineteen": 1900, "eighteen": 1800, "twenty": 2000}[m.group(1)]; b = m.group(2)
    if b.startswith("oh-"): v = U.index(b[3:]) if b[3:] in U else 0
    else:
        w = re.split(r"[ -]", b); v = T.get(w[0], 0) + (U.index(w[1]) if len(w) > 1 else 0) if w[0] in T else U.index(w[0])
    return a + v
STOP = set("The He His She Her They Their It In On At When Then But And After Before During By For From With That This These Those There Here What Why How Every Everyone Nobody One Two If As So Yet While Until Like Even Just Some Many Most Both Each Later Today Tomorrow Soon Still Also Not No Yes You I We My Your Our Mr Mrs Dr It's He's She's I'm".split())
DROP = set("January February March April May June July August September October November December American British Greek Greeks Turkish Argentinian Argentinians Europe Mediterranean Canadian German Americans British French Japanese Chinese Indian Russian Italian Spanish Jewish English Earth Congress Sunday Monday Friday Saturday Christmas Depression Second First Third Great World War Mr Mrs".split())
NOUNS = "tanker freighter yacht casino airline airplane island wedding funeral hospital shipyard oil refinery store supermarket restaurant factory warehouse truck car train railroad steel bank courthouse newspaper telegraph telephone computer garage rocket laptop software hamburger franchise milkshake cinema studio theater hotel ship port harbor stock exchange".split()
from collections import Counter
C = Counter(re.findall(r"[A-Z][a-z]+ [A-Z][a-z]+", rot)); mm = re.search(r"[Hh]is name is ((?:[A-Z][a-z]+\.? ?){2,3})", rot); SUBJ = mm.group(1).strip() if mm else C.most_common(1)[0][0]
out = []; seen = set()
sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"^### .*$", "", rot, flags=re.M).replace("\n", " ")) if len(s.strip()) > 20]
for i, s in enumerate(sents):
    y = yr(s); ents = []
    for m in re.finditer(r"(?:[A-Z][\w'.-]+)(?:\s+(?:of|de|the|and)?\s*[A-Z][\w'.-]+)*", s):
        e = m.group(0).strip(); w = e.split()
        if " and " in e or (m.start() == 0 and len(w) == 1): continue
        while w and w[0] in STOP: w = w[1:]
        e = re.sub(r"[.,;:!?'\"]+$", "", " ".join(w).replace("'s", ""))
        if e and len(e) > 4 and e not in STOP and e not in DROP and not all(x in DROP or x in STOP for x in e.split()): ents.append(e)
    nouns = [n for n in NOUNS if re.search(r"\b" + n + r"s?\b", s.lower())]
    qs = []
    for e in ents[:2]: qs.append(e + (" " + str(y) if y and len(e.split()) == 1 and False else ""))
    for n in nouns[:2]: qs.append(n + (" " + str(y // 10 * 10) + "s" if y else ""))
    if y: qs.append(f"{SUBJ} {y // 10 * 10}s" if (y // 10 * 10) != 2000 else SUBJ)
    for q in qs:
        if q.lower() in seen: continue
        seen.add(q.lower()); out.append(f"s{i:03d}|{q}")
open(R + f"/video{N}-imagens/commons_f.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(N, len(sents), "frases", len(out), "buscas")
