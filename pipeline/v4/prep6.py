import glob, os
from PIL import Image, ImageOps
exec(open("/home/claude/video_build5/prep.py").read().split("REAL=")[0].replace('video5','video6').replace('video_build5','video_build6'))
exec("def fit"+open("/home/claude/video_build5/prep.py").read().split("def fit")[1].split("for f in sorted")[0])
for f in sorted(glob.glob(src+"/*.jpg")): bright(Image.open(f).convert("RGB")).save(dst+"/"+os.path.basename(f),quality=93)
KW={"Wall Street in chaos":"wallstreet1_2","Brokers' empty":"blackfriday2_0","Crowd shadows":"blackfriday_1","A railroad station":"unionpacific_0","A printing press room":"gould3_1",
"A river ferry":"nyworld_0","A grand hotel":"gould4_0","A tall railroad bridge":"unionpacific_1","An empty trading hall with a giant":"blackfriday_0","The White House":"grant_1",
"A telegraph office":"telegraph_0","Wall Street crowds":"blackfriday2_1","Western railroad tracks":"upmap_0","The Union Pacific train":"unionpacific_0","An elevated railway":"elevated_1",
"An elevated train station":"elevated_0","A newspaper printing room":"nyworld_3","A quiet mansion library":"lyndhurst_0","Railroad workers":"strike_0","A union hall":"knights_0",
"A stock ticker":"wallstreet1_0","A grand empty mansion":"lyndhurst_2","A dark telegraph room":"gould3_2","A panic on Wall Street":"gould5_0","A hotel staircase":"gould1_0",
"A telegraph pole line":"gould4_0","A horse drawn funeral":"gould2_2"}
sc=[l.split("|",1)[1] for l in open(R+"/video6-imagens/scenes.txt") if "|" in l]; used=set(); n=0
for key,nm in KW.items():
    for i,t in enumerate(sc,1):
        if t.startswith(key) and i not in used:
            p=glob.glob(R+f"/video6-commons/fotos/{nm}.*")
            if p: fit(ImageOps.autocontrast(Image.open(p[0]).convert("RGB"),cutoff=0.3)).save(dst+f"/{i:03d}_real.jpg",quality=93); used.add(i); n+=1
            break
print("reais",n)
