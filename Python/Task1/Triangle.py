base   = int(input("Enter Base of Triangle: "))
height = int(input("Enter Height of Triangle: "))
half   = 1 / 2

def areaofTriangle1():
    print("Area of Triangle Is ", half * base * height)
# areaofTriangle1()

def areaofTriangle2(base, height):
    print("Area of Triangle Is ", half * base * height)
# areaofTriangle2(base, height)

def areaofTriangle3():
    return half * base * height
# print("Area of Triangle Is ", areaofTriangle3())

def areaofTriangle4(base, height):
    return half * base * height
print("Area of Triangle Is ", areaofTriangle4(base, height))