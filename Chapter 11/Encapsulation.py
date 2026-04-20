class Bank:
    def __init__(self, balance):
        self.__balance = balance # private varibale (encapsulation)
    def show(self):
        print("Balance is", self.__balance) 

d = Bank(1000) 
d.show()  