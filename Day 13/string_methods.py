# Checking Character Types

text = "Python123"

print(text.isalpha())   # False, because it contains digits
print(text.isdigit())   # False, because it contains letters
print(text.isalnum())   # True, because it contains only letters and digits

text2 = "   "
print(text2.isspace())  # True, because it contains only spaces

text3 = "python"
print(text3.islower())  # True, because all letters are lowercase

text4 = "PYTHON"
print(text4.isupper())  # True, because all letters are uppercase

# String Formatting using f-strings

name = "Leena"
age = 19

print(f"My name is {name} and I am {age} years old.")
print(f"Next year, I will be {age + 1} years old.")