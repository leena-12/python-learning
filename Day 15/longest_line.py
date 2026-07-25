# Problem : Display the longest line from a file
with open("notes.txt", "w") as file:
    file.write("Short line\nThis is a much longer line in the file\nMedium length line\n")

with open("notes.txt", "r") as file:
    lines = file.readlines()

longest = ""
for line in lines:
    if len(line.strip()) > len(longest):
        longest = line.strip()

print("Longest line:", longest)