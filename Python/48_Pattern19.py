# 1        
# 2 3      
# 4 5 6    
# 7 8 9 10 

n = 5
n2 = 1

for i in range(1, n + 1):
    for j in range(1, i):
        print(n2, end = " ")
        n2+=1
    print()
