class Livro:
    def __init__(self, titulo:str, editora:str, ano:int, autor_principal:str, nr_pags:int):
        self.titulo = titulo
        self.editora = editora
        self.ano = ano
        self.autor_principal = autor_principal
        self.nr_pags = nr_pags

    def nome_livro(self):
        return self.titulo

    def paginas_livro(self):
        return self.nr_pags

    def ano_livro(self):
        return self.ano




livro1 = Livro('Python OOP', 'UM', 2020, 'Sr.X', 100)
livro2 = Livro('Python A&DS', 'UM', 2022, 'Sr.Y', 200)

print(livro1.__dict__)
print(livro1.nome_livro())
print(livro1.paginas_livro())
print(livro1.ano_livro())