# write a program which accepts one number and prints its factors.

def Factors(no):
    for i in range(1, no + 1):
        if no % i == 0:
            print(i)

Factors(12)