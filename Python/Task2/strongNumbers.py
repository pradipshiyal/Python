def strongNumber(number):
    res = 0
    for i in str(number):
        fact = 1
        for j in range(1, int(i) + 1):
            fact *= j
        res += fact

    return res

# n = int(input("Enter a number: "))
# if n == strongNumber(n):
#     print("Strong Number")
# else:
#     print("Not Strong Number")

list1 = [145, 153, 255, 378, 40585, 371]

for i in list1:
    if strongNumber(i) in list1:
        print(f"{i} is strong")