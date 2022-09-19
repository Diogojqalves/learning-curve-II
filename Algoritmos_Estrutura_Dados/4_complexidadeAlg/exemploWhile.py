import time
inicio = time.time()

n = 10000
total = 0
num = 0

while(num < n):
    total += num
    num += 1

print('total', total)

fim = time.time()
 #contar tempo de execução do algoritmo
print('demorou a executar',fim-inicio)

# demorou a executar 0.0049893856048583984