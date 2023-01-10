def soma(a, b, c=0, d=0, e= 0):
    return sum(a,b,c,d,e)

# no caso, a partir do terceiro parametro posicional (C), se define como
# zero por ser opcional para uma soma mais de dois digitos. porém, se
# tentarmos fazer uma soma maior que 5 digitos, a função retornará erro

#print(soma(1,2,3,4,5,6))

# para isso utilizamos o *arg, que pega quantos argumentos você quiser, e
# arranja numa tupla pra que a função funcione com todos os números

def myfunc(*num):
    return sum(num)

# print(myfunc(1,2,3,4,5,6,7,8,9,11))

# também existe o **kwargs, que arranja um dicionário (key, value) para
# todos os argumentos passados

def myfunc2(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print(f"A minha fruta favorita é {kwargs['fruit']}")
    else:
        print("Não encontrei nenhuma fruta por aqui")

# print(myfunc2(fruit='maça', veggie='batata'))

# trabalhando com os dois ao mesmo tempo

def myfunc3(*args, **kwargs):
    print(f"Eu gostaria de {args[0]} {kwargs['food']}")

myfunc3(2,3,4,5, fruit = "Laranja", food = "picanhas", animal = "cachorro")