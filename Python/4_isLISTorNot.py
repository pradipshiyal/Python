# 4) WAP to check whether is given input is LIST or not
list1 = eval(input("Enter a List: "))
if type(list1) == list:
    print("It is a List")
else:
    print("It is NOT a list.")