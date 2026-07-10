"""
membership operators.
"""

fruits =["apple", "kiwi", "grapes"]

print("apple" in fruits)
print("kiwi" in fruits)

print("grapes" not in fruits)

"""
using membership operators in statements.
"""

fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Yes, apple is in the list")
else:
    print("Apple not found.")


"""
add another elements to the list.
"""

fruits = ["apple", "banana"]
print(fruits)

new_fruit = [str(x) for x in input("enter the fruit names separated by spaces to add in the list:").split()]

if new_fruit not in fruits:
    fruits.append(new_fruit)
    print("Added!")
else:
    print("Already exists, not adding")
print("Updated list:", fruits)