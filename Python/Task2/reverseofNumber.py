def reveseofNumber(number):
    res = ""
    for  i in range(len(str(number))-1, -1, -1):
        res += str(number)[i]

    return res

value = int(input("Enter a number: "))
print(reveseofNumber(value))