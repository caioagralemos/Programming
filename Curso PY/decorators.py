# RETORNANDO FUNCOES SECUNDARIAS EM UMA FUNC PRIMARIA

def hello(name='Caio'):
    print("A função hello() foi executada!")
    
    def greet():
        return f"\t Olá {name}!" # \t serve pra dar um tab
    
    def welcome():
        return f"\t Bem vindo(a) {name}"

    if name == "Caio":
        return greet()
    else:
        return welcome()

#greet = hello()
#print(greet)

def cool():

    def super_cool():
        return "I am very cool"

    return super_cool()

legal = cool()
#print(legal)

# PASSANDO UMA FUNCAO COMO PARAMETRO PRA OUTRA FUNCAO

def outrafuncao(some_func):
    print("Essa função executa outra função!")
    print(some_func)

#outrafuncao(hello())

# CRIANDO UM DECORATOR

def new_decorator(original_func):

    def wrap_func():
        print("Código extra adicionado para rodar antes da minha função original")

        original_func()

        print("Código extra adicionado para rodar depois da minha função original")

    return wrap_func

#def func_decorated():
    #print("I wanna be decorated!!")

#decorated_func = new_decorator(func_decorated)
#decorated_func()

# JEITO MAIS SIMPLES DE CRIAR UM DECORATOR

@new_decorator # o uso do @ substitui #decorated_func = new_decorator(func_decorated), decorated_func()
def func_decorated():
    print("I wanna be decorated!!")

func_decorated()