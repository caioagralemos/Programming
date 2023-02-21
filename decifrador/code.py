alfabeto = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'x': 23,
    'w': 24,
    'y': 25,
    'z': 26}

arrayalfa = ['zero','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']

txtfilename = input("input the name of your file: ")
cypher = int(input("input your coding cypher: "))
f = open(txtfilename)
txt = f.read().lower()
txt = list(txt)


for i in range(0,len(txt)):
    if txt[i] == " " or txt[i] == "." or txt[i] == "," or txt[i] == "\n":
        pass
    else:
        novo = alfabeto[str(txt[i])] + cypher
        txt[i] = novo
        txt[i] = arrayalfa[txt[i]]

txt = ''.join(txt)

f = open("coded.txt", "w")
f.write(txt)

