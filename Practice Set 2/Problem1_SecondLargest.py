"""
Problem 1 — Second Largest
Input: [10, 5, 8, 20, 15]
Output: 15
Don't use sort() or sorted()
"""

"""
Approach:
Scan the list once and keep track of the largest and second largest values.
When a bigger number is found, shift the old largest to second largest.
"""

"""
Pseudocode:
1. Take the first two elements.
2. Set largest and second largest in correct order.
3. Loop through remaining elements.
4. If current number is greater than largest:
   update second largest and largest.
5. Else if current number is between largest and second largest:
   update second largest.
6. Print second largest.
"""

def second_largest(nums):
    if len(nums) < 2:
        return None

    if nums[0] > nums[1]:
        largest = nums[0]
        second = nums[1]
    else:
        largest = nums[1]
        second = nums[0]

    for num in nums[2:]:
        if num > largest:
            second = largest
            largest = num
        elif second < num < largest:
            second = num

    return second

"""
Test cases:
[10, 5, 8, 20, 15] -> 15
[1, 2, 3, 4] -> 3
[9, 9, 8] -> 8
"""

print(second_largest([10, 5, 8, 20, 15]))
print(second_largest([1, 2, 3, 4]))
print(second_largest([9, 9, 8]))

"""
Time complexity:
O(n)
"""
