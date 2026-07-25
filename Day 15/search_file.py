# Problem : Search for a student's name inside a file
search_name = input("Enter name to search: ")

found = False

with open("students.txt", "r") as file:
    for line in file:
        if line.strip().lower() == search_name.strip().lower():
            found = True
            break

if found:
    print("Student Exists")
else:
    print("Student Not Found")