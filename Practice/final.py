def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))