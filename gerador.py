from inner.qrGenerator import *

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
nulo = "99"

#Parametros: tipo, sala, quantidade de números (indice começa em 1 e inclui o ultimo número).
lista = geraQr(etc, slaveOne, 20)

