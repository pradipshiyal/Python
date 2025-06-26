diagonal1 = int(input("Enter Diagonal 1 of Rhombus: "))
diagonal2 = int(input("Enter Diagonal 2 of Rhombus: "))
half   = 1 / 2

def areaofRhombus1():
    print("Area of Rhombus Is ", half * diagonal1 * diagonal2)
# areaofRhombus1()

def areaofRhombus2(diagonal1, diagonal2):
    print("Area of Rhombus Is ", half * diagonal1 * diagonal2)
# areaofRhombus2(diagonal1, diagonal2)

def areaofRhombus3():
    return half * diagonal1 * diagonal2
# print("Area of Rhombus Is ", areaofRhombus3())

def areaofRhombus4(diagonal1, diagonal2):
    return half * diagonal1 * diagonal2
print("Area of Rhombus Is ", areaofRhombus4(diagonal1, diagonal2))