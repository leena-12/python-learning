FILE_NAME = "student_database.txt"


def add_student():
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "," + roll_no + "," + branch + "\n")

    print("Student added.")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No students found.")
            return

        print("\n--- All Students ---")
        for record in records:
            name, roll_no, branch = record.strip().split(",")
            print("Roll No:", roll_no, "| Name:", name, "| Branch:", branch)

    except FileNotFoundError:
        print("No records found yet.")


def search_student():
    roll_no_to_find = input("Enter roll number to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        for record in records:
            name, roll_no, branch = record.strip().split(",")
            if roll_no == roll_no_to_find:
                print("Found -> Name:", name, "| Roll No:", roll_no, "| Branch:", branch)
                return

        print("Student not found.")

    except FileNotFoundError:
        print("No records found yet.")


def update_student():
    roll_no_to_update = input("Enter roll number to update: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No records found yet.")
        return

    updated_records = []
    found = False

    for record in records:
        name, roll_no, branch = record.strip().split(",")

        if roll_no == roll_no_to_update:
            found = True
            print("Enter new details for this student:")
            new_name = input("New name: ")
            new_branch = input("New branch: ")
            updated_records.append(new_name + "," + roll_no + "," + new_branch + "\n")
        else:
            updated_records.append(record)

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
        print("Student updated successfully.")
    else:
        print("Student not found.")


def delete_student():
    roll_no_to_delete = input("Enter roll number to delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No records found yet.")
        return

    updated_records = []
    found = False

    for record in records:
        name, roll_no, branch = record.strip().split(",")

        if roll_no == roll_no_to_delete:
            found = True
        else:
            updated_records.append(record)

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
        print("Student deleted successfully.")
    else:
        print("Student not found.")


while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting the program, byeeee!!")
        break
    else:
        print("Invalid choice.")