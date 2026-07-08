# write a program which accept one number and display below pattern

def pattern(no):
    for i in range(no, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

pattern(5)

