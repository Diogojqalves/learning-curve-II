## Stack com base numa lista
class Editora:
  def __init__(self, nome:str, website:str):
    self.nome = nome
    self.website = website
    self.listaFilmes = []

  # adicionar um valor no topo da pilha
  def push (self, filme):
    self.listaFilmes.append(filme)

  # remover um valor no topo da pilha
  def pop (self):
    if self.listaFilmes:
      return self.listaFilmes.pop()
    
  def printStack (self):
    print (self.nome + ':')
    for filme in self.listaFilmes:
      print(filme.nome)
    