class Employee:
    language = "hindi" # class atrributes
    salary = 12000
     
    def getInfo(self): # it is creating method we must used self if we used it or not
        print(f"The language is {self.language}.The salary is {self.salary}")

    def greet(self):
        print("Good morning")

harry = Employee()
harry.name = "harry" 
print(harry.name, harry.language, harry.salary)
harry.greet()
harry.getInfo() # this and below line is same
# Employee .getInfo(harry)