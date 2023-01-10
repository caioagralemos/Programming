def myfunc(string):
    string = list(string)
    tam = len(string)
    cont = 0
    while cont < tam:
        if cont % 2 == 0:
            string[cont] = string[cont].upper()
        else:
            string[cont] = string[cont].lower()
        cont+=1
    string = ''.join(string)
    return string

print(myfunc("Paralelepipedo"))