#creating functions and objects for use in python classes
class CreateFormBy:

    def __init__(self,v:int,i:int)->None:
        self.val = v
        self.incr=i

    def increase(self) -> None:
        self.val +=self.incr

    def __repr__(self) -> str:
        return str(self.val)

a = CreateFormBy(100,10)
print(a.val)
print(a.incr)
print(a.increase())
print(a)
b=CreateFormBy(1,2)
print(b.val)#prints out the value of b
b.increase()
print(b)
