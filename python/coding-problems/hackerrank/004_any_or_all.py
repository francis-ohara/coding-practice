# Link: https://www.hackerrank.com/challenges/any-or-all/problem
# Task:
# You are given a space separated list of integers.
# If all the integers are positive, then you need to check if any integer is a palindromic integer.
# Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

N = int(input())
nums = list(map(int, input().split()))


def any_or_all(numbers):
    if all((False for number in numbers if number <= 0)):
        if any((True for number in numbers if str(number) == "".join(reversed(str(number))))):
            return True
    return False


print(any_or_all(nums))
