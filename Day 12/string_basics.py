# Creating strings
name = "Leena"
greeting = 'Hello'
print(name)
print(greeting)

# Strings are sequences of characters
print(name[0])       
print(name[-1])      
# Slicing
print(name[0:3])     
print(name[:2])      
print(name[2:])      

# Length of a string
print(len(name))

# Concatenation
full_greeting = greeting + ", " + name
print(full_greeting)

# Repetition
print(name * 3)

# Looping through a string
for ch in name:
    print(ch)

# Membership check
print("Lee" in name)
print("xyz" in name)