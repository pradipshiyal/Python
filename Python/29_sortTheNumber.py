l = [4, 1, 3, 5, 2]
temp = 0

for i in range(len(l)):
    for  j in range(len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]

# print(set(l))
print(l)