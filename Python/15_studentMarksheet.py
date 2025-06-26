# 15) WAP to check the result of given marks
per = float(input("Enter your Marks: "))

if per >= 90 and per <=100:
    print("Distinction")
elif per >= 75 and per<90:
    print("First class")
elif per >= 60 and per < 75:
    print("Second class")
elif per >= 35 and per < 60:
    print("Third class")
elif per >= 0 and per <35:
    print("Fail")
else:
    print("Invalid Marks")