# link: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    for num in range(1, number + 1):
        width = len(f"{number:b}")
        decimal = f"{num:d}".rjust(width)
        octal = f"{num:o}".rjust(width)
        hexadecimal = f"{num:x}".rjust(width)
        binary = f"{num:b}".rjust(width)
        print(decimal, octal, hexadecimal, binary)


print_formatted(17)
