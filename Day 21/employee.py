class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())
        print("--------------------")


class Manager(Employee):
    def calculate_salary(self):
        bonus = 20000
        return self.basic_salary + bonus


class Developer(Employee):
    def calculate_salary(self):
        project_bonus = 10000
        return self.basic_salary + project_bonus


if __name__ == "__main__":
    employees = [
        Manager("Priya", 70000),
        Developer("Aman", 60000),
        Employee("Rahul", 40000)
    ]

    for employee in employees:
        employee.display()