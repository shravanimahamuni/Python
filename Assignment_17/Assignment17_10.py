# write a program which accept number from user and retur addition of digits in that number.

def SumDigits(no):
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    return sum

ret = SumDigits(5187934)
print(ret)