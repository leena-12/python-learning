nums = [1, 2, 3, 2, 4, 2, 5, 1, 2]

most_frequent = nums[0]
max_count = 0

for num in nums:
    count = nums.count(num)
    if count > max_count:
        max_count = count
        most_frequent = num

print(most_frequent)