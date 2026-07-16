
#Print every element of a list using a loop.

numbers =[1,2,3,5,7,9,6,5,9]

for num in numbers:
    print(num)


#Calculate the sum of all numbers in a list without using sum().



numbers = [int(x) for x in input("enter the numbers in the list separated by spaces:").split()]

print("Entered numbers list is :", numbers)
total = 0
for num in numbers:
    total += num

print("The sum of the list is:", total)


#Count positive and negative numbers separately.


numbers = [int(x) for x in input("enter the numbers in the list separated by spaces:").split()]

print("Entered numbers list is :", numbers)

positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)


#Create a new list containing the square of every number.


#using comprehension
original = [int(x) for x in input("enter the numbers in the list separated by spaces:").split()]
squares = [x*x for x in original]

print("Squares:",squares)
new_list = original.copy()

#using for loop
numbers = [int(x) for x in input("enter the numbers in the list separated by spaces:").split()]

squares = []
for num in numbers:
    squares.append(num ** 2)

print("Squares:", squares)



#Find the second largest number in a list.

numbers = [int(x) for x in input("enter the numbers in the list separated by spaces:").split()]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)

#with sorting

numbers = [int(x) for x in input("enter the numbers in the list separated by spaces:").split()]

unique_numbers = list(set(numbers))   
unique_numbers.sort()                  

second_largest = unique_numbers[-2]    

print("Second largest:", second_largest)