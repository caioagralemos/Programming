import math

print("\n*************************")
print("CALCULADORA by Caio Lemos")
print("*************************\n")

class Calculadora ():
    def __init__(self):
        pass

    def soma():
        try:
            x = float(input("primeiro número: "))
            y = float(input("segundo número: "))
        except:
            return "algo deu errado"
        else:
            return x + y
    
    def subtracao():
        try:
            x = float(input("primeiro número: "))
            y = float(input("segundo número: "))
        except:
            return "algo deu errado"
        else:
            return x - y
    
    def multiplicacao():
        try:
            x = float(input("primeiro número: "))
            y = float(input("segundo número: "))
        except:
            return "algo deu errado"
        else:
            return x * y
    
    
    def divisao():
        try:
            x = float(input("primeiro número: "))
            y = float(input("segundo número: "))
        except:
            return "algo deu errado"
        else:
            return x / y
    
    def resto():
        try:
            x = float(input("primeiro número: "))
            y = float(input("segundo número: "))
        except:
            return "algo deu errado"
        else:
            return x % y
    
    def elevar():
        try:
            x = int(input("seu número: "))
            y = int(input("elevado a: "))
            z = 0
            for i in range(1, y):
                if i == 1:
                    z = x*x
                else:
                    z = x*z
        except:
            return "algo deu errado"
        else:
            return z
    
    def raizquadrada():
        try:
            x = float(input("seu número: "))
        except:
            return "algo deu errado"
        else:
            return math.sqrt(x)
    
    def arredondar():
        try:
            x = float(input("seu número: "))
        except:
            return "algo deu errado"
        else:
            return round(x,0)

def menu():
    while True:
        menu = input("Menu - pressione:\n1 para somar\n2 para subtrair\n3 para multiplicar\n4 para dividir\n5 para obter resto de divisão\n6 para exponenciação\n7 para raiz quadrada\n8 para arredondar\n0 para sair\n\nSua escolha: ")
        try:
            return int(menu)
        except:
            print("Não está entre 0 e 8.")
        if menu in range(0,9):
            break

menunum = menu()

def checkmenu():
    resposta = input("pressione 1 para fazer outra operação ou qualquer botão pra sair: ")
    if resposta == "1":
        menunum = menu()
        return menunum
    else:
        pass

while menunum in range(0,9):
    if menunum == 0:
        break
    elif menunum == 1:
        print(f"\nSua resposta é: {Calculadora.soma()}\n")
        menunum = checkmenu()
    elif menunum == 2:
        print(f"\nSua resposta é: {Calculadora.subtracao()}\n")
        menunum = checkmenu()
    elif menunum == 3:
        print(f"\nSua resposta é: {Calculadora.multiplicacao()}\n")
        menunum = checkmenu()
    elif menunum == 4:
        print(f"\nSua resposta é: {Calculadora.divisao()}\n")
        menunum = checkmenu()
    elif menunum == 5:
        print(f"\nSua resposta é: {Calculadora.resto()}\n")
        menunum = checkmenu()
    elif menunum == 6:
        print(f"\nSua resposta é: {Calculadora.elevar()}\n")
        menunum = checkmenu()
    elif menunum == 7:
        print(f"\nSua resposta é: {Calculadora.raizquadrada()}\n")
        menunum = checkmenu()
    elif menunum == 8:
        print(f"\nSua resposta é: {Calculadora.arredondar()}\n")
        menunum = checkmenu()