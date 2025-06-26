# 14) wap to check which quadrant does the coordinates belongs
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

if x > 0 and y > 0:
    print("The point is in the First quadrant")
elif x < 0 and y > 0:
    print("The point is in the Second quadrant")
elif x < 0 and y < 0:
    print("The point is in the Third quadrant")
elif x > 0 and y < 0:
    print("The point is in the Fourth quadrant")
elif x == 0 and y == 0:
    print("The point is at the origin")
elif x == 0:
    print("The point lies on the Y-axis")
elif y == 0:
    print("The point lies on the X-axis")
else:
    print("Invalid Inputs")