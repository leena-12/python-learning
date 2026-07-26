# Keep asking the user for a number until a valid integer is entered

def get_valid_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            print("You entered:", num)
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    get_valid_integer()