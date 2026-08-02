from bank_account import BankAccount

accounts = {}


def create_account():
    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")

    if account_number in accounts:
        print("Account already exists.")
        return

    accounts[account_number] = BankAccount(name)
    print("Account created successfully.")


def deposit():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter amount to deposit: "))
        accounts[account_number].deposit(amount)
        print("Deposit successful.")
    except ValueError as e:
        print("Error:", e)


def withdraw():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter amount to withdraw: "))
        accounts[account_number].withdraw(amount)
        print("Withdrawal successful.")
    except ValueError as e:
        print("Error:", e)


def check_balance():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return

    print("Balance: Rs.", accounts[account_number].get_balance())


while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")