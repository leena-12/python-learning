# Problem 5: Find the most frequent element

# Understand: Find the number that appears the most times.
# Brute force: Count every number and keep the highest count.
# Optimization: Use count() inside one loop.
# Data structure: list and count() method.

numbers = [1, 3, 2, 1, 4, 1, 3]

most_frequent = numbers[0]
maximum_count = numbers.count(most_frequent)

for number in numbers:
    count = numbers.count(number)

    if count > maximum_count:
        most_frequent = number
        maximum_count = count

print("Most frequent element:", most_frequent)

# Edge cases:
# [] -> IndexError, so the list should not be empty
# [7] -> 7
# [5, 6, 6, 5] -> 5, because it appears first