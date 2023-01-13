from random import shuffle

mylist = ["0", " ", " "]

def shuffle_list(list):
    shuffle(mylist)
    return mylist

mylist = shuffle_list(mylist)

def guess():
    guess = input("Pick a number: 0, 1 or 2: ")
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1 or 2: ")
    return guess

player_guess = int(guess())

def game(copos, chute):
    if mylist[player_guess] == "0":
        print("You got it right")
        print(mylist)
    else:
        print("Wrong answer baby")
        print(mylist)

game(mylist, player_guess)