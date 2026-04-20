# default arguments
class Calculator :
    def add(self, a,b=0):
        return a +b
c = Calculator()
print(c.add(5))
print(c.add(5,20))

# *args
class Multiple :
    def mul(self,*numbers):
        print(numbers)

s = Multiple()
s.mul(2,3,4) 
s.mul(5,7,8)      