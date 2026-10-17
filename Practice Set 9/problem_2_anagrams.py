# Problem 2: Check whether two strings are anagrams

# Understand: Two strings are anagrams if they have the same characters with the same counts.
# Brute force: Sort both strings and compare them.
# Optimization: sorted() is simple and works well for beginner practice.
# Data structure: sorted list of characters.

first = "listen"
second = "silent"

if sorted(first) == sorted(second):
    print(True)
else:
    print(False)

# Edge cases:
# "" and "" -> True
# "abc" and "abcd" -> False
# "aabb" and "abab" -> True