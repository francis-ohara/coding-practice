# link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
scores = list(map(int, input().split()))
highest = -101
second_highest = -101

for score in scores:
    if score > highest:
        second_highest = highest
        highest = score
    elif highest > score > second_highest:
        second_highest = score

print(second_highest)
