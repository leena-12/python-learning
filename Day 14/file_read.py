# Read and display the file created in file_write.py
with open("intro.txt", "r") as file:
    print(file.read())

# Reading line by line
print("--- Reading line by line ---")
with open("intro.txt", "r") as file:
    for line in file:
        print(line.strip())

# Problem : print only lines containing the word "Python"
with open("notes.txt", "r") as file:
    print("\n--- Lines containing 'Python' ---")
    for line in file:
        if "Python" in line:
            print(line.strip())