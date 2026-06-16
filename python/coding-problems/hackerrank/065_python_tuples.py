# https://www.hackerrank.com/challenges/python-tuples/problem

n = int(input())

t = tuple(int(input()) for i in range(n))  # tuple comprehension
print(hash(t))
