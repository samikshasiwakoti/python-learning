def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number:"))    
print(f"The factorial of {n}  is ;{factorial(n)}")

def fact(n):
    if(n==0):
        return 1 
    return n* fact(n-1)
print("The fact of 6 is", fact(6))
    