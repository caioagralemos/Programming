import bs4, requests

resposta = requests.get('https://relogioonline.com.br/horario/bras%C3%ADlia/')

soup = bs4.BeautifulSoup(resposta.text, 'lxml')
noscript = soup.select("#lbl-time noscript")
time = str(noscript[0])[10: 18]
print(time)