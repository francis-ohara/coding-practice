# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for row in range(n):
        print(" " * (n - (row + 1)), end="")
        print("#" * (row + 1))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
