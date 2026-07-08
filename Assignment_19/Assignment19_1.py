# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.

Power = lambda No : 2 ** No

def main():
    Value = int(input("Enter number : "))

    Ans = Power(Value)

    print("Output :", Ans)

if __name__ == "__main__":
    main()