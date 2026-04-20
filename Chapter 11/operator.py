#operator overrloading
class Number:
    def __int__(self,value):
        self.value = value
    def __add__(self, other):# special method should we used 
        return self.value + other.value
b1 = Number(5) 
b2 = Number(10)   
print(b1+b2)
    