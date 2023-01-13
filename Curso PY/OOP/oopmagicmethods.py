# os magic methods são configurações de como a classe trabalha se executada em metodos padrões do py como
# print(inst_de_classe), len(inst_de_classe), str(inst_de_classe)

class Livro():

    def __init__(self,titulo,autor,pags):
        self.titulo = titulo
        self.autor = autor
        self.pags = pags
    
    def __str__(self): # agora, quando tentarem converter book p string, retorna isso (print ou str)
        return f"{self.titulo} de {self.autor}"
    
    def __len__(self): # agora, quando tentarem usar a funcao len(), retorna isso
        return self.pags
    
    # def __del__(self): # agora, quando tentarem converter book p string, retorna isso (print ou str)
        # print("Livro deletado")
    
mnn = Livro(titulo="Morte no Nilo", autor= "Agatha Christie", pags= 255)

print(mnn)
print(len(mnn))