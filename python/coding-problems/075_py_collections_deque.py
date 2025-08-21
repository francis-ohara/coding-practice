# link: https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

deq = deque()
N = int(input())

for _ in range(N):
    command, *args = input().split()

    if command == "append":
        deq.append(args[0])
    elif command == "appendleft":
        deq.appendleft(args[0])
    elif command == "pop":
        deq.pop()
    else:
        deq.popleft()

print(*deq)
