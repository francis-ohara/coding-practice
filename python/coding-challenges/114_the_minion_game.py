# link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        n_substrings = len(string) - i  # no. of substrings beginning with string[i]
        if string[i] in vowels:
            kevin += n_substrings
        else:
            stuart += n_substrings

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")

s = input()
minion_game(s)
