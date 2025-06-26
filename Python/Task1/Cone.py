radius = int(input("Enter a radius of Cone: "))
slantHeight = int(input("Enter a slant height of Cone: "))
pi = 3.14

def areaofCone1():
    print("Area of Cone is ", pi * radius * slantHeight + pi * radius ** 2)
# areaofCone1()

def areaofCone2(radius):
    print("Area of Cone is ", pi * radius * slantHeight + pi * radius ** 2)
# areaofCone2(radius)

def areaofCone3():
    return pi * radius * slantHeight + pi * radius ** 2
# print("Area of Cone is ",areaofCone3())

def areaofCone4(radius):
    return pi * radius * slantHeight + pi * radius ** 2
print("Area of Cone is ",areaofCone4(radius))