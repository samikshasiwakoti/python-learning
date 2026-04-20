# one child class inherits from more than one parent class

class Father:
    def skill1 (self):
        print("Driving")
class Mother:
    def skill2 (self) :
        print("Cooking")
class Child(Father, Mother):
    def skill3(self):
        print("Dancing")
c = Child()
c . skill1()   
c . skill2() 
c. skill3()    



     
