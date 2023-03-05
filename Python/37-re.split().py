# Link: https://www.hackerrank.com/challenges/re-split/problem
# Task:
# You are given a string s consisting only of digits 0-9, commas „ and dots .
# Your task is to complete the regex_pattern defined below, which will be used to re.split() all the , and . symbols in s.
# It's guaranteed that every comma and every dot in s is preceded and followed by a digit.
import re

regex_pattern = r"[,.]"  # Do not delete 'r'.

print("\n".join(re.split(regex_pattern, input())))
