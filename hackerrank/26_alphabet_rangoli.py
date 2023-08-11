# link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# iterate over reverse of first size english alphabets

# list of alphabets so far
#     append to list of alphabets so far
#     store last alphabet in this list in the format -alphabet-
#     concatenate "-".join of remaining slice of alphabets in reverse to left of -alphabet-
#     concatenate "-".join of remaining slice of alphabets to right of -alphabet-
#     print result

def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    curr_alphabets = []
    rangoli_width = (4 * size) - 3
    for alphabet in reversed(alphabets[:size]):
        curr_alphabets.append(alphabet)
        result = curr_alphabets[:-1] + [curr_alphabets[-1]] + list(reversed(curr_alphabets[:-1]))
        result = "-".join(result).center(rangoli_width, "-")
        print(result)

    # bottom half
    for _ in range(len(curr_alphabets) - 1):
        curr_alphabets = curr_alphabets[:-1]
        result = curr_alphabets[:-1] + [curr_alphabets[-1]] + list(reversed(curr_alphabets[:-1]))
        result = "-".join(result).center(rangoli_width, "-")
        print(result)


print_rangoli(2)
