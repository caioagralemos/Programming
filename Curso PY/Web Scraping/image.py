
import bs4, requests

resposta = requests.get("https://pt.wikipedia.org/wiki/Lionel_Messi")

soup = bs4.BeautifulSoup(resposta.text, 'lxml')

images = soup.select('.thumbimage')

image = images[1]

image_link = requests.get(f"https:{image['src']}")

f = open ("messi.jpeg", "wb") #wb = write binary
f.write(image_link.content)
f.close()
