def porquinho():
    print("oinc")

contador = 0

# while contador != 50:
#    porquinho()
#    contador += 1

def seunome(nome= "Padrão"):
    print(f"Olá, {nome}")

# nome = input("Nos diga seu nome: ")
# seunome(nome)

def soma(num1, num2):
    return num1 + num2

# resultado = soma(1,5)
# print(resultado)

def ehPar(numero):
    return numero % 2 == 0

# print(ehPar(2))
# print(ehPar(3))

mynumlist = [num for num in range(0,11) if num % 2 == 0]

def lista_ehPar(list):
    for num in list:
        if num % 2 == 0:
            return True
        else:
            pass # não é possivel colocar return false aqui! (quebraria o loop)

# print(lista_ehPar(mynumlist))

# Trabalhando com funções e tuplas --
work_hours = [("Everaldo", 1000), ("Edmilson", 700), ("Eliot", 720)]

def func_do_mes(horas):
    current_max = 0
    funcionario_mes = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            funcionario_mes = employee
        else:
            pass
    
        return(funcionario_mes, current_max)

# name,hours = func_do_mes(work_hours)
# print(name)
# print(hours)



# FUNÇÃO MAP PARA ITERAR UMA FUNÇÃO POR CADA ITEM DE UMA LISTA --

def square(n):
    return n**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    #print(item)
    pass

# FUNÇÃO FILTER PARA FILTRAR UMA LISTA POR UMA FUNÇÃO

mnms = [1,2,3,4,5,6,7,8]

for item in map(ehPar, my_nums):
    #print(item)
    pass

for n in filter(ehPar, mnms):
    #print(n)
    pass

# enquanto o map retorna se é true ou false, o filter retorna uma lista só com os números que passam pelo filtro