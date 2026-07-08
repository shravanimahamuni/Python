import Assignment18_5_1

def ListPrime(Data):
    Sum = 0

    for no in Data:
        if Assignment18_5_1.ChkPrime(no):
            Sum = Sum + no

        return Sum
    
def main():
    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements: ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = ListPrime(Data)

    print("Addition of Prime numbers is: ",Ans)

if __name__=="__main__":
    main()