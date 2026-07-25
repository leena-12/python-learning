# Problem : Replace one word with another in a file
# Workflow: read all data -> modify in memory -> rewrite the file

with open("notes.txt", "w") as file:
    file.write("I am learning Python.\nPython is a great language.\n")

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

# Step 1: Read all data
with open("notes.txt", "r") as file:
    content = file.read()

# Step 2: Modify it in memory
updated_content = content.replace(old_word, new_word)

# Step 3: Rewrite the file
with open("notes.txt", "w") as file:
    file.write(updated_content)

print("File updated successfully.\n")

with open("notes.txt", "r") as file:
    print(file.read())