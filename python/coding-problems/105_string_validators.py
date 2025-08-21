# link: https://www.hackerrank.com/challenges/string-validators/problem

alnum = False
alpha = False
digit = False
lower = False
upper = False

S = input()

for char in S:
    if char.isalnum():
        alnum = True
        if char.isdigit():
            digit = True
            continue
        else:
            alpha = True
            if char.islower():
                lower = True
            else:
                upper = True

    else:
        continue

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)
