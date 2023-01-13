# usar name == main serve para descobrir se um arquivo está sendo executado diretamente ou sendo importado

from colorama import Fore

def func():
    print("FUNC() IN mainname1.py")

print("Top level in mainname1.py")

def func_especifica():
    print("Essa função só será executada se esse programa for executado diretamente")

if __name__ == '__main__':
    print(Fore.BLUE + 'mainname1.py está sendo executado diretamente!')
    func_especifica()
else:
    print(Fore.RED + 'mainname1.py foi importado!')