class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter First Number :"))
        self.Value2 = int(input("Enter Second Number :"))


    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            print("Unable to divide by zero")
        else:
            return self.Value1 / self.Value2
        
Obj1 = Arithmetic()
Obj1.Accept()

print("Addition:",Obj1.Addition())
print("Substraction:",Obj1.Substraction())
print("multiplication:",Obj1.multiplication())

Ans = Obj1.Division()
if Ans != None:
    print("Division:",Ans)

Obj2 = Arithmetic()
Obj2.accept()

print("Addition:",Obj2.Addition())
print("Substraction:",Obj2.Substraction())
print("multiplication:",Obj2.multiplication())

Ans = Obj2.Division()
if Ans != None:
    print("Division:",Ans)


