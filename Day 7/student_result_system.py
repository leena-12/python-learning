
#Simple mini project student result system that calculates total, percentage, and grade.

def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    grade = get_grade(percentage)
    return total, percentage, grade


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
        marks.append(mark)

    total, percentage, grade = calculate_result(marks)

    print("\n--- Result ---")
    print(f"Name: {name}")
    print(f"Total Marks: {total}/{num_subjects * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()