#         *
#       *   *
#     *   *   *
#   *   *   *   *        
# *   *   *   *   *   

n = 5
rows = 5
cols = 9

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if i + j >= rows + 1 and j - i <= rows - 1 and (i + j) % 2 == 0:
            print("*", end =" ")
        else:
            print(" ", end =" ")
    print()
