class Transporte:

	# Constructor
	def __init__(self, capacidade: int, velocidade: int):
            self.capacidade = capacidade
            self.velocidade = velocidade



# Inherited or Sub class (Note Person in bracket)
class Terrestre(Transporte):

	# Constructor
    def __init__(self, capacidade, velocidade, rodas: int):
        Transporte.__init__(self, capacidade, velocidade)
        self.rodas = rodas

    def acelera(self, incremento_velocidade):
        self.velocidade = self.velocidade + incremento_velocidade
        

    def abranda(self, decremento_velocidade):
        self.velocidade = self.velocidade - decremento_velocidade

    def para(self):
        self.velocidade = 0



class Carro(Terrestre):
	def __init__(self, capacidade, velocidade, rodas, cor: int, portas: int):
            Terrestre.__init__(self, capacidade, velocidade, rodas)
            self.cor = cor
            self.portas = portas




g = Carro(5, 100, 4, 1, 4)
print(g.__dict__)

g.acelera(50)
print(g.velocidade)

g.abranda(10)
print(g.velocidade)

g.para()
print(g.velocidade)

print(g.__dict__)