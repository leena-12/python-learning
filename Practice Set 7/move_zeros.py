def move_zeros(numbers):
    left = 0

    for right in range(len(numbers)):
        if numbers[right] != 0:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1

    return numbers


values = [0, 1, 0, 3, 12]
print(move_zeros(values))