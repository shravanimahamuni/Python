# Write a program which accepts N number from user and store it into list. Return maximum number from that list.

def Maximum(Data):
    Max = Data[0]

    for no in Data:
        if no > Max:
            Max = no

    return Max

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = Maximum(Data)

    print("Maximum number is :",Ans)

if __name__=="__main__":
    main()