
#Simple program to find the maximum and minimum values in a list of numbers.

def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def find_min(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


if __name__ == "__main__":
    values = input("Enter numbers separated by spaces: ").split()
    numbers = [float(v) for v in values]

    print(f"Maximum value: {find_max(numbers)}")
    print(f"Minimum value: {find_min(numbers)}")