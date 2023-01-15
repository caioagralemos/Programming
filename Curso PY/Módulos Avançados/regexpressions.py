import re

texto = "O telefone do rapaz é (82) 99980-0020. Ligue agora!"

padrao = "telefone"

match = re.search(padrao, texto)
print(match)
# <re.Match object; span=(2, 10), match='telefone'>

padrao = "nao esta no texto"

print(re.search(padrao,texto))
# None

match.span()
# (2, 10)

match.start()
# 2

match.end()
# 10

texto = "meu telefone aqui, meu telefone ali"

padrao = "telefone"

match = re.search(padrao, texto)
print(match) # retorna apenas o primeiro

matches = re.findall(padrao, texto)
print(matches)
len(matches)
# 2

for match in re.finditer(padrao, texto):
    print(match.span())

texto = "O telefone do rapaz é 82 99980-0020. Ligue agora!"

celular = re.search(r'\d{2}\s\d{4,5}-\d{4}', texto)
print(celular.group())

padrao_celular = re.compile(r'(\d{2})\s(\d{4,5})-(\d{4})')

celular = re.search(padrao_celular, texto)
print(celular.group(1))

# Extras

re.search(r'gato|cachorro', 'o gato tá aqui') # | == ou
# <re.Match object; span=(2, 6), match='gato'>

re.findall(r'.ato', 'o rato que morava no sapato foi comido pelo gato') # . == wildcard
# ['rato', 'pato', 'gato']

print(re.findall(r'^\d|\d$', '2 é um número')) # verificando se inicia ou termina com número
# ['2']

frase_num = "quero remover todos os 3 números 1 e 2 que coloquei nessa frase"

padrao_rmvnum = r'[^\d]+'

frase_num = re.findall(padrao_rmvnum, frase_num)

print(''.join(frase_num))