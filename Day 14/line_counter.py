# Problem: Count total lines in a file
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))

# Problem: Count total words in a file
with open("notes.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Total words:", len(words))