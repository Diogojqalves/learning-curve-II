##Swap
#Metodo 1
a = 3
b = 5

aux = a

a = b
b= aux

print(a)
print(b)

#Metodo 2
c = 10
d = 20

c, d = d, c
print(c)
print(d)


############### Sort method
clubes = ['SCPortugal', 'FCPorto', 'SLB']
clubes.sort()

print(clubes)
clubes.sort(reverse=True)
print(clubes)


# critério sorting
def ordenar(lista):
    return len(lista)

clubes.sort(key=ordenar)
print('a ordenar de acordo com o tamanho da string')
print(clubes)


#############################
class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota


def ordenacao(aluno):
    return aluno.nota
    
aluno1 = Aluno('Nelson', 18, 18)
aluno2 = Aluno('Ricardo', 19, 10)
aluno3 = Aluno('Diogo', 29, 10)

listaAlunos = [aluno1, aluno2, aluno3]
listaAlunos.sort(key=ordenacao)
print(listaAlunos)

