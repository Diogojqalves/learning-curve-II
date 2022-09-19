## Stack com base numa lista
class TurmaB:
  def __init__(self):
    self.listaInterna = []
    
  # verifica se está vazio
  # (1)
  def isEmpty (self):
    return self.listaInterna == []
    # len (listaInterna) == 0

  # adicionar um valor no topo da pilha
  def push (self, elemento):
    self.listaInterna.append (elemento)

  # remover um valor no topo da pilha
  def pop (self):
    if self.listaInterna:
      return self.listaInterna.pop()

  # mostra a referencia do elemento no topo da stack
  # sem o remover
  def top (self):   # peek
    if not self.isEmpty():  # se tiver elementos entra no if
      return self.listaInterna[-1]
      
  # mostra o tamanho da stack
  def size(self):
    return len(self.listaInterna)
    
  def printStack (self):
    print ('Turma B: ' + str(self.listaInterna))