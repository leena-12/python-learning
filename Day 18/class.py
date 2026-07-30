class Student:
    college_name = "college name"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks


s1 = Student("leena", 99)
s1.welcome()
print(s1.get_marks())


class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hello", self.name, "Your avreage score is :", sum/3)

s1 = StudentMarks("Leena Kinkar",[99, 98, 90])
s1.get_avg()

