# Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem
# Task:
# You are given a string N.
# Your task is to verify that N is a floating point number.
# In this task, a valid float number must satisfy all of the following requirements:
# > Number can start with +, - or . symbol.
# For example:
# +4.50
# Vt-I.o
# —+4.5
# > Number must contain at least 1 decimal value.
# For example:
# 12
# > Number must have exactly one . symbol.
# > Number must not give any exceptions when converted using float(N).
# Input Format
# The first line contains an integer T, the number of test cases.
# The next T line(s) contains a string N.
# Output Format
# Output True or False for each test case.

import re

T = int(input())
regex = "^[+-]{0,1}[0-9]*\.[0-9]+$"

for i in range(T):
    N = input()
    print(bool(re.search(regex, N)))
