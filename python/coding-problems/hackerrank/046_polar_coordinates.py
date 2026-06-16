# link: https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import phase


z = complex(input())

modulus = abs(z)
phase_angle = phase(z)

print(modulus)
print(phase_angle)
