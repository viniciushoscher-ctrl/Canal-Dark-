#!/usr/bin/env python3
"""uso: python3 mkgen.py N Tag cfg.py gfx.py  -> gera /home/claude/video_buildN/build_vN.py + part3 files"""
import sys, os, re
N, TAG, CFG, GFX = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
H = os.path.dirname(os.path.abspath(__file__)); B = f"/home/claude/video_build{N}"; os.makedirs(B, exist_ok=True)
t = open(H + "/template_build.py", encoding="utf-8").read()
t = t.replace("video_build6", f"video_build{N}").replace("video6-", f"video{N}-").replace("Gould_Video6", f"{TAG}_Video{N}").replace("part3_gould.py", f"part3_v{N}.py")
cfg = open(CFG, encoding="utf-8").read(); sec = {}
for m in re.finditer(r"#--(\w+)\n(.*?)(?=#--\w+\n|\Z)", cfg, re.S): sec[m.group(1)] = m.group(2)
def blk(a, b, new):
    global t
    i = t.index(a); j = t.index(b, i); t = t[:i] + new + t[j:]
blk("KEY = {", "def is_key", sec["KEY"])
blk("CH = [", "QUOTES = []", sec["CH"])
blk("def FFg", "BR = []", sec["BRT"].replace("video%N", f"video{N}"))
blk("PHOTOS = [", "PH = []", sec["PHOTOS"])
blk("EMPH = [", "emph_t = []", sec["EMPH"])
blk("DEF = {", "segs = [(chap_start", sec["MUSIC"])
t = t.replace("TRACK_N = 6", f"TRACK_N = {N}")
t = re.sub(r"NSC = \d+", "NSC = " + sec["NSC"].strip(), t)
open(f"{B}/build_v{N}.py", "w", encoding="utf-8").write(t)
com = open(H + "/part3_common.tpl", encoding="utf-8").read().replace("%(N)s", N)
open(f"{B}/part3_v{N}.py", "w", encoding="utf-8").write(open(GFX, encoding="utf-8").read() + "\n" + com + "\n" + sec.get("MAP", ""))
for f in ["part3_graphics.py", "plates.py", "dust.mp4"]:
    src = "/home/claude/video_build6/" + f
    if not os.path.exists(f"{B}/{f}"): os.system(f"cp {src} {B}/{f}")
print("ok", B)
