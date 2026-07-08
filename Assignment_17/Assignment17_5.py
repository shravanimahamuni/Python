# write a program which accept one number for user and check whether number is prime or not

def ChkPrime(no):
    flag = True

    for i in range(2,no):
        if no % i == 0:
            flag = False
            break
    if flag == True:
        print("it is Prime number")
    else:
        print("it is Not Prime Number")

ChkPrime(5)