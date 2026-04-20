class Person:
    def show1(self):
        print('This is a person')
class Student(Person):
    def show2(self) :
        super().show1()  
        print("This is student")
s = Student()
s.show2()        


class Vehicel:
    def __init__(self):
        print("This is vehicel ")
class Car(Vehicel):
    def __init__(self):
        super().__init__()
        print("This is car")  
c = Car()
