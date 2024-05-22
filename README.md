# LEDS QR MAKER


> Faça os adesivos de controle de ativos do LEDS de forma dinâmica e simples em Python!

## Pré-requisitos

Antes de começar, baixe as seguintes libs:

- **QR Code**
usado para, pasmem, criar QR Codes:

```
pip install qrcode
```

- **Pillow**
lib usada para criar imagens de forma dinâmica: 

```
pip install pillow
```

Geralmente ela já está instalada junto com o qrcode.

- **Colorama**
para dar cor ao terminal e ficar bonitinho......

```
pip install colorama
```


## Instalando LEDS QR MAKER

Para instalar o LEDS QR MAKER, siga estas etapas:

- Na página do Github, clique em **code** e baixe o zip.
- Extraia o ZIP com o seu gerenciador de pacotes de preferência.
- Abra e execute **gerador.py** com seu editor de código ou IDE,

## Usando LEDS QR MAKER
Dentro do GERADOR, você pode utilizar duas funções:
- **geraQr**<br>
A função geraQr vai gerar as imagens de forma simples. Ela utiliza esses parametros (nessa ordem):
```
geraQr(TIPO_DE_EQUIPAMENTO, SALA_DO_LEDS, QUANTIDADE) 
```

- **geraQrRatio**<br>
A função geraQrRatio vai gerar as imagens de forma em que duas salas vão compartilhar a mesma quantidade. Ela utiliza esses parametros (nessa ordem):
```
geraQr(TIPO_DE_EQUIPAMENTO, SALA1_DO_LEDS, SALA2_DO_LEDS, RATIO, QUANTIDADE) 
```
(OBS): *O ratio vai ser o divisor (inteiro) da quantidade, ou seja, se for 2, metade das máquinas será da sala 1 e metade da sala 2.*

#### O output das imagens completas será em PNG e pode ser encontrado na pasta png na raiz do projeto. Os Qr Codes podem ser encontrados em inner/qr.

Para mais informações, leia o código, que está comentado. As funções estão localizadas em `inner/qrGenerator.py`