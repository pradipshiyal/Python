length = int(input("Enter a length: "))
width  = int(input("Enter a width: "))

def areaofRectangle1():
    print("Area of Rectangle is ", length * width)
# areaofRectangle1()

def areaofRectangle2(length, width):
    print("Area of Rectangle is ", length * width)
# areaofRectangle2(length, width)

def areaofRectangle3():
    return length * width
# print("Area of Rectangle is ", areaofRectangle3())

def areaofRectangle4(length, width):
    return length * width
print("Area of Rectangle is ", areaofRectangle4(length, width))