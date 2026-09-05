"""
Problem 4 — Rotate List
Input: [1, 2, 3, 4, 5]
Rotate right by 2
Output: [4, 5, 1, 2, 3]
"""

"""
Approach:
Use slicing to split the list into two parts and join them in rotated order.
"""

"""
Pseudocode:
1. Take list and k.
2. Make k smaller than list length using modulo.
3. Take last k elements.
4. Add them before the remaining elements.
5. Return the new list.
"""

def rotate_right(nums, k):
    if len(nums) == 0:
        return nums

    k = k % len(nums)
    return nums[-k:] + nums[:-k]

"""
Test cases:
[1, 2, 3, 4, 5], 2 -> [4, 5, 1, 2, 3]
[10, 20, 30], 1 -> [30, 10, 20]
"""

print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([10, 20, 30], 1))

"""
Time complexity: O(n)
Space complexity: O(n)
"""