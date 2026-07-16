#print the sum of two numbers

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
def calc_sum(a,b):
  return a+b
sum = calc_sum(a,b)
print ("Sum :",sum)

#print the result if number is even or odd.

x = int (input("Enter the number:"))
def eve_odd(x):
  return x
if x % 2 == 0 :
    print("The number is EVEN.")
else :
    print("The number is ODD.")


#Function that returns the square of a number.

y = int (input("Enter the number:"))
def square_calc(y):
   return y*y
square = square_calc(y)
print ("The square of entered number is:",square)

#Function to find the largest among three numbers.

p = int(input("Enter the first number:"))
q = int(input("Enter the second number:"))
r = int(input("Enter the third number:"))
def greatest(p,q,r):
   return p,q,r
if p>r>q :
   print("The first number is greater. ")
elif q>r>p :
   print("The second number is greater. ")
else :
   print("The third number is greater. ")
   
   
   # Function to calculate factorial

def fact_calc(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter the number: "))
result = fact_calc(num)
print("The factorial of entered number is:", result)