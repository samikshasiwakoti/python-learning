# create a class "Programmer" for storing information of few programmers working at microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("harry", 15000, 555)
print(p.name, p.salary, p.pin, p.company)

p1 = Programmer("asmii", 12000, 666)
print(p1.name, p1.salary, p1.pin, p1.company)

p2 = Programmer("sami" , 15000,  777)
print(p2.name, p2.salary , p2.pin, p2.company)