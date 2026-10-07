text = "swiss"

for character in text:
    if text.count(character) == 1:
        print("First non-repeating character:", character)
        break
else:
    print("No non-repeating character")