# Write a program which accepts one number from user and return its factorial.

def Factorial(no):
    fact = 1

    for i in range(1,no + 1):
        fact = fact * i

    return fact

ret = Factorial(5)
print(ret)