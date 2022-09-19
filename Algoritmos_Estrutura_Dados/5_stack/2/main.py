from StackEditora import Editora

class Filme:
 
    def __init__(self, nome:str, ano:int, duracao:str):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

stack = Editora('HBO' , 'www.hbo.com')
filme1 = Filme('Dr.Strange', 2022, '120min')
filme2 = Filme('The Batman', 2022, '180min')
stack.push(filme1)
stack.push(filme2)

stack.printStack()

print('waiting for pop method...')
print('...')
print('pop!')
stack.pop()
stack.printStack()

