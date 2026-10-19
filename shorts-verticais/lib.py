import re,subprocess,sys,os
M="/mnt/project-files/entregas/"
def ts(s):
    h,m,r=s.split(":");sec,ms=r.split(",");return int(h)*3600+int(m)*60+int(sec)+int(ms)/1000
def cues(f):
    out=[]
    for b in open(f).read().strip().split("\n\n"):
        l=b.split("\n");a,b2=l[1].split(" --> ");out.append((ts(a),ts(b2)," ".join(l[2:])))
    return out
def ass_t(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60;return f"{h}:{m:02d}:{s:05.2f}"
def make(n,vid,srt,a,b,hook,cta="FULL STORY ON THE CHANNEL"):
    cs=[c for c in cues(M+srt) if c[1]>a and c[0]<b]
    a=cs[0][0]-0.05 if cs[0][0]>a else a
    a=max(a,0); b=cs[-1][1]+0.25; dur=b-a
    ev=[]
    for s,e,tx in cs:
        w=re.sub(r"[^\w'’%$,.?!-]"," ",tx).upper().split()
        # chunks of 3 words
        ch=[" ".join(w[i:i+3]) for i in range(0,len(w),3)]
        d=(e-s)/len(ch)
        for i,c in enumerate(ch):
            st=max(s-a,0)+i*d;en=max(s-a,0)+(i+1)*d
            ev.append(f"Dialogue: 0,{ass_t(st)},{ass_t(en)},Cap,,0,0,0,,{c}")
    ev.append(f"Dialogue: 1,{ass_t(0)},{ass_t(dur+2.6)},Hook,,0,0,0,,{hook}")
    ev.append(f"Dialogue: 1,{ass_t(dur)},{ass_t(dur+2.6)},Cta,,0,0,0,,{cta}\\N▶ LINK IN DESCRIPTION")
    hdr="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Inter,104,&H0000E0FF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,9,3,2,40,40,560,1
Style: Hook,Inter,84,&H00FFFFFF,&H000000FF,&H00000000,&HAA000000,-1,0,0,0,100,100,0,0,3,14,0,8,50,50,300,1
Style: Cta,Inter,84,&H0000E0FF,&H000000FF,&H00000000,&HAA000000,-1,0,0,0,100,100,0,0,3,14,0,2,50,50,520,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
    open(f"/tmp/w/{n}.ass","w").write(hdr+"\n".join(ev)+"\n")
    # fg: crop caption-free 1280x600, zoom cycles every 3.5s via concat of segments
    seg=3.5;k=int(dur//seg)+1;parts=[];lab=""
    fc=f"[0:v]crop=1280:600:0:0,split=2[bgs][fgs];[bgs]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5,eq=brightness=-0.25[bg];"
    fc+=f"[fgs]crop=900:600:190:0,scale=1080:720,split={k}"+"".join(f"[f{i}]" for i in range(k))+";"
    for i in range(k):
        z=[1.0,1.15,1.0,1.25][i%4];cx=[0,-.8,0,-.8][i%4]
        w=int(1080*z)//2*2;h=int(720*z)//2*2
        fc+=f"[f{i}]trim={i*seg}:{min((i+1)*seg,dur)},setpts=PTS-STARTPTS,scale={w}:{h},crop=1080:720:(iw-1080)/2+{cx}*(iw-1080)/2:(ih-720)/2,setsar=1[s{i}];"
    fc+="".join(f"[s{i}]" for i in range(k))+f"concat=n={k}[fg];[bg][fg]overlay=0:480,tpad=stop_mode=clone:stop_duration=2.6,ass=/tmp/w/{n}.ass[v]"
    fc+=f";[0:a]apad=pad_dur=2.6,afade=t=in:d=0.05[a]"
    out=f"/tmp/w/out3/{n}.mp4"
    subprocess.run(["ffmpeg","-v","error","-y","-ss",str(a),"-t",str(dur),"-i",M+vid,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",str(dur+2.6),"-r","25","-c:v","libx264","-preset","veryfast","-crf","22","-pix_fmt","yuv420p","-c:a","aac","-b:a","128k","-movflags","+faststart",out],check=True)
    print(n,round(dur+2.6,1))
