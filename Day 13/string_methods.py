# Checking Character Types
text = "Python123"

print(text.isalpha())   # False, contains digits
print(text.isdigit())   # False, contains letters
print(text.isalnum())   # True, only letters and digits

text2 = "   "
print(text2.isspace())  
text3 = "python"
print(text3.islower())  

text4 = "PYTHON"
print(text4.isupper())  

# String Formatting using f-strings
name = "Leena"
age = 19
print(f"My name is {name} and I am {age} years old.")