import time # BIBLIOTECA TIME ------

def func_one(n):
    list = []
    for x in range(n):
        list.append(x)
    return list

def func_two(n):
    return list(map(str,range(n)))

# TEMPO ANTES DE COMEÇAR
start_time = time.time()
# EXECUTANDO O CÓDIGO
result = func_one(10000)
# TEMPO APÓS EXECUÇÃO
end_time = time.time()
# TEMPO GASTO
elapsed_time = end_time - start_time

print(f"Primeira func: {elapsed_time}")

# TEMPO ANTES DE COMEÇAR
start_time = time.time()
# EXECUTANDO O CÓDIGO
result = func_two(10000)
# TEMPO APÓS EXECUÇÃO
end_time = time.time()
# TEMPO GASTO
elapsed_time = end_time - start_time

print(f"Segunda func: {elapsed_time}")

import timeit # BIBLIOTECA TIMEIT ------

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    list = []
    for x in range(n):
        list.append(x)
    return list
'''

tempo200k = timeit.timeit(stmt, setup, number= 200000) # execucao, funcao, number = vezes que quer rodar o cod

print(tempo200k)