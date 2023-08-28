# link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

N = int(input())
columns = ",".join(input().split())
Student = namedtuple("Student", columns)
sum_of_marks = 0

for _ in range(N):
    values = input().split()
    current_student = Student(*values)
    sum_of_marks += int(current_student.MARKS)

avg_of_marks = sum_of_marks / N
print(f"{avg_of_marks:0.2f}")
