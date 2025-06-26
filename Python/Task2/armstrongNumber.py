def armstrongNumber(number):
    i = number
    res = 0

    while number > 0:
        rem = number % 10
        res = res + rem ** len(str(i))
        number //= 10

    return res

# n = int(input("Enter a number: "))
# if n == armstrongNumber(n):
#     print("Armstrong number")
# else:
#     print("Not a Armstrong number")

list1 = [145, 153, 255, 378, 40585, 371]

for i in list1:
    if armstrongNumber(i) in list1:
        print(f"{i} is Armstrong")