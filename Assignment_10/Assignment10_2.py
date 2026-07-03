# Write a program which accepts one number and prints sum of first N natural number

def Sum(no):
    total = 0

    for i in range(1,no + 1):
        total = total + i

    return total

ret = Sum(5)
print(ret)