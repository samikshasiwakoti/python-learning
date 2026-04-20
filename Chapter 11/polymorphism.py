class Animal: # this is method overriding which occurs on runtime
    def sound(self):
        print("Produces Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meoow")

b1 = Dog()  
b2 = Cat()    
b3 = Animal() 
b1.sound()
b2.sound()
b3.sound()
