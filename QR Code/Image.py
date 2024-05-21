from PIL import Image
background = Image.new('RGBA', (176, 225), (255,255,255,255))
from PIL import ImageDraw
draw = ImageDraw.Draw(background)
draw.text((5,5), "Top text", (0,0,0))
draw.text((5,210),"Bottom", (0,0,0))
qr = Image.open('qr.png')
background.paste(qr, (60,20))
background.save('back.png')