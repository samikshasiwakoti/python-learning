# Add a static method in problem2., to greet status(no of seats) and get fare information of train running under indian railways
class Calculator:
    def __init__(self, n): # instance method
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
    @staticmethod
    def hello():
        print("Hello there")

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()