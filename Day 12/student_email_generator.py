first_name = input("Enter First Name: ").strip().lower()
last_name = input("Enter Last Name: ").strip().lower()
birth_year = input("Enter Birth Year: ").strip()

year_suffix = birth_year[-2:]   # last 2 digits of the year

email = first_name + "." + last_name + year_suffix + "@gmail.com"

print("Generated Email:", email)