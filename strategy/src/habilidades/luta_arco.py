from .interfaces import Ihabilidade

class UsoArco(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Atirar flechas")

    def nivel_atributo(self):
        print("Nivel de uso Arco: {}".format(self.nivel))