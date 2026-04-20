from abc import ABC, abstractmethod

# Abstract Class it is liked strict rule where it have same method
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
