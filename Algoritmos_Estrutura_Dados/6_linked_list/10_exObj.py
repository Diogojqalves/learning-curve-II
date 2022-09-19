#Editora (Nome Website Lista Livros)

#Livro (nome, nr_paginas, ano)

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
    

    def removerMeio(self, data):
        atualNode = self.head
        if atualNode and atualNode.data == data:
            self.head = atualNode.next
            atualNode = None
        else:
            previous = None
            while atualNode and atualNode.data != data:
                previous = atualNode
                atualNode = atualNode.next
            if atualNode is None:
                return
            else:
                previous.next = atualNode.next
                atualNode = None



class Editora:
    def __init__(self, website, nome):
        self.nome = nome
        self.website = website
        self.livros = ListaLigada()

    def adicionarLivro(self, varLivro):
        self.livros.adicionar(varLivro)

    def print(self):
        self.livros.imprimir()
    
    def removerLivro(self, varLivro):
        self.livros.removerMeio(varLivro)


class Livro:
    def __init__(self, nome, nrPaginas, ano):
        self.nome = nome
        self.nrPaginas = nrPaginas
        self.ano = ano


editora1 = Editora('Almedina', 'www.almedina.pt')
livro1 = Livro('AED', '555', 2022)
livro2 = Livro('POO', '333', 2021)
editora1.adicionarLivro(livro1)
editora1.adicionarLivro(livro2)
editora1.print()
editora1.removerLivro(livro2)
print('a remover o livro')
editora1.print()
