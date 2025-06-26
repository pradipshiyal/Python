radius = int(input("Enter a radius of Sphere: "))
pi = 3.14

def areaofSphere1():
    print("Area of Sphere is ", 4 * pi * radius ** 2)
# areaofSphere1()

def areaofSphere2(radius):
    print("Area of Sphere is ", 4 * pi * radius ** 2)
# areaofSphere2(radius)

def areaofSphere3():
    return 4 * pi * radius ** 2
# print("Area of Sphere is ",areaofSphere3())

def areaofSphere4(radius):
    return 4 * pi * radius ** 2
print("Area of Sphere is ",areaofSphere4(radius))