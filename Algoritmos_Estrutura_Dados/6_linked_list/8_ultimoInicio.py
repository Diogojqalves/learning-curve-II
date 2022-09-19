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

    def imprimir(self):
        lastNode = self.head #encontrar o ultimo, começando na cabeça/primeiro
        while lastNode:
            print(lastNode.data)
            lastNode = lastNode.next

    def trocarCabecaCauda(self):
        ult = self.head # vamos empurrar a Head até ser apontar para None
        segundoNo = None 
        if not ult or not ult.next: #lista vazia ou apenas com 1 elemento
            return

        while ult and ult.next :
            segundoNo = ult
            ult = ult.next
        segundoNo.next = None
        ult.next = self.head
        self.head = ult

ll = ListaLigada()
ll.adicionar('A')
ll.adicionar('B')
ll.adicionar('C')
ll.adicionar('D')

ll.imprimir()
print("transferir tale para head...")
ll.trocarCabecaCauda()
ll.imprimir()

