def linear(lista, valor):
    n = len(lista)
    for i in range(n):
        print('comparações:', i)
        if lista[i] == valor:
            return True
    return False

clubes = ['SCPortugal', 'FCPorto', 'SLB']


print(linear(clubes, 'FCPorto'))
print(linear(clubes, 'XYZ'))
#########################################################

def linearOrdenada(lista, valor):
    n = len(lista)
    for i in range(n):
        print('comparações:', i)
        if lista[i] == valor:
            return True
        elif lista[i] > valor: ## [1 , 22, 33, 55] ---> Encontra 5 .... 
            return False #...como 22 é maior que 5 é porque o 5 não vai ser encontrado nos próximos valores, break
    return False

nomes = ['André', 'João', 'Martins', 'Tiago', 'Zé']


print(linearOrdenada(nomes, 'João'))
print(linearOrdenada(nomes, 'Diogo'))
