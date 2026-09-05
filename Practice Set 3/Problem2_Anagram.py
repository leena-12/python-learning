"""
Problem 2 — Anagram
Create are_anagrams(a, b)
listen, silent -> True
"""

"""
Approach:
Count characters in both strings and compare the counts.
"""

"""
Pseudocode:
1. If lengths are different, return False.
2. Count characters of first string.
3. Count characters of second string.
4. Compare both dictionaries.
5. Return True if same, else False.
"""

def are_anagrams(a, b):
    if len(a) != len(b):
        return False

    count = {}

    for ch in a:
        count[ch] = count.get(ch, 0) + 1

    for ch in b:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return len(count) == 0

"""
Test cases:
listen, silent -> True
hello, world -> False
race, care -> True
"""

print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))
print(are_anagrams("race", "care"))

"""
Time complexity: O(n)
Space complexity: O(n)
"""