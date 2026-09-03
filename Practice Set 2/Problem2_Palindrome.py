"""
Problem 2 — Palindrome
Create is_palindrome(text)
Examples:
madam -> True
hello -> False
"""

"""
Approach:
Compare the string with its reverse.
If both are same, it is a palindrome.
"""

"""
Pseudocode:
1. Take text as input.
2. Reverse the text.
3. Compare original and reversed text.
4. Return True if same, else False.
"""

def is_palindrome(text):
    return text == text[::-1]

"""
Test cases:
madam -> True
hello -> False
level -> True
"""

print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("level"))

"""
Time complexity:
O(n)
"""
