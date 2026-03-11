# Exercício 3 – Herdando atributos
# Complete o código para que o aluno possa acessar o atributo nome.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    pass


# Perguntas:
# 1. Onde o atributo nome foi criado?= Na classe Pessoa.
# 2. Por que a classe Aluno consegue usar esse atributo?= Porque ela esta herdando da classe mãe.