# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    num_positive = 0
    num_negative = 0
    num_zeros = 0

    for num in arr:
        if num > 0:
            num_positive += 1
        elif num == 0:
            num_zeros += 1
        else:
            num_negative += 1
    
    print(f"{num_positive/len(arr):0.6f}")
    print(f"{num_negative/len(arr):0.6f}")
    print(f"{num_zeros/len(arr):0.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
