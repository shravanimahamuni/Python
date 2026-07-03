# Write a program which accepts one number and prints binary equivalent.

def Binary(no):
    binary = ""

    while no > 0:
        binary = str(no % 2) + binary
        no = no//2

    print(binary)

Binary(10)