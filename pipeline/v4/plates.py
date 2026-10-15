from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
def plate(src, out, gray=True, crop_bottom=0):
    im = Image.open(src).convert("RGB"); w, h = im.size; im = im.crop((0, 0, w, h - crop_bottom))
    if gray: im = ImageEnhance.Contrast(im.convert("L").convert("RGB")).enhance(1.15)
    W, H = 2880, 1620
    s = max(W / im.width, H / im.height); bg = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.BICUBIC)
    bx, by = (bg.width - W) // 2, (bg.height - H) // 2; bg = bg.crop((bx, by, bx + W, by + H)).filter(ImageFilter.GaussianBlur(55))
    bg = ImageEnhance.Brightness(bg).enhance(0.28)
    fs = min(1380 / im.height, 1760 / im.width); fw, fh = int(im.width * fs), int(im.height * fs)
    fg = im.resize((fw, fh), Image.LANCZOS).filter(ImageFilter.UnsharpMask(3, 90, 2))
    x, y = 1000 + (1800 - fw) // 2, (H - fh) // 2
    sh = Image.new("L", (W, H), 0); ImageDraw.Draw(sh).rectangle([x + 18, y + 26, x + fw + 18, y + fh + 26], fill=210)
    sh = sh.filter(ImageFilter.GaussianBlur(36)); bg = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), bg, sh)
    ImageDraw.Draw(bg).rectangle([x - 8, y - 8, x + fw + 8, y + fh + 8], fill=(238, 232, 220))
    bg.paste(fg, (x, y)); bg.save(out)
if __name__ == "__main__":
    import sys
    L = [("carnegie_retrato", True, 0), ("carnegie_16_anos", True, 80), ("casa_dunfermline", True, 0), ("eads_bridge", True, 52),
         ("carnegie_1878", True, 48), ("edgar_thomson", True, 52), ("syracuse", False, 0)]
    ims = []
    for n, g, c in L:
        plate(f"/home/claude/canal-dark-/video3-fotos/{n}.png", f"/tmp/pl_{n}.png", g, c); ims.append(Image.open(f"/tmp/pl_{n}.png").resize((640, 360)))
    m = Image.new("RGB", (640 * 4, 360 * 2))
    for k, i in enumerate(ims): m.paste(i, ((k % 4) * 640, (k // 4) * 360))
    m.save("/tmp/plates.jpg", quality=80)
