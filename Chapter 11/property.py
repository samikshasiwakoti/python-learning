#Property Decoretor
# it is liked using  methods like a variables. it is used withgetter and setter

class Student:
    def __init__(self,name):
        self.name = name
        
        @property # to make getter method to an attribute we used it
        def name(self):# it created property called name
            return self.name
        
        @name.setter
        def name(self,value):
            self.name = value
s = Student("Ram") 
print(s.name)   

s.name ="Samii"
print(s.name)
        
