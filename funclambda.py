# Funções lambda são como funções comuns, mas que são escritas para serem usadas uma única vez
# Por isso, elas são escritas de uma maneira mais enxuta, para caberem em métodos como map ou filter

mynums = [1,2,3,4,5]

# o jeito comum de pegar essa lista ao quadrado seria o seguinte:

def square(n):
    return n**2

#mynums = list(map(square,mynums))

print(mynums)

# porém, caso essa lista fosse a única vez que fossemos pegar algum número ao quadrado, fariamos assim:

mynums = list(map(lambda num: num**2,mynums))

print(mynums)

# ou seja, é um jeito de fazer uma função caber em uma linha, caso ela só seja usada uma vez