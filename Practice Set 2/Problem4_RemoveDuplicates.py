"""
Problem 4 — Remove duplicates
Do it without using set()
"""

"""
Approach:
Create a new list.
Add only those elements that are not already in the new list.
"""

"""
Pseudocode:
1. Take input list.
2. Create empty list unique.
3. Loop through original list.
4. If item is not in unique, append it.
5. Return unique list.
"""

def remove_duplicates(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique

"""
Test cases:
[1, 2, 2, 3, 4, 4, 5] -> [1, 2, 3, 4, 5]
[10, 10, 20, 30, 20] -> [10, 20, 30]
"""

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([10, 10, 20, 30, 20]))

"""
Time complexity:
O(n^2)
"""
