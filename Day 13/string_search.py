#Searching in Strings
text = "Python Programming"

print(text.find("Python"))   
print(text.find("Java"))     # returns -1, not found 

# index() works like find(), but crashes if not found
print(text.index("Python"))
# print(text.index("Java"))  # this would raise ValueError

text2 = "Programming"
print(text2.count("m"))
print(text2.count("g"))

# Reversing a String
word = "Python"

# Method 1: slicing
print(word[::-1])

# Method 2: using a loop
reversed_word = ""
for ch in word:
    reversed_word = ch + reversed_word
print(reversed_word)

# Comparing Strings
a = "Python"
b = "python"
print(a == b)   # False, comparison is case-sensitive