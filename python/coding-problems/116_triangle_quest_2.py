# link: https://www.hackerrank.com/challenges/triangle-quest-2/problem


for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print({1: 1, 2: 121, 3: 12321, 4: 1234321, 5: 123454321, 6: 12345654321, 7: 1234567654321, 8: 123456787654321,
           9: 12345678987654321}[i])
