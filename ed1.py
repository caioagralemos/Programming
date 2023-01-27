lista1 = set()
lista1.add(1)
lista1.add(2)
lista1.add(5)
lista2 = set()
lista2.add(3)
lista2.add(4)
lista2.add(5)

print(lista1, lista2)

print(f"União: {lista1.union(lista2)}")
print(f"Interseção: {lista1.intersection(lista2)}")
print(f"Complemento: {lista1.difference(lista2)}")