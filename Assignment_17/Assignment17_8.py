# write a progrsm which accept one number and display below pattern

def Pattern(no):
    for i in range(1,no + 1):
      for j in range(i):
        print(i,end="")
      print()

Pattern(5)