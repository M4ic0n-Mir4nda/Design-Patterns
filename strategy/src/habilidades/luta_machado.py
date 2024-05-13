from .interfaces import Ihabilidade

class LutaMachado(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Lutar com machado")

    def nivel_atributo(self):
        print("Nivel de uso Machado: {}".format(self.nivel))