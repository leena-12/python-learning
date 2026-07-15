"""
Create a dictionary for a student containing:

Name
Age
Branch
CGPA

Print all details.
"""
student = {
    "Name": "Leena",
    "Age": 19,
    "Branch": "CSE",
    "CGPA": 9.5
}
print(student)



"""
Update the CGPA.

Print the updated dictionary.
"""
student = {
    "Name": "Leena",
    "Age": 19,
    "Branch": "CSE",
    "CGPA": 9.5
}

student["CGPA"] = 10.0
print(student)


"""
Take five subjects and marks.
Store them in a dictionary.
Print:

Highest mark
Lowest mark
Average mark
"""
marks = {
    "Maths": 85,
    "Physics": 78,
    "Chemistry": 90,
    "English": 65,
    "Computer": 95
}

values = marks.values()

print("Highest mark:", max(values))
print("Lowest mark:", min(values))
print("Average mark:", sum(values) / len(values))



"""
Count how many students passed.
"""
students = {
    "Rahul": 75,
    "Priya": 32,
    "Amit": 68,
    "Riya": 29
}

passed = 0
failed = 0

for name, marks in students.items():
    if marks >= 40:
        passed += 1
    else:
        failed += 1

print("Passed =", passed)
print("Failed =", failed)



"""
Print all keys and values using a loop.
"""
student = {
    "Name": "Leena",
    "Age": 19,
    "Branch": "CSE",
    "CGPA": 9.5
}

for key, value in student.items():
    print(key, ":", value)