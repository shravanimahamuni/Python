# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers

from functools import reduce

FilterX = lambda No : No % 2 == 0
MapX = lambda No : No * No
ReduceX = lambda A, B : A + B

def main():

    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    print("Input List :", Data)

    FData = list(filter(FilterX, Data))
    print("List after filter :", FData)

    MData = list(map(MapX, FData))
    print("List after map :", MData)

    Ans = reduce(ReduceX, MData)
    print("Output of reduce :", Ans)

if __name__ == "__main__":
    main()