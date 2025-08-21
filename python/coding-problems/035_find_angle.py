# link: https://www.hackerrank.com/challenges/find-angle/problem


from math import atan, degrees

AB = int(input())
BC = int(input())

theta = degrees(atan(BC / AB))

print(90-round(theta), "\u00B0", sep="")
