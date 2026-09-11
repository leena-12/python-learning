numbers = [2, 3, 2, 5, 2, 3, 4]

most_frequent = numbers[0]
maximum_count = 0

for number in numbers:
    count = numbers.count(number)

    if count > maximum_count:
        maximum_count = count
        most_frequent = number

print("Most frequent element:", most_frequent)