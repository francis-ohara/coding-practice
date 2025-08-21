# link: https://www.hackerrank.com/challenges/itertools-product/problem

A = list(map(int, input().split()))
B = list(map(int, input().split()))


for a in A:
    for b in B:
        print((a, b), end = " ")

