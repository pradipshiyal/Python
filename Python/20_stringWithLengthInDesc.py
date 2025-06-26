# 20) WAP to store all the string in the given list with there length
List = ["hi", "hello", "hehehehe", "python"]
i = 0
res = {}

while i < len(List):
    res[List[i]] = len(List[i])
    i += 1

print(res)