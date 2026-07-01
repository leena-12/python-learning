# project a student grade calculator.

a = float(input("Enter marks for physics: "))
b = float(input("Enter marks for maths: "))
c = float(input("Enter marks for chemistry: "))
d = float(input("Enter marks for IKS: "))
e = float(input("Enter marks for CMS: "))

def get_marks(a, b, c, d, e):
    return a,b,c,d,e

def calculate_percentage(a, b, c, d, e):
    return (a + b + c + d + e) / 500 * 100

def calculate_grade(percent):
    if percent > 90:
        return "A"
    elif percent > 75:
        return "B"
    elif percent > 60:
        return "C"
    elif percent > 40:
        return "D"
    else:
        return "F"


def display_result(percent, grade):
    print("Percentage:", percent)
    print("Grade:", grade)


percent = calculate_percentage(a, b, c, d, e)
grade = calculate_grade(percent)

print("Percentage:", percent)
print("Grade:", grade)