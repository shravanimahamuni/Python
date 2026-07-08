# Maximum and minimum From List

import threading

def Maximum(Data):
    print("Maximum element :", max(Data))

def Minimum(Data):
    print("Minimum element :", min(Data))

def main():

    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target=Maximum, args=(Data,))
    T2 = threading.Thread(target=Minimum, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()