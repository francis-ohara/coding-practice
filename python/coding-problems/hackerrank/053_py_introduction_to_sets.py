# link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(arr):
    arr = set(arr)
    avg = sum(arr) / len(arr)
    avg = round(avg, 3)
    return avg


print(average(map(int, input().split())))
