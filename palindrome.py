string = input("passe uma string: ")
inverse = string[::-1]

if string == inverse:
    print("Palindrome!")
else:
    print("Not palindrome")