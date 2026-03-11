class Pessoa:
   
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        return(f"Sou {self.nome} e tenho {self.idade} anos de idade!")
    
class Aluno(Pessoa):
    
    def estudar(self):
        return (f"{self.nome}, está estudando!")

class Professor(Pessoa):
    def ensinar(self):
        return (f"{self.nome}, está ensinando!")

