# link: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year: int) -> bool:
    result = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
        else:
            result = True
    return result


print(is_leap(1990))
