
# ================= b-roll graficos + fotos + mixagem final =================
def make(name, fn, dur):
    nfr = int(dur * FR); pr = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1920x1080", "-r", str(FR), "-i", "-",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", name], stdin=subprocess.PIPE)
    for i in range(nfr):
        u = i / (nfr - 1); fr = np.asarray(fn(u), np.float32) * min(1, u * 9, (1 - u) * 9)
        pr.stdin.write(np.clip(fr, 0, 255).astype(np.uint8).tobytes())
    pr.stdin.close(); pr.wait()
cut_in = []
for j, (fn, st, dd) in enumerate(BR):
    make(f"broll{j}.mp4", fn, dd); cut_in.append((f"broll{j}.mp4", st, st + dd))
print("b-roll grafico:", [round(c[1], 1) for c in cut_in])

# fotos reais: placas documentais (moldura + fundo desfocado + push lento)
exec(open("plates.py", encoding="utf-8").read().split('if __name__')[0])
for j, (pth, a_, d_, gray_, cb_) in enumerate(PH):
    plate(pth, f"plate{j}.png", gray_, cb_)
    nf = int(d_ * FR); u = f"(on/{nf})"; e = f"(3*{u}*{u}-2*{u}*{u}*{u})"
    sh(f"ffmpeg -y -v error -loop 1 -i plate{j}.png -vf \"zoompan=z='1.0+0.10*{e}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={nf}:s=1920x1080:fps={FR},"
       f"eq=contrast=1.05,vignette=PI/3.4,noise=alls=10:allf=t,fade=t=in:st=0:d=0.4,fade=t=out:st={d_-0.4:.2f}:d=0.4,format=yuv420p\" "
       f"-frames:v {nf} -c:v libx264 -preset veryfast -crf 17 photo{j}.mp4")
    cut_in.append((f"photo{j}.mp4", a_, a_ + d_))

ins = " ".join(f"-itsoffset {st:.2f} -i {nm}" for nm, st, en in cut_in)
chain = ("[0:v]eq=contrast=1.07:saturation=1.0,curves=all='0/0 0.25/0.21 0.75/0.8 1/1',vignette=PI/4.5,noise=alls=4:allf=t[g0];"
         "[g0][3:v]blend=c0_mode=screen:c0_opacity=0.30:c1_mode=normal:c1_opacity=0:c2_mode=normal:c2_opacity=0[b0]"); last = "b0"
for j, (nm, st, en) in enumerate(cut_in):
    chain += f";[{last}][{4+j}:v]overlay=enable='between(t,{st:.2f},{en:.2f})':eof_action=pass[b{j+1}]"; last = f"b{j+1}"
chain += (f";[{last}]ass=captions.ass[v];[1:a]apad=pad_dur=5,loudnorm=I=-16:TP=-1.5:LRA=9,asplit=2[n][k];"
          "[2:a]aecho=0.8:0.5:60:0.25[bed];[bed][k]sidechaincompress=threshold=0.03:ratio=5:attack=15:release=350[duck];"
          "[n][duck]amix=inputs=2:duration=first:normalize=0[a]")
OUT = "Carnegie_Video3_Final.mp4" if not TLIM else "test_v3.mp4"
sh(f"ffmpeg -y -v error -i base.mp4 -i narracao.wav -i bed.wav -stream_loop -1 -i dust.mp4 {ins} -filter_complex \"{chain}\" "
   f"-map '[v]' -map '[a]' -c:v libx264 -preset veryfast -crf 22 -maxrate 8M -bufsize 16M -pix_fmt yuv420p -c:a aac -b:a 192k -t {TT:.2f} {OUT}")
print("FINAL", os.path.getsize(OUT) // 1024, "KB")
open("timeline.txt", "w").write("capitulos: " + " ".join(f"{c:.1f}" for c in chap_t) + "\ncartoes: " + " ".join(f"{c:.1f}" for c in card_t) + "\nbroll: " + " ".join(f"{c[1]:.1f}" for c in cut_in) + "\n")
