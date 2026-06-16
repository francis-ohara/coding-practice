# link: https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=false
from itertools import permutations

S, k = input().split()
k = int(k)
S = sorted(S)

for item in permutations(S, k):
    item = "".join(item)
    print(item)
