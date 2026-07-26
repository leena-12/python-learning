# Student Grade Calculator with exception handling and file storage

def get_valid_mark(subject_name):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject_name} (0-100): "))

            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

            return mark

        except ValueError as e:
            print("Error:", e)

def calculate_grade(percentage):
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

def student_grade():
    try:
        name = input("Enter student name: ")

        m1 = get_valid_mark("Subject 1")
        m2 = get_valid_mark("Subject 2")
        m3 = get_valid_mark("Subject 3")

        total = m1 + m2 + m3
        percentage = total / 3

        grade = calculate_grade(percentage)

        print("\n=== Result ===")
        print("Name:", name)
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)

        try:
            with open("grades.txt", "a") as f:
                f.write(f"{name}, {m1}, {m2}, {m3}, {percentage:.2f}, {grade}\n")
            print("Record saved to grades.txt")
        except Exception as e:
            print("Could not save to file:", e)

    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    student_grade()