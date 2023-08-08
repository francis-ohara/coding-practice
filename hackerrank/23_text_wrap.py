# link: https://www.hackerrank.com/challenges/text-wrap/problem

from math import ceil


def wrap(string, max_width):
    paragraph = ""
    start = 0
    end = max_width

    for _ in range(ceil(len(string)/max_width)):
        paragraph = paragraph + string[start:end] + "\n"
        start += max_width
        end += max_width

    return paragraph


print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))
