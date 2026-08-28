nums = [3, 8, 2, 10, 5]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print(largest)