# Simple calculator with exception handling

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation (+ - * /): ")

        if operation == "+":
            print("Result:", add(a, b))
        elif operation == "-":
            print("Result:", subtract(a, b))
        elif operation == "*":
            print("Result:", multiply(a, b))
        elif operation == "/":
            try:
                print("Result:", divide(a, b))
            except ZeroDivisionError as e:
                print("Error:", e)
        else:
            print("Invalid operation.")

    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    calculator()