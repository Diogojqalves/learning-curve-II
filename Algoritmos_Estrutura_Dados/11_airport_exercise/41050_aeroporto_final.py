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

class Lista(): 
# Decidi utilizar a estrutura de dados lista por ser ordenada e indexada sendo muito útil nas funções registarPassag e atenderPassgeiros da class Embarque() uma vez que estamos a aceder ao Balcao numa determinada posição.
# No python os valores são atribuidos a uma posição da memória especifica por isso, independentemente do tamanho da lista, ao aceder ao item demoramos O(1).
    def __init__(self):
        self.items = []
    
    def append(self, item):
        return self.items.append(item)

    def pop(self, item):
        return self.items.pop(item)

    def size(self):
        return len(self.items)

    def index(self, item): 
        return self.items.index(item)

    def access(self, item): 
        return self.items[item]


class Embarque():
    def __init__(self, nrVoo: int, quantidadeBalcoes: int):
        assert quantidadeBalcoes <= 10, f"A quantidade de Balcoes {quantidadeBalcoes} não é igual ou menor do que 10!" 
        #10 é o limite máximo de Balcoes por Embarque
        self.__nrVoo = nrVoo
        self.__quantidadeBalcoes = quantidadeBalcoes
        self.listaBalcoes = Lista() # Decide optar pela estrutura de dados Fila uma vez que é a mais utilizada nos aeroportos no qual os balcões são processados por ordem de chegada e como estamos a lidar com pequenos volumes de dados a complexidade algoritmica é aceitável.

    def adicionarBalcao(self, item):
        if self.listaBalcoes.size() < self.__quantidadeBalcoes: #confirmar que a Lista não excede o limite de 10 Balcões
            self.listaBalcoes.append(item) #adicionar balcao = O(1)
            print(f"\nbalcao {item} adicionado")
            return True
        else:
            print('Não foi possível adicionar o Balcão uma vez que a lista está cheia')
            return False

    def registarPassag(self, nomeBalcao:str, nrPassageiro): 
        for balcao in self.listaBalcoes.items: # O(n)
            if balcao.nome == nomeBalcao: # encontrar o balcao.nome
                balcao.registarPassageiro(nrPassageiro)
                return True # chamar a funcao da Class Balcao com o valor nrPassageiro
            

    #alternativa com o número do balcao em vez do nome
    def registarPassag2(self, nrBalcao:int, nrPassageiro):
        count = 0
        for balcao in self.listaBalcoes.items: #O(n)
            if count == nrBalcao: # encontrar o balcao.nome
                balcao.registarPassageiro(nrPassageiro) # chamar a funcao da Class Balcao com o valor nrPassageiro
            count += 1

    def atenderPassgeiros(self, nomeBalcao): #confirmar que todos os passageiros do primeiro balcao embarcaram para removerem o mesmo
        count = -1
        for balcao in self.listaBalcoes.items: #O(n)
            count +=1 # guardar o indice para introduzir no método pop
            if balcao.nome == nomeBalcao:
                balcao.atenderPassageiro() # chamar a funcao da Class Balcao para embarcar todos os passageiros
        self.listaBalcoes.pop(count) # remover balcao apos todos os passageiros embarcarem
        self.__quantidadeBalcoes -= 1 # atualizar o nr de balcoes

    def tamanhoEmbarque(self): #adicionar passageiro
        print(f"\nO Avião de embarque nr.º{self.__nrVoo} tem {self.__quantidadeBalcoes} balcoes por atender")

class Balcao:
    def __init__(self, nome: str):
        self.nome = nome
        self.listaPassageiros = Fila()
    
    def registarPassageiro(self, passageiro): #adicionar passageiro
        novoPassageiro = Passageiro(passageiro)
        self.listaPassageiros.enqueue(novoPassageiro) #O(1)
        print(f"\npassageiro {passageiro} registado no balcao {self.nome}")
        return True

    def atenderPassageiro(self): #remover passageiros a começar pelo primeiro introduzido até esvaziar a fila
        while self.listaPassageiros.size() > 0: # O(n)
            print(f'\nA embarcar o passageiro {self.listaPassageiros.front()}')
            self.listaPassageiros.dequeue() #O(1)

    def tamanho(self): #adicionar passageiro
        print(f"\nO Balcão {self.nome} registou {self.listaPassageiros.size()} passageiros")
    
    
class Passageiro:
    def __init__(self, num: int):
        self.__num = num
    
    def getNum(self):
        print(f'\nChamou o passageiro {self.num}')


embarque1 = Embarque(1, 10) # 10 representa o limite máximo de balcões

balcao1 = Balcao('TAP')
balcao2 = Balcao('Ryanair')
balcao3 = Balcao('Iberia')
balcao4 = Balcao('Delta')
balcao5 = Balcao('TAAG')
balcao6 = Balcao('AirFrance')
balcao7 = Balcao('Easyjet')
balcao8 = Balcao('WizzAir')
balcao9 = Balcao('QatarAir')
balcao10 = Balcao('EmiratesAir')
embarque1.adicionarBalcao(balcao1)
embarque1.adicionarBalcao(balcao2)
embarque1.adicionarBalcao(balcao3)
embarque1.adicionarBalcao(balcao4)
embarque1.adicionarBalcao(balcao5)
embarque1.adicionarBalcao(balcao6)
embarque1.adicionarBalcao(balcao7)
embarque1.adicionarBalcao(balcao8)
embarque1.adicionarBalcao(balcao9)
embarque1.adicionarBalcao(balcao10)
embarque1.tamanhoEmbarque()
embarque1.registarPassag('TAP', 1)
embarque1.registarPassag('TAP', 2)
embarque1.registarPassag('TAP', 3)
embarque1.registarPassag('TAP', 4)
embarque1.registarPassag('TAP', 5)
balcao1.tamanho()
embarque1.atenderPassgeiros('TAP')
balcao1.tamanho()
embarque1.tamanhoEmbarque()
embarque1.registarPassag2(2, 27)