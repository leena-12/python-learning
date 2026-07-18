"""
Take your name as input.

Print:
Length
Uppercase
Lowercase
"""
name = input("Enter your name: ")

print("Length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())


"""
Take a word.

Print:
First character
Last character
Middle character
"""
word = input("Enter a word: ")

print("First character:", word[0])
print("Last character:", word[-1])
print("Middle character:", word[len(word) // 2])


"""
Take a sentence.

Count total characters.
"""
sentence = input("Enter a sentence: ")

print("Total characters:", len(sentence))


"""
Replace every space with "-"
"""
sentence = input("Enter a sentence: ")

result = sentence.replace(" ", "-")
print(result)


"""
Check whether a string starts with a particular letter.
"""
text = input("Enter a string: ")
letter = input("Enter a letter to check: ")

if text.startswith(letter):
    print("Yes, it starts with", letter)
else:
    print("No, it does not start with", letter)