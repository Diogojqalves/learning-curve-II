class Filme:
    def __init__(self, nome:str, duracao:str, ano:int, artista_principal:str):
        self._nome = nome
        self._duracao = duracao
        self._ano = ano
        self._artista_principal = artista_principal

    def nome_filme(self):
        return self._nome

    def duracao_filme(self):
        return self._duracao

    def ano_filme(self):
        return self._ano




filme1 = Filme('Python OOP', '120 min', 2020, 'Sr.X')
filme2 = Filme('Python A&DS', '100 min', 2022, 'Sr.Y')

print(filme1.__dict__)
print(filme1.nome_filme())
print(filme1.duracao_filme())
print(filme1.ano_filme())

