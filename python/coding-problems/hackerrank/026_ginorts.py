# Link: https://www.hackerrank.com/challenges/ginorts/problem
# Task:
#   You are given a string
#   S contains alphanumeric characters only.
#   Your task is to sort the string S in the following manner:
#    • All sorted lowercase letters are ahead of uppercase letters.
#    • All sorted uppercase letters are ahead of digits.
#    • All sorted odd digits are ahead of sorted even digits.
# Input Format
#   A single line of input contains the string S.
# Output Format
#   Output the sorted string

def key(val):
    if val.islower():
        return 0
    if val.isupper():
        return 1
    if int(val) % 2 == 1:
        return 2
    if int(val) % 2 == 0:
        return 3

# sort1 = sorted("ortingS475")
# print("".join(sort1))
#
# sort2 = sorted(sort1, key=key)
# print("".join(sort2))


S = input()
sort1 = sorted(S)
sort2 = sorted(sort1, key=key)
print("".join(sort2))
