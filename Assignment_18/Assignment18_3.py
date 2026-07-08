# Write a program which accepts N number from user and store it into list. Return minimum number from that list.

def Minimum(Data):
    Min = Data[0]

    for no in Data:
        if no < Min:
            Min = no

    return Min

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = Minimum(Data)

    print("Minimum number is :",Ans)

if __name__=="__main__":
    main()