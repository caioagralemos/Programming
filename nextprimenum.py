numlist = []

for num in range(2,1001):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        numlist.append(num)

n = 0

while True:
    next = input("press ! to get your next number or anything else to quit: ")
    if next == "!":
        print(f"your {n} prime number: {numlist[n]}")
        n = n + 1
    else:
        pass
