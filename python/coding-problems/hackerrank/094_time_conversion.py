# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=false
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    result = s[2:8]
    if s[8:] == "AM":
        if s[:2] == "12":
            result = "00" + result
        else:
            result = s[:2] + result
    else:
        if s[:2] == "12":
            result = s[:2] + result
        else:
            result = str(int(s[:2]) + 12) + result
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
