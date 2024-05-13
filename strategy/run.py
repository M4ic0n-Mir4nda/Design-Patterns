from src import Guerreiro, UsoArco, LutaEspada, Curar, LutaMachado

cavaleiro = Guerreiro(LutaEspada(6))
arqueiro = Guerreiro(UsoArco(9))
curandeiro = Guerreiro(Curar(7))
cavaleiro_machado = Guerreiro(LutaMachado(8))

cavaleiro.acao()
arqueiro.acao()
arqueiro.attributos()
curandeiro.acao()
curandeiro.attributos()
cavaleiro_machado.acao()