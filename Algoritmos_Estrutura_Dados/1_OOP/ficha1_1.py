class Data:

    def __init__(self, ano:int, mes:int, dia:int):
        self.ano = ano
        self.mes = mes
        self.dia = dia

    def dia_seguinte(self):
        self.dia += 1

feriado = Data(2020, 4, 15)
feriado.mes = 5
print(feriado.__dict__)

feriado.dia_seguinte()
print(feriado.dia)