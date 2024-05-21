import qrcode
from idGenerator import *

from PIL import Image, ImageDraw, ImageFont

courier = ImageFont.truetype('CourierPrime-BoldItalic.ttf', 16)
montserrat = ImageFont.truetype('Montserrat-Medium.ttf', 16)

#Tipos: 
computador = "COM"
monitor = "MNT"
cadeira = "CDR"
mesa = "MSA"
etc = "ETC"

#Salas:
slaveOne = "01"
antigo = "02"
colatina = "03"

lista = gerador(computador, slaveOne, antigo, 2, 10)

for i in lista:
    img = qrcode.make(i)
    type(img)  # qrcode.image.pil.PilImage
    img.save(f"pngs/{i}.png")
    
for i in lista:
    background = Image.new('RGBA', (350, 350), (12, 27, 84, 255))
    draw = ImageDraw.Draw(background)
    draw.text((160,5), "NÂO RETIRE", (255,255,255), font=montserrat)
    draw.text((5,210),f"{i}", (255,255,255))
    qr = Image.open(f'pngs/{i}.png')
    background.paste(qr, (30,20))
    background.save(f'qr/{i}.png')
