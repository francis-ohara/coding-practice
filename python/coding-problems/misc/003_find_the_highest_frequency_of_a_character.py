# https://www.youtube.com/watch?v=AdG_3GRDUfI

def find_highest_frequency(s: str) -> str:
    char_frequencies = {}

    for char in s:
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1

    highest_frequency = 0
    highest_char = None

    for char in char_frequencies:
        if char_frequencies[char] > highest_frequency:
            highest_char = char
            highest_frequency = char_frequencies[char]

    return highest_char

print(find_highest_frequency("aababcaab"))