
#Simple program to calculate area of different shapes.


import math


def area_of_square(side):
    return side * side


def area_of_rectangle(length, width):
    return length * width


def area_of_circle(radius):
    return math.pi * radius * radius


def area_of_triangle(base, height):
    return 0.5 * base * height


def main():
    print("Area Calculator")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")

    choice = input("Choose a shape (1-4): ")

    if choice == "1":
        side = float(input("Enter side length: "))
        print(f"Area of square = {area_of_square(side)}")
    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print(f"Area of rectangle = {area_of_rectangle(length, width)}")
    elif choice == "3":
        radius = float(input("Enter radius: "))
        print(f"Area of circle = {area_of_circle(radius):.2f}")
    elif choice == "4":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area of triangle = {area_of_triangle(base, height)}")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()