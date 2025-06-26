# 16) WAP to check whether the given character is is Vowel or Consonant
string = input("Enter a single Character: ")
if len(string) == 1:
    if (string in "aeiouAEIOU"):
        print(f"{string} is Vowel")
    else:
        print(f"{string} is Consonant")
else:
    print("Length should be one")