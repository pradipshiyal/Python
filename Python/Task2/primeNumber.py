def primeNumber(number):
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1

n = int(input("Enter a number: "))

if primeNumber(n):
    print("Prime")
else:
    print("Not Prime")
        