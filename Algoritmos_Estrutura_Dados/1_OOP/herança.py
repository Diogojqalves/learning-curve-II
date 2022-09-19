class Pessoa:
    def __init__(self, nome:str, idade:int):
        self._nome = nome
        self._idade = idade


class Estudante(Pessoa):
    def __init__(self, nome:str, idade:int):
       
        super().__init__(
            nome, idade
        )


class Professor(Pessoa):
    def __init__(self, nome:str, idade:int):
       
        super().__init__(
            nome, idade
        )

