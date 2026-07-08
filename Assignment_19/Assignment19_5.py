# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions

from functools import reduce

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

FilterX = lambda No : ChkPrime(No)
MapX = lambda No : No * 2
ReduceX = lambda A, B : A if A > B else B

def main():

    Data = [2, 70, 11, 10, 17, 23, 31, 77]

    print("Input List :", Data)

    FData = list(filter(FilterX, Data))
    print("List after filter :", FData)

    MData = list(map(MapX, FData))
    print("List after map :", MData)

    Ans = reduce(ReduceX, MData)
    print("Output of reduce :", Ans)

if __name__ == "__main__":
    main()