class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age :", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, cgpa):
        super().__init__(name, age) 
        self.roll_no = roll_no
        self.cgpa = cgpa

    def display(self):
        super().display() 
        print("Roll No:", self.roll_no)
        print("CGPA   :", self.cgpa)


if __name__ == "__main__":
    p = Person("Muktai", 21)
    print("=== Person ===")
    p.display()

    s = Student("leena", 20, "CS64", 9.76)
    print("\n=== Student ===")
    s.display()