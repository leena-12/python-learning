nums = [1, 2, 2, 3, 4, 4, 5]
result = []

for n in nums:
    if n not in result:
        result.append(n)

print(result)