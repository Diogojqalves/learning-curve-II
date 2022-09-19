class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaLigada:
    def __init__(self):
        self.head = None

    def adicionar(self, data):
        no = Node(data) # criar Node
        if self.head is None:
            self.head = no # node 1 = head
        



ll = ListaLigada()
ll.adicionar(3)