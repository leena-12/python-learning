# print square of the entered numbers.

a = int(input("enter the first range:"))
b = int(input("enter the last range:"))


squares = [x*x for x in range(a,b)]

print(squares)



# print cube of the entered numbers.

a = int(input("enter the first range:"))
b = int(input("enter the last range:"))


cube = [x*x*x for x in range(a,b)]

print(cube)


# print the length of the entered strings.

words = ["apple", "banana", "kiwi"]
lengths = [len(word) for word in words]
print(lengths)   



# print the length of the entered strings.

words = ["apple", "grapes", "guava"]
upper_words = [word.upper() for word in words]
print(upper_words)  