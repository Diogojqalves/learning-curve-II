# https://visualgo.net/en/sorting


nrs = [1, 23, 321, 212, 3123, 12, 3]

def bubblesort(lista):
    n = len(lista)
    trocas = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j +1]:
                trocas += 1
                print('nr de trocas:', trocas)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

bubblesort(nrs)
print(nrs)
