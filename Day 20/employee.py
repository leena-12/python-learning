class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name   :", self.name)
        print("Emp ID :", self.emp_id)
        print("Salary :", self.salary)


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


if __name__ == "__main__":
    e = Employee("Rahul", "E101", 60000)
    m = Manager("Neha", "M001", 90000, "IT")

    print("=== Employee ===")
    e.display()

    print("\n=== Manager ===")
    m.display()