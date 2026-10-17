# Problem 1: Find the second largest element

# Understand: Find the second largest different number.
# Brute force: Sort the numbers and choose the second last unique value.
# Optimization: Remove duplicates first, then sort.
# Data structure: set() to remove duplicates, list to sort.

numbers = [10, 5, 8, 12, 3]

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("No second largest element")
else:
    unique_numbers.sort()
    print("Second largest element:", unique_numbers[-2])

# Edge cases:
# [7] -> No second largest element
# [5, 5] -> No second largest element
# [4, 4, 2, 1] -> 2