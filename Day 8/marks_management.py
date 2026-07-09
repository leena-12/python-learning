"""
Student Marks Management System 

Menu:

1. Add Marks
2. Display Marks
3. Highest Marks
4. Lowest Marks
5. Average Marks
6. Exit

Requirements:

Store marks in a list.
Use functions.
Use loops.
Validate that marks are between 0 and 100.
"""

marks_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]


def add_marks():
    while True:
        try:
            mark = float(input("Enter marks (0-100): "))
            if 0 <= mark <= 100:
                marks_list.append(mark)
                print(f"Added mark: {mark}")
                break
            else:
                print("Invalid input. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_marks():
    if not marks_list:
        print("No marks have been added yet.")
        return
    print("Marks List:")
    for i, mark in enumerate(marks_list, start=1):
        print(f"{i}. {mark}")


def highest_marks():
    if not marks_list:
        print("No marks have been added yet.")
        return
    highest = marks_list[0]
    for mark in marks_list:
        if mark > highest:
            highest = mark
    print(f"Highest marks: {highest}")


def lowest_marks():
    if not marks_list:
        print("No marks have been added yet.")
        return
    lowest = marks_list[0]
    for mark in marks_list:
        if mark < lowest:
            lowest = mark
    print(f"Lowest marks: {lowest}")


def average_marks():
    if not marks_list:
        print("No marks have been added yet.")
        return
    total = 0
    for mark in marks_list:
        total += mark
    average = total / len(marks_list)
    print(f"Average marks: {average:.2f}")


def show_menu():
    print("\n--- Student Marks Management System ---")
    print("1. Add Marks")
    print("2. Display Marks")
    print("3. Highest Marks")
    print("4. Lowest Marks")
    print("5. Average Marks")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_marks()
        elif choice == "2":
            display_marks()
        elif choice == "3":
            highest_marks()
        elif choice == "4":
            lowest_marks()
        elif choice == "5":
            average_marks()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()