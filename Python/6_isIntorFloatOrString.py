# 6) WAP to check whether the given number is Int, Float, or String
number = eval(input("Enter some value: "))
if type(number) == int:
    print("It is an Integer.")
elif type(number) == float:
    print("It is an Float.")
elif type(number) == str:
    print("It is an String.")
else:
    print("Invailid Datatype")