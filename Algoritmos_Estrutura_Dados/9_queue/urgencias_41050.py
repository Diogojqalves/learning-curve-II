class Fila:
    def __init__(self):
        self.items = [] 
        # Implementação da Fila(Queue) com recurso a um Array (estrutura de dados). Em vez de utilizarmos diretamente o enqueue() e o dequeu(), introduzimos o método append() e pop()
        # O Array é uma estrutura de dados lenta a inserir e remover um elemento tendo um tempo de O(n)
        #No método Access a complexidade algorítmica é igual a O(1)
        # Fila apresenta nos métodos de Access e Search uma complexidade algoritmica de O(n) e nos métodos de Insertion e Deletion O(1)

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item): # Adicionamos um elemento à fila na posição 0
        self.items.append(item)

    def dequeue(self): # Removemos o primeiro elemento introduzido, First In First Out (FIFO)
        return self.items.pop(0)

    def front(self): # Acesso ao primeiro elemento introduzido;
        return self.items[0]

    def rear(self): # Acesso ao último elemento introduzido;
        return self.items[len(self.items)-1]

    def size(self): #Devolve o tamanho da fila
        return len(self.items)

class Urgencia:
    def __init__(self):
        self.listaPacientes = Fila()
    
    def regPaciente(self, item): #adicionar passageiro
        self.listaPacientes.enqueue(item)

    def atenderPaciente(self): #remover passageiros a começar pelo primeiro introduzido até esvaziar a fila
        print(f'A atender o paciente {self.listaPacientes.front()}')
        self.listaPacientes.dequeue()

    def proxPaciente(self): #adicionar passageiro
        print(f"O próximo paciente é {self.listaPacientes.front()}")
    

class Paciente:
    def __init__(self, nome: str, idade: int, sintomas: str):
        self.nome = nome
        self.idade = idade
        self.sintomas = sintomas
    
    def getNome(self):
        print(self.nome)

    def getIdade(self):
        print(self.idade)
      
    def getSintomas(self):
        print(self.sintomas)

    def setNome(self, item: str):
        self.nome = item

    def setIdade(self, item: int):
        self.idade = item

    def setSintomatologia(self, item: str):
        self.sintomas = item

hMaia = Urgencia()
paciente1 = Paciente('António', 18, 'Nariz Entupido e Manchas Vermelas')
paciente1.getIdade()
paciente1.setSintomatologia('Bronquite Alérgica')
paciente1.getSintomas()
paciente2 = Paciente('Bruno', 20, 'Hematoma no tornozelo')
hMaia.regPaciente(paciente1)
hMaia.regPaciente(paciente2)
hMaia.atenderPaciente()
hMaia.proxPaciente()

# a) o Queue é a estrutura de dados mais adequada às coleções supra uma vez que se aplica a regra First In First Out, semelhante à regra das Urgencias