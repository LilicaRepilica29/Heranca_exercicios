class Animal:

    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def falar(self):
        return (f"O Cachorro {self.nome} late: AuAu...")

class Gato(Animal):
    def falar(self):  
        return (f"O Gato {self.nome} mia: MiauMiau...")  
    
