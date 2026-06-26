#A program to find factorial of natural numbers(using while).

num= int(input("Enter the number:"))
fact = 1
i = 1
while i <= num :
    fact *= i
    i += 1
    
    
print("The factorial is:",fact)