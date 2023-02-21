# Link: https://www.hackerrank.com/challenges/python-sort-sort/problem
# Task:
# You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on).
# You are required to sort the data based on the Kth attribute and print the final resulting table.
#
# Note that K is indexed from 0 to M-1, where M is the number of attributes.
# Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.
#
# Input Format
# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.
#
# Output Format
# Print the  lines of the sorted table. Each line should contain the space separated elements.


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    athletes = []

    for _ in range(n):
        athletes.append(input().split())

    k = int(input())

    for i in range(1, n):
        for j in range(1, i + 1):
            if athletes[j - 1][k] > athletes[j][k]:
                athletes[j - 1], athletes[j] = athletes[j], athletes[j - 1]

    for athlete in athletes:
        print(" ".join(athlete))


#input
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# expected output
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12