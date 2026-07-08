# write a program which accept one number and display below pattern.

def Pattern(no):
    value = 1

    for i in range(1,no + 1):
      for j in range(i):
        print(value,end="")
        value = value + 1
      print()

Pattern(5)