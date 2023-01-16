import requests
import bs4

result = requests.get('http://example.com')

soup = bs4.BeautifulSoup(result.text, 'lxml')

title = soup.select('title')[0].getText()

print(title)

paragrafos_site = soup.select('p')

print(paragrafos_site[0].getText)