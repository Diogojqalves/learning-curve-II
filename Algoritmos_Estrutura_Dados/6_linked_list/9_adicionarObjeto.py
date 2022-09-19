class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaLigada:
    def __init__(self):
        self.head = None

    def adicionar(self, data):
        no = Node(data)
        if self.head is None:
            self.head = no
        else:
            lastNode = self.head #encontrar o ultimo, começando na cabeça/primeiro
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = no #ultimo 
    
    def adicionarHead(self, data): #acresecentar um Node no inicio da lista
        novoNo = Node(data)
        novoNo.next = self.head
        self.head = novoNo

    def imprimir(self):
        lastNode = self.head #encontrar o ultimo, começando na cabeça/primeiro
        while lastNode:
            print(lastNode.data)
            lastNode = lastNode.next


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.aluno = ListaLigada()

    def adicionarAluno(self, varAluno):
        self.aluno.adicionar(varAluno)

    def print(self):
        self.aluno.imprimir()


class Aluno:
    def __init__(self, nome):
        self.nome = nome


escola1 = Escola('ISMAI')
aluno1 = Aluno('Diogo')
escola1.adicionarAluno(aluno1)
escola1.print()
