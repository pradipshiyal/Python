# 19) WAP to extract vowels and store in dict
# why nested loop ?
#  - ietarate between nested collection
#  - compare two values
List = ["hi", "hello", "hehehehe", "python"]
i = 0
res = {}

while i < len(List):
    j = 0
    count = ""
    subStar = List[i]

    while j < len(subStar):
        if subStar[j] in "aeiouAEIOU":
            count += subStar[j]
        j += 1
    res[List[i]] = count
    i += 1

print(res)