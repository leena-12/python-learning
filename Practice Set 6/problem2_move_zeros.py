numbers = [0, 1, 0, 3, 12]
result = []
zero_count = 0

for number in numbers:
    if number == 0:
        zero_count = zero_count + 1
    else:
        result.append(number)

for i in range(zero_count):
    result.append(0)

print(result)