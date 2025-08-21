# link: https://www.hackerrank.com/challenges/most-commons/problem

s = input()

# create dictionary of each character and their frequency
frequencies = {}
for char in s:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

# convert dictionary into more sortable format
frequencies = list(frequencies.items())

# sort by characters alphabetically
frequencies = sorted(frequencies, key=lambda item: item[0])

# sort by frequencies in descending order
frequencies = sorted(frequencies, key=lambda item: item[1], reverse=True)

# print the first 3 items ()
for char, frequency in frequencies[:3]:
    print(char, frequency)
