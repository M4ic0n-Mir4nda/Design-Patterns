def decorator(funcao):
    def wrapper(*arg, **kwargs): # Para evitar que de algum erro por se tratar de uma chamada de um método de classe é feito desta forma
        print("Ola Mundo!")
        print(arg[1]) # E o contexto da classe, ou seja tudo que for passado na classe o decorator vai conseguir interpretar
        print(kwargs)
        funcao(*arg, **kwargs) # O que acontece nesta função: print("Ola, estou na minha funcao! :D")

    return wrapper # Em alguns casos de literatura ou na internet este nome é dado para funções superiores

@decorator # Isso é == minha_funcao = decorator(minha_funcao)\n minha_funcao()
def minha_funcao():
    print("Ola, estou na minha funcao! :D")

class minha_classe():

    @decorator
    def metodo(self, num):
        print("Estou na minha classe")

cl = minha_classe()
cl.metodo(4)