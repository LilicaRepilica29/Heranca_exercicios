class Personagem:

    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        return ("Hora do ataque!")
    
class Guerreiro(Personagem):
    def atacar(self):
        return (f"{self.nome} ataca com Espada!")
    
class Mago(Personagem):
    def atacar(self):
        return (f"{self.nome} lança Magia!")
    