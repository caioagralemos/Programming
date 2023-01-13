 # keyword in

boolean = 'a' in 'a world'
print(boolean)

#func min e max
mylist = [10, 20, 30, 40, 50]
print(min(mylist))
print(max(mylist))

# botar string em lista
mystring = 'Hello'
mylist = [letter for letter in mystring]
print(mylist)

# criar lista de numero
mynumlist = [num for num in range(0,11)]
print(mynumlist)
mynumlist = [num*2 for num in range(0,11)]
print(mynumlist)
mynumlist = [num for num in range(0,11) if num % 2 == 0]
print(mynumlist)

# exemplo mais complexo
celsius = [0, 20, 32.5]
fahrenheit = [( (9/5) * temp + 32 ) for temp in celsius]

# outro exemplo
results = [x if x%2 == 0 else 'IMPAR' for x in range(0,11)]
print(results)

# metodo help
 # help(mylist.insert)