# 11) WAP to check whether the given String is palindrome or not
string = input("Enter a string: ")
if string == string[::-1]:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")