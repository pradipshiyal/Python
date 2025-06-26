# 5) WAP to check whether the given input is string or list
data = eval(input("Enter some value: "))
if type(data) == str:
    print("It is a String")
elif type(data) == list:
    print("It is a List")
else:
    print("Invailid Input")