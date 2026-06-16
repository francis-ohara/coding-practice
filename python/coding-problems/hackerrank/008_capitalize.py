# link: https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    s = list(s)
    s[0] = s[0].capitalize()
    for i in range(1, len(s)):
        if s[i - 1] == " ":
            s[i] = s[i].capitalize()
    return "".join(s)


name = input()
print(solve(name))
