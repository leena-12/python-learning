text = "leetcode"

for character in text:
    if text.count(character) == 1:
        print("First unique character:", character)
        break
    