import glob, os, shutil
from PIL import Image, ImageOps, ImageFilter, ImageStat
import numpy as np
R="/home/claude/canal-dark-"; src=R+"/video5-imagens/imagens"; dst="/home/claude/video_build5/bright"; os.makedirs(dst,exist_ok=True)
REAL={22:"quad_1",23:"quad_0",3:"workers_1",55:"workers_0",35:"modelt_0",36:"modelt_1",37:"modelt2_1",38:"modelt3_0",43:"line2_2",46:"line1_2",47:"modelt3_1",
56:"rouge1_0",57:"rouge1_1",59:"rouge1_2",65:"modela_1",66:"modela_0",67:"modela_2",68:"modela_3",71:"willow1_3",72:"willow1_0",73:"willow1_1",74:"willow1_2",
75:"overpass_0",31:"motor1903_2",32:"motor1903_1",78:"edsel_2",70:"edsel_0",84:"ford5_1",85:"ford5_0",40:"tractor_0",42:"modelt3_1",
17:"line0_0",60:"dodge_1",63:"fordhome_1"}
def fit(im):
    W,H=1280,720; r=im.width/im.height
    if abs(r-16/9)<0.25:
        s=max(W/im.width,H/im.height); im=im.resize((int(im.width*s)+1,int(im.height*s)+1),Image.LANCZOS)
        x=(im.width-W)//2; y=(im.height-H)//2; return im.crop((x,y,x+W,y+H))
    s=max(W/im.width,H/im.height); bg=im.resize((int(im.width*s)+1,int(im.height*s)+1),Image.BICUBIC)
    x=(bg.width-W)//2; y=(bg.height-H)//2; bg=bg.crop((x,y,x+W,y+H)).filter(ImageFilter.GaussianBlur(40))
    bg=Image.eval(bg,lambda v:int(v*0.35))
    fs=min(H/im.height,W/im.width)*0.96; fg=im.resize((int(im.width*fs),int(im.height*fs)),Image.LANCZOS)
    bg.paste(fg,((W-fg.width)//2,(H-fg.height)//2)); return bg
def bright(im):
    im=ImageOps.autocontrast(im,cutoff=0.4); l=ImageStat.Stat(im.convert("L")).mean[0]/255
    if l<0.40 and l>0.02:
        g=np.log(0.40)/np.log(l); a=np.asarray(im).astype(np.float32)/255; im=Image.fromarray((np.clip(a**g,0,1)*255).astype(np.uint8))
    return im
for f in sorted(glob.glob(src+"/*.jpg")):
    bright(Image.open(f).convert("RGB")).save(dst+"/"+os.path.basename(f),quality=93)
n=0
for k,nm in REAL.items():
    p=glob.glob(R+f"/video5-commons/fotos/{nm}.*")
    if not p: print("falta",nm); continue
    fit(ImageOps.autocontrast(Image.open(p[0]).convert("RGB"),cutoff=0.3)).save(dst+f"/{k:03d}_real.jpg",quality=93); n+=1
print("reais",n,"geradas",len(glob.glob(src+"/*.jpg")))
