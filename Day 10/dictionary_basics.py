student = {
    "name": "Leena",
    "age": 19,
    "branch": "CSE"
}
print(student)

# Accessing values
print(student["name"])
print(student.get("age"))
print(student.get("college", "Not Provided"))

# Adding new data
student["college"] = "XYZ Engineering College"
print(student)

# Updating data
student["age"] = 20
print(student)

# Removing data
student.pop("age")
del student["name"]
print(student)