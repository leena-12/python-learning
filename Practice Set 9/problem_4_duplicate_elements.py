# Problem 4: Find duplicate elements in a list

# Understand: Find values that appear more than once.
# Brute force: Count each number and add it only once to the result.
# Optimization: Check number not in duplicates before adding it.
# Data structure: list to store duplicate values.

numbers = [1, 2, 3, 2, 4, 1, 5, 3]
duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate elements:", duplicates)

# Edge cases:
# [1, 2, 3] -> []
# [] -> []
# [5, 5, 5] -> [5]