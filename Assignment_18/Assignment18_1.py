# Write a program which accepts N number from user and store it into list. Return addition of all elements from that list.

def ListAdd(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = ListAdd(Data)

    print("Addition is :",Ans)

if __name__=="__main__":
    main()