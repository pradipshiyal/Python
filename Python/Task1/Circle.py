radius = int(input("Enter a radius of Circle: "))
pi = 3.14

def areaofCircle1():
    print("Area of Circle is ", pi * radius ** 2)
# areaofCircle1()

def areaofCircle2(radius):
    print("Area of Circle is ", pi * radius ** 2)
# areaofCircle2(radius)

def areaofCircle3():
    return pi * radius ** 2
# print("Area of Circle is ",areaofCircle3())

def areaofCircle4(radius):
    return pi * radius ** 2
print("Area of Circle is ",areaofCircle4(radius))