# write a program using fucntions to find the greatest of three numbers


def greatest():
     a = int(input("Enter a one number"))
     b = int(input("Enter a two number"))
     c= int(input("Enter a three number"))
     
     if a>= b and a>= c:
          print("Greatest numbe is:",a)
     elif b>=a and b>=c :
           print("Greatest number is :",b)
     else:
      print("Greatest number is :",c)
    #  print("Greatest number is:" , max(a,b,c))
greatest()