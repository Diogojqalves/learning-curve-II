class Aluno ():
  def __init__ (self, vNome:str, vIdade:int):
    self.nome = vNome
    self.idade = vIdade

  def imprimeIdade (self):
    return self.idade
  
  def __str__(self):
    return self.nome + str(self.idade)


class Escola ():
  def __init__ (self, vNome:str, vAluno:Aluno):
    self.nomeEscola = vNome
    self.aluno = vAluno


objAluno = Aluno (" Ricardo ", 18)

objEscola = Escola ( "ISMAI", objAluno)
print (objEscola.aluno.imprimeIdade() ) 