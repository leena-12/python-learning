# Problem : Write five student names into a file, then display them one by one
students = [
    "Rahul\n",
    "Amit\n",
    "Leena\n",
    "Priya\n",
    "Riya\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)

print("Students written to file.\n")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())