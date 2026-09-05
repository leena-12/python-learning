"""
Problem 3 — First Non-Repeating Character
Input: "swiss"
Output: "w"
"""

"""
Approach:
First count all characters, then scan again to find the first character with count 1.
"""

"""
Pseudocode:
1. Count each character using a dictionary.
2. Loop through the string again.
3. Return the first character whose count is 1.
4. If none found, return None.
"""

def first_non_repeating(text):
    count = {}

    for ch in text:
        count[ch] = count.get(ch, 0) + 1

    for ch in text:
        if count[ch] == 1:
            return ch

    return None

"""
Test cases:
swiss -> w
hello -> h
aabb -> None
"""

print(first_non_repeating("swiss"))
print(first_non_repeating("hello"))
print(first_non_repeating("aabb"))

"""
Time complexity: O(n)
Space complexity: O(n)
"""