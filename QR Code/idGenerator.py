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

def gerador(tipo, sala1, sala2, ratio, numero):
    lista = list()
    for i in range(1, (numero+1)//ratio):
        lista.append(f"{tipo}{sala1}{i:05d}")
    for i in range((numero+1)//ratio, numero+1):
        lista.append(f"{tipo}{sala2}{i:05d}")
    return lista

print(gerador(computador, slaveOne, antigo, 2, 4))

