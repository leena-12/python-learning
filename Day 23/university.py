# Aggregation: Students exist independently of University.
# If University object is deleted, Students still exist.

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


class University:
    def __init__(self, name):
        self.name = name
        self.students = []  # aggregation - not created by University

    def enroll(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.name}")

    def list_students(self):
        for s in self.students:
            print(f"{s.roll_no} - {s.name}")


s1 = Student("Amit", "CSE01")
s2 = Student("Priya", "CSE02")

uni = University("VNIT")
uni.enroll(s1)
uni.enroll(s2)
uni.list_students()

# students still exist even without university reference
print(s1.name, "still exists independently")