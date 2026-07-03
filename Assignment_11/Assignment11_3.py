# Write a program which accepts one number and prints sum of digits.

def SumDigits(no):
    sum = 0 

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no//10

    print(sum)

SumDigits(123)