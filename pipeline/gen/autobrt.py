#!/usr/bin/env python3
"""uso: autobrt.py N  -> /home/claude/video_buildN/autobrt.txt  (frase-gatilho|clipe) para cenas que seriam cartao; usa so clipes de videoN-imagens/ia_keep.txt"""
import sys, re, os
N = sys.argv[1]; R = "/home/claude/canal-dark-"; B = f"/home/claude/video_build{N}"
keep = [l.strip() for l in open(f"{R}/video{N}-imagens/ia_keep.txt") if l.strip() and not l.startswith("#")]
clips = [f"{R}/video{N}-footage-ia/clips/{k}.mp4" for k in keep if os.path.exists(f"{R}/video{N}-footage-ia/clips/{k}.mp4")]
out, i = [], 0
for l in open(B + "/auto_log.txt", encoding="utf-8"):
    m = re.match(r"(\d+) CARTAO\s*\|\s*(.*)", l)
    if not m or not clips: continue
    w = re.sub(r"[^a-z0-9' -]", "", m.group(2).lower()).split()[:4]
    if len(w) < 3: continue
    out.append(" ".join(w) + "|" + clips[i % len(clips)]); i += 1
open(B + "/autobrt.txt", "w").write("\n".join(out) + "\n"); print(len(out), "gatilhos,", len(clips), "clipes")
