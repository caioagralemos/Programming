class Animal():

    def __init__(self):
        print('Animal criado.')

    def quemsou(self):
        print("Eu sou um animal.")
    
    def comer(self):
        print('Estou comendo')

    def cagar(self):
        print('Estou cagando')

    def dormir(self):
        print('ZzZzZzzzzzz...')

class Cachorro(Animal):

    especie = "Cachorro"
    classe = "Mamífero"
    nome_cientifico = "Canis lupus familiaris"
    estadoente = False

    def __init__(self, nome, raca, idade):
        Animal.__init__(self)
        print("Cachorro criado.")
        self.nome = nome
        self.raca = raca
        self.idade = idade

        if idade <= 1:
            self.idadeemhumano = 9
        elif idade > 1 and idade <= 2:
            self.idadeemhumano = 24
        elif idade > 2:
            self.idadeemhumano = 24 + (5*(idade-2))

# É POSSIVEL DAR OVERWRITE SÓ POR ESCREVER UMA NOVA FUNÇÃO COM O MESMO NOME DA ORIGINAL
    def quemsou(self):
        print("Eu sou um cachorro.")

    def bark(self):
        print(f"au au! (tradução: meu nome é {self.nome})")
    
    def doente(self):
        self.estadoente = True

    def curado(self):
        self.estadoente = False
    
    def falar(self):
        print(self.nome + " diz au!")

class Gato(Animal):

    especie = "Gato"
    classe = "Mamífero"
    nome_cientifico = "Felis catus"

    def __init__(self, nome, raca, idade):
        Animal.__init__(self)
        print("Gato criado.")
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def falar(self):
        print(self.nome + " diz miau!")




cao = Cachorro(nome = "Luke", raca= "Bulldog Francês", idade= 6)

cao.bark()

cao.cagar()

cao.quemsou()

if cao.estadoente == True:
    print(f"Ligar para dono do {cao.raca} {cao.nome}")

print(cao.idadeemhumano)

gatito = Gato(nome= "Feli", raca= "Persa", idade=4)

# perceba que eu criei dois metodos com o mesmo nome em diferentes classes

cao.falar()
gatito.falar()

# esse é um exemplo de polimorfismo, onde é possível criar dois metodos com o mesmo nome mas partindo de
# diferentes classes. Cachorro.falar() é diferente de Gato.falar(), apesar do mesmo nome.