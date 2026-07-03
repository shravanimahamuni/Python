# Write a program which accepts one number and prints reverse of that number

def Reverse(no):
    rev = 0

    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no//10

    print(rev)

Reverse(123)