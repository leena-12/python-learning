FILE_NAME = "expenses.txt"


def add_expense():
    description = input("Enter expense description: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a") as file:
        file.write(description + "," + amount + "\n")

    print("Expense added.")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No expenses found.")
            return

        print("\n--- All Expenses ---")
        for record in records:
            description, amount = record.strip().split(",")
            print(description, ":", amount)

    except FileNotFoundError:
        print("No expenses found yet.")


def calculate_total():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No expenses found.")
            return

        total = 0
        highest = 0
        highest_desc = ""

        for record in records:
            description, amount = record.strip().split(",")
            amount = float(amount)
            total += amount

            if amount > highest:
                highest = amount
                highest_desc = description

        print("Total expense:", total)
        print("Highest expense:", highest_desc, "-", highest)

    except FileNotFoundError:
        print("No expenses found yet.")


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Exiting the program, byee!!!")
        break
    else:
        print("Invalid choice.")