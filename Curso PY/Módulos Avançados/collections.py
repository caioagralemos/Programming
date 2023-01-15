# Função COUNTER -------------

from collections import Counter

mylist = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3]

listcounter = Counter(mylist)

#print(listcounter)

frase = "Eu quero fazer uma frase que o counter possa contar a quantidade de vezes que eu escrevi cada palavra contida nesta mesma frase"

wordscount = Counter(frase.lower().split())

#print(wordscount)

letras = 'aaaaaaaaaaabbbbbbbbbbbbcccccccccccccccddddddddddddd'

c = Counter(letras)

print(c)

# Funções mais comuns de serem utilizadas com o método counter --

#print(list(c)) # cria uma lista sem repetição de elementos
#print(dict(c)) # converte em um dicionário
print(c.most_common()[::-1]) # lista os elementos menos comuns
c += Counter() # remove contagens zero e negativos

# Função DEFAULTDICT -------------

from collections import defaultdict

d = defaultdict(lambda: 0) # define um valor padrão para qualquer chave que não for atribuida um valor
d["correct"] = 100
print(d["wrong"])  
print(d)

# Função NAMEDTUPLE -------------

from collections import namedtuple

Dog = namedtuple('Dog',['age', 'breed','name'])

godo = Dog(age=6,breed='French Bulldog', name='Luke')

print(godo.name)
