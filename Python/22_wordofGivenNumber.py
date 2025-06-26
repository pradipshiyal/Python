# 22) WAP to print the word of given number

n = int(input("Enter a number: "))
digits = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
res = ""
i = n

while n > 0:
    rem = n % 10
    res = digits[rem] + ' ' + res
    n //= 10

print(res) 