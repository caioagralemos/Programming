import csv

data = open('example.csv')

# lendo o arquivo csv
csv_data = csv.reader(data)
# convertendo o arquivo em uma lista
data_lines = list(csv_data)

for n in range(1,1001):
    # print(f"id: {data_lines[n][0]} name: {data_lines[n][1]} {data_lines[n][2]}")
    pass # funcao que printa todos os nomes completos e os ids das pessoas com os dados contidos no csv

emails = []

for x in range(1,1001):
    emails.append(data_lines[x][3])
    # criando lista com todos os emails

arquivo_saida = open("lista_emails.txt", "w",newline= '')
csv_writer = csv.writer(arquivo_saida, delimiter="\n") #delimiter e newline funcionam como delimitadores de espaço
csv_writer.writerow(emails)
arquivo_saida.close()
