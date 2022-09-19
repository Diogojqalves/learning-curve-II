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
    
    def adicionarMeio(self, prev, data):
        if not prev:
            print('Esse prev node não existe')
        else:
            print('a adicionar no meio')
            novo = Node(data)
            novo.next = prev.next
            prev.next = novo
        
    def removerHead(self):
        print('a remover a cabeça')
        self.head = self.head.next

ll = ListaLigada()
ll.adicionar(3)
ll.adicionar(5)
ll.adicionar(7)
ll.adicionarHead(10)

ll.imprimir()

ll.adicionarMeio(ll.head.next, 21)

ll.imprimir()

ll.removerHead()
ll.imprimir()