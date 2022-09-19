tabelaHash = [[] for _ in range(5)]

def funHash(chave):
    n = len(tabelaHash)
    return chave % n

def adicionar(tabelaHash, chave, value):
    indice = funHash(chave)
    tabelaHash[indice].append(value)

def imprimir(tabelaHash):
    for i in range(len(tabelaHash)):
        print(i, end=" ")
        for j in tabelaHash[i]:
            print('-->', end=" ")
            print(j, end=" ")
        print()
    

adicionar(tabelaHash, 2, "Ricardo")
adicionar(tabelaHash, 4, "João")
adicionar(tabelaHash, 3, "Nélson")
adicionar(tabelaHash, 44, "Zé")
adicionar(tabelaHash, 55, "Diogo")
adicionar(tabelaHash, 29, "Tiago")
adicionar(tabelaHash, 41, "Bruno")
imprimir(tabelaHash)