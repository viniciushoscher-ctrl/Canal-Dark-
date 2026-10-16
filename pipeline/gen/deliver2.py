#!/usr/bin/env python3
"""uso: deliver2.py N 'titulo1|titulo2|titulo3' 'descricao' -> /mnt/project-files/entregas/videoN (mp4, srt, thumb, titulo_descricao.md com capitulos, REVISAO.md)"""
import sys, re, os, shutil, glob
N, TITLES, DESC = sys.argv[1:4]; R = "/home/claude/canal-dark-"; B = f"/home/claude/video_build{N}"; D = f"/mnt/project-files/entregas/video{N}"; os.makedirs(D, exist_ok=True)
for f in glob.glob(B + "/*_Final.mp4") + glob.glob(B + "/*_English.srt"): shutil.copy(f, D)
shutil.copy(R + f"/video{N}-thumb/Thumbnail_Video{N}.png", D)
tl = open(B + "/timeline.txt").read(); ch = [float(x) for x in re.search(r"capitulos:(.*)", tl).group(1).split()]
cfg = open(R + f"/pipeline/gen/cfg/cfg{N}.py", encoding="utf-8").read(); ns = {}
exec(re.search(r"CH = \[.*?\]\n", cfg, re.S).group(0), ns)
fmt = lambda s: "%d:%02d" % (int(s) // 60, int(s) % 60)
lines = ["0:00 Introduction"] + [f"{fmt(t)} {a.title()} {b.title()}".strip() for t, (_, a, b) in zip(ch, ns["CH"])]
open(D + "/titulo_descricao.md", "w", encoding="utf-8").write("# Titulos (3 opcoes)\n" + "\n".join(f"{i+1}. {t}" for i, t in enumerate(TITLES.split("|"))) + f"\n\n# Descricao\n{DESC}\n\n" + "\n".join(lines) + "\n\nPhotos: Wikimedia Commons / Wikipedia (public domain or CC). Synthetic narration.\n")
pc = open(B + "/plan_counts.txt").read().split()
open(D + "/REVISAO.md", "w", encoding="utf-8").write(f"# Revisao V{N}\n- Sem imagem de IA. Todas as imagens: fotos, gravuras e pinturas de epoca (Commons/Wikipedia) escolhidas a mao, uma por plano, sem repetir (hook de 30 s pode repetir).\n- Imagens por capitulo: {' '.join(pc)}. Zoom out centrado, um zoom por imagem.\n- Duracao: ver mp4. Hook de 30 s em b-roll rapido com imagens do proprio video.\n- Pendente: graficos de numeros e b-roll em video real ainda nao implementados.\n")
print(D)
