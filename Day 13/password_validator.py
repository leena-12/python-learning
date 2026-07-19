password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_characters:
        has_special = True

is_long_enough = len(password) >= 8

if is_long_enough and has_upper and has_lower and has_digit and has_special:
    print("Strong password")
else:
    print("Weak password")
    if not is_long_enough:
        print("- Must be at least 8 characters long")
    if not has_upper:
        print("- Must contain an uppercase letter")
    if not has_lower:
        print("- Must contain a lowercase letter")
    if not has_digit:
        print("- Must contain a digit")
    if not has_special:
        print("- Must contain a special character")