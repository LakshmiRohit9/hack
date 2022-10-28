class arithematic:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y
class calculator:
    def __init__(self,x,y):
        self.op=arithematic(x,y)
        print(f"addition of {self.op.x} and {self.op.y}:",self.op.add())
        print(f"subtraction of {self.op.x} and {self.op.y}:",self.op.sub())
        print(f"product of {self.op.x} and {self.op.y}:",self.op.mul())
        print(f"division of {self.op.x} and {self.op.y}:",self.op.div())
c=calculator(20,10)
