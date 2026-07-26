# Take age from the user and raise an exception if age is negative

def get_age():
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative.")

        print("Your age is:", age)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    get_age()