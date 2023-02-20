string = input("passe uma string: ").lower()
tamanho = len(string)
contador = 0

for i in range(0,tamanho):
    if (string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "e" or string[i] == "u"):
        contador = contador + 1
    else:
        pass

print(contador)
