import random

print(random.randint(1, 10))

fruits = ["apple", "banana", "mango"]
print(random.choice(fruits))

random.shuffle(fruits)
print(fruits)
