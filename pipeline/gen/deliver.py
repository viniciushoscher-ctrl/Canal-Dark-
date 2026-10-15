#!/usr/bin/env python3
"""uso: deliver.py N Tag 'titulo1|titulo2|titulo3' 'resumo da descricao' -> /mnt/project-files/entregas/videoN"""
import sys, re, os, shutil, glob
N, TAG, TITLES, DESC = sys.argv[1:5]; R = "/home/claude/canal-dark-"; B = f"/home/claude/video_build{N}"; D = f"/mnt/project-files/entregas/video{N}"; os.makedirs(D, exist_ok=True)
for f in (glob.glob(B + "/*_Final.mp4") + glob.glob(B + "/*_English.srt")): shutil.copy(f, D)
shutil.copy(R + f"/video{N}-thumb/Thumbnail_Video{N}.png", D)
tl = open(B + "/timeline.txt").read(); ch = [float(x) for x in re.search(r"capitulos:(.*)", tl).group(1).split()]
cfg = open(R + f"/pipeline/gen/cfg/cfg{N}.py", encoding="utf-8").read(); CH = eval(re.search(r"CH = (\[.*?\])\nQUOTES|CH = (\[.*?\])\n#--", cfg, re.S).group(1) or "[]") if False else None
names = re.findall(r'\("(?:CHAPTER \d|THE LESSON)", "([^"]+)", "([^"]+)"\)', cfg)
fmt = lambda s: "%d:%02d" % (int(s) // 60, int(s) % 60)
lines = ["0:00 Introduction"] + [f"{fmt(t)} {a.title()} {b.title()}".strip() for t, (a, b) in zip(ch, names)]
log = open(B + "/auto_log.txt").read().split("\n") if os.path.exists(B + "/auto_log.txt") else []
cart = [l for l in log if " CARTAO " in l]; fotos = len(log) - len(cart)
open(D + "/titulo_descricao.md", "w", encoding="utf-8").write(f"# Titulos (3 opcoes)\n" + "\n".join(f"{i+1}. {t}" for i, t in enumerate(TITLES.split("|"))) + f"\n\n# Descricao\n{DESC}\n\n" + "\n".join(lines) + "\n\nPhotos: Wikimedia Commons (public domain / CC). Synthetic narration.\n")
open(D + "/REVISAO.md", "w", encoding="utf-8").write(f"# Revisao V{N}\n- Sem imagem de IA: so fotos de Wikimedia Commons escolhidas a mao + cartoes e graficos.\n- Cenas: {len(log)}; com foto: {fotos}; cartao tipografico (sem foto especifica do fato): {len(cart)}.\n- Cartoes sem foto (frase da cena):\n" + "\n".join("  - " + l[:110] for l in cart) + "\n")
print(D, len(log), fotos, len(cart))
