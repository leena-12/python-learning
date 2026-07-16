numbers = {1, 2, 3, 4, 5}

numbers.add(10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.discard(100)   # not in set, no error
print(numbers)

removed_value = numbers.pop()
print("Removed:", removed_value)
print(numbers)

# Membership operators
print(20 in numbers)
print(50 not in numbers)

numbers.clear()
print(numbers)