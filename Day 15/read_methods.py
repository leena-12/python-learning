# Create a sample file to demonstrate read methods
with open("students.txt", "w") as file:
    file.write("Rahul\nAmit\nLeena\nPriya\nRiya\n")

# read() - reads the entire file as one single string
with open("students.txt", "r") as file:
    print("--- read() ---")
    print(file.read())

# readline() - reads only ONE line at a time
with open("students.txt", "r") as file:
    print("--- readline() ---")
    print(file.readline())

# readlines() - reads all lines into a list
with open("students.txt", "r") as file:
    print("--- readlines() ---")
    lines = file.readlines()
    print(lines)

# Problem : Count total lines, words, and characters
with open("students.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("\nTotal lines:", len(lines))
print("Total words:", len(words))
print("Total characters:", characters)

# File pointers: tell() and seek()
with open("students.txt", "r") as file:
    print("\n--- File Pointers ---")
    print("Position before reading:", file.tell())

    file.read()
    print("Position after reading everything:", file.tell())

    file.seek(0)   # move pointer back to the beginning
    print("Position after seek(0):", file.tell())
    print("Reading again from start:", file.readline())