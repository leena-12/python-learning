
#Simple program to calculate the cube of a number.


def cube(number):
    return number ** 3


if __name__ == "__main__":
    num = float(input("Enter a number: "))
    result = cube(num)
    print(f"The cube of {num} is {result}")