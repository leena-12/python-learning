from employee import Employee

employees = {}


def add_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        print("Employee already exists.")
        return

    name = input("Enter name: ")
    department = input("Enter department: ")

    try:
        salary = float(input("Enter salary: "))
        if salary < 0:
            raise ValueError("Salary cannot be negative")
    except ValueError as e:
        print("Error:", e)
        return

    employees[emp_id] = Employee(emp_id, name, department, salary)
    print("Employee added successfully.")


def display_employee():
    emp_id = input("Enter employee ID: ")
    if emp_id not in employees:
        print("Employee not found.")
        return

    employees[emp_id].display()


def increase_salary():
    emp_id = input("Enter employee ID: ")
    if emp_id not in employees:
        print("Employee not found.")
        return

    try:
        amount = float(input("Enter increase amount: "))
        employees[emp_id].increase_salary(amount)
        print("Salary increased successfully.")
    except ValueError as e:
        print("Error:", e)


while True:
    print("\n1. Add Employee")
    print("2. Display Employee")
    print("3. Increase Salary")
    print("4. Total Employees")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employee()
    elif choice == "3":
        increase_salary()
    elif choice == "4":
        print("Total employees:", Employee.total_employees)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")