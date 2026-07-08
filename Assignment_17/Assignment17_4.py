# write a program which accept one number form user and return addition of its factors.

def AddFactors(no):
    sum = 0

    for i in range(1,no):
     if no % i == 0:
        sum = sum + i

    return sum

ret = AddFactors(12)
print(ret)
