# Numbers Class

class Numbers:

    def __init__(self,value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
            
        return True
    
    def ChkPerfect(self):
        Sum = 0

        for i in range(1,self.Value):
            if self.value % i == 0:
                Sum = Sum + i

        if Sum == self.value:
            return True
        else:
            return False
        
    def Factors(self):
        print("Factors are:")
        for i in range(1,self.Value):
            if self.value % i == 0:
                print(i)

    def SumFactors(self):
        Sum = 0

        for i in range(1,self.Value):
            if self.value % i == 0:
                Sum = Sum + i

        return Sum
    
Obj1 = Numbers(int(input("Enter Number:")))

print("Prime:",Obj1.ChkPrime())
print("Perfect:",Obj1.ChkPerfect())

Obj1.Factors()

print("Sum of Factors:",Obj1.SumFactors())

Obj2 = Numbers(int(input("Enter Number:")))

print("Prime:",Obj2.ChkPrime())
print("Perfect:",Obj2.ChkPerfect())

Obj1.Factors()

print("Sum of Factors:",Obj2.SumFactors())