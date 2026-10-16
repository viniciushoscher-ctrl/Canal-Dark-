#!/usr/bin/env python3
"""uso: autobrt.py N  -> /home/claude/video_buildN/autobrt.txt  (frase-gatilho|clipe) para cenas que seriam cartao; usa so clipes de videoN-imagens/ia_keep.txt"""
import sys, re, os, glob
N = sys.argv[1]; R = "/home/claude/canal-dark-"; B = f"/home/claude/video_build{N}"
clips = []
out, i = [], 0
for l in open(B + "/auto_log.txt", encoding="utf-8"):
    m = re.match(r"(\d+) CARTAO\s*(\S*)\s*\|\s*(.*)", l)
    if not m: continue
    w = re.sub(r"[^a-z0-9' -]", "", m.group(3).lower()).split()[:4]
    if len(w) < 3 or not m.group(2): continue
    cl = [c for c in glob.glob(f"{R}/video{N}-footage-*/clips/{m.group(2)}.mp4")]
    if cl: out.append(" ".join(w) + "|" + cl[0])
open(B + "/autobrt.txt", "w").write("\n".join(out) + "\n"); print(len(out), "gatilhos,", len(clips), "clipes")
