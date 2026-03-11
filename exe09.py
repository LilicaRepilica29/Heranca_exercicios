class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        return (f"O Veículo {self.marca}, se moveu!")
    
class Carro(Veiculo):
    def mover(self):
        return (f"O Carro da Marca: {self.marca} está se movendo!")
    
class Moto(Veiculo):
    def mover(self):
        return (f"A Moto da Marca: {self.marca} está se movendo pela Rodovia!")
    
