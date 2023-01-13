
try:
    # cod. que eu quero tentar mas nao tenho certeza que vai funcionar
    pass
except:
    # executar caso o código nao funcione
    pass
else:
    # resposta do código se tudo der certo
    pass

try:
    # resultado = 10 + int(input("Número pra ser somado com 10: "))
    pass
except:
    print("Algo deu errado.")
else:
    # print(f"Soma bem sucedida, retornando {resultado}")
    pass

try:
    # f = open('testfile', 'w')
    # f.write(input("Me diz o que você quer escrever no seu novo arquivo:\n"))
    pass
except TypeError: # você pode criar exceções para tipos específicos (Built-in exceptions)
    print("There was a type error!")
except OSError:
    print("You have an OS Error")
finally: # o finally sempre roda independente de qualquer coisa
    print("Eu sempre sou executado")

def pedir_int():
    while True:
        try:
            result = int(input("Digite seu número: "))
        except:
            print("Algo deu errado. Tente novamente")
            continue
        else:
            print(result**2)
            break

pedir_int()
