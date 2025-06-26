l = ["demo.py", "file1.txt", "numPy.py", "google.com", "sample.py", "file2.txt"]
result = {}  

# for i in l:  
#     parts = i.split('.')  
#     if len(parts) == 2:
#         name, ext= parts

#         if ext not in result:
#             result[ext] = []
        
#         result[ext].append(name)

# print(result)  

for i in l:
    s = i.split(".")
    if s[-1] not in result:
        result[s[-1]] = []
    result[s[-1]].append(s[0])

print(result)