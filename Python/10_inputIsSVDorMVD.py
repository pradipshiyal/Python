# 10) WAP to check whether the given input is single value data type Or multi value data type
value = eval(input("Enter a Value: "))
if type(value) in (int, float, complex, bool):
    print("It is a Single Value Data Type.")
else:
    print("It is a Multi Value Data Type.")