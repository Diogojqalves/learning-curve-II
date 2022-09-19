class Fila():
    def __init__(self):
        self.listInterna = []

    def add(self, item):
        self.listInterna.append(item)

    def rem(self, item):
        tamanho = len(self.listInterna)
        self.listInterna.pop(tamanho - 1)

fila = Fila()
fila.add("carro")
print('o valor removido', fila.rem())