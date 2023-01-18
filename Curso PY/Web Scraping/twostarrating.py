import bs4, requests

for x in range(1,51):
    resposta = requests.get(f'http://books.toscrape.com/catalogue/page-{x}.html')

    soup = bs4.BeautifulSoup(resposta.text, 'lxml')

    produtos = soup.select('.product_pod')

    lista2star = []

    for x in range(0,20):
        livro = produtos[x]

        if livro.select(".star-rating.Two") != []:
            print(livro.select("a")[1]['title'])
        else:
            pass
        
#print(exemplo.select(".star-rating.Two")) # checkando se tem 2 estrelas
#print(exemplo.select("a")[1]['title']) # pegando o titulo do livro