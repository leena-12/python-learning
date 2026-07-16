
#Simple program to count vowels in a given string.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    text = input("Enter a string: ")
    total = count_vowels(text)
    print(f"Number of vowels: {total}")