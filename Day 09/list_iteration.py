"""
Iterating through lists using for loop.
"""

numbers = [int(x) for x in input("enter the numbers separated by spaces:").split()]

for num in numbers:
    print(num)


"""
Iterating through lists using for loop.(range)
"""

numbers = [int(x) for x in input("enter the numbers separated by spaces:").split()]

for i in  range(len(numbers)):
    print(i, numbers[i])