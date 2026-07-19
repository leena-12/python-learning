#Reverse a string.

text = input("Enter a string: ")

reversed_text = text[::-1]
print(reversed_text)

"""Count:

Uppercase letters
Lowercase letters
Digits """

text = input("Enter a string: ")

uppercase_count = 0
lowercase_count = 0
digit_count = 0

for ch in text:
    if ch.isupper():
        uppercase_count += 1
    elif ch.islower():
        lowercase_count += 1
    elif ch.isdigit():
        digit_count += 1

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)

"""
Count vowels and consonants.
"""

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


"""
Check whether a string is a palindrome.
"""

text = input("Enter a string: ")

reversed_text = text[::-1]

if text == reversed_text:
    print("Palindrome")
else:
    print("Not Palindrome")


"""
Count the frequency of each character.
"""

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch, count in frequency.items():
    print(ch, ":", count)