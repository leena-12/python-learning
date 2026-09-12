numbers = [1, 2, 3, 4, 5]
k = 2

if len(numbers) == 0:
    result = []
else:
    k = k % len(numbers)
    result = numbers[len(numbers) - k:] + numbers[:len(numbers) - k]

print(result)