numbers = [10, 5, 8, 10, 3]

largest = None
second_largest = None

for number in numbers:
    if largest is None or number > largest:
        if number != largest:
            second_largest = largest
        largest = number
    elif number != largest and (second_largest is None or number > second_largest):
        second_largest = number

if second_largest is None:
    print("There is no second-largest distinct element.")
else:
    print("Second-largest element:", second_largest)