# Problem : Take user input and append it to diary.txt
entry = input("Enter your diary entry: ")

with open("diary.txt", "a") as file:
    file.write(entry + "\n")

print("Entry added to diary.txt")