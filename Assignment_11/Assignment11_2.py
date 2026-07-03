# Write a program which accepts one number amd prints count of digital in that number

def CountDigits(no):
    count = 0

    while no > 0:
        count = count + 1
        no = no//10

    print(count)

CountDigits(7521)