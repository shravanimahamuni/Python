# Demo Class

class Demo:
    value = 10        # Class Variable

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print("inside Fun")
        print(self.no1, self.no2)

    def Gun(self):
        print("Inside Gun")
        print(self.no1, self.no2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()