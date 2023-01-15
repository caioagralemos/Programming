import os, re

dir = "/Users/macbook/Desktop/Desafio/ok/extracted_content"

for subdir, dirs, files in os.walk(dir):
    for file in files:
        f = open(f"{subdir}/{file}", 'r')
        f = f.read()
        #print(f"Currently looking at {file}")
        padrao = r"\d\d\d-\d\d\d-\d\d\d\d"
        celular = re.search(padrao, str(f))
        print(celular, file)