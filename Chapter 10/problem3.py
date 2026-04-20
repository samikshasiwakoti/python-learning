#Create a class with a class attribute a; create an object from it and set "a" directly using object.a=0. Does this change the class sttribute?

class Example:
      a = 123
object = Example()
print(object.a)# prints class attributes because instance attribute is not present
object.a=0 # prints the instance attribute beacues instance attribute is present
print(object.a)