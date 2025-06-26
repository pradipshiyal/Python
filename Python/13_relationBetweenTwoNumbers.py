# 13) WAP to check relation between two numbers
number1 = float(input("Enter a Number 1: "))
number2 = float(input("Enter a Number 2: "))

if number1 == number2:
    print("Both numbers are equal.")
elif number1 > number2:
    print(f"{number1} is greater than {number2} number.")
elif number1 < number2:
    print(f"{number1} is Less than {number2} number.")
else:
    print("Invailid input")