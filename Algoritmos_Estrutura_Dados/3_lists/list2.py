class Clube:
    def __init__ (self, nome:str):
        self.nome = nome

class Liga:
    def __init__ (self):
        self.listaClubes = []

    def adicionarClubes(self, novoClube: Clube):
        self.listaClubes.append(novoClube)

    def printClubes(self):
        for clube in self.listaClubes:
            print(clube.nome)


insClube = Clube('fcp')

insClube2 = Clube('bfc')

ligaPortuguesa = Liga()
ligaPortuguesa.adicionarClubes(insClube)
ligaPortuguesa.adicionarClubes(insClube2)
ligaPortuguesa.printClubes()


