class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name:",self.Name)
        print("Balance:",self.Amount)

    def Deposite(self):
        Value = float(input("Enter amount to deposit:"))
        self.Amount = self.Amount + Value

    def Withdraw(self):
        Value = float(input("Enter amount to Withdraw:"))

        if Value <= self.Amount:
            self.Amount = self.Amount - Value
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.RIO)/100
        return Interest
    
Obj1 = BankAccount("Amit",1000)

Obj1.Display()
Obj1.Deposite()
Obj1.Display()
Obj1.Withdraw()
Obj1.Display()
print("Interest:",Obj1.CalculateInterest())

Obj2 = BankAccount("Rahul",5000)

Obj2.Display()
Obj2.Deposite()
Obj2.Display()
Obj2.Withdraw()
Obj2.Display()
print("Interest:",Obj2.Calculateinterest())