"""
Problem 3 — Frequency
Given: "programming"
Find the frequency of every character.
Use a dictionary.
"""

"""
Approach:
Create an empty dictionary.
Loop through each character and count occurrences.
"""

"""
Pseudocode:
1. Create empty dictionary freq.
2. For each character in string:
   if character exists in dictionary, increase count.
   else set count to 1.
3. Print dictionary.
"""

def character_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

"""
Test cases:
programming -> {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
"""

print(character_frequency("programming"))

"""
Time complexity:
O(n)
"""
