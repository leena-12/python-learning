from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Designer(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


if __name__ == "__main__":
    employees = [
        Developer("Dev A", 500, 160),
        Designer("Designer B", 40000),
        Manager("Manager C", 60000, 15000)
    ]

    for e in employees:
        print(e.name, "salary:", e.calculate_salary())