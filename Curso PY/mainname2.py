import mainname1 as one

print("Top level in mainname2.py")

one.func()

if __name__ == "__main__":
    print("mainname2.py está sendo executado diretamente!")
else:
    print("mainname2.py foi importado!")