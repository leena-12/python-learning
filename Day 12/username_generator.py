first_name = input("Enter First Name: ").strip().lower()
last_name = input("Enter Last Name: ").strip().lower()
fav_number = input("Enter Favorite Number: ").strip()

# Suggestion 1: firstname_lastname + favorite number
username1 = first_name + "_" + last_name + fav_number

# Suggestion 2: initials (uppercase) + favorite number
username2 = first_name[0].upper() + last_name[0].upper() + fav_number

# Suggestion 3: firstname + favorite number
username3 = first_name + fav_number

print("Here are your username suggestions:")
print(username1)
print(username2)
print(username3)