# uma Função de Generator permite retornar um valor e depois continuar a ser executada
# um exemplo de gerador é a função range, que guarda só seu inicio e seu fim (range nao retorna uma lista)

def create_cubes(n):

    for x in range(n):
        yield (x**3) # função yield só retorna algo quando é iterada, solta um número de cada vez para
    # não ser necessária a alocação de muita memória. é possivel usar list(create_cubes(n)) para obter
    # o resultado que uma função convencional obteria

print(create_cubes(10)) # note que esse print retorna apenas o endereço

for x in create_cubes(10):
    print(x)
