def print_P():
    for i in range(7):
        for j in range(5):
            if j == 0 or (i == 0 or i == 3) and j < 4 or (j == 4 and i < 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

def print_R():
    for i in range(7):
        for j in range(5):
            if j == 0 or (i == 0 or i == 3) and j < 4 or (j == 4 and i < 3) or (i - j == 3 and i > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

def print_A():
    for i in range(7):
        for j in range(5):
            if j == 0 or j == 4 or i == 0 or i == 3:
                if i == 0 and (j == 0 or j == 4):
                    print(" ", end="")
                else:
                    print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

def print_D():
    for i in range(7):
        for j in range(5):
            if j == 0 or (j == 4 and i != 0 and i != 6) or (i == 0 or i == 6) and j < 4:
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

def print_I():
    for i in range(7):
        for j in range(5):
            if i == 0 or i == 6 or j == 2:
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

def print_name():
    for i in range(7):
        # Each print function handles its own line
        for j in range(5):
            if j == 0 or (i == 0 or i == 3) and j < 4 or (j == 4 and i < 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        for j in range(5):
            if j == 0 or (i == 0 or i == 3) and j < 4 or (j == 4 and i < 3) or (i - j == 3 and i > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        for j in range(5):
            if j == 0 or j == 4 or i == 0 or i == 3:
                if i == 0 and (j == 0 or j == 4):
                    print(" ", end="")
                else:
                    print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        for j in range(5):
            if j == 0 or (j == 4 and i != 0 and i != 6) or (i == 0 or i == 6) and j < 4:
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        for j in range(5):
            if i == 0 or i == 6 or j == 2:
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        for j in range(5):
            if j == 0 or (i == 0 or i == 3) and j < 4 or (j == 4 and i < 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Call function to print PRADIP
print_name()
