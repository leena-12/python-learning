numbers = {10, 20, 30, 40}
print(numbers)

# No duplicates
numbers2 = {10, 20, 20, 30, 10}
print(numbers2)

# Creating sets
fruits = {"Apple", "Banana", "Mango"}
numbers3 = set([1, 2, 3, 4])
empty = set()

print(fruits)
print(numbers3)
print(empty)

# {} creates a dictionary, not a set
not_a_set = {}
print(type(not_a_set))
print(type(empty))

# Adding elements
fruits.add("Orange")
print(fruits)

# Removing elements
fruits.remove("Banana")   # crashes if not found
fruits.discard("Apple")   # safe, no crash if not found
print(fruits)