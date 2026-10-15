import sys, glob
from PIL import Image, ImageDraw
d0=sys.argv[1]; fs=sorted(glob.glob(d0+"/*.jpg")+glob.glob(d0+"/*.png")); cols=12; w,h=165,110
sh=Image.new("RGB",(cols*w,((len(fs)+cols-1)//cols)*(h+13)),(20,20,20)); d=ImageDraw.Draw(sh)
for i,f in enumerate(fs):
    try: im=Image.open(f).convert("RGB"); im.thumbnail((w,h))
    except: continue
    x,y=(i%cols)*w,(i//cols)*(h+13); sh.paste(im,(x,y)); d.text((x+1,y+h),f.split("/")[-1][:24],fill=(255,255,0))
sh.save(sys.argv[2],quality=65); print(len(fs))
