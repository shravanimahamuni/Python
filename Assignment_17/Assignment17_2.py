# Write a program which accept one number and display below pattern.

def Pattern(no):
    for i in range(no):
        for j in range(no):
            print("*", end="")
        print()

Pattern(5)