
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


