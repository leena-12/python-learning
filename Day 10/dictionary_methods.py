student = {
    "name": "Leena",
    "age": 19,
    "branch": "CSE"
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

for key, value in student.items():
    print(key, "->", value)