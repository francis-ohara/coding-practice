# link: https://www.hackerrank.com/challenges/exceptions/problem?

T = int(input())

for _ in range(T):
    dividend, divisor = map(int, input().split())

    try:
        print(dividend // divisor)

    except ZeroDivisionError as error:
        print("Error Code:", error)
