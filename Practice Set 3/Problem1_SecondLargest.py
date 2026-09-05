"""
Problem 1 — Second Largest
[10, 4, 7, 20, 15] -> 15
Don't use sort() or sorted()
"""

"""
Approach:
Use one traversal and keep track of the largest and second largest values.
"""

"""
Pseudocode:
1. Set largest and second largest.
2. Loop through the list.
3. If current number is bigger than largest, update both.
4. Else if current number is between largest and second largest, update second largest.
5. Return second largest.
"""

def second_largest(nums):
    if len(nums) < 2:
        return None

    largest = float("-inf")
    second = float("-inf")

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

"""
Test cases:
[10, 4, 7, 20, 15] -> 15
[1, 2, 3, 4] -> 3
[9, 9, 8] -> 8
"""

nums = [10, 4, 7, 20, 15]
print(second_largest(nums))

"""
Time complexity: O(n)
Space complexity: O(1)
"""