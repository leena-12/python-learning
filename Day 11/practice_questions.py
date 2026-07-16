"""
Create a set of your favorite programming languages.

Print every language.
"""
languages = {"Python", "Java", "C++", "HTML"}
print("My favourite Programming languages are:",languages)


"""
Take ten numbers from the user.

Store them in a set.

Print only the unique numbers.
"""
numbers = set()

for _ in range(10):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Unique numbers:")
for num in numbers:
    print(num)

"""
Count the number of unique words in a sentence.
"""
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)

print(len(unique_words))


"""
Remove duplicate values from a list using a set.
"""
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print(unique_numbers)

"""
Check whether a given value exists inside a set.
"""

my_set = {10, 20, 30, 40, 50}
value = int(input("Enter a value: "))

if value in my_set:
    print("Value exists in the set")
else:
    print("Value does not exist in the set")