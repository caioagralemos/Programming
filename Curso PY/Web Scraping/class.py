import bs4, requests

resposta = requests.get('https://pt.wikipedia.org/wiki/The_Last_of_Us_(franquia)')

soup = bs4.BeautifulSoup(resposta.text, 'lxml')

for item in soup.select('.mw-content-container'):
    print(item.text)

