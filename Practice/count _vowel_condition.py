def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count


def find_max(numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


def character_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


print("Vowels:", count_vowels("software engineer"))
print("Max:", find_max([3, 8, 2, 10, 5]))
print("Unique:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print("Frequency:", character_frequency("banana"))