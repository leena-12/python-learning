text = "  Hello, World!  "

# Case conversion
print(text.upper())
print(text.lower())
print(text.title())

# Removing whitespace
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Searching
print(text.find("World"))     
print(text.count("l"))

# Replacing
print(text.replace("World", "Python"))

# Splitting and joining
sentence = "Python is fun"
words = sentence.split()
print(words)

joined = "-".join(words)
print(joined)

# Checking string content
print("12345".isdigit())
print("Hello".isalpha())
print("Hello123".isalnum())

# Starts / ends with
print(sentence.startswith("Python"))
print(sentence.endswith("fun"))

# Formatting
name = "Leena"
age = 19
print(f"My name is {name} and I am {age} years old.")