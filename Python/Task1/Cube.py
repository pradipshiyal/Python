value = int(input("Enter a Value: "))

def areaofCube1():
    print("Area of Cube is ", 6 * value ** 2)
# areaofCube1()

def areaofCube2(value):
    print("Area of Cube is ", 6 * value ** 2)
# areaofCube2(value)

def areaofCube3():
    return 6 * value ** 2
# print("Area of Cube is ",areaofCube3())

def areaofCube4(value):
    return 6 * value ** 2
print("Area of Cube is ",areaofCube4(value))