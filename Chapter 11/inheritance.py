class Animal:
    def speak(self):
        print("ANimal speaks")
class Dog(Animal) :
    def bark(self) :
        print("Dog barks")  
# class Cat(Animal): # this is multilevel inhritance
#     def meows(self):
#         print("Cat MewMew")   
# class Cow(Animal) :
#     def moo(self):
#         print("Cow Moos")         

a = Dog()       
a.speak() 
a.bark()

# b = Cat()
# b.speak()
# b. meows()

# c = Cow()
# c.speak()
# c.moo()


