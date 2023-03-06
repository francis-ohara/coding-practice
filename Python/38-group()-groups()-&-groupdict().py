# Link: https://www.hackerrank.com/challenges/re-group-groups/problem
# Task:
# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character in
# repetitions.
# Input Format
# A single line of input containing the string
# Constraints
# O < ten(S) < 100
# Output Format
# (read from left to right) that has consecutive
# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()

regex = "([A-Za-z0-9]){2,}"
result = re.match(regex, S)
print(result.group(1))