numbers = [1, 3, 2, 1, 4, 1, 3]
most_frequent = numbers[0]
maximum_count = numbers.count(most_frequent)

for number in numbers:
    count = numbers.count(number)

    if count > maximum_count:
        most_frequent = number
        maximum_count = count

print("Most frequent element:", most_frequent)