# Write a program  which accepts one number and checks whether it is prime or not .

def ChkPrime(no):
    flag = True

    for i in range(2,no):
        if no % i == 0:
            flag = False
            break

    if flag == True:
        print("Prime number")
    else:
        print("Not Prime Number")

ChkPrime(11)