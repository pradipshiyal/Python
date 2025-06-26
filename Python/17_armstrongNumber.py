# 17) WAP to print armstrong number
n = int(input("Enter a number: "))
i = n
res = 0

while n > 0:
    rem = n % 10
    res = res + rem ** len(str(i))
    n //= 10

if res == i:
    print("Armstrong number")
else:
    print("Not a Armstrong number")