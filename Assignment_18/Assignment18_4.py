# Write a program which accept N numbers from user and store it into List. Accept one another number, from user and return frequency of that number from List.

def Frequency(Data, Value):
    Count = 0

    for no in Data:
        if no == Value:
            Count = Count + 1

    return Count

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Search = int(input("Enter element to search : "))

    Ans = Frequency(Data, Search)

    print("Frequency is: ",Ans)

if __name__=="__main__":
    main()