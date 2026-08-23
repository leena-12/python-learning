def find_max(numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


nums = [10, 25, 7, 99, 18]
print(find_max(nums))