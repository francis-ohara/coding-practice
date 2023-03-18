# Link: https://www.hackerrank.com/challenges/hex-color-code/problem
# Task:
# CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
# Specifications of HEX Color Code
# • It must start with a '#' symbol.
# It can have 3 or 6 digits.
# • Each digit is in the range of O to F. (1, 2, 3, 4, 5, 6, 7, 8, 9, O, A, B, C, D, E and F).
# A — F letters can be lower case. (a, b, c, d, e and f are also valid digits).
#
# Examples
# Valid Hex Color Codes
# # FFF
# #025
# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff
#
# You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to
# bottom.
#
# CSS Code Pattern
# Selector
# {
# Property: value;
# }
#
# Input Format
# The first line contains N, the number of code lines.
# The next N lines contains CSS Codes.
#
# Constraints
# O < N < 50
#
# Output Format
# Output the color codes with symbols on separate lines.
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# n = int(input())
# regex = "\{.*(#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})).*\}"
#
# string = ""
# for i in range(n):
#     string = string + input()

# ---Debugging---
# Problem so far: Stops working the moment ".*" expression is included. ".*" Probably doesn't do what we think it does.
# Explanation so far: multiple possible ways of interpreting said regex. Last occurrence is chosen among different options for some reason.
regex = ".*#[0-9A-F-a-f]{3}"
string = "{property: #ADA123; property: #AFD #FED #123}"

results = re.findall(regex, string)

for result in results:
    print(result)
