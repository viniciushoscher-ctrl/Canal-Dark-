#!/usr/bin/env python3
"""Video 3 Carnegie - mesma edicao em camadas do video 1, com tempos de palavra EXATOS (edge-tts)."""
import re, subprocess, glob, math, wave, os, sys, json, textwrap
import numpy as np

R = "/home/claude/canal-dark-"
B = "/home/claude/video_build3"
AUD = R + "/video3-narracao/audio"
IMG = sorted(glob.glob(os.environ.get("V3IMG", R + "/video3-imagens/imagens") + "/*.jpg"))
NAMES = ["00_hook","01_cap1","02_cap2","03_cap3","04_cap4","05_cap5","06_cap6","07_cap7","08_cap8","09_lesson"]
PLAN = [5,6,6,6,8,8,8,8,10,3]
TLIM = float(os.environ.get("TLIM", "0")) or None
FR = 25
os.chdir(B)
sh = lambda c: subprocess.run(c, shell=True, check=True, capture_output=True, text=True)
dur = lambda f: float(sh(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {f}").stdout)

off = []; t0 = 0.0
for n in NAMES:
    sh(f"ffmpeg -y -v error -i {AUD}/{n}.mp3 -ar 44100 -ac 1 w_{n}.wav")
    off.append(t0); t0 += dur(f"w_{n}.wav")
T = t0
open("wl.txt", "w").write("\n".join(f"file 'w_{n}.wav'" for n in NAMES))
sh("ffmpeg -y -v error -f concat -safe 0 -i wl.txt -c copy narracao.wav")
print("duracao", round(T, 1), "min", round(T / 60, 2))

rot = open(R + "/video3-narracao/roteiro.txt", encoding="utf-8").read()
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

