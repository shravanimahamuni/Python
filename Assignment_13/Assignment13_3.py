# Write a program which accepts one number and checks whether it is perfect number or not

def ChkPerfect(no):
    sum = 0

    for i in range(1, no):
        if no % i == 0:
            sum = sum + i

    if sum == no:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

ChkPerfect(6)