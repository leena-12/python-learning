def remove_duplicates(numbers):
    if len(numbers) == 0:
        return []

    left = 0

    for right in range(1, len(numbers)):
        if numbers[right] != numbers[left]:
            left += 1
            numbers[left] = numbers[right]

    return numbers[:left + 1]


values = [1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(values))