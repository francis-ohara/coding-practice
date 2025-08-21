# link: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))
    stackable = True
    top = float("inf")

    while len(blocks) > 0:
        left = blocks[0]
        right = blocks[-1]
        if left <= top:
            if right <= top:
                if left > right:
                    top = left
                    blocks.popleft()
                else:
                    top = right
                    blocks.pop()
            else:
                stackable = False
                break
        else:
            stackable = False
            break

    if stackable:
        print("Yes")
    else:
        print("No")
