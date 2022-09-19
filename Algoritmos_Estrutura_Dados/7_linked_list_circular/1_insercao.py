class Node:
    def __init__(self, element):
        self.data = element
        self.next = None

class ListaCircular:
    def __init__(self):
        self.head = None

    def append(self, elemento):
        if not self.head:
            #lista vazia
            self.head = Node(elemento)
            self.head.next = self.head
        else:
            novoNo = Node(elemento)
            #percorre a lista ate encontrar o ultimo
            current = self.head #aponta para a cabeça da lista
            while current.next != self.head:
                current = current.next
            #associar o novoNo
            current.next = novoNo
            novoNo.next = self.head # reajustar o head

    def imprimir(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr.next == self.head:
                break
        print(curr.data)

    def adicionarCabeca(self, elemento):
        novoNo = Node(elemento)
        cur = self.head
        #apontar o novo no.next para o head
        novoNo.next = self.head
        if not self.head: #caso não exista self.head
            novoNo.next = novoNo
        else:#percorre a lista ate encontrar o ultimo
            while cur.next != self.head:
                cur = cur.next
            cur.next = novoNo #fechar ciclo
            self.head = novoNo

llc = ListaCircular()

llc.append('a')
llc.append('b')
llc.append('c')
llc.adicionarCabeca('d')
llc.imprimir()