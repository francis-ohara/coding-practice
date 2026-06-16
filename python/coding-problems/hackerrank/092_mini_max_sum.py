# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=false
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_sum = 10_000_000_000
    max_sum = 0
    for excluded_position in range(len(arr)):
        current_sum = 0
        for num in (arr[:excluded_position] + arr[excluded_position + 1:]):
            current_sum += num
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > max_sum:
            max_sum = current_sum
    print(min_sum, max_sum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
