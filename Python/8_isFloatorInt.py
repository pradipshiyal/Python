# 8) WAP to check whether the given input is Float or Int
number = eval(input("Enter a number: "))
if type(number) == int:
    print("It is a Integer Number.")
else:
    print("It is a Float Number.")