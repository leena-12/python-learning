class Employee:
    total_employees = 0

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.__salary = salary
        Employee.total_employees += 1

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):
        if amount <= 0:
            raise ValueError("Increase amount must be positive")
        self.__salary += amount

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.__salary)