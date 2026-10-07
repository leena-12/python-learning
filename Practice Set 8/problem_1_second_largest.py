numbers = [10, 5, 8, 12, 3]
unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("No second largest element")
else:
    unique_numbers.sort()
    print("Second largest:", unique_numbers[-2])
    