# EvenList and OddList

import threading

def EvenList(Data):
    Sum = 0

    for i in Data:
        if i % 2 == 0:
            Sum = Sum + i

    print("Sum of Even Numbers :", Sum)

def OddList(Data):
    Sum = 0

    for i in Data:
        if i % 2 != 0:
            Sum = Sum + i

    print("Sum of Odd Numbers :", Sum)

def main():

    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    T2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()