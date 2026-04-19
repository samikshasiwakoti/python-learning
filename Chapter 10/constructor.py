
class Employee:
    language = "hindi"
    salary = 12000
     
    def __init__(self, name, salary, language): # It is called dunder method which is automitacally called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
     
    @staticmethod
    def greet():
        print("Good morning")


harry = Employee("samii", 130000, "Javascript")
print(harry.name, harry.language, harry.salary)