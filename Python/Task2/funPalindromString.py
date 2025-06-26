def palindromString(string):
    string = string.split()
    temp = []

    for i in string:
        if i == i[::-1]:
            temp.append(i)        
    return temp

s = "my mom and dad are soo cool"
print(palindromString(s))