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
        


ll = ListaLigada()
ll.adicionar(3)
ll.adicionar(5)
ll.adicionar(7)
ll.adicionarHead(10)