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
    def __init__ (self, nome:str, idade:int, Endereco:Endereco):
        super().__init__(
            nome, idade
        )
        self.Endereco = Endereco
        self.listaNota = []

    def inserirNota(self, item):
        self.listaNota.append(item)

    def atualizarEndereco(self, novoCod, novaRua, novaPorta):
        self.Endereco.cod = novoCod
        self.Endereco.rua = novaRua
        self.Endereco.porta = novaPorta

    def atualizarNota(self, item, novaNota):
        for i in self.listaNota:
            if i.cadeira == item:
                i.media = novaNota
                break
        else:
            'A cadeira que selecionou não foi encontrada'

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
    
#Estudante1
objEndereco1 = Endereco(4050, "Rua Oliveira Monteiro", 737)
objNota1 = Nota(18, 'AED')
objNota11 = Nota(19, 'POO')
objEstudante1 = Estudante ("Diogo", 25, objEndereco1)
objEstudante1.inserirNota(objNota1)
objEstudante1.inserirNota(objNota11)

#lista notas do Estudante1
for x in objEstudante1.listaNota:
    print(x.__dict__)

#atualizar nota 
objEstudante1.atualizarNota('AED', 20)

#lista notas com a nota Atualizada
print('a atualizar a nota...')
for x in objEstudante1.listaNota:
    print(x.__dict__)

objEstudante1.atualizarEndereco(4400, "Rua da Bélgica", 1958)

#Estudante 2
objEndereco2 = Endereco(4050, "Rua de Serpa Pinto", 737)
objNota2 = Nota(17, 'AED')
objEstudante2 = Estudante ("António", 26, objEndereco2)
objEstudante2.inserirNota(objNota2)

#Escola
objEscola = Escola("UMaia")
objEscola.inserirEstudante(objEstudante1)

objEscola.inserirEstudante(objEstudante2)


print(objEstudante1.__dict__)
print(objEstudante1.Endereco.__dict__)
print(objEscola.__dict__)

#Print lista de Estudantes da Escola
for i in objEscola.listaEstudantes:
    print(i.__dict__)

