
#Simple program to check whether a given string/number is a palindrome.

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    value = input("Enter a word, phrase, or number: ")
    if is_palindrome(value):
        print(f"'{value}' is a palindrome.")
    else:
        print(f"'{value}' is not a palindrome.")