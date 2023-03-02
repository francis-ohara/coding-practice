# Link: https://www.hackerrank.com/challenges/py-check-subset/problem
# Task:
# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.
# Input Format
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set
# The second line of each test case contains the space separated elements of set
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.
# Output Format
# Output True or False for each test case on separate lines.

T = int(input())

for i in range(T):
    n_A = int(input())
    A = set(map(int, input().split()))
    n_B = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))
