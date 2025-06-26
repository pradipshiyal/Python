# l = ["hi", "car", "racecar", "malayalam", "hello"]
# for i in l:
#     if i == i[::-1]:
#         print(f"{i} is Palindrome")
#     else:
#         print(f"{i} is not a Palindrome")

# --------------------------------------------------------------------
# number = int(input("Enter a number: "))
# temp = 1
# for i in range(1, number + 1):
#     temp *= i
# print(temp)

# --------------------------------------------------------------------
# n = 10
# n1 = 0
# n2 = 1

# for i in range(n):
#     n3 = n1 + n2
#     print(n1, end=' ')
#     n1, n2 = n2, n3

# --------------------------------------------------------------------
# n = 10
# n1 = 0
# n2 = 1

# print(n1, n2, end=' ')
# for i in range(n):
#     n3 = n1 + n2
#     print(n3, end=' ')
#     n1, n2 = n2, n3

# --------------------------------------------------------------------
# remove duplicates from the list
# l = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# l = [1, 3, 2, 3, 6, 7, 1, 2, 4, 9]
# res = []

# for i in l:
#     if i not in res:
#         res.append(i)
# res.sort()
# print(res)

# --------------------------------------------------------------------
# store even numbered string into another list
# l = ["hi", "hello", "you?", "how"]
# res = []

# for i in l:
#     if len(i) % 2 == 0:
#         res.append(i)

# print(res)

# --------------------------------------------------------------------
# string = input("Enter a string: ")
# string1 = ""

# for i in string:
#     if i == " ":
#         i = "_"
#     string1 += i
# print(string1)

# --------------------------------------------------------------------
# l = ["Boat", "Python", "en", "String"]
# out = {}

# for i  in l:
#     out[i] = i[0] + i[-1]

# print(out)

# --------------------------------------------------------------------
# l = [1, (2+3j), "hey", 3.147528, "hello"]
# out = []

# for i in l:
#     if isinstance(i, str):
#     # if type(i) == str:
#         out.append(i)


# print(out)

# --------------------------------------------------------------------
# l = ["hi", "how", "are", "you?"]
# # output = "hi hw ar y?"
# res = ""
# for i in l:
#     res += i[0] + i[-1] + " "

# print(f'"{res}"')

# -------------------------------------------------------------------- working
# l = ["demo.py", "file1.txt", "goggle.com", "sample.py", "file2.txt"] 
# output = {"py": ["demo", "sample"], "txt": ["file1", "file2"], "com": ["google"]}
# res = {}

# for  i in l:
    # temp = i.split(".")
    # list1 = []
    # res[temp[-1]] = [temp[0]]
    # print(temp)  

# print(res)
    
# -------------------------------------------------------------------- 
# l = [1, "Program", 2.5, True, "Hello"]
# res = {}

# for i in l:
#     if isinstance(i, str):
#         vow = ""
#         for j in i:
#             if j in "aeiouAEIOU":
#                 vow += j
#         res[i] = vow

# print(res)        
# -------------------------------------------------------------------- 
# l = [1, "Program", 2.5, True, "Hello"]
# res = {}

# for i in l:
#     if isinstance(i, str):
#         notVow = ""
#         for j in i:
#             if j not in "aeiouAEIOU":
#                 notVow += j
#         res[i] = notVow

# print(res)
# -------------------------------------------------------------------- 
# s = "Malayalam"
# res = {}

# for  i in s:
#     count = 0
#     for j in s:
#         if i == j:
#             count += 1
#     res[i] = count

# print(res)
# -------------------------------------------------------------------- 

# l = [4, 1, 3, 5, 2]
# temp = 0

# for i in range(len(l)):
#     for  j in range(len(l)):
#         if l[i] < l[j]:
#             temp = l[i]
#             l[i] = l[j]
#             l[j] = temp

# # print(set(l))
# print(l)

# l = [4, 1, 3, 5, 2]
# temp = 0

# for i in range(len(l)):
#     for  j in range(len(l)):
#         if l[i] < l[j]:
#             l[i], l[j] = l[j], l[i]

# # print(set(l))
# print(l)
# -------------------------------------------------------------------- 

# myRange = range(1, 3 + 1)
# myList = []

# for i in myRange:
#     for j in myRange:
#         myList.append([i,j])

# print(myList)

# -------------------------------------------------------------------- 

# a = 10
# b = 20
# print(a, b)
# def demo():
#     global a, b
#     print(a, b)
#     a, b = 100, 200
#     print(a, b)

# print(a, b)
# demo()
# print(a, b)

# -------------------------------------------------------------------- 
# n = 5
# def demo(n, res = 0):
#     if n == 0:
#         return res
    
#     res += n
#     return demo(n - 1, res)

# print(demo(n))

# -------------------------------------------------------------------- 
# n = 5
# num1 = 0
# num2 = 1

# def demo(n):
#     global num1, num2
#     if n < 1:
#         return
#     num3 = num1 + num2
#     print(num1)
#     num1, num2 = num2, num3
#     demo(n - 1)
# demo(n)

# -------------------------------------------------------------------- 
# reverse a number 
# n = 123
# n = 1500
# def demo(n, rev = 0):
#     if n == 0:
#         return rev
#     rem = n % 10
#     rev = rev * 10 + rem    
#     return demo(n // 10, rev)
# print(demo(n))

# -------------------------------------------------------------------- 
# wap to add all the digit in the given number if 123 then 6
# n = 12356
# def demo(n, sum1 = 0):
#     if n == 0:
#         return sum1
#     rem = n % 10    
#     return demo(n // 10, sum1 + rem)
# print(demo(n))
