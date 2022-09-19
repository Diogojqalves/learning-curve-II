import time
inicio = time.time()

n = 10000
total = 0


for i in range(1, n):
    total += i

print('total', total)

fim = time.time()
 #contar tempo de execução do algoritmo
print('demorou a executar',fim-inicio)

# demorou a executar 0.002996683120727539