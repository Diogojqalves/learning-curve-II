from StackTurmaB import TurmaB

class TurmaA:
 
    def __init__(self):
        self.lista = []

    def push (self, elemento):
        self.lista.append(elemento)
    
    def printStack(self):
        print('Turma A: ' + str(self.lista))

stack = TurmaB()
stack.push("Bruno")
stack.push("Diogo")
stack.push("Vitor")

stack.printStack()

outraStack = TurmaA()
outraStack.push(stack.pop())
outraStack.push(stack.pop())
outraStack.push(stack.pop())
outraStack.printStack()

