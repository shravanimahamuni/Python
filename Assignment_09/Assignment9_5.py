# Write a program which accepts one number and checks whether it is divisible by 3 & 5.

def ChkDivisible(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

ChkDivisible(15)