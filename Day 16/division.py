# division.py
# Take two numbers from the user and handle invalid input and division by zero

def safe_division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2
        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers only.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    safe_division()