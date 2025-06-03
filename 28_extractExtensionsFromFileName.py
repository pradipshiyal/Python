l = ["demo.py", "file1.txt", "numPy.py", "google.com", "sample.py", "file2.txt"]
result = {}  

for i in l:  
    parts = i.split('.')  
    if len(parts) == 2:
        name, ext= parts

        if ext not in result:
            result[ext] = []
        
        result[ext].append(name)

print(result)  
