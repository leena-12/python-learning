first = "listen"
second = "silent"

frequency = {}

for character in first:
    if character in frequency:
        frequency[character] = frequency[character] + 1
    else:
        frequency[character] = 1

for character in second:
    if character in frequency:
        frequency[character] = frequency[character] - 1
    else:
        frequency[character] = -1

is_anagram = True

for count in frequency.values():
    if count != 0:
        is_anagram = False
        break

if is_anagram:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")