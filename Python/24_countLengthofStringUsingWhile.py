# 24) WAP to count length of string without using len() function
text = input("Enter a string: ")
count = 0

while text[count:count + 1] != "":
    count +=1

print(count)