# ATM System using functions and exception handling

balance = 0.0

def get_amount(prompt):

    try:
        amount = float(input(prompt))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        return amount
    except ValueError as e:
        print("Error:", e)
        return None

def check_balance():
    print("Current balance:", balance)

def deposit():
    global balance
    amount = get_amount("Enter amount to deposit: ")
    if amount is not None:
        balance += amount
        print("Deposited:", amount)
        print("New balance:", balance)

def withdraw():
    global balance
    amount = get_amount("Enter amount to withdraw: ")
    if amount is not None:
        if amount > balance:
            print("Error: Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawn:", amount)
            print("New balance:", balance)

def atm_menu():
    while True:
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    atm_menu()