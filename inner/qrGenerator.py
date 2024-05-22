#Importação das libs.
import qrcode
from PIL import Image, ImageDraw, ImageFont
from colorama import init
from colorama import Fore

#A Lib de cores Colorama precisa ser iniciada, é isto que essa linha faz.     
init()

#Fontes, estão armazenadas em media.
courier = ImageFont.truetype('inner\media\CourierPrime-BoldItalic.ttf', 80)
montserrat = ImageFont.truetype('inner\media\Montserrat-Medium.ttf', 16)

#Gerador com Ratio. A lógica está errada, mas decidi não usar essa opção. Sinta-se livre para futucar.
def geradorRatio(tipo, sala1, sala2, ratio, numero):
    lista = list()
    for i in range(1, (numero+1)//ratio):
        lista.append(f"{tipo}{sala1}{i:05d}")
    for i in range((numero+1)//ratio, numero+1):
        lista.append(f"{tipo}{sala2}{i:05d}")
    return lista

#Gerador dos IDs únicos para cada adesivo, será o código usado para a geração dos QR.
def gerador(tipo, sala1, numero):
    lista = list()
    for i in range(1, (numero+1)):
        lista.append(f"{tipo}{sala1}{i:05d}")
    return lista

#Gera a imagem do QR no Ratio, os QRs ficam armazenados na pasta qr.
def geraQrRatio(a, b, c, d, e):
    print(Fore.BLUE + f"Gerando {e} QR Codes :)")
    lista = geradorRatio(a, b, c, d, e)
    for i in lista:
        img = qrcode.make(i, box_size="14") 
        type(img)  
        img.save(f"inner/qr/{i}.png")
    print(Fore.GREEN + f"Os seus {e} QR Codes foram gerados, acesse-os na pasta png! :)")  

#Gera a imagem do QR, os QRs ficam armazenados na pasta qr.
def geraQr(a, b, c):
    print(Fore.BLUE + f"Gerando {c} QR Codes :)")
    lista = gerador(a, b, c)
    for i in lista:
        img = qrcode.make(i, box_size="14") 
        type(img)  
        img.save(f"inner/qr/{i}.png")
    print(Fore.GREEN + f"Os seus {c} QR Codes foram gerados, acesse-os na pasta png! :)")    
    
#Gera a imagem do QR Code com os códigos e logo do leds com a lib Pillow.        
    for i in lista:
        background = Image.new('RGBA', (600, 600), (12, 27, 84, 255))
        draw = ImageDraw.Draw(background)
        draw.text((600//2, 20), "NÃO RETIRAR", (255,255,255), anchor="mm", font=montserrat)
        draw.text((600//2, 65),f"{i}", (255,255,255), anchor="mm", font=courier)
        qr = Image.open(f'inner/qr/{i}.png')
        background.paste(qr, (97, 97))
        logo = Image.open('inner\media\ledslogo.png')
        background.paste(logo, (225, 525))
        background.save(f'png/{i}.png')
