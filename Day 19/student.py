class Student:
    def __init__(self, name, age, branch, cgpa):
        self.name = name
        self.age = age
        self.branch = branch
        self.cgpa = cgpa

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print("CGPA:", self.cgpa)