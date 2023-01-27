class Produto:

    def __init__(self, _item, _id, _preco, _quantidade):
        print("Item criado.")
        self._item = _item
        self._id = _id
        self._preco = _preco
        self._quantidade =_quantidade

    def __str__(self):
        return f"ID do produto: {self._id}\nTipo do produto: {self._item}\nPreço do produto: R$ {self._preco}.00\nQuantidade de itens em estoque: {self._quantidade}"

    def id(self):
        return self._id
    
    def item(self):
        return self._item
    
    def preco(self):
        return f"R$ {self._preco}.00"
    
    def quantidade(self):
        return self._quantidade
    
biscoito = Produto('Cookies Bauducco',1,8,150)
sorvete = Produto("Sorvete Bacio de Latte - SABOR CHOCOLATE", 2, 30, 30)

print(f"\n{biscoito}\n\n{sorvete}")

print(biscoito.preco())