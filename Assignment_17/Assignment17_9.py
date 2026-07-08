# Write a program which accept number from user and return number of digits in that number.

def CountDigits(no):
    count = 0 

    while no < 0:
        count = count + 1
        no = no // 10

    return count

ret = CountDigits(5187934)
print(ret)