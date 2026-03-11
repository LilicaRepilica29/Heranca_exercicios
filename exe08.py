class Pessoa:
    def __init__(self, nome):
        self.nome = nome
class Professor(Pessoa):
    def ensinar(self):
        print(self.nome, "está ensinando")


