class Pessoa:
    def __init__(self, nome:str, idade:int):
        self._nome = nome
        self._idade = idade

class Endereco():
    def __init__(self, cod:int, rua:str, porta:int):
        self.cod = cod 
        self.rua = rua    
        self.porta = porta

class Nota():
    def __init__ (self, media:float, cadeira:str):
        self.media = media
        self.cadeira = cadeira

class Estudante(Pessoa):
    def __init__ (self, nome:str, idade:int, Endereco:Endereco, Nota:Nota):
        super().__init__(
            nome, idade
        )
        self.Endereco = Endereco
        self.Nota = Nota

    def atualizarNota(self, novaNota):
        self.Nota.media = novaNota

    def atualizarEndereco(self, novoCod, novaRua, novaPorta):
        self.Endereco.cod = novoCod
        self.Endereco.rua = novaRua
        self.Endereco.porta = novaPorta


class Escola():
    def __init__ (self, nomeEscola):
        self.nomeEscola = nomeEscola
        self.listaEstudantes = []
    
    def inserirEstudante(self, item):
        self.listaEstudantes.append(item) 

class Professor(Pessoa):
    def __init__(self, nome:str, idade:int):
       
        super().__init__(
            nome, idade
        )
    

objEndereco1 = Endereco(4050, "Rua Oliveira Monteiro", 737)
objNota1 = Nota(18, 'AED')
objEstudante1 = Estudante ("Diogo", 25, objEndereco1, objNota1)

objEndereco2 = Endereco(4050, "Rua de Serpa Pinto", 737)
objNota2 = Nota(17, 'AED')
objEstudante2 = Estudante ("António", 26, objEndereco2, objNota2)

objEscola = Escola("UMaia")
objEscola.inserirEstudante(objEstudante1)
objEstudante1.atualizarNota(20)
objEstudante1.atualizarEndereco(4400, "Rua da Bélgica", 1958)
objEscola.inserirEstudante(objEstudante2)


print(objEstudante1.__dict__)
print(objEstudante1.Endereco.__dict__)
print(objEstudante1.Nota.__dict__)
print(objEscola.__dict__)

for i in objEscola.listaEstudantes:
    print(i.__dict__)