text = input("Enter a paragraph: ")

# Total characters (including spaces)
total_characters = len(text)

# Total words
words = text.split()
total_words = len(words)

# Total sentences (counted using . ! ?)
sentence_enders = ".!?"
total_sentences = 0
for ch in text:
    if ch in sentence_enders:
        total_sentences += 1

# Total vowels
vowels = "aeiouAEIOU"
total_vowels = 0
for ch in text:
    if ch in vowels:
        total_vowels += 1

# Total digits
total_digits = 0
for ch in text:
    if ch.isdigit():
        total_digits += 1

# Longest word
longest_word = ""
for word in words:
    cleaned_word = word.strip(".,!?;:")
    if len(cleaned_word) > len(longest_word):
        longest_word = cleaned_word

# Bonus: most frequently used character (ignoring spaces)
frequency = {}
for ch in text:
    if ch != " ":
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

most_frequent_char = ""
highest_count = 0
for ch, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_frequent_char = ch

print("\n----- Text Analysis -----")
print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)
print("Total Vowels:", total_vowels)
print("Total Digits:", total_digits)
print("Longest Word:", longest_word)
print("Most Frequent Character:", most_frequent_char, "(", highest_count, "times )")