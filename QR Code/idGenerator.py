def gerador(tipo, sala1, sala2, ratio, numero):
    for i in range(1, (numero+1)//ratio):
        print(f"{tipo}{sala1}{i:05d}")
    for i in range((numero+1)//ratio, numero+1):
        print(f"{tipo}{sala2}{i:05d}")



