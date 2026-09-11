numbers = [1, 2, 3, 2, 4, 5, 1, 3, 6]
duplicates = []

for number in numbers:
    if numbers.count(number) > 1:
        if number not in duplicates:
            duplicates.append(number)

print("Duplicate elements:", duplicates)