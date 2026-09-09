nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
duplicates = []

for num in nums:
    if nums.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)