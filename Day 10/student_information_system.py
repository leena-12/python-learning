"""
Student Information System
Menu:
1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Display All Students
6. Exit
"""

students = {}


def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    branch = input("Enter branch: ")

    students[roll_no] = {"name": name, "age": age, "branch": branch}
    print("Student added.")


def search_student():
    roll_no = input("Enter roll number to search: ")
    if roll_no in students:
        print(students[roll_no])
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ")
    if roll_no in students:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        branch = input("Enter new branch: ")
        students[roll_no] = {"name": name, "age": age, "branch": branch}
        print("Student updated.")
    else:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")
    if roll_no in students:
        del students[roll_no]
        print("Student deleted.")
    else:
        print("Student not found.")


def display_all_students():
    for roll_no, info in students.items():
        print(roll_no, ":", info)


while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_all_students()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")