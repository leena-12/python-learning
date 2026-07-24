FILE_NAME = "students.txt"


def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    branch = input("Enter branch: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "," + age + "," + branch + "\n")

    print("Student added.")


def display_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No students found.")
            return

        print("\n--- Student Records ---")
        for record in records:
            name, age, branch = record.strip().split(",")
            print("Name:", name, "| Age:", age, "| Branch:", branch)

    except FileNotFoundError:
        print("No records found yet.")


def search_student():
    search_name = input("Enter name to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False
        for record in records:
            name, age, branch = record.strip().split(",")
            if name.lower() == search_name.lower():
                print("Found -> Name:", name, "| Age:", age, "| Branch:", branch)
                found = True

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No records found yet.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting the program, byeee!!")
        break
    else:
        print("Invalid choice.")