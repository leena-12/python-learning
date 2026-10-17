# Problem 3: Find the first non-repeating character

# Understand: Find the first character that appears only one time.
# Brute force: Check every character using count().
# Optimization: Use count() for each character and stop at the first match.
# Data structure: string.count() method.

text = "swiss"

for character in text:
    if text.count(character) == 1:
        print("First non-repeating character:", character)
        break
else:
    print("No non-repeating character")

# Edge cases:
# "aabb" -> No non-repeating character
# "a" -> a
# "" -> No non-repeating character