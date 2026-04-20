#Write a class Train which has methods to book a ticket .get status(no of seats) and get fare information of train running under  railways.
from random import randint

class Train:

    def book(self, trainNo, fro, to):
        print(f"Ticket is booked in train no: {trainNo} from {fro} to {to}")

    def getStatus(self, trainNo):
        print(f"Train no {trainNo} is running and seats are available")

    def getFare(self, trainNo, fro, to):
        fare = randint(222, 5555)
        print(f"Ticket fare in train no {trainNo} from {fro} to {to} is {fare}")


# creating object
t = Train()

t.book(12345, "Kathmandu", "Pokhara")
t.getStatus(12345)
t.getFare(12345, "Kathmandu", "Pokhara")