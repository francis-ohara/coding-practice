# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=false
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    counts = {}
    max_value = 0
    for i in range(len(candles)):
        if candles[i] > max_value:
            max_value = candles[i]
        counts[candles[i]] = counts.get(candles[i], 0) + 1
    return counts[max_value]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + "\n")

    fptr.close()
