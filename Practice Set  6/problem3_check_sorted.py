numbers = [1, 2, 3, 4, 5]
sorted_list = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        sorted_list = False
        break

if sorted_list:
    print("The list is sorted.")
else:
    print("The list is not sorted.")