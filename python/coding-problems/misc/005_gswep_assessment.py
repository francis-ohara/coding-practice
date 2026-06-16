# Question 1
def solution(commands):
    position = 0

    for command in commands:
        if command == "L":
            position -= 1
        else:
            position += 1

    if position == 0:
        return ""
    elif position < 0:
        return "L"
    else:
        return "R"

print(solution("LRLLRLRLRRRLR"))

# Question 2
def solution(message, n):
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonant_counter = 0

    for i in range(len(message)):
        if message[i].lower() in consonants:
            consonant_counter += 1
            if consonant_counter % n == 0:
                if message[i].lower() == "z":
                    replacement = "b" if message[i].islower() else "B"
                elif message[i].islower():
                    replacement = consonants[consonants.index(message[i]) + 1]
                else:
                    replacement = consonants[consonants.index(message[i].lower()) + 1].upper()
                message = message[:i] + replacement + message[i+1:]

    return message

print(solution("CodeSignal", 3))


# Question 4
def solution(titles):
    count = 0
    for i in range(len(titles)):
        for j in range(i + 1, len(titles)):
            if titles[i].startswith(titles[j]) or titles[j].startswith(titles[i]):
                print(i, titles[i], j, titles[j])
                count += 1
    return count

print(solution(["abc", "a", "a", "b", "ab", "ac"]))