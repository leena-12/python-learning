"""
Student Attendance System
--------------------------
Menu:
1. Add Student
2. Mark Present
3. Display Attendance
4. Count Present Students
5. Exit
"""

students = []          # stores student names
attendance = {}        # stores attendance status: {"name": "Present"/"Absent"}


def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty. Try again.")
        return

    if name in students:
        print(f"{name} already exists in the list.")
        return

    students.append(name)
    attendance[name] = "Absent"   # default status when added
    print(f"{name} added successfully.")


def mark_present():
    if not students:
        print("No students added yet.")
        return

    name = input("Enter student name to mark present: ").strip()

    if name not in students:
        print(f"{name} not found in the student list.")
        return

    attendance[name] = "Present"
    print(f"{name} marked as Present.")


def display_attendance():
    if not students:
        print("No students added yet.")
        return

    print("\n--- Attendance List ---")
    for name in students:
        print(f"{name} : {attendance[name]}")
    print("------------------------")


def count_present():
    present_count = 0
    for name in students:
        if attendance[name] == "Present":
            present_count += 1

    print(f"Total present students: {present_count}")


def get_menu_choice():
    print("\n===== Student Attendance System =====")
    print("1. Add Student")
    print("2. Mark Present")
    print("3. Display Attendance")
    print("4. Count Present Students")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid input. Please enter a number between 1 and 5.")
        return None

    return choice


def main():
    while True:
        choice = get_menu_choice()

        if choice is None:
            continue
        elif choice == "1":
            add_student()
        elif choice == "2":
            mark_present()
        elif choice == "3":
            display_attendance()
        elif choice == "4":
            count_present()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()