# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])
    diagonal_sum = 0
    antidiagonal_sum = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if row == col:
                diagonal_sum += arr[row][col]
            if col == num_rows - 1 - row:
                antidiagonal_sum += arr[row][col]
    return abs(diagonal_sum - antidiagonal_sum)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
